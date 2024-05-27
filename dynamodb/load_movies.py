import json

from dynamodb_helpers import *
from core import DecimalEncoder
dynamo_resource = get_dynamodb_resource()

movies_table = get_movies_table(dynamo_resource)

movie_item = get_movie_item(movies_table, 1994, "The Shawshank Redemption")

#movies_by_year = query_movies_by_year(movies_table, 1994)
# Load data from DynamoDB
raw_data_path = get_raw_data_path()
raw_data_path.mkdir(parents=True, exist_ok=True)

dec_encoder= DecimalEncoder()
# Save data in JSON 
with open(raw_data_path / 'rawdata.json', 'w') as f:
    json.dump(movie_item, f, cls=dec_encoder)

print(f"Movie data saved to {raw_data_path / 'rawdata.json'}")