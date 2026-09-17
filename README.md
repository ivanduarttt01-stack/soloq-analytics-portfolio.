# 🎮 SoloQ Pulse — Competitive Analytics

<p align="center">
  <strong>End-to-end Data Analytics portfolio project</strong><br>
  Python · SQL · Power BI · Data Quality · Product Analytics
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Analytics-informational?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/SQL-Analysis-informational?logo=postgresql" alt="SQL">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-informational?logo=powerbi" alt="Power BI">
  <img src="https://img.shields.io/badge/Data-Quality-informational" alt="Data Quality">
</p>

---

## 📌 Project overview

**SoloQ Pulse** is a fictional analytics case study designed to reproduce the type of work a Data Analyst, BI Analyst or Product Analyst could perform for a competitive-gaming platform.

The objective is not simply to create charts. The project follows a complete analytical workflow:

**Business question → data validation → transformation → SQL/Python analysis → KPI → dashboard → business insight → action → measurement**

> ⚠️ **Data disclaimer:** all observations are synthetic and generated specifically for this portfolio. They are not Riot Games, OP.GG or real-player data.

---

## 🎯 Business problem

A fictional product team wants to understand:

- Which player behaviors are associated with winning?
- How do role, champion and play style relate to performance?
- Which players show consistent performance over time?
- How important are objectives compared with raw combat statistics?
- Which metrics could be used to improve post-game feedback and player engagement?

The analysis is designed to answer these questions with evidence rather than isolated visualizations.

---

## 📊 Dataset at a glance

| Dataset | Records | Description |
|---|---:|---|
| `matches` | 1,800 | Match context, duration, patch, MMR balance and result |
| `match_participants` | 18,000 | Player-level combat, CS, vision, gold and objective metrics |
| `players` | 80 | Account, tier, role, region and play-style attributes |
| `champions` | 40 | Champion class, role, difficulty and pick/ban assumptions |
| `match_objectives` | 1,800 | Dragons, Barons and towers by team |

### Core analytical dimensions

**Performance**
- Win rate
- KDA
- Kill participation
- CS/min
- Gold/min
- Damage/min
- Vision score/min
- Objective participation

**Context**
- Role
- Tier
- Champion
- Champion class
- Patch
- Match duration
- Player style

**Engagement**
- Matches per player
- Monthly activity
- Repeat activity
- Session intensity

---

## 🔎 Analytical questions

### 01 — Winning behavior
What player-level metrics are most strongly associated with match outcome?

### 02 — Player performance
Which players are consistently above or below their relevant peer group?

### 03 — Champion intelligence
How do champion role, difficulty, sample size and win rate interact?

### 04 — Objective impact
Is objective participation associated with winning after considering role and game context?

### 05 — Engagement
What behavioral signals could indicate changes in player activity?

---

## 🧪 Data quality

Data quality is treated as part of the analysis rather than an afterthought.

The project includes automated checks for:

- duplicate records
- null values
- invalid win flags
- impossible durations
- invalid K/D/A values
- participant counts
- referential integrity
- champion/player consistency
- objective consistency

Run the quality checks before using the data for the dashboard.

Results are documented in:

`docs/data_quality_results.csv`

---

## 🐍 Python analysis

Main notebook:

`notebooks/01_analysis_template.ipynb`

The notebook is structured around:

1. Data loading
2. Data validation
3. Cleaning
4. Feature engineering
5. Descriptive statistics
6. Exploratory analysis
7. Player segmentation
8. Champion/role analysis
9. Objective analysis
10. Statistical testing
11. Business interpretation

The goal is to keep the analysis **reproducible and explainable**.

---

## 🗄️ SQL analysis

Main SQL file:

`sql/analysis.sql`

The queries cover:

- KPI extraction
- player rankings
- champion performance
- role comparisons
- objective analysis
- temporal trends
- aggregation logic

SQL is used to demonstrate that the analysis can be performed directly at the data layer rather than only inside Python.

