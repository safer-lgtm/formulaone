import os
import sys
import pytest
import configparser
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Add the formulaone model directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from formulaone.dynamodb_helpers import (
    get_dynamodb_resource,
    list_dynamodb_tables,
    get_movies_table,
    get_movie_item,
    query_movies_by_year
)

def test_aws_config_keys():
    """Test the necessary AWS config keys."""
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '../config.ini'))
    assert 'AWS' in config, "AWS section is missing"
    assert 'aws_access_key_id' in config['AWS'], "aws_access_key_id is missing in AWS"
    assert 'aws_secret_access_key' in config['AWS'], "aws_secret_access_key is missing in AWS"
    assert 'region_name' in config['AWS'], "region_name is missing in AWS"

def test_dynamodb_config_keys():
    """Test the necessary DynamoDB config keys."""
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '../config.ini'))
    assert 'DYNAMODB' in config, "DYNAMODB section is missing"
    assert 'table_name' in config['DYNAMODB'], "table_name is missing in DYNAMODB"

def test_dynamodb_connection():
    """Test the DynamoDB connection using the provided credentials and configuration."""
    # Read the config file
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '../config.ini'))

    # Credentials and region
    aws_access_key_id = config['AWS']['aws_access_key_id']
    aws_secret_access_key = config['AWS']['aws_secret_access_key']
    region_name = config['AWS']['region_name']
    table_name = config['DYNAMODB']['table_name']

    # Create session with credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name 
    )

    # DynamoDB object resource
    dynamo_resource = session.resource('dynamodb')

    # Describe the table
    try:
        table = dynamo_resource.Table(table_name)
        response = table.table_status
        assert response in ['ACTIVE', 'CREATING', 'UPDATING', 'DELETING'], "Table status should be valid"
    except NoCredentialsError:
        assert False, "NO CREDENTIALS FOUND!"
    except PartialCredentialsError:
        assert False, "INCOMPLETE CREDENTIALS!!"
    except Exception as e:
        assert False, f"UNEXPECTED ERROR: {str(e)}"

def test_dynamodb_resource():
    """Test the DynamoDB resource initialization."""
    dynamo_resource = get_dynamodb_resource()
    assert dynamo_resource is not None, "DynamoDB resource should be initialized"

if __name__ == "__main__":
    pytest.main()
