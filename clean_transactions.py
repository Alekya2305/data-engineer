#converting csv to df

import pandas as pd

df = pd.read_csv("transactions.csv")

print("---RAW DATA---")
print(f"Rows: {len(df)}")
print(f"columns: {list(df.columns)}")

#introducing dirty data
import random

#duplicates
duplicates = df.sample(10)
df = pd.concat([df,duplicates], ignore_index=True)

#null values
df.loc[random.sample(range(len(df)), 10), "amount"] = None

#negative amount
df.loc[random.sample(range(len(df)), 5), "amount"] = -99.99

print("---AFTER DIRTY DATA---")
print(f"Rows: ", {len(df)})
print(f"Null amounts: {df['amount'].isnull().sum()}")
print(f"Negative amounts: {(df['amount']<0).sum()}")
print(f"Duplicate values: {df.duplicated().sum()}")

#clean dirty data
df = df.drop_duplicates()
print(f"After removing duplicates rows {len(df)}")

mean_amount = df["amount"].mean()
df["amount"] = df["amount"].fillna(round(mean_amount, 2))
print(f"Null values removed and filled with average amount ${round(mean_amount, 2)}")

df.loc[df["amount"]<0,"amount"] = round(mean_amount, 2)
print(f"Negavive values replaced with average amount ${round(mean_amount, 2)}")

#rechecking
assert df.duplicated().sum()==0
assert df["amount"].isnull().sum()==0
assert (df["amount"]<0).sum()==0

#cleaned data
print("---CLEANED DATA---")
print(f"Number of rows after cleaning {len(df)}")
print(f"Number of duplicates {df.duplicated().sum()}")
print(f"Null values {df['amount'].isnull().sum()}")
print(f"Negative values {(df['amount']<0).sum()}")

#save to clean file
df.to_csv("transactions_cleaned.csv", index=False)
print("\nCleaned data saved to transactions_cleaned.csv")