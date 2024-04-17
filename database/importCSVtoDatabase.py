import sqlite3, csv

# Connecting to database
conn = sqlite3.connect('database/database.db')

# Creating a cursor to execute SQL queries
cur = conn.cursor()


# Reading data from CSV file
with open('database/customers_sales_2021_2022.csv') as f:
    reader = csv.reader(f, delimiter=';')
    data = list(reader)

# Seperate column names from values 
column_names = data[0]
data.remove(data[0])

# Creating a table
sql_create_table = 'CREATE TABLE IF NOT EXISTS "customers_sales_2021_2022"('
for i, name in enumerate(column_names):
    if i:   # print a separator if this isn't the first element
        sql_create_table += ','
    sql_create_table += f'"{str(name)}" TEXT'
sql_create_table += ');'
try:
    cur.execute(sql_create_table)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

# Inserting data into the table
for row in data:
    sql_insert_data = "INSERT INTO customers_sales_2021_2022 VALUES ("
    for i, item in enumerate(row):
        if i:   # print a separator if this isn't the first element
            sql_insert_data += ","
        sql_insert_data += f'"{str(item)}"'
    sql_insert_data += ");"
    cur.execute(sql_insert_data)
conn.commit()

# Close connection
conn.close()