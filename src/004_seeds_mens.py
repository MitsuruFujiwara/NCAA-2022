
import numpy as np
import pandas as pd
import sys

from utils import save2pkl, line_notify
from utils import DICT_SEED

#==============================================================================
# preprocess seeds mens
#==============================================================================

def main():

    # load csv
    TourneySeeds = pd.read_csv('../input/mens/MDataFiles_Stage1/MNCAATourneySeeds.csv')

    # split seeds
    TourneySeeds['region'] = TourneySeeds['Seed'].apply(lambda x: x[0])
    TourneySeeds['seed_in_region'] = TourneySeeds['Seed'].apply(lambda x: x[1:3]).astype(int)
    TourneySeeds['seed_in_region2'] = TourneySeeds['Seed'].apply(lambda x: x[-1]).map(DICT_SEED)

    # drop seed
    TourneySeeds.drop('Seed',axis=1,inplace=True)

    # save pkl
    save2pkl('../feats/seeds_mens.pkl', TourneySeeds)

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()