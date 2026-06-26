#!/usr/bin/env python3
"""Enhanced RWE analyses for opioid prescribing evidence report.

Addresses feedback items A-F:
A. Cross-tab NP/PA × Specialty × State
B. Within-specialty IQR and percentile ratios
C. LA opioid by specialty/provider type/outlier/state-rate
D. Volume tier analysis within specialty
E. Lorenz by specialty + HHI + state concentration scatter
F. Suppression sensitivity
G. Minor: outlier state overlap, leverage ratio
"""

import pandas as pd
import numpy as np
import json
from pathlib import Path

DATA = Path("C:/PROJECTS/ASSAY/reports/CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001/run1/outputs")
OUT = DATA / "enhanced"
OUT.mkdir(exist_ok=True)
FIG = Path("C:/PROJECTS/SHELL/papers/RWE_OPIOID_VARIATION_2026-05-16_001/run1/figures")
FIG.mkdir(parents=True, exist_ok=True)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv(DATA / "analysis_prescribers.csv")
print(f"Loaded {len(df):,} prescribers")

# Classify provider types
def classify_provider(ptype):
    if 'Nurse Practitioner' in str(ptype):
        return 'NP'
    elif 'Physician Assistant' in str(ptype):
        return 'PA'
    else:
        return 'MD/DO'

df['provider_class'] = df['Prscrbr_Type'].apply(classify_provider)

# Classify specialty groups
def classify_specialty(spec):
    spec = str(spec).lower()
    if any(x in spec for x in ['pain', 'anesthesiology', 'physical medicine']):
        return 'Pain/Anesthesia'
    elif any(x in spec for x in ['orthopedic', 'surgery', 'surgical']):
        return 'Surgery/Ortho'
    elif any(x in spec for x in ['family', 'internal medicine', 'general practice', 'geriatric']):
        return 'Primary Care'
    elif any(x in spec for x in ['nurse practitioner', 'physician assistant']):
        return 'NP/PA'
    elif any(x in spec for x in ['oncology', 'hematology']):
        return 'Oncology'
    elif any(x in spec for x in ['dentist', 'oral']):
        return 'Dentistry'
    else:
        return 'Other'

df['specialty_group'] = df['Prscrbr_Type'].apply(classify_specialty)

# Mark outliers
spec_means = df.groupby('Prscrbr_Type')['opioid_claims_rate'].transform('mean')
spec_stds = df.groupby('Prscrbr_Type')['opioid_claims_rate'].transform('std')
df['z_score'] = (df['opioid_claims_rate'] - spec_means) / spec_stds.replace(0, np.nan)
df['is_outlier'] = df['z_score'] > 3

# State rate classification
state_rates = df.groupby('Prscrbr_State_Abrvtn')['opioid_claims_rate'].mean()
median_state_rate = state_rates.median()
df['state_rate_class'] = df['Prscrbr_State_Abrvtn'].map(
    lambda s: 'High-rate' if state_rates.get(s, 0) > state_rates.quantile(0.75) else
              'Low-rate' if state_rates.get(s, 0) < state_rates.quantile(0.25) else 'Middle'
)

print("\n=== A. CROSS-TAB: Provider Type × Specialty Group ===")
crosstab = df.groupby(['provider_class', 'specialty_group']).agg(
    n=('opioid_claims_rate', 'count'),
    mean_rate=('opioid_claims_rate', 'mean'),
    median_rate=('opioid_claims_rate', 'median'),
    opioid_claims=('Opioid_Tot_Clms', 'sum'),
).reset_index()
crosstab['mean_rate'] = (crosstab['mean_rate'] * 100).round(3)
crosstab['median_rate'] = (crosstab['median_rate'] * 100).round(3)
crosstab.to_csv(OUT / "crosstab_provider_specialty.csv", index=False)
print(crosstab.to_string(index=False))

