#!/usr/bin/env python3
"""Run all RWE analyses for the opioid prescribing evidence report.

Produces: concentration metrics, policy simulation, variance decomposition,
NP vs MD comparison, and 4 publication-quality figures.
"""

import pandas as pd
import numpy as np
import json
from pathlib import Path

DATA = Path("C:/PROJECTS/ASSAY/reports/CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001/run1/outputs")
FIG = Path("C:/PROJECTS/SHELL/papers/RWE_OPIOID_VARIATION_2026-05-16_001/run1/figures")
FIG.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA / "analysis_prescribers.csv")
state_df = pd.read_csv(DATA / "table1_state_opioid_rates.csv")
print(f"Loaded {len(df)} prescribers, {len(state_df)} states")

# === POLICY SIMULATION ===
print("\n=== POLICY SIMULATION ===")
median_rate = state_df['Opioid_Claims_Rate'].median()
total_claims = df['Opioid_Tot_Clms'].sum()

above = state_df[state_df['Opioid_Claims_Rate'] > median_rate]
reductions = []
for _, row in above.iterrows():
    state, rate = row['State'], row['Opioid_Claims_Rate']
    target = rate - (rate - median_rate) * 0.5
    st_data = df[df['Prscrbr_State_Abrvtn'] == state]
    st_opioid = st_data['Opioid_Tot_Clms'].sum()
    if rate > 0:
        reduced = int(st_opioid * (1 - target / rate))
        reductions.append({'state': state, 'current': round(rate, 4), 'target': round(target, 4), 'reduced': reduced})

reductions.sort(key=lambda x: -x['reduced'])
total_reduced = sum(r['reduced'] for r in reductions)
print(f"National opioid claims: {total_claims:,}")
print(f"50% convergence: -{total_reduced:,} ({total_reduced/total_claims*100:.1f}%)")

# Outlier claims
spec_means = df.groupby('Prscrbr_Type')['opioid_claims_rate'].transform('mean')
spec_stds = df.groupby('Prscrbr_Type')['opioid_claims_rate'].transform('std')
df['z_score'] = (df['opioid_claims_rate'] - spec_means) / spec_stds.replace(0, np.nan)
outliers = df[df['z_score'] > 3]
outlier_claims = outliers['Opioid_Tot_Clms'].sum()
print(f"Outlier claims: {outlier_claims:,} ({outlier_claims/total_claims*100:.1f}%)")

json.dump({
    'half_convergence': {'states': len(above), 'claims_reduced': int(total_reduced),
                         'pct': round(total_reduced/total_claims*100, 2), 'top5': reductions[:5]},
    'outlier_claims': {'count': int(len(outliers)), 'claims': int(outlier_claims),
                       'pct': round(outlier_claims/total_claims*100, 2)},
    'total': int(total_claims),
}, open(DATA / "policy_simulation.json", "w"), indent=2, default=str)

# === VARIANCE DECOMPOSITION ===
print("\n=== VARIANCE DECOMPOSITION ===")
total_var = df['opioid_claims_rate'].var()
state_var = df.groupby('Prscrbr_State_Abrvtn')['opioid_claims_rate'].transform('mean').var()
spec_var = df.groupby('Prscrbr_Type')['opioid_claims_rate'].transform('mean').var()
resid = max(total_var - state_var - spec_var, 0)
decomp = {
    'specialty_pct': round(spec_var/total_var*100, 1),
    'state_pct': round(state_var/total_var*100, 1),
    'individual_pct': round(resid/total_var*100, 1),
}
print(f"Specialty: {decomp['specialty_pct']}%  State: {decomp['state_pct']}%  Individual: {decomp['individual_pct']}%")
json.dump(decomp, open(DATA / "variance_decomposition.json", "w"), indent=2)

# === NP vs MD ===
print("\n=== NP vs MD ===")
np_rates = df[df['Prscrbr_Type'].isin(['Nurse Practitioner', 'Physician Assistant'])].groupby('Prscrbr_State_Abrvtn')['opioid_claims_rate'].mean()
md_rates = df[df['Prscrbr_Type'].isin(['Internal Medicine', 'Family Practice', 'General Practice'])].groupby('Prscrbr_State_Abrvtn')['opioid_claims_rate'].mean()
comp = pd.DataFrame({'np': np_rates, 'md': md_rates}).dropna()
comp['ratio'] = comp['np'] / comp['md']
print(f"NP > MD in {(comp['ratio']>1).sum()}/{len(comp)} states, mean ratio: {comp['ratio'].mean():.2f}")
comp.to_csv(DATA / "np_vs_md_by_state.csv")

