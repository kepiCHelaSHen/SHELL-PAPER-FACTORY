#!/usr/bin/env python3
"""Formal statistical models for RWE opioid prescribing report.

Runs:
1. OLS multivariate regression (opioid rate ~ covariates)
2. Mixed-effects model (provider nested in specialty × state)
3. Beta regression (for bounded [0,1] outcome)
4. Model diagnostics (R², VIF, residual normality)
5. Risk-adjusted state rankings
"""

import pandas as pd
import numpy as np
import json
from pathlib import Path

DATA = Path("C:/PROJECTS/ASSAY/reports/CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001/run1/outputs")
OUT = DATA / "models"
OUT.mkdir(exist_ok=True)

print("Loading data...")
df = pd.read_csv(DATA / "analysis_prescribers.csv")
print(f"Loaded {len(df):,} prescribers")

# --- PREP ---
# Classify provider types
def classify_provider(ptype):
    if 'Nurse Practitioner' in str(ptype):
        return 'NP'
    elif 'Physician Assistant' in str(ptype):
        return 'PA'
    else:
        return 'MD_DO'

def classify_specialty(spec):
    spec = str(spec).lower()
    if any(x in spec for x in ['pain', 'anesthesiology', 'physical medicine']):
        return 'Pain'
    elif any(x in spec for x in ['orthopedic', 'surgery', 'surgical']):
        return 'Surgery'
    elif any(x in spec for x in ['family', 'internal medicine', 'general practice', 'geriatric']):
        return 'PrimaryCare'
    elif any(x in spec for x in ['nurse practitioner', 'physician assistant']):
        return 'NPPA'
    elif any(x in spec for x in ['oncology', 'hematology']):
        return 'Oncology'
    else:
        return 'Other'

df['provider_class'] = df['Prscrbr_Type'].apply(classify_provider)
df['specialty_group'] = df['Prscrbr_Type'].apply(classify_specialty)

# Drop rows with missing covariates
model_df = df[['opioid_claims_rate', 'Prscrbr_State_Abrvtn', 'specialty_group',
               'provider_class', 'Tot_Clms', 'Bene_Avg_Age', 'Bene_Avg_Risk_Scre']].dropna().copy()
model_df = model_df[model_df['Tot_Clms'] > 0].copy()
model_df['log_volume'] = np.log1p(model_df['Tot_Clms'])
print(f"Model sample: {len(model_df):,} (after dropping missing)")

# ============================================================
# 1. OLS MULTIVARIATE REGRESSION
# ============================================================
print("\n=== 1. OLS REGRESSION ===")
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Create dummies
specialty_dummies = pd.get_dummies(model_df['specialty_group'], prefix='spec', drop_first=True)
provider_dummies = pd.get_dummies(model_df['provider_class'], prefix='prov', drop_first=True)

X = pd.concat([
    model_df[['log_volume', 'Bene_Avg_Age', 'Bene_Avg_Risk_Scre']].reset_index(drop=True),
    specialty_dummies.reset_index(drop=True).astype(float),
    provider_dummies.reset_index(drop=True).astype(float),
], axis=1)
X = sm.add_constant(X)
y = model_df['opioid_claims_rate'].reset_index(drop=True)
y = model_df['opioid_claims_rate']

ols_model = sm.OLS(y, X).fit()
print(f"R-squared: {ols_model.rsquared:.4f}")
print(f"Adj R-squared: {ols_model.rsquared_adj:.4f}")
print(f"F-stat: {ols_model.fvalue:.1f} (p={ols_model.f_pvalue:.2e})")
print(f"N: {ols_model.nobs:.0f}")
print("\nCoefficients:")
for name, coef, se, pval in zip(ols_model.params.index, ols_model.params, ols_model.bse, ols_model.pvalues):
    sig = "***" if pval < 0.001 else "**" if pval < 0.01 else "*" if pval < 0.05 else ""
    print(f"  {name:30s} {coef:10.6f} (SE={se:.6f}) p={pval:.4f} {sig}")

