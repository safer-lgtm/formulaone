# content of test_sample.py
import os
import sys

# add the formulaone model directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from formulaone.sample.helpers import get_tidy_data_path
from dynamodb.helpers import get_tidy_data_path


import pandas as pd

def test_check_dataframe_size():
    df = pd.read_parquet(get_tidy_data_path() / 'current_race.parquet')
    assert df.shape[1] == 26

def test_file_format():
    # Assuming get_tidy_data_path returns a Path object
    file_path = get_tidy_data_path() / 'current_race.parquet'
    # Check if the file extension is .parquet
    assert file_path.suffix == '.parquet', "File format should be .parquet"
