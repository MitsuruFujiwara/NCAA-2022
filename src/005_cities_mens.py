
import numpy as np
import pandas as pd
import sys

from utils import save2pkl, line_notify

#==============================================================================
# preprocess cities mens
#==============================================================================

def main():

    # load csv
    Cities = pd.read_csv('../input/mens/MDataFiles_Stage1/Cities.csv')

    # label encoding
    Cities['State'] = Cities['State'].map(Cities['State'].value_counts())

    # drop city name
    Cities.drop('City',axis=1,inplace=True)

    # save pkl
    save2pkl('../feats/cities_mens.pkl', Cities)

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()