print("\n=== B. WITHIN-SPECIALTY PERCENTILE RATIOS ===")
specialty_iqr = df.groupby('specialty_group')['opioid_claims_rate'].agg(
    n='count',
    p5=lambda x: x.quantile(0.05),
    p25=lambda x: x.quantile(0.25),
    median=lambda x: x.quantile(0.50),
    p75=lambda x: x.quantile(0.75),
    p95=lambda x: x.quantile(0.95),
    mean='mean',
).reset_index()
specialty_iqr['p90_p10_ratio'] = df.groupby('specialty_group')['opioid_claims_rate'].apply(
    lambda x: x.quantile(0.90) / max(x.quantile(0.10), 0.0001)
).values
specialty_iqr['iqr'] = specialty_iqr['p75'] - specialty_iqr['p25']
# Convert to percentage
for col in ['p5','p25','median','p75','p95','mean','iqr']:
    specialty_iqr[col] = (specialty_iqr[col] * 100).round(3)
specialty_iqr.to_csv(OUT / "within_specialty_iqr.csv", index=False)
print(specialty_iqr.to_string(index=False))

# Within-specialty, how much does state explain?
within_spec_state = []
for spec, grp in df.groupby('specialty_group'):
    total_v = grp['opioid_claims_rate'].var()
    state_v = grp.groupby('Prscrbr_State_Abrvtn')['opioid_claims_rate'].transform('mean').var()
    if total_v > 0:
        within_spec_state.append({'specialty_group': spec, 'total_var': total_v, 'state_pct': round(state_v/total_v*100, 2)})
within_state_df = pd.DataFrame(within_spec_state)
within_state_df.to_csv(OUT / "within_specialty_state_variance.csv", index=False)
print("\nState variance % within each specialty:")
print(within_state_df.to_string(index=False))

print("\n=== C. LA OPIOID ANALYSIS ===")
# LA ratio by provider type, specialty, outlier status, state-rate
la_by_provider = df.groupby('provider_class')['la_ratio'].agg(['mean','median','count']).round(4)
la_by_specialty = df.groupby('specialty_group')['la_ratio'].agg(['mean','median','count']).round(4)
la_by_outlier = df.groupby('is_outlier')['la_ratio'].agg(['mean','median','count']).round(4)
la_by_state_class = df.groupby('state_rate_class')['la_ratio'].agg(['mean','median','count']).round(4)

la_results = {
    'by_provider_type': la_by_provider.to_dict(),
    'by_specialty': la_by_specialty.to_dict(),
    'by_outlier': la_by_outlier.to_dict(),
    'by_state_rate_class': la_by_state_class.to_dict(),
}
print("LA ratio by provider type:")
print(la_by_provider)
print("\nLA ratio by outlier status:")
print(la_by_outlier)

# Save
la_by_provider.to_csv(OUT / "la_ratio_by_provider.csv")
la_by_specialty.to_csv(OUT / "la_ratio_by_specialty.csv")
la_by_outlier.to_csv(OUT / "la_ratio_by_outlier.csv")

print("\n=== D. VOLUME TIER ANALYSIS ===")
# Within major specialties, bin by volume quartile
volume_results = []
for spec in ['Primary Care', 'Pain/Anesthesia', 'Surgery/Ortho', 'NP/PA']:
    grp = df[df['specialty_group'] == spec].copy()
    if len(grp) < 100:
        continue
    grp['volume_quartile'] = pd.qcut(grp['Tot_Clms'], 4, labels=['Q1 (low)', 'Q2', 'Q3', 'Q4 (high)'])
    vol_rates = grp.groupby('volume_quartile', observed=True)['opioid_claims_rate'].agg(['mean','median','count'])
    for q, row in vol_rates.iterrows():
        volume_results.append({
            'specialty_group': spec, 'volume_quartile': q,
            'mean_opioid_rate': round(row['mean']*100, 3),
            'median_opioid_rate': round(row['median']*100, 3),
            'n': int(row['count']),
        })

