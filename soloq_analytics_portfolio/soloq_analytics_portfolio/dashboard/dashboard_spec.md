# Dashboard specification

## Page 1 — Executive Overview

**Header KPIs:** Matches | Players | Win Rate | Avg. Duration | Avg. MMR

**Visuals:**
1. Monthly match volume
2. Win rate by tier
3. Win rate by role
4. Objective participation vs. win rate
5. Match duration distribution

**Executive callout:** one text box with the strongest evidence-backed finding.

## Page 2 — Player Intelligence

Filters: month, tier, region, role, play style

Visuals:
- Scatter: CS/min vs. win rate
- Scatter: vision/min vs. win rate
- Boxplot: KDA by role
- Player leaderboard with minimum sample-size filter
- Segment distribution

## Page 3 — Champion Intelligence

Filters: role, tier, patch

Visuals:
- Pick rate vs. win rate scatter
- Champion table with sample size
- Difficulty vs. win rate
- Champion consistency by role

**Guardrail:** do not rank champions from tiny samples. Use a minimum pick threshold.

## Page 4 — Engagement

Visuals:
- Monthly active players
- Matches/player by tier
- Repeat-player rate
- Activity distribution
- Optional “at-risk” rule based on declining activity (descriptive, not predictive)

## Design

Use a dark competitive-game aesthetic with restrained accent colors, large KPI cards, clear hierarchy and generous spacing. Keep chart count low enough that every visual has a question to answer.
