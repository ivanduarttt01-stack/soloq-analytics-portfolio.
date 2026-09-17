from pathlib import Path
import numpy as np, pandas as pd

SEED = 42
rng = np.random.default_rng(SEED)
BASE = Path(__file__).resolve().parents[1]
RAW = BASE / 'data' / 'raw'
RAW.mkdir(parents=True, exist_ok=True)

champions = [
('Ahri','Mage','Mid'),('Aatrox','Fighter','Top'),('Ashe','Marksman','Bottom'),('Thresh','Support','Support'),('Lee Sin','Fighter','Jungle'),('Jinx','Marksman','Bottom'),('Orianna','Mage','Mid'),('Malphite','Tank','Top'),('Nautilus','Tank','Support'),('Viego','Fighter','Jungle'),('Caitlyn','Marksman','Bottom'),('Leona','Tank','Support'),('Yasuo','Fighter','Mid'),('Jarvan IV','Fighter','Jungle'),('Gnar','Fighter','Top'),('Kai’Sa','Marksman','Bottom'),('Lulu','Enchanter','Support'),('Kha’Zix','Assassin','Jungle'),('Camille','Fighter','Top'),('Syndra','Mage','Mid'),('Ezreal','Marksman','Bottom'),('Morgana','Mage','Support'),('Graves','Marksman','Jungle'),('Renekton','Fighter','Top'),('Viktor','Mage','Mid'),('Xayah','Marksman','Bottom'),('Rakan','Enchanter','Support'),('Sejuani','Tank','Jungle'),('Darius','Fighter','Top'),('Akali','Assassin','Mid'),('Lucian','Marksman','Bottom'),('Braum','Support','Support'),('Nocturne','Assassin','Jungle'),('Ornn','Tank','Top'),('Twisted Fate','Mage','Mid'),('Tristana','Marksman','Bottom'),('Alistar','Tank','Support'),('Elise','Mage','Jungle'),('Fiora','Fighter','Top'),('Vex','Mage','Mid')]
champ_df = pd.DataFrame(champions, columns=['champion','class','primary_role'])
champ_df['pick_rate_base'] = np.round(rng.uniform(.02,.10,len(champ_df)),4)
champ_df['ban_rate_base'] = np.round(rng.uniform(.01,.12,len(champ_df)),4)
champ_df['difficulty_score'] = rng.integers(1,6,len(champ_df))
champ_df.to_csv(RAW/'champions.csv', index=False, encoding='utf-8-sig')

regions=['LAS','LAN','BR','NA','EUW']; styles=['Aggressive','Objective','Vision','Scaling','Roamer']; roles=['Top','Jungle','Mid','Bottom','Support']
tier_probs=[.08,.16,.22,.20,.16,.13,.05]; tiers=['Bronze','Silver','Gold','Platinum','Emerald','Diamond','Master']; tier_base=dict(zip(tiers,[1050,1250,1450,1650,1820,2050,2250]))
pl=[]
for i in range(1,81):
    tier=rng.choice(tiers,p=tier_probs); pl.append({'player_id':f'P{i:03d}','summoner_name':f'Player_{i:03d}','region':rng.choice(regions,p=[.40,.10,.18,.14,.18]),'tier':tier,'current_mmr':int(rng.normal(tier_base[tier],75)),'main_role':rng.choice(roles,p=[.19,.19,.23,.21,.18]),'play_style':rng.choice(styles,p=[.25,.22,.16,.20,.17]),'account_age_months':int(rng.integers(4,73)),'daily_active_target':int(rng.integers(1,6))})
players=pd.DataFrame(pl); players.to_csv(RAW/'players.csv',index=False,encoding='utf-8-sig')

