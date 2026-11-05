import random
import uuid
from datetime import datetime, timezone

customer=["CUST101","CUST102","CUST103","CUST104","CUST105"]
merchants=["Flipcart","Amazon","Zepto","Swiggy"]
cities=["Bangalore","Hyderabad","Chennai","Mumbai"]
devices=["Phone","Laptop","Tablet"]

def generate_transaction():
    return{
        "transaction_id":str(uuid.uuid4())[:8],
        "customer_id":random.choice(customer),
        "amount":round(random.uniform(500,50000),2),
        "merchant":random.choice(merchants),
        "city":random.choice(cities),
        "device":random.choice(devices),
        "timestamp":datetime.now(timezone.utc).isoformat()
    }

while True:
    transaction=generate_transaction()
    print(transaction)
    time.sleep(2)