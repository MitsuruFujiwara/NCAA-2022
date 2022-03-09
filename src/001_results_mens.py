
import numpy as np
import pandas as pd
import sys

from utils import save2pkl, line_notify
from utils import BASE_DIR, DICT_LOC

#==============================================================================
# preprocess results mens
#==============================================================================

def main():

    # load csv
    TourneyCompactResults = pd.read_csv(f'{BASE_DIR}/MNCAATourneyCompactResults.csv')
    RegularSeasonCompactResults = pd.read_csv(f'{BASE_DIR}/MRegularSeasonCompactResults.csv')
    SecondaryTourneyCompactResults = pd.read_csv(f'{BASE_DIR}/MSecondaryTourneyCompactResults.csv')
    MSampleSubmissionStage1 = pd.read_csv(f'{BASE_DIR}/MSampleSubmissionStage1.csv')

    # drop unnecessary columns
    SecondaryTourneyCompactResults.drop('SecondaryTourney',axis=1,inplace=True)

    # merge season & tourney
    df_w = TourneyCompactResults.append(RegularSeasonCompactResults)
    df_w = df_w.append(SecondaryTourneyCompactResults)
    del TourneyCompactResults, RegularSeasonCompactResults, SecondaryTourneyCompactResults

    # drop unnecessary columns
    df_w.drop('NumOT',axis=1,inplace=True)

    # merge inverse data
    df_l = df_w.copy()
    df_l.columns = ['Season', 'DayNum', 'LTeamID', 'LScore', 'WTeamID', 'WScore', 'WLoc']
    df = df_w.append(df_l)

    del df_w, df_l

    # add target
    df['target'] = df['WScore'] - df['LScore']

    # add ID
    df['ID'] = df['Season'].astype(str) +'_'+ df['WTeamID'].astype(str) +'_'+ df['LTeamID'].astype(str)

    # to numeric
    df['WLoc'] = df['WLoc'].map(DICT_LOC)

    # save pkl
    save2pkl('../feats/result_mens.pkl', df)

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()