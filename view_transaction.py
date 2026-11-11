import sqlite3
import pandas as pd
from database import DB_PATH

with sqlite3.connect(DB_PATH) as conn:
    df=pd.read_sql_query("" \
    "SELECT COUNT(*) FROM transactions WHERE amount>30000 ",conn)

print(df.head(5))

