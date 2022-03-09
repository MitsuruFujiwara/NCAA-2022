#!/bin/sh
cd feats
rm *.feather
rm *.pkl
cd ../src

python 001_results_mens.py
python 002_teams_mens.py
python 003_seasons_mens.py
python 004_seeds_mens.py
python 005_cities_mens.py
python 006_game_cities_mens.py
python 007_massey_ordinals_mens.py
python 008_coaches_mens.py
python 009_conferences_mens.py
python 010_conference_games_mens.py

python 101_aggregate_mens.py