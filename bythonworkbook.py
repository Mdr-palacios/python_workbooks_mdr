## this is a very fast very loose blocks of code for students
## to build on. It should be relatively easy to either port it 
## into a local machine or run and modify inside codespaces
## this is not a particularly pretty book, but it should let people
## work as they might wish. 


## we're making sure we have the various drivers for bigquery
import os
import pandas as pd

## doing a system call to verify the packages 
os.system("curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get update && sudo apt-get install google-cloud-cli")
## similar to above, pulling in python
os.system("pip install BigQuery-connector-python")

from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
