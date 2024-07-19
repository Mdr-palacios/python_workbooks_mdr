## this is a very fast very loose blocks of code for students
## to build on. It should be relatively easy to either port it 
## into a local machine or run and modify inside codespaces
## this is not a particularly pretty book, but it should let people
## work as they might wish. 

## here we've imported the first few packages for you. 
import os
import pandas as pd

## exercise 0: read in the data from the csv, hint:  pd.read_csv is your friend
## again, pandas documentation, which you can refer to frequently, is here
## https://pandas.pydata.org/docs/user_guide/index.html

pd.read_csv("Fictitious_Records.csv")

## exercise 1: Inspect the DataFrame to understand its structure and content
## hint: Use the head(), dtypes, and describe() methods to quickly inspect the DataFrame, as mentioned in the slides.

## exercise 2: Filter data based on specific conditions.
## hint: Remember how we used the > operator to filter data. Apply similar techniques here to filter and count rows.

## exercise 3: Select specific columns and rename them.
## hint: Use double brackets to select multiple columns and the rename() method to change column names.

## exercise 4: Identify and handle missing data in the DataFrame.
## hint: Use isnull(), dropna(), and fillna() to handle missing data.

## exercise 5: Translate a SQL query into Pandas code.
## code is Given SQL: SELECT Name, Age FROM your_table WHERE Age > 25 ORDER BY Age DESC;
## hint: Break down the SQL query into its components (filtering, selecting columns, sorting) and translate each part into Pandas code.

## exercise 6: Perform grouping and aggregation operations.
## hint: Use the groupby() method followed by an aggregation function like mean(). 
