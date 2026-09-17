# 🎮 SoloQ Pulse — Competitive Analytics Portfolio Project

> **Portfolio project — Data Analyst / BI / Product Analytics**
>
> A complete analytics case study around a fictional Solo Queue platform. The dataset is synthetic and intentionally designed to look like operational game data.

## 🧠 Business story

Imagine a product team wants to understand why some players climb consistently while others stagnate or stop playing. The analytics team receives match-level, player-level, champion-level and objective data.

Your job is to answer:

**What behaviors and game conditions are most associated with winning, climbing and sustained engagement — and what should the product team do about it?**

This project is deliberately broader than a basic EDA. It combines:

- SQL data modeling and KPI extraction
- Python data cleaning, EDA and statistical testing
- Player segmentation
- Cohort / engagement analysis
- Champion and role performance analysis
- Executive dashboard design
- Data quality checks
- Business recommendations with an explicit evidence trail

## 📦 Dataset

Synthetic data generated with a reproducible Python script.

| Table | Rows | Purpose |
|---|---:|---|
| `matches` | 1,800 | Match context, duration, patch, MMR balance, outcome |
| `match_participants` | 18,000 | 10 player records per match with combat, CS, vision, gold and objective metrics |
| `players` | 80 | Account, tier, role, region and play-style attributes |
| `champions` | 40 | Champion class, role, base pick/ban assumptions and difficulty |
| `match_objectives` | 1,800 | Dragons, barons and towers by team |

**Important:** these are fictional/synthetic observations. Do not present them as Riot Games, OP.GG or real-player data.

## 🎯 Deliverables to complete

### 1. Executive dashboard
Create a Power BI or Tableau dashboard with four pages:

**Overview**
- Win rate
- Average MMR
- Avg. match duration
- Avg. kills/deaths/assists
- Objective control
- Trend by month and patch

**Player performance**
- Win rate by tier / role / play style
- KDA distribution
- CS/min
- Vision score/min
- Objective participation
- Player segmentation

**Champion intelligence**
- Pick rate
- Win rate
- Win rate by role
- Sample size
- Difficulty vs. performance
- Consistency / volatility

**Engagement**
- Matches per player
- Active players by month
- Repeat-player rate
- Session intensity
- “Risk” signals for reduced activity

### 2. SQL analysis
Complete the queries in `sql/analysis.sql`.

### 3. Python analysis
Use `notebooks/01_analysis_template.ipynb` and turn every TODO into a reproducible analysis.

### 4. Business case
Finish `docs/business_case.md` with:

- 3–5 findings
- Evidence for each finding
- Business impact
- Recommended action
- Measurement plan
- Caveats / limitations

## ⭐ What makes this stand out

The key is not having the most charts. It is connecting **metric → diagnosis → business action → follow-up metric**.

Example structure:

> **Finding:** Players with higher objective participation show higher win rates.
>
> **Evidence:** quantify the gap, control for role where possible, report sample size.
>
> **Action:** design an objective-focused post-game coaching prompt.
>
> **Success metric:** change in objective participation and 7-day repeat activity.

Avoid claiming causality from observational synthetic data. Use language such as “associated with”, “correlated with” and “consistent with”.

## 🛠 Recommended stack

- Python: pandas, numpy, matplotlib, scipy, seaborn (optional)
- SQL: PostgreSQL / DuckDB / SQLite
- BI: Power BI or Tableau
- GitHub: README + notebooks + SQL + dashboard screenshots

## 📁 Repository structure

```text
soloq_analytics_portfolio/
├── data/
│   └── raw/
├── dashboard/
│   └── dashboard_spec.md
├── docs/
│   ├── business_case.md
│   ├── data_dictionary.md
│   └── methodology.md
├── notebooks/
│   └── 01_analysis_template.ipynb
├── sql/
│   └── analysis.sql
├── src/
│   ├── generate_data.py
│   └── data_quality.py
└── README.md
```

## 🚀 GitHub checklist

Before publishing, add:

- dashboard screenshots
- a short project GIF/video if you have one
- your final findings in the README
- a “Key Insights” section at the top
- a data-quality result table
- a clear note that the data is synthetic

## 💼 CV-ready project description

**SoloQ Pulse — Competitive Analytics | Python, SQL, Power BI**  
Built an end-to-end analytics case study using 18K participant records and match-level data; modeled KPIs, segmented players, analyzed champion/role performance and designed an executive dashboard linking behavioral metrics to product actions.
