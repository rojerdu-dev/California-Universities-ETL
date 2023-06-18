# California Universities ETL 
This project contains an Extract, Transform, Load (ETL) script written in Python. 

Data is ingested from an API, transformed, and then loaded into a SQLite database.

# TL;DR 
This project retrieves information about universities in California. 

The information allows you to easily access and analyze data about these institutions.

# Installation 
To use the script, follow the steps below: 

1. Clone the repository:

`git clone https://github.com/your-username/california-universities-etl.git`

2. Navigate to the project directory:

`cd california-universities-etl`

3. Install the required dependencies. It's recommended to use a virtual environment (e.g., poetry, venv, etc):

`pip install -r requirements.txt`

# Usage 
To run the ETL script, execute the following command: 

`python etl.py` 

This command will initiate the data extraction from the API, transformation, and loading into a SQLite database named `my_db.db`. 

The extracted data is filtered to include only universities in California. 

The resulting dataset includes columns for domains, country, web pages, and university names. 

