import pandas as pd
from sqlalchemy import create_engine

print("1. Reading the clean data...")

df = pd.read_csv('clean_master_data.csv')

print("2. Connecting to PostgreSQL...")
# The Connection String format is: dialect://username:password@host:port/database

connection_string = 'postgresql://postgres:Sarya_12@localhost:5432/ecommerce_db'

# Create the engine (the bridge between Python and the Database)
engine = create_engine(connection_string)

print("3. Loading data into the database (this might take a few seconds)...")
# Send the data to a new table called 'sales_data'
# if_exists='replace' means if we run this script again, it will overwrite the old table instead of crashing
df.to_sql('sales_data', engine, if_exists='replace', index=False)

print("\n SUCCESS! ETL Pipeline Complete! Data is now in PostgreSQL.")