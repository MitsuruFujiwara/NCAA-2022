
import numpy as np
import pandas as pd
import sys

from utils import loadpkl, to_feature, to_json, line_notify

#==============================================================================
# preprocess results mens
#==============================================================================

def main():

    # load pkls
    df = loadpkl('../feats/result_mens.pkl')
    Teams = loadpkl('../feats/teams_mens.pkl')
    Seasons = loadpkl('../feats/seasons_mens.pkl')
    TourneySeeds = loadpkl('../feats/seeds_mens.pkl')
    Cities = loadpkl('../feats/cities_mens.pkl')
    GameCities = loadpkl('../feats/game_cities_mens.pkl')
    MasseyOrdinals = loadpkl('../feats/massey_ordinals_mens.pkl')
    TeamCoaches = loadpkl('../feats/coaches_mens.pkl')
    Conferences = loadpkl('../feats/conferences_mens.pkl')
    ConferenceTourneyGames = loadpkl('../feats/conference_game_mens.pkl')

    # merge teams
    Teams_w = Teams.copy()
    Teams_l = Teams.copy()

    Teams_w.columns = ['WTeamID', 'Teams_FirstD1Season_W', 'Teams_LastD1Season_W','Teams_diff_D1Season_W']
    Teams_l.columns = ['LTeamID', 'Teams_FirstD1Season_L', 'Teams_LastD1Season_L','Teams_diff_D1Season_L']

    df = df.merge(Teams_w,on='WTeamID',how='left')
    df = df.merge(Teams_l,on='LTeamID',how='left')

    # merge seasons
    df = df.merge(Seasons,on='Season',how='left')

    # merge tourney seeds
    TourneySeeds_w = TourneySeeds.copy() 
    TourneySeeds_l = TourneySeeds.copy()
    
    TourneySeeds_w.columns = ['Season', 'WTeamID', 'region_W', 'seed_in_region_W', 'seed_in_region2_W']
    TourneySeeds_l.columns = ['Season', 'LTeamID', 'region_L', 'seed_in_region_L', 'seed_in_region2_L']

    df = df.merge(TourneySeeds_w,on=['Season', 'WTeamID'],how='left')
    df = df.merge(TourneySeeds_l,on=['Season', 'LTeamID'],how='left')

    # merge game cities
    GameCities = GameCities.merge(Cities,on='CityID',how='left').drop('CityID',axis=1)

    df = df.merge(GameCities,on=['Season','DayNum','WTeamID','LTeamID'],how='left')

    # merge massey ordinals
    MasseyOrdinals_w = MasseyOrdinals.copy()
    MasseyOrdinals_l = MasseyOrdinals.copy()

    MasseyOrdinals_w.columns = ['Season', 'DayNum', 'WTeamID', 'OrdinalRank_W']
    MasseyOrdinals_l.columns = ['Season', 'DayNum', 'LTeamID', 'OrdinalRank_L']

    df = df.merge(MasseyOrdinals_w,on=['Season','DayNum','WTeamID'],how='left')
    df = df.merge(MasseyOrdinals_l,on=['Season','DayNum','LTeamID'],how='left')

    # merge team coaches
    TeamCoaches_w = TeamCoaches.copy()
    TeamCoaches_l = TeamCoaches.copy()

    TeamCoaches_w.columns = ['Season', 'WTeamID', 'days_coaches_W']
    TeamCoaches_l.columns = ['Season', 'LTeamID', 'days_coaches_L']

    df = df.merge(TeamCoaches_w,on=['Season','WTeamID'],how='left')
    df = df.merge(TeamCoaches_l,on=['Season','LTeamID'],how='left')

    # merge conferences
    Conferences_w = Conferences.copy()
    Conferences_l = Conferences.copy()

    Conferences_w.columns = ['Season', 'WTeamID', 'ConfAbbrev_W']
    Conferences_l.columns = ['Season', 'LTeamID', 'ConfAbbrev_L']

    df = df.merge(Conferences_w,on=['Season','WTeamID'],how='left')
    df = df.merge(Conferences_l,on=['Season','LTeamID'],how='left')

    # merge conferences tourney games
    df = df.merge(ConferenceTourneyGames,on=['Season','DayNum','WTeamID','LTeamID'],how='left')

    # save as feather
    to_feature(df, '../feats/f101')

    # save feature name list
    features_json = {'features':df.columns.tolist()}
    to_json(features_json,'../configs/101_all_features_mens.json')

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()