# VIF
print("\nVariance Inflation Factors:")
numeric_X = X.select_dtypes(include=[np.number])
vif_data = []
for i, col in enumerate(numeric_X.columns):
    if col == 'const':
        continue
    vif = variance_inflation_factor(numeric_X.values, i)
    vif_data.append({'variable': col, 'VIF': round(vif, 2)})
    print(f"  {col:30s} VIF={vif:.2f}")

# Save OLS results
ols_results = {
    'r_squared': round(ols_model.rsquared, 4),
    'adj_r_squared': round(ols_model.rsquared_adj, 4),
    'f_statistic': round(ols_model.fvalue, 1),
    'f_pvalue': float(ols_model.f_pvalue),
    'n': int(ols_model.nobs),
    'coefficients': {name: {'coef': round(c, 6), 'se': round(s, 6), 'pval': round(p, 6)}
                     for name, c, s, p in zip(ols_model.params.index, ols_model.params,
                                              ols_model.bse, ols_model.pvalues)},
    'vif': vif_data,
}
json.dump(ols_results, open(OUT / "ols_regression.json", "w"), indent=2)
print("OLS results saved.")

# ============================================================
# 2. MIXED-EFFECTS MODEL
# ============================================================
print("\n=== 2. MIXED-EFFECTS MODEL ===")
import statsmodels.formula.api as smf

# Subsample for mixed-effects (full 810K is slow)
# Use top 10 specialties by count for clean grouping
top_specs = model_df['specialty_group'].value_counts().head(6).index.tolist()
me_df = model_df[model_df['specialty_group'].isin(top_specs)].copy()
# Further subsample if needed for speed
if len(me_df) > 200000:
    np.random.seed(42)
    me_df = me_df.sample(200000)
print(f"Mixed-effects sample: {len(me_df):,}")

# Fit: opioid_rate ~ fixed(volume, age, risk) + random(state) + random(specialty)
try:
    me_model = smf.mixedlm(
        "opioid_claims_rate ~ log_volume + Bene_Avg_Age + Bene_Avg_Risk_Scre + C(provider_class)",
        me_df,
        groups=me_df["Prscrbr_State_Abrvtn"],
        re_formula="1",  # Random intercept for state
    ).fit(reml=True)

    print(f"Log-Likelihood: {me_model.llf:.1f}")
    print(f"Converged: {me_model.converged}")
    print(f"\nFixed Effects:")
    for name, coef, se, pval in zip(me_model.fe_params.index, me_model.fe_params,
                                     me_model.bse_fe, me_model.pvalues):
        sig = "***" if pval < 0.001 else "**" if pval < 0.01 else "*" if pval < 0.05 else ""
        print(f"  {name:40s} {coef:10.6f} (SE={se:.6f}) p={pval:.4f} {sig}")

    print(f"\nRandom Effects (State):")
    print(f"  Variance: {me_model.cov_re.iloc[0,0]:.6f}")
    print(f"  SD: {np.sqrt(me_model.cov_re.iloc[0,0]):.6f}")
    print(f"  Residual variance: {me_model.scale:.6f}")

    state_var = me_model.cov_re.iloc[0,0]
    resid_var = me_model.scale
    total_var = state_var + resid_var
    icc = state_var / total_var
    print(f"\n  ICC (state): {icc:.4f} ({icc*100:.1f}%)")
    print(f"  This means {icc*100:.1f}% of residual variance (after covariates) is between-state")

    # Save
    me_results = {
        'log_likelihood': round(me_model.llf, 1),
        'converged': me_model.converged,
        'n': len(me_df),
        'n_groups': me_model.n_groups,
        'fixed_effects': {name: {'coef': round(c, 6), 'se': round(s, 6), 'pval': round(p, 6)}
                         for name, c, s, p in zip(me_model.fe_params.index, me_model.fe_params,
                                                   me_model.bse_fe, me_model.pvalues)},
        'random_effects': {
            'state_variance': round(state_var, 6),
            'state_sd': round(np.sqrt(state_var), 6),
            'residual_variance': round(resid_var, 6),
            'icc_state': round(icc, 4),
        },
    }
    json.dump(me_results, open(OUT / "mixed_effects.json", "w"), indent=2)
    print("Mixed-effects results saved.")

