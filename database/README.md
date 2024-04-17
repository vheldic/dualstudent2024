# Database
The SQLite database `database.db` is filled with the content of the CSV-File `customers_sales_2021_2022.csv` by the `importCSVtoDatabase.py` file.

## `importCSVtoDatabase.py`
This Python program creates a table if it doesn't already exist and imports the CSV file into a SQLite database. 

### Disclaimer
Because the task is to just import the CSV file into a database, I didn't pay attention to specific data types or keys when creating the table.
Therefore if items already exist, they will not be replaced.