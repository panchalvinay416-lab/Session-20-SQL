import pandas as pd
from sqlalchemy import create_engine

# 1. Read the CSV file
df = pd.read_csv("mi_matches.csv")

# 2. Keep only matches won by Mumbai Indians
# Change "winner" if your CSV uses a different column name.
mi_wins = df[df["winner"] == "Mumbai Indians"]

# 3. Create a SQLite database connection
engine = create_engine("sqlite:///mi_matches.db")

# 4. Save the filtered rows to a new SQL table
mi_wins.to_sql("mi_wins", con=engine, if_exists="replace", index=False)

print("Mumbai Indians winning matches saved to the mi_wins table.")
print(mi_wins.head())
print("Total rows inserted:", len(mi_wins))
