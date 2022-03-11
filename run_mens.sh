#!/bin/sh
cd feats
rm *.feather
rm *.pkl
cd ../src

python 001_tourney_results_mens.py
python 002_season_results_mens.py
python 003_teams_mens.py
python 004_seasons_mens.py
python 005_seeds_mens.py
python 006_massey_ordinals_mens.py
python 007_coaches_mens.py
python 008_conferences_mens.py

python 101_aggregate_mens.py
python 103_aggregate_mens_simple.py

python 201_train_lgbm_mens.py
python 203_train_lgbm_mens_simple.py