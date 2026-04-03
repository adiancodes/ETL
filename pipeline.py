import pandas as pd
print("--------------------------------Starting the ETL pipeline--------------------------------")

customers_df = pd.read_csv("customer_details.csv")
baskets_df = pd.read_csv("basket_details.csv")
print(customers_df.isnull().sum())
# print("--------------------------------Data loaded successfully--------------------------------")

# print("\n----------------------CUSTOMER DETAILS----------------------")
# print(customers_df.head())
# print("\n----------------------BASKET DETAILS----------------------")
# print(baskets_df.head())

# print("--------------------------------Data previewed successfully--------------------------------")

# print("\n2. TRANSFORMING DATA...")
# customers_df = customers_df.dropna()
# baskets_df = baskets_df.dropna()
# print("Missing values removed.")

# #joining the 2 tables into one single table 

# print("\n3. JOINING TABLES...")
# master_df = pd.merge(baskets_df, customers_df, on="customer_id", how="inner")
# print("Tables joined successfully.")

# print("\n--- MASTER TABLE PREVIEW ---")
# print(master_df.head())
# print(f"\nTotal rows in master table: {len(master_df)}")

# master_df.to_csv('clean_master_data.csv', index=False)
