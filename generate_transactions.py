import random
from faker import Faker
import csv

fake = Faker()

transactions = []

for i in range(1000):
    transaction = {
        "transaction_id": i + 1,
        "user_id": random.randint(1,100) ,
        "amount": round(random.uniform(1,1000),2),
        "category" : random.choice(["Food", "Entertainment", "Shopping", "Bills"]),
        "merchant": fake.company(),
        "timestamp": fake.date_time_this_year().strftime("%Y-%m-%d %H-%M-%S"),
        "isFrauad": random.choice(["True", "False"]),
        }
    transactions.append(transaction)
    
with open("transactions.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
    writer.writeheader()
    writer.writerows(transactions)

print(f"Done, Generated {len(transactions)} transactions")
print("First transaction:", transactions[0])