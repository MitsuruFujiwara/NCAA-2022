
import numpy as np
import pandas as pd
import sys

from utils import save2pkl, line_notify
from utils import BASE_DIR

#==============================================================================
# preprocess results mens
#==============================================================================

def main():

    # load csv
    TourneyCompactResults = pd.read_csv(f'{BASE_DIR}/MNCAATourneyCompactResults.csv')
    RegularSeasonCompactResults = pd.read_csv(f'{BASE_DIR}/MRegularSeasonCompactResults.csv')
    SecondaryTourneyCompactResults = pd.read_csv(f'{BASE_DIR}/MSecondaryTourneyCompactResults.csv')
    SampleSubmission = pd.read_csv(f'{BASE_DIR}/MSampleSubmissionStage1.csv')

    # drop unnecessary columns
    SecondaryTourneyCompactResults.drop('SecondaryTourney',axis=1,inplace=True)

    # merge season & tourney
    df_w = TourneyCompactResults.append(RegularSeasonCompactResults)
    df_w = df_w.append(SecondaryTourneyCompactResults)
    del TourneyCompactResults, RegularSeasonCompactResults, SecondaryTourneyCompactResults

    # drop unnecessary columns
    df_w.drop(['NumOT'],axis=1,inplace=True)

    # merge inverse data
    df_l = df_w.copy()
    df_l.columns = ['Season', 'DayNum', 'LTeamID', 'LScore', 'WTeamID', 'WScore', 'WLoc']
    df = df_w.append(df_l)

    del df_w, df_l

    # add target
    df['target'] = df['WScore'] - df['LScore']

    # drop score
    df.drop(['WScore','LScore'],axis=1,inplace=True)

    # add ID
    df['ID'] = df['Season'].astype(str) +'_'+ df['WTeamID'].astype(str) +'_'+ df['LTeamID'].astype(str)

    # split ID
    SampleSubmission['Season'] = SampleSubmission['ID'].apply(lambda x: x[:4]).astype(int)
    SampleSubmission['WTeamID'] = SampleSubmission['ID'].apply(lambda x: x[5:9]).astype(int)
    SampleSubmission['LTeamID'] = SampleSubmission['ID'].apply(lambda x: x[10:14]).astype(int)

    # add test flag
    df['is_test'] = False
    SampleSubmission['is_test'] = True

    # merge 
    df = df.append(SampleSubmission.drop('Pred',axis=1))

    # save pkl
    save2pkl('../feats/result_mens.pkl', df)

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()