import pandas as pd
import mysql.connector

#load cleaned data
df = pd.read_csv("transactions_cleaned.csv")
print(f"Loaded {len(df)} rows from csv")

#connect to MYSQL
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sweety@23",
    database = "bank_pipeline"
)

cursor = conn.cursor()
print("connected successfully to MYSQL")

#clear the old data before loading fresh data
cursor.execute("truncate table transactions")
print("cleared old data form the table")

#insert all rows
insert_query = """
    insert into transactions
    (transaction_id, user_id, amount, category, merchant, timestamp, is_fraud)
    values(%s, %s, %s, %s, %s, %s, %s)
"""

#convert dataframe rows into a list of tuples
rows = list(df.itertuples(index=False, name=None))

#executemany runs the insert query once for EVERY row — all 1000 at once
cursor.executemany(insert_query, rows)

conn.commit()
print(f"inserted {cursor.rowcount} rows into MySQL")


#Verify the data landed correctly
cursor.execute("select count(*) from transactions")
count = cursor.fetchone()[0]
print(f"{count} rows in the database")

cursor.execute("select * from transactions limit 3")
rows = cursor.fetchall()
print("First 3 rows in database")
for row in rows:
    print(row)


#close connection
cursor.close()
conn.close()
print("connection closed. level 3 complete!")