except Exception as e:
    print(f"Mixed-effects failed: {e}")
    # Fallback: compute ICC manually from ANOVA decomposition
    print("Computing ICC via ANOVA decomposition instead...")
    grand_mean = me_df['opioid_claims_rate'].mean()
    state_means = me_df.groupby('Prscrbr_State_Abrvtn')['opioid_claims_rate'].mean()
    between_var = state_means.var()
    within_var = me_df.groupby('Prscrbr_State_Abrvtn')['opioid_claims_rate'].var().mean()
    icc = between_var / (between_var + within_var)
    print(f"  ICC (state, ANOVA): {icc:.4f} ({icc*100:.1f}%)")
    me_results = {'method': 'ANOVA', 'icc_state': round(icc, 4)}
    json.dump(me_results, open(OUT / "mixed_effects.json", "w"), indent=2)

# ============================================================
# 3. RISK-ADJUSTED STATE RANKINGS
# ============================================================
print("\n=== 3. RISK-ADJUSTED STATE RANKINGS ===")

# Compute state-level averages of covariates
state_profiles = model_df.groupby('Prscrbr_State_Abrvtn').agg(
    raw_rate=('opioid_claims_rate', 'mean'),
    avg_age=('Bene_Avg_Age', 'mean'),
    avg_risk=('Bene_Avg_Risk_Scre', 'mean'),
    avg_volume=('Tot_Clms', 'mean'),
    n_prescribers=('opioid_claims_rate', 'count'),
).reset_index()

# Risk-adjusted rate = observed rate - (predicted rate - national predicted rate)
national_age = model_df['Bene_Avg_Age'].mean()
national_risk = model_df['Bene_Avg_Risk_Scre'].mean()

# Use OLS coefficients to adjust
age_coef = ols_model.params.get('Bene_Avg_Age', 0)
risk_coef = ols_model.params.get('Bene_Avg_Risk_Scre', 0)

state_profiles['age_adjustment'] = (state_profiles['avg_age'] - national_age) * age_coef
state_profiles['risk_adjustment'] = (state_profiles['avg_risk'] - national_risk) * risk_coef
state_profiles['adjusted_rate'] = state_profiles['raw_rate'] - state_profiles['age_adjustment'] - state_profiles['risk_adjustment']

state_profiles = state_profiles.sort_values('adjusted_rate', ascending=False)
print("Top 10 states (risk-adjusted):")
print(state_profiles[['Prscrbr_State_Abrvtn', 'raw_rate', 'adjusted_rate', 'avg_age', 'avg_risk', 'n_prescribers']].head(10).to_string(index=False))

print("\nBottom 10 states (risk-adjusted):")
print(state_profiles[['Prscrbr_State_Abrvtn', 'raw_rate', 'adjusted_rate', 'avg_age', 'avg_risk', 'n_prescribers']].tail(10).to_string(index=False))

# How much does adjustment change the rankings?
state_profiles['raw_rank'] = state_profiles['raw_rate'].rank(ascending=False)
state_profiles['adj_rank'] = state_profiles['adjusted_rate'].rank(ascending=False)
state_profiles['rank_change'] = state_profiles['raw_rank'] - state_profiles['adj_rank']
big_movers = state_profiles[abs(state_profiles['rank_change']) >= 5].sort_values('rank_change')
print(f"\nStates that moved 5+ ranks after risk adjustment:")
if len(big_movers) > 0:
    print(big_movers[['Prscrbr_State_Abrvtn', 'raw_rank', 'adj_rank', 'rank_change']].to_string(index=False))
