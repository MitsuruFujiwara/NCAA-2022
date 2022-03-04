
import numpy as np
import pandas as pd
import sys

from utils import save2pkl, line_notify

#==============================================================================
# preprocess massaey ordinals mens
#==============================================================================

def main():

    # load csv
    MasseyOrdinals = pd.read_csv('../input/mens/MDataFiles_Stage1/MMasseyOrdinals.csv')

    # TODO

    # save pkl
    save2pkl('../feats/massey_ordinals_mens.pkl', MasseyOrdinals)

    # LINE notify
    line_notify('{} done.'.format(sys.argv[0]))

if __name__ == '__main__':
    main()