import sqlite3
import pandas as pd
from database import DB_PATH

with sqlite3.connect(DB_PATH) as conn:
    df=pd.read_sql_query("" \
    "SELECT * from quarantine_transactions ",conn)

print(df.head(5))

import sqlite3
from database import DB_PATH

with sqlite3.connect(DB_PATH) as conn:

    columns = conn.execute(
        "PRAGMA table_info(transaction_features)"
    ).fetchall()

    for column in columns:
        print(column)
