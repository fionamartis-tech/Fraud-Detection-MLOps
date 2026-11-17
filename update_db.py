
import sqlite3
from database import DB_PATH, create_database

with sqlite3.connect(DB_PATH) as conn:
    conn.execute(
        "DROP TABLE IF EXISTS transaction_features"
    )

create_database()

print("Feature table updated successfully!")
