Formula One Module Repository
========================

This Ptyhon project downloads and prepares formula one data from the API ergast.com.

# Formula One Module Repository
## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/safer-lgtm/formulaone.git
    cd formulaone
    ```

2. Create a `config.ini` file in the root directory of the project:

    ```ini
    [AWS]
    aws_access_key_id = your_access_key_id
    aws_secret_access_key = your_secret_access_key
    region_name = your_region

    [DYNAMODB]
    table_name = your_table_name
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the tests:

    ```bash
    pytest
    ```
