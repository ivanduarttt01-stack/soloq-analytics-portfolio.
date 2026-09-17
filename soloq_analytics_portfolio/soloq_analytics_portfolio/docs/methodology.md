# Methodology

## Unit of analysis

There are three important grains:

- **match** — one game
- **participant** — one player's record in one game
- **player** — one account across the dataset

Always state the grain before computing a KPI.

## Recommended derived metrics

- KDA = `(kills + assists) / max(deaths, 1)`
- CS/min = `cs / duration_min`
- Damage/min = `damage_to_champions / duration_min`
- Vision/min = `vision_score / duration_min`
- Gold/min = `gold_earned / duration_min`
- Objective index = normalized combination of objective participation + team objective control
- Win rate = `wins / matches`
- Player activity = unique matches per player per month

## Statistical guidance

For group comparisons, report sample size and confidence intervals where useful. Avoid causal claims because this dataset is observational and synthetic.

Suggested tests:

- Difference in means: Welch's t-test when assumptions are acceptable
- Non-normal continuous distributions: Mann–Whitney U
- Categorical association: chi-square test
- Correlation: Spearman for ordinal/non-normal relationships

## Data-quality checks

At minimum validate:

- Unique match IDs
- Exactly 10 participants per match
- No impossible negative values
- Valid role / tier / region categories
- Win variable is binary
- Duration is within an explicit analytical range
- No duplicated participant keys `(match_id, player_id)`
