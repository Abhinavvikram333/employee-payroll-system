# analysis.py - Payroll Analytics using Pandas + NumPy + Matplotlib + Seaborn
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

# ── 1. LOAD DATA ───────────────────────────────────────────────────────────────
df = pd.read_csv("data/payroll_history.csv")

print("=== DATASET OVERVIEW ===")
print(f"Shape   : {df.shape}")
print(f"Columns : {list(df.columns)}")
print(f"\nFirst 3 rows:")
print(df.head(3))
print(f"\nData types:")
print(df.dtypes)
print(f"\nNull values:")
print(df.isnull().sum())

# ── 2. BASIC STATS (NumPy) ─────────────────────────────────────────────────────
print("\n=== BASIC STATS ===")
wages = df["wage"].values
print(f"Average wage  : ${np.mean(wages):.2f}")
print(f"Highest wage  : ${np.max(wages):.2f}")
print(f"Lowest wage   : ${np.min(wages):.2f}")
print(f"Std deviation : ${np.std(wages):.2f}")
print(f"Median wage   : ${np.median(wages):.2f}")

# ── 3. AVG WAGE PER DEPARTMENT ─────────────────────────────────────────────────
dept_avg = (
    df.groupby("department")["wage"]
    .mean().round(2)
    .sort_values(ascending=False)
)

# ── 4. SALARY TREND BY YEAR ────────────────────────────────────────────────────
year_avg = df.groupby("year")["wage"].mean().round(2)

# ── 5. TOP 5 TOTAL EARNERS ─────────────────────────────────────────────────────
top_earners = (
    df.groupby("name")["wage"]
    .sum().sort_values(ascending=False).head(5)
)

# ── 6. LEAVES PER DEPARTMENT ───────────────────────────────────────────────────
dept_leaves = (
    df.groupby("department")["leaves"]
    .mean().round(2)
    .sort_values(ascending=False)
)

# ── 7. PIVOT TABLE — DEPT x YEAR ──────────────────────────────────────────────
pivot = df.pivot_table(
    values="wage", index="department",
    columns="year", aggfunc="mean"
).round(2)

# ── 8. FULL EMPLOYEE SUMMARY ───────────────────────────────────────────────────
emp_summary = df.groupby(["name", "department"]).agg(
    total_wage=("wage", "sum"),
    avg_monthly_wage=("wage", "mean"),
    total_leaves=("leaves", "sum"),
    total_hours=("hours_worked", "sum")
).round(2).sort_values("total_wage", ascending=False)

print("\n=== AVG WAGE PER DEPARTMENT ===")
print(dept_avg)
print("\n=== AVG WAGE PER YEAR ===")
print(year_avg)
print("\n=== TOP 5 EARNERS ===")
print(top_earners)
print("\n=== AVG LEAVES PER DEPT ===")
print(dept_leaves)
print("\n=== PIVOT: DEPT x YEAR ===")
print(pivot)
print("\n=== EMPLOYEE SUMMARY ===")
print(emp_summary)

# ══════════════════════════════════════════════════════════════════════════════
# CHARTS
# ══════════════════════════════════════════════════════════════════════════════

# ── CHART 1: Avg Wage per Department (horizontal bar) ─────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
dept_avg.plot(kind="barh", ax=ax, color="steelblue", edgecolor="white")
ax.set_title("Average Monthly Wage by Department", fontsize=14, fontweight="bold")
ax.set_xlabel("Avg Wage ($)")
ax.set_ylabel("Department")
for bar in ax.patches:
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2,
            f"${bar.get_width():,.0f}", va="center", fontsize=10)
plt.tight_layout()
plt.savefig("charts/dept_avg_wage.png", dpi=150)
plt.show()
print("Saved: charts/dept_avg_wage.png")

# ── CHART 2: Salary Trend by Year (line chart) ────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
year_avg.plot(kind="line", ax=ax, marker="o", color="green",
              linewidth=2.5, markersize=8)
ax.set_title("Average Wage per Year (5% Annual Raise)", fontsize=14, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Avg Wage ($)")
ax.set_xticks([2023, 2024, 2025, 2026])
for x, y in zip(year_avg.index, year_avg.values):
    ax.annotate(f"${y:,.0f}", (x, y), textcoords="offset points",
                xytext=(0, 10), ha="center", fontsize=10)
plt.tight_layout()
plt.savefig("charts/salary_trend_by_year.png", dpi=150)
plt.show()
print("Saved: charts/salary_trend_by_year.png")

# ── CHART 3: Dept x Year Grouped Bar ──────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 6))
pivot.plot(kind="bar", ax=ax, edgecolor="white")
ax.set_title("Avg Wage by Department and Year", fontsize=14, fontweight="bold")
ax.set_xlabel("Department")
ax.set_ylabel("Avg Wage ($)")
ax.set_xticklabels(pivot.index, rotation=30, ha="right")
ax.legend(title="Year")
plt.tight_layout()
plt.savefig("charts/dept_year_grouped_bar.png", dpi=150)
plt.show()
print("Saved: charts/dept_year_grouped_bar.png")

# ── CHART 4: Heatmap — Dept x Year (Seaborn) ──────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd",
            linewidths=0.5, ax=ax, cbar_kws={"label": "Avg Wage ($)"})
ax.set_title("Wage Heatmap: Department × Year", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("charts/wage_heatmap.png", dpi=150)
plt.show()
print("Saved: charts/wage_heatmap.png")

# ── CHART 5: Top 5 Earners (Seaborn) ──────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 4))
sns.barplot(x=top_earners.values, y=top_earners.index,
            ax=ax, palette="Blues_r", edgecolor="white")
ax.set_title("Top 5 All-Time Earners (2023–2026)", fontsize=14, fontweight="bold")
ax.set_xlabel("Total Wage ($)")
ax.set_ylabel("Employee")
for bar in ax.patches:
    ax.text(bar.get_width() + 200, bar.get_y() + bar.get_height() / 2,
            f"${bar.get_width():,.0f}", va="center", fontsize=10)
plt.tight_layout()
plt.savefig("charts/top5_earners.png", dpi=150)
plt.show()
print("Saved: charts/top5_earners.png")

print("\nAll 5 charts saved to charts/")
