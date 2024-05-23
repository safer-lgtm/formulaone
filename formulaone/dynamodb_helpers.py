import boto3
import configparser
from boto3.dynamodb.conditions import Key

def get_config():
    """
    Reads the configuration file and returns the config object.
    
    Returns:
        config: The config object.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def get_dynamodb_resource():
    """
    Creates a DynamoDB resource using the AWS session.
    
    Returns:
        dynamo_resource: The DynamoDB resource.
    """
    config = get_config()
    aws_access_key_id = config['AWS']['aws_access_key_id']
    aws_secret_access_key = config['AWS']['aws_secret_access_key']
    region_name = config['AWS']['region_name']

    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
    
    dynamo_resource = session.resource('dynamodb')
    return dynamo_resource

def list_dynamodb_tables(dynamo_resource):
    """
    Lists all tables in the DynamoDB resource.
    
    Args:
        dynamo_resource: The DynamoDB resource.
    
    Returns:
        list: List of table names.
    """
    tables = [table.name for table in dynamo_resource.tables.all()]
    return tables

def get_movies_table(dynamo_resource):
    """
    Gets the movies table from DynamoDB.
    
    Args:
        dynamo_resource: The DynamoDB resource.
    
    Returns:
        table: The DynamoDB table resource for movies.
    """
    config = get_config()
    table_name = config['DYNAMODB']['table_name']
    return dynamo_resource.Table(table_name)

def get_movie_item(table, year, title):
    """
    Gets a movie item from the DynamoDB table.
    
    Args:
        table: The DynamoDB table resource.
        year: The year of the movie.
        title: The title of the movie.
    
    Returns:
        dict: The movie item.
    """
    response = table.get_item(Key={'year': year, 'title': title})
    return response.get('Item')

def query_movies_by_year(table, year):
    """
    Queries movies by year from the DynamoDB table.
    
    Args:
        table: The DynamoDB table resource.
        year: The year to query.
    
    Returns:
        list: List of movies for the given year.
    """
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    return response.get('Items', [])
