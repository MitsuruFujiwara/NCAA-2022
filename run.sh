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
python 006_cities_mens.py
python 007_game_cities_mens.py
python 008_massey_ordinals_mens.py
python 009_coaches_mens.py
python 010_conferences_mens.py
python 011_conference_games_mens.py

python 101_aggregate_mens.py

python 201_train_lgbm_mens.py