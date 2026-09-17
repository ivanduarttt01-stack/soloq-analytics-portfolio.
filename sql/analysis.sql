-- SoloQ Pulse — SQL practice
-- Complete every TODO and explain the business meaning of each result.

-- 1) Basic match KPIs
SELECT
  COUNT(*) AS matches,
  ROUND(AVG(duration_min), 2) AS avg_duration,
  ROUND(AVG(team_a_avg_mmr), 2) AS avg_team_a_mmr,
  ROUND(AVG(team_b_avg_mmr), 2) AS avg_team_b_mmr
FROM matches;

-- 2) Participant KPIs
SELECT
  COUNT(*) AS participant_rows,
  ROUND(AVG((kills + assists) / NULLIF(deaths, 0)), 2) AS avg_kda_raw,
  ROUND(AVG(cs / NULLIF(duration_min, 0)), 2) AS avg_cs_per_min
FROM match_participants mp
JOIN matches m USING (match_id);

-- TODO 3: Win rate by role.

-- TODO 4: Win rate by tier.

-- TODO 5: Monthly active players.

-- TODO 6: Top champions by pick volume with a minimum sample threshold.

-- TODO 7: Champion win rate by role.

-- TODO 8: Objective participation bands vs win rate.

-- TODO 9: Player leaderboard with matches, wins, win rate, KDA and CS/min.

-- TODO 10: Identify players whose recent monthly activity is lower than their prior monthly activity.

-- TODO 11: Compare aggressive vs scaling play styles while controlling descriptively for role.

-- TODO 12: Create a final “executive KPI” query returning one row.