---

## 📈 Dashboard

The planned BI layer contains four views:

### Executive Overview
- Win rate
- Average MMR
- Match volume
- Average KDA
- Objective control
- Performance trend

### Player Performance
- Player ranking
- Win rate
- KDA
- CS/min
- Vision
- Objective participation
- Performance segmentation

### Champion Intelligence
- Pick rate
- Win rate
- Role
- Sample size
- Difficulty
- Performance volatility

### Engagement
- Active players
- Matches per player
- Monthly activity
- Repeat-player rate
- Activity signals

Dashboard specification:

`dashboard/dashboard_spec.md`

> Add final Power BI/Tableau screenshots to `images/` and embed them here once the dashboard is completed.

---

## 💡 From metric to business decision

A strong analytics project should connect every important finding to an action.

Example framework:

| Finding | Evidence | Potential action | Success metric |
|---|---|---|---|
| Higher objective participation is associated with higher win rate | Compare groups + sample size | Objective-focused feedback | Objective participation |
| Some players outperform their peer group consistently | Peer-normalized KPIs | Personalized performance feedback | Performance consistency |
| Certain champion/role combinations show different outcomes | Role-adjusted champion analysis | Improve recommendations | Win rate / adoption |

**Important:** observational analysis does not prove causality. Findings should therefore be described as associations unless a causal experiment is performed.

---

## 🧱 Project architecture

```text
soloq-analytics-portfolio/
│
├── data/
│   └── raw/
│       ├── matches.csv
│       ├── match_participants.csv
│       ├── players.csv
│       ├── champions.csv
│       └── match_objectives.csv
│
├── dashboard/
│   └── dashboard_spec.md
│
├── docs/
│   ├── business_case.md
│   ├── data_dictionary.md
│   ├── methodology.md
│   └── data_quality_results.csv
│
├── images/
│   └── dashboard screenshots go here
│
├── notebooks/
│   └── 01_analysis_template.ipynb
│
├── sql/
│   └── analysis.sql
│
├── src/
│   ├── generate_data.py
│   └── data_quality.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🛠️ Tech stack

| Tool | Purpose |
|---|---|
| Python | Cleaning, EDA, feature engineering |
| Pandas / NumPy | Data manipulation |
| Matplotlib / Seaborn | Visualization |
| SciPy | Statistical analysis |
| SQL | Data extraction and KPI logic |
| Power BI / Tableau | Business dashboard |
| Git / GitHub | Version control and portfolio delivery |

---

## 🚀 Reproducibility

The dataset can be regenerated using:

```bash
python src/generate_data.py
```

Data quality checks:

```bash
python src/data_quality.py
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📚 Documentation

- `docs/business_case.md` — business context and analytical objectives
- `docs/data_dictionary.md` — dataset and field definitions
- `docs/methodology.md` — analytical methodology
- `docs/data_quality_results.csv` — automated validation results
- `dashboard/dashboard_spec.md` — dashboard design specification

---

## 📌 Portfolio roadmap

- [x] Synthetic dataset generation
- [x] Data quality framework
- [x] SQL analysis foundation
- [x] Python analysis template
- [x] Business case
- [ ] Complete exploratory analysis
- [ ] Finalize statistical analysis
- [ ] Build Power BI dashboard
- [ ] Add dashboard screenshots
- [ ] Write final findings
- [ ] Add executive summary
- [ ] Publish final case study

---

## 💼 CV-ready description

**SoloQ Pulse — Competitive Analytics | Python, SQL, Power BI**

Built an end-to-end analytics case study using 18K player-match records and 1.8K matches, including data-quality validation, KPI modeling, player segmentation, champion/role analysis, objective analysis and an executive BI dashboard designed to translate behavioral patterns into measurable product actions.

---

<p align="center">
  <sub>Built as a Data Analytics portfolio project · Synthetic data · Reproducible workflow</sub>
</p>