vol_df = pd.DataFrame(volume_results)
vol_df.to_csv(OUT / "volume_tier_analysis.csv", index=False)
print(vol_df.to_string(index=False))

print("\n=== E. LORENZ BY SPECIALTY + HHI ===")
# Compute Gini per specialty group
spec_ginis = {}
for spec, grp in df[df['Opioid_Tot_Clms'] > 0].groupby('specialty_group'):
    claims = np.sort(grp['Opioid_Tot_Clms'].values)
    N = len(claims)
    if N < 50:
        continue
    gini = (2 * np.sum(np.arange(1, N+1) * claims) / (N * claims.sum())) - (N+1)/N
    # HHI: sum of squared shares
    shares = claims / claims.sum()
    hhi = (shares**2).sum() * 10000  # scale to 0-10000
    eff_n = 1 / (shares**2).sum()  # effective number of prescribers
    spec_ginis[spec] = {'gini': round(gini, 4), 'hhi': round(hhi, 2), 'effective_n': round(eff_n, 0), 'n_prescribers': N}

spec_gini_df = pd.DataFrame.from_dict(spec_ginis, orient='index').reset_index()
spec_gini_df.columns = ['specialty_group', 'gini', 'hhi', 'effective_n', 'n_prescribers']
spec_gini_df = spec_gini_df.sort_values('gini', ascending=False)
spec_gini_df.to_csv(OUT / "specialty_gini_hhi.csv", index=False)
print(spec_gini_df.to_string(index=False))

# State concentration vs rate scatter data
state_data = pd.read_csv(DATA / "concentration_metrics.json".replace('.json', '.json'))
# Actually load from JSON
with open(DATA / "concentration_metrics.json") as f:
    conc = json.load(f)
state_ginis = conc.get('state_ginis', {})
state_rates_dict = dict(zip(
    df.groupby('Prscrbr_State_Abrvtn')['opioid_claims_rate'].mean().index,
    df.groupby('Prscrbr_State_Abrvtn')['opioid_claims_rate'].mean().values
))
scatter_data = pd.DataFrame([
    {'state': s, 'gini': g, 'rate': state_rates_dict.get(s, 0)}
    for s, g in state_ginis.items() if s in state_rates_dict
])
scatter_data.to_csv(OUT / "state_gini_vs_rate.csv", index=False)

print("\n=== F. SUPPRESSION SENSITIVITY ===")
# Simulate: what if suppressed providers (those we can't see) have rate = 0?
# CMS suppresses providers with < 11 claims. We have 810K who passed.
# Estimate: ~100K-200K may be suppressed. Test with imputed 0% opioid rate.
n_visible = len(df)
scenarios = []
for n_suppressed in [50000, 100000, 200000]:
    # Add zero-rate providers
    adjusted_total_claims = df['Tot_Clms'].sum() + n_suppressed * df['Tot_Clms'].median()
    adjusted_opioid_claims = df['Opioid_Tot_Clms'].sum()  # suppressed assumed 0
    adjusted_rate = adjusted_opioid_claims / adjusted_total_claims
    scenarios.append({'suppressed': n_suppressed, 'adjusted_rate': round(adjusted_rate*100, 3)})
    print(f"With {n_suppressed:,} suppressed (rate=0): national rate = {adjusted_rate*100:.3f}% (vs {0.0416*100:.2f}%)")

suppression = {
    'visible_providers': n_visible,
    'scenarios': scenarios,
}
with open(OUT / "suppression_sensitivity.json", "w") as f:
    json.dump(suppression, f, indent=2)

print("\n=== G. OUTLIER STATE DISTRIBUTION ===")
outlier_states = df[df['is_outlier']].groupby('Prscrbr_State_Abrvtn').size().sort_values(ascending=False)
outlier_state_df = outlier_states.reset_index()
outlier_state_df.columns = ['state', 'n_outliers']
outlier_state_df['pct_of_outliers'] = (outlier_state_df['n_outliers'] / outlier_state_df['n_outliers'].sum() * 100).round(1)
outlier_state_df.to_csv(OUT / "outlier_by_state_detailed.csv", index=False)
print("Top 10 states by outlier count:")
print(outlier_state_df.head(10).to_string(index=False))

