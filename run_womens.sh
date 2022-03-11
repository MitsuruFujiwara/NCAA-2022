#!/bin/sh
cd feats
rm *.feather
rm *.pkl
cd ../src

python 011_tourney_results_womens.py
python 012_season_results_womens.py
python 013_seasons_womens.py
python 014_seeds_womens.py
python 015_conferences_womens.py

python 102_aggregate_womens.py