
import numpy as np
import pandas as pd
import sys

from utils import save2pkl, line_notify

#==============================================================================
# preprocess conference games mens
#==============================================================================

def main():

    # load csv
    ConferenceTourneyGames = pd.read_csv('../input/mens/MDataFiles_Stage1/MConferenceTourneyGames.csv')

    # label encoding
    ConferenceTourneyGames['ConfAbbrev'] = ConferenceTourneyGames['ConfAbbrev'].map(ConferenceTourneyGames['ConfAbbrev'].value_counts())

    # rename columns
    ConferenceTourneyGames.rename({'ConfAbbrev':'ConfAbbrev_game'},inplace=True)

    # save pkl
    save2pkl('../feats/conference_game_mens.pkl', ConferenceTourneyGames)

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()