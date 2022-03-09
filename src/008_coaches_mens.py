
import numpy as np
import pandas as pd
import sys

from utils import save2pkl, line_notify
from utils import BASE_DIR

#==============================================================================
# preprocess coaches mens
#==============================================================================

def main():

    # load csv
    TeamCoaches = pd.read_csv(f'{BASE_DIR}/MTeamCoaches.csv')

    # add days coaches
    TeamCoaches['days_coaches'] = TeamCoaches['LastDayNum'] - TeamCoaches['FirstDayNum']

    # drop unnecessary columns
    TeamCoaches.drop(['FirstDayNum','LastDayNum','CoachName'],axis=1,inplace=True)

    # save pkl
    save2pkl('../feats/coaches_mens.pkl', TeamCoaches)

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()