# === FIGURES ===
print("\n=== GENERATING FIGURES ===")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Fig 1: State rates
ss = state_df.sort_values('Opioid_Claims_Rate', ascending=True)
colors = ['#d32f2f' if r>0.055 else '#ff9800' if r>0.045 else '#4caf50' if r>0.035 else '#2196f3'
          for r in ss['Opioid_Claims_Rate']]
fig, ax = plt.subplots(figsize=(10, 14))
ax.barh(ss['State'], ss['Opioid_Claims_Rate']*100, color=colors, height=0.7)
ax.axvline(x=4.16, color='white', ls='--', lw=1.5, label='National avg (4.16%)')
ax.set_xlabel('Opioid Claims Rate (%)')
ax.set_title('Opioid Prescribing Rate by State\nMedicare Part D, CY2023', fontweight='bold')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(FIG / 'fig1_state_opioid_rates.png', dpi=300, bbox_inches='tight')
plt.close()
print("Fig 1 done")

# Fig 2: Lorenz
opioid_vals = np.sort(df[df['Opioid_Tot_Clms']>0]['Opioid_Tot_Clms'].values)
N = len(opioid_vals)
cumshare = np.cumsum(opioid_vals) / opioid_vals.sum()
lx = np.linspace(0, 1, 200)
ly = np.interp(lx, np.linspace(0, 1, N), cumshare)
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(lx*100, ly*100, color='#2196f3', lw=2.5, label='Opioid prescribing')
ax.plot([0,100], [0,100], 'k--', lw=1, alpha=0.5, label='Perfect equality')
ax.fill_between(lx*100, ly*100, lx*100, alpha=0.15, color='#2196f3')
ax.set_xlabel('Cumulative % of Prescribers')
ax.set_ylabel('Cumulative % of Opioid Claims')
ax.set_title('Lorenz Curve: Opioid Prescribing Concentration', fontweight='bold')
ax.legend(loc='upper left')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(FIG / 'fig2_lorenz_opioid.png', dpi=300, bbox_inches='tight')
plt.close()
print("Fig 2 done")

# Fig 3: Top specialties
spec_df = pd.read_csv(DATA / "table2_specialty_opioid_rates.csv")
st = spec_df.nlargest(15, 'Opioid_Claims_Rate').sort_values('Opioid_Claims_Rate', ascending=True)
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(st['Specialty'], st['Opioid_Claims_Rate']*100, color='#2196f3', height=0.6)
ax.axvline(x=4.16, color='#ff9800', ls='--', lw=1.5, label='National avg')
ax.set_xlabel('Opioid Claims Rate (%)')
ax.set_title('Top 15 Specialties by Opioid Prescribing Rate', fontweight='bold')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(FIG / 'fig3_specialty_rates.png', dpi=300, bbox_inches='tight')
plt.close()
print("Fig 3 done")

# Fig 4: Variance decomposition
fig, ax = plt.subplots(figsize=(8, 8))
labels = ['Specialty', 'Geography', 'Individual']
sizes = [decomp['specialty_pct'], decomp['state_pct'], decomp['individual_pct']]
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%',
    colors=['#2196f3', '#ff9800', '#4caf50'],
    startangle=90,
    textprops={'fontsize': 13, 'fontweight': 'bold'}
)
ax.set_title('Variance Decomposition:\nOpioid Prescribing Rate', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(FIG / 'fig4_variance_decomposition.png', dpi=300, bbox_inches='tight')
plt.close()
print("Fig 4 done")

# Read concentration for summary
conc = json.load(open(DATA / "concentration_metrics.json"))
print(f"\n=== SUMMARY OF NEW FINDINGS ===")
print(f"Gini (opioid prescribing): {conc['national_gini']} [{conc['gini_ci_lower']}, {conc['gini_ci_upper']}]")
print(f"Top 1%: {conc['top1pct_share']}%  Top 5%: {conc['top5pct_share']}%  Top 10%: {conc['top10pct_share']}%")
print(f"Variance: Specialty {decomp['specialty_pct']}%, State {decomp['state_pct']}%, Individual {decomp['individual_pct']}%")
print(f"Policy sim: {total_reduced:,} claims reduced under 50% convergence ({total_reduced/total_claims*100:.1f}%)")
print(f"Outliers account for {outlier_claims/total_claims*100:.1f}% of all opioid claims")
print(f"NP/PA prescribe at {comp['ratio'].mean():.2f}x the MD rate on average")
print(f"\n=== ALL COMPLETE ===")