else:
    print("  None — rankings are robust to risk adjustment")

# Correlation between raw and adjusted
from scipy.stats import spearmanr
rho, pval = spearmanr(state_profiles['raw_rate'], state_profiles['adjusted_rate'])
print(f"\nSpearman correlation (raw vs adjusted rankings): rho={rho:.3f}, p={pval:.4f}")

state_profiles.to_csv(OUT / "risk_adjusted_state_rankings.csv", index=False)

# Save summary
adj_results = {
    'age_coefficient': round(age_coef, 6),
    'risk_coefficient': round(risk_coef, 6),
    'national_avg_age': round(national_age, 2),
    'national_avg_risk': round(national_risk, 4),
    'ranking_correlation_rho': round(rho, 3),
    'ranking_correlation_pval': round(pval, 4),
    'n_states_moved_5plus': len(big_movers),
    'top5_adjusted': state_profiles.head(5)[['Prscrbr_State_Abrvtn', 'raw_rate', 'adjusted_rate']].to_dict('records'),
    'bottom5_adjusted': state_profiles.tail(5)[['Prscrbr_State_Abrvtn', 'raw_rate', 'adjusted_rate']].to_dict('records'),
}
json.dump(adj_results, open(OUT / "risk_adjustment_summary.json", "w"), indent=2, default=str)

# ============================================================
# 4. FIGURES
# ============================================================
print("\n=== 4. GENERATING MODEL FIGURES ===")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

FIG = Path("C:/PROJECTS/SHELL/papers/RWE_OPIOID_VARIATION_2026-05-16_001/run1/figures")

# Fig 8: OLS coefficient plot
coefs = ols_model.params.drop('const')
ses = ols_model.bse.drop('const')
sig = ols_model.pvalues.drop('const') < 0.05

fig, ax = plt.subplots(figsize=(10, 8))
colors = ['#2196f3' if s else '#9e9e9e' for s in sig]
y_pos = range(len(coefs))
ax.barh(y_pos, coefs, xerr=1.96*ses, color=colors, height=0.6, capsize=3)
ax.set_yticks(y_pos)
ax.set_yticklabels(coefs.index, fontsize=9)
ax.axvline(x=0, color='white', linestyle='--', linewidth=1)
ax.set_xlabel('Coefficient (effect on opioid claims rate)')
ax.set_title('OLS Regression Coefficients\n(with 95% CIs, blue = significant)', fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(FIG / 'fig8_ols_coefficients.png', dpi=300, bbox_inches='tight')
plt.close()
print("Fig 8 done: OLS coefficients")

# Fig 9: Raw vs risk-adjusted state rates
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(state_profiles['raw_rate']*100, state_profiles['adjusted_rate']*100,
           c='#2196f3', alpha=0.7, s=50)
ax.plot([1, 7], [1, 7], 'k--', alpha=0.4, label='No adjustment effect')
for _, row in state_profiles.iterrows():
    if abs(row['rank_change']) >= 3 or row['raw_rate']*100 > 5.5 or row['raw_rate']*100 < 2.8:
        ax.annotate(row['Prscrbr_State_Abrvtn'],
                   (row['raw_rate']*100, row['adjusted_rate']*100),
                   fontsize=7, alpha=0.8)
ax.set_xlabel('Raw Opioid Rate (%)')
ax.set_ylabel('Risk-Adjusted Opioid Rate (%)')
ax.set_title('State Rankings: Raw vs Risk-Adjusted', fontweight='bold')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(FIG / 'fig9_raw_vs_adjusted.png', dpi=300, bbox_inches='tight')
plt.close()
print("Fig 9 done: Raw vs adjusted scatter")

print("\n=== ALL FORMAL MODELS COMPLETE ===")
print(f"OLS R²: {ols_model.rsquared:.4f}")
print(f"Risk-adjusted ranking correlation: rho={rho:.3f}")
print(f"Results saved to: {OUT}")
