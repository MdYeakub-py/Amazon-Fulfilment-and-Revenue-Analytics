import pandas as pd
df = pd.read_csv("Amazon Sale Report.csv",
    low_memory=False
)

# Clean Date

df["Date"] = pd.to_datetime(df["Date"], format = 'mixed')


#clean status
df["Status_Clean"] = df["Status"].str.split("_").str[0].str.strip()

# Promotion Count
df["Promotion_"] = df["promotion-ids"].fillna("").apply(lambda x: len(x.split(",")) if x != "" else 0) 

# Revenue
df["Revenue"] = df["Amount"].fillna(0)

# Region
df["Region"] = df["ship-state"]

# Convert Qty to numeric
df["Qty"] = pd.to_numeric(df["Qty"], errors= "coerce").fillna(0)

df.to_csv("Clean_Amazon_Orders_Data.csv", index=False)

print("Cleaning Complete")