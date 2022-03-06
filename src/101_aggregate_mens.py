
import numpy as np
import pandas as pd
import sys

from utils import loadpkl, line_notify

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

    #TODO

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()