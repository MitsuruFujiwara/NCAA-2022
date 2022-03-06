
import feather
import gc
import json
import os
import pandas as pd
import numpy as np
import requests
import pickle

from glob import glob
from multiprocessing import Pool, cpu_count
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from time import time, sleep
from tqdm import tqdm

#==============================================================================
# utils
#==============================================================================

NUM_FOLDS = 5

FEATS_EXCLUDED = []

COMPETITION_NAME_M = 'mens-march-mania-2022'
COMPETITION_NAME_W = 'womens-march-mania-2022'

# dict for location
DICT_LOC = {'H':1, 'A':-1, 'N':0}

# dict for seed
DICT_SEED = {'a':0, 'b':1}

# save pkl
def save2pkl(path, df):
    f = open(path, 'wb')
    pickle.dump(df, f)
    f.close

# load pkl
def loadpkl(path):
    f = open(path, 'rb')
    out = pickle.load(f)
    return out

# to feather
def to_feature(df, path):
    if df.columns.duplicated().sum()>0:
        raise Exception('duplicated!: {}'.format(df.columns[df.columns.duplicated()]))
    df.reset_index(inplace=True)
    df.columns = [c.replace('/', '-').replace(' ', '-') for c in df.columns]
    for c in df.columns:
        df[[c]].to_feather('{}_{}.feather'.format(path,c))
    return

# rmse
def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

# LINE Notify
def line_notify(message):
    f = open('../input/line_token.txt')
    token = f.read()
    f.close
    line_notify_token = token.replace('\n', '')
    line_notify_api = 'https://notify-api.line.me/api/notify'

    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    print(message)

# API submission https://github.com/KazukiOnodera/Home-Credit-Default-Risk/blob/master/py/utils.py
def submit(file_path, is_men=True, comment='from API'):
    if is_men:
        COMPETITION_NAME = COMPETITION_NAME_M
    else:
        COMPETITION_NAME = COMPETITION_NAME_W

    os.system('kaggle competitions submit -c {} -f {} -m "{}"'.format(COMPETITION_NAME,file_path,comment))
    sleep(360) # tekito~~~~
    tmp = os.popen('kaggle competitions submissions -c {} -v | head -n 2'.format(COMPETITION_NAME)).read()
    col, values = tmp.strip().split('\n')
    message = 'SCORE!!!\n'
    for i,j in zip(col.split(','), values.split(',')):
        message += '{}: {}\n'.format(i,j)
    line_notify(message.rstrip())

# save json
def to_json(data_dict, path):
    with open(path, 'w') as f:
        json.dump(data_dict, f, indent=4)