print("\n=== GENERATING ENHANCED FIGURES ===")

# Fig 5: Lorenz by specialty group
fig, ax = plt.subplots(figsize=(10, 8))
colors_spec = {'Pain/Anesthesia': '#d32f2f', 'Primary Care': '#4caf50', 'NP/PA': '#ff9800', 'Surgery/Ortho': '#2196f3', 'Other': '#9e9e9e'}
for spec in ['Pain/Anesthesia', 'Primary Care', 'NP/PA', 'Surgery/Ortho']:
    grp = df[(df['specialty_group'] == spec) & (df['Opioid_Tot_Clms'] > 0)]
    claims = np.sort(grp['Opioid_Tot_Clms'].values)
    N = len(claims)
    if N < 50:
        continue
    cumshare = np.cumsum(claims) / claims.sum()
    lx = np.linspace(0, 1, 200)
    ly = np.interp(lx, np.linspace(0, 1, N), cumshare)
    ax.plot(lx*100, ly*100, lw=2, label=f"{spec} (Gini={spec_ginis.get(spec,{}).get('gini','?')})", color=colors_spec.get(spec, '#666'))

ax.plot([0,100], [0,100], 'k--', lw=1, alpha=0.4)
ax.set_xlabel('Cumulative % of Prescribers')
ax.set_ylabel('Cumulative % of Opioid Claims')
ax.set_title('Lorenz Curves by Specialty Group', fontweight='bold')
ax.legend(loc='upper left', fontsize=10)
ax.set_xlim(0, 100); ax.set_ylim(0, 100)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(FIG / 'fig5_lorenz_by_specialty.png', dpi=300, bbox_inches='tight')
plt.close()
print("Fig 5 done: Lorenz by specialty")

# Fig 6: Volume tier boxplot (Primary Care)
pc = df[df['specialty_group'] == 'Primary Care'].copy()
pc['volume_q'] = pd.qcut(pc['Tot_Clms'], 4, labels=['Q1\n(lowest)', 'Q2', 'Q3', 'Q4\n(highest)'])
fig, ax = plt.subplots(figsize=(8, 6))
pc.boxplot(column='opioid_claims_rate', by='volume_q', ax=ax, showfliers=False)
ax.set_xlabel('Volume Quartile (Total Claims)')
ax.set_ylabel('Opioid Claims Rate')
ax.set_title('Primary Care: Opioid Rate by Volume Quartile', fontweight='bold')
plt.suptitle('')  # Remove auto-generated title
plt.tight_layout()
plt.savefig(FIG / 'fig6_volume_quartile_primary_care.png', dpi=300, bbox_inches='tight')
plt.close()
print("Fig 6 done: Volume quartile boxplot")

# Fig 7: State Gini vs Rate scatter
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(scatter_data['rate']*100, scatter_data['gini'], c='#2196f3', alpha=0.7, s=50)
for _, row in scatter_data.iterrows():
    if row['rate']*100 > 5.5 or row['gini'] > 0.75 or row['rate']*100 < 2.8:
        ax.annotate(row['state'], (row['rate']*100, row['gini']), fontsize=7, alpha=0.8)
ax.set_xlabel('State Opioid Rate (%)')
ax.set_ylabel('State Gini (Prescribing Concentration)')
ax.set_title('State-Level: Rate vs Concentration', fontweight='bold')
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(FIG / 'fig7_state_rate_vs_gini.png', dpi=300, bbox_inches='tight')
plt.close()
print("Fig 7 done: State rate vs Gini scatter")

print("\n=== ALL ENHANCED ANALYSES COMPLETE ===")
print(f"Output files in: {OUT}")
print(f"Figures in: {FIG}")
