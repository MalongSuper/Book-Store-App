from sqlalchemy import create_engine
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "db", "user.db")
engine = create_engine(f"sqlite:///{DB_PATH}")
conn = engine.connect()
result = conn.execute("SELECT * FROM users")
for row in result:
    print(row)
