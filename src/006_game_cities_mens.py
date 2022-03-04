
import numpy as np
import pandas as pd
import sys

from utils import save2pkl, line_notify

#==============================================================================
# preprocess game cities mens
#==============================================================================

def main():

    # load csv
    GameCities = pd.read_csv('../input/mens/MDataFiles_Stage1/MGameCities.csv')

    # label encoding
    GameCities['CRType'] = GameCities['CRType'].map(GameCities['CRType'].value_counts())

    # save pkl
    save2pkl('../feats/game_cities_mens.pkl', GameCities)

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()