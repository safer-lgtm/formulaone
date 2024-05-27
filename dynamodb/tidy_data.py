import json

from dynamodb_helpers import *

raw_data_path = get_raw_data_path()
raw_data_path.mkdir(parents=True, exist_ok=True)

tidy_data_path = get_tidy_data_path()
tidy_data_path.mkdir(parents=True, exist_ok=True)


with open(get_raw_data_path() / 'rawdata.json', 'r') as f:
    movie_item = json.load(f)

if not isinstance(movie_item, list):
    movie_item = [movie_item]

tidy_movies = tidy_movie_data(movie_item)

tidy_movies.to_parquet(tidy_data_path / 'current_race.parquet')
