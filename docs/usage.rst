Usage
=====

Helpers
-------

You can use the ``dynamodb.dynamodb_helpers.get_path_to_data()`` function:

.. autofunction:: dynamodb.dynamodb_helpers.get_path_to_data

Raw data folder is returned by ``dynamodb.dynamodb_helpers.get_raw_data_path()`` function:

.. autofunction:: dynamodb.dynamodb_helpers.get_raw_data_path

You can also use the ``dynamodb.dynamodb_helpers.get_tidy_data_path()`` function:

.. autofunction:: dynamodb.dynamodb_helpers.get_tidy_data_path

DynamoDB
--------

To create a DynamoDB resource, use the ``dynamodb.dynamodb_helpers.get_dynamodb_resource`` function:

.. autofunction:: dynamodb.dynamodb_helpers.get_dynamodb_resource

To list all DynamoDB tables, use the ``dynamodb.dynamodb_helpers.list_dynamodb_tables`` function:

.. autofunction:: dynamodb.dynamodb_helpers.list_dynamodb_tables

To get the movies table from DynamoDB, use the ``dynamodb.dynamodb_helpers.get_movies_table`` function:

.. autofunction:: dynamodb.dynamodb_helpers.get_movies_table

To get a specific movie item, use the ``dynamodb.dynamodb_helpers.get_movie_item`` function:

.. autofunction:: dynamodb.dynamodb_helpers.get_movie_item

To query movies by year, use the ``dynamodb.dynamodb_helpers.query_movies_by_year`` function:

.. autofunction:: dynamodb.dynamodb_helpers.query_movies_by_year

Data Transformation
-------------------

To transform raw movie data into a tidy DataFrame, use the ``dynamodb.dynamodb_helpers.tidy_movie_data`` function:

.. autofunction:: dynamodb.dynamodb_helpers.tidy_movie_data