N=1800
match_ids=np.array([f'M{i:05d}' for i in range(1,N+1)])
dt=pd.to_datetime('2026-01-01')+pd.to_timedelta(rng.random(N)*(pd.Timestamp('2026-09-15')-pd.Timestamp('2026-01-01')).total_seconds(),unit='s')
duration=np.clip(rng.normal(28,6,N),16,48).round().astype(int)
surrender=((duration<25)&(rng.random(N)<.08)).astype(int)
# assemble teams with repeated sampling; no need strict player uniqueness across entire match after vector generation because within-match uniqueness handled by per-match choices below
mmr_map=players.set_index('player_id').current_mmr.to_dict(); role_map=players.set_index('player_id').main_role.to_dict()
rows=[]; obj=[]; match_rows=[]
for j,mid in enumerate(match_ids):
    ps=rng.choice(players.player_id.values,10,replace=False); A=ps[:5]; B=ps[5:]
    mmr=np.mean([mmr_map[x] for x in A]), np.mean([mmr_map[x] for x in B])
    p=1/(1+np.exp(-(mmr[0]-mmr[1])/180)); winA=int(rng.random()<p)
    patch=rng.choice(['26.5','26.6','26.7','26.8','26.9'],p=[.10,.16,.22,.26,.26])
    match_rows.append({'match_id':mid,'match_datetime':dt[j].strftime('%Y-%m-%d %H:%M:%S'),'duration_min':int(duration[j]),'surrendered':int(surrender[j]),'team_a_avg_mmr':round(mmr[0],1),'team_b_avg_mmr':round(mmr[1],1),'team_a_win':winA,'patch':patch})
    for t,team in [('A',A),('B',B)]:
        team_win=int((t=='A' and winA) or (t=='B' and not winA))
        for pid in team:
            role=role_map[pid]; mmr_player=mmr_map[pid]
            pool=champ_df[champ_df.primary_role==role]
            champ=pool.iloc[int(rng.integers(len(pool)))]
            skill=max(0,(mmr_player-1200)/600)
            kills=int(np.clip(rng.poisson(max(.5,5+2.5*skill+2*team_win)),0,18)); deaths=int(np.clip(rng.poisson(max(.8,6-1.2*skill+(0 if team_win else .6))),1,14)); assists=int(np.clip(rng.poisson(5+(3 if role=='Support' else 0)+(3*team_win)),0,22))
            cs_min={'Top':7.0,'Jungle':5.2,'Mid':7.4,'Bottom':8.1,'Support':1.4}[role]
            cs=int(np.clip(rng.normal(cs_min*duration[j]*(1.02 if team_win else .96),18),8,320)); vision=int(np.clip(rng.normal(8+duration[j]*.8+(6 if role=='Support' else 0),7),2,90)); wards=int(np.clip(rng.poisson(2.2+(2 if role=='Support' else 0)),0,12))
            damage=int(np.clip(rng.normal(14000+kills*700+duration[j]*180+(1800 if role in ['Mid','Bottom'] else 0),3200),2500,65000)); gold=int(np.clip(rng.normal(9000+cs*18+kills*250,1000),4500,22000)); opp=float(max(0,rng.poisson(1.3+team_win+.6*(role in ['Jungle','Support'])))); lane=float(rng.normal(0,1)+(.35 if team_win else -.15))
            rows.append({'match_id':mid,'player_id':pid,'team':t,'role':role,'champion':champ.champion,'win':team_win,'kills':kills,'deaths':deaths,'assists':assists,'cs':cs,'vision_score':vision,'wards_placed':wards,'damage_to_champions':damage,'gold_earned':gold,'objective_participation':round(opp,2),'first_blood':int(rng.random()<(.13+.04*team_win)),'lane_advantage':round(lane,2)})
    dragA=int(np.clip(rng.poisson(2+(1 if winA else 0)),0,6)); dragB=int(np.clip(rng.poisson(.8+(0 if winA else 1)),0,6)); barA=int(np.clip(rng.poisson(.35+.35*winA),0,2)); barB=int(np.clip(rng.poisson(.25+.35*(not winA)),0,2)); torA=int(np.clip(rng.poisson(4+2*winA),1,11)); torB=int(np.clip(rng.poisson(4+2*(not winA)),1,11))
    obj.append({'match_id':mid,'team_a_dragons':dragA,'team_b_dragons':dragB,'team_a_barons':barA,'team_b_barons':barB,'team_a_towers':torA,'team_b_towers':torB})

a=pd.DataFrame(match_rows); b=pd.DataFrame(rows); c=pd.DataFrame(obj)
a.to_csv(RAW/'matches.csv',index=False,encoding='utf-8-sig'); b.to_csv(RAW/'match_participants.csv',index=False,encoding='utf-8-sig'); c.to_csv(RAW/'match_objectives.csv',index=False,encoding='utf-8-sig')
print(f'Generated {len(a):,} matches, {len(b):,} participant rows, {len(players):,} players, {len(champ_df):,} champions')
