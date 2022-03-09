
import numpy as np
import pandas as pd
import sys

from utils import save2pkl, line_notify
from utils import BASE_DIR

#==============================================================================
# preprocess teams mens
#==============================================================================

def main():

    # load csv
    Teams = pd.read_csv(f'{BASE_DIR}/MTeams.csv')

    # add features
    Teams['diff_D1Season'] = Teams['LastD1Season'] - Teams['FirstD1Season']

    # drop team name
    Teams.drop('TeamName',axis=1,inplace=True)

    # save pkl
    save2pkl('../feats/teams_mens.pkl', Teams)

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()