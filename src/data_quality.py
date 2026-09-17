from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / 'data' / 'raw'

matches = pd.read_csv(RAW / 'matches.csv')
participants = pd.read_csv(RAW / 'match_participants.csv')
players = pd.read_csv(RAW / 'players.csv')
champions = pd.read_csv(RAW / 'champions.csv')
objectives = pd.read_csv(RAW / 'match_objectives.csv')

checks = []
def add(name, passed, detail):
    checks.append({'check': name, 'passed': bool(passed), 'detail': detail})

add('unique_match_id', matches.match_id.is_unique, f"duplicates={matches.match_id.duplicated().sum()}")
add('10_participants_per_match', participants.groupby('match_id').size().eq(10).all(), f"bad_matches={(participants.groupby('match_id').size()!=10).sum()}")
add('unique_match_player_key', ~participants.duplicated(['match_id','player_id']).any(), f"duplicates={participants.duplicated(['match_id','player_id']).sum()}")
add('valid_binary_win', participants.win.isin([0,1]).all(), 'allowed={0,1}')
add('positive_duration', matches.duration_min.gt(0).all(), f"min={matches.duration_min.min()}")
add('non_negative_core_metrics', (participants[['kills','deaths','assists','cs','vision_score','wards_placed','damage_to_champions','gold_earned']] >= 0).all().all(), 'checked combat/economy metrics')
add('all_participants_exist', participants.player_id.isin(players.player_id).all(), 'foreign-key check to players')
add('all_champions_exist', participants.champion.isin(champions.champion).all(), 'foreign-key check to champions')
add('objectives_match_keys', objectives.match_id.isin(matches.match_id).all(), 'foreign-key check to matches')

out = pd.DataFrame(checks)
print(out.to_string(index=False))
out.to_csv(BASE / 'docs' / 'data_quality_results.csv', index=False)
print(f"\nPassed: {out.passed.sum()}/{len(out)}")
