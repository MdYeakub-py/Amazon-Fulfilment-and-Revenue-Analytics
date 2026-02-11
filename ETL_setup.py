import pandas as pd
from sqlalchemy import create_engine

# ==========================================================
# 1. MYSQL CONNECTION
# ==========================================================
mysql_user = 'root'
mysql_pass = 'yeakub1234'
mysql_host = 'localhost'
mysql_db = 'amazon_sales_data'

engine = create_engine(
    f'mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}/{mysql_db}',
    echo=False
)
print("MySQL engine connected!")

# ==========================================================
# 2. LOAD CSV
# ==========================================================
df = pd.read_csv("Amazon Sale Report.csv", dtype=str)

print("\nCSV COLUMNS FOUND:")
print(df.columns.tolist())

# Standardize column names (strip spaces)
df.columns = [c.strip() for c in df.columns]

# ==========================================================
# 3. CLEANING
# ==========================================================
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Parse date
df["order_date"] = pd.to_datetime(df["Date"], errors="coerce")

# Qty and amount
df["qty"] = pd.to_numeric(df["Qty"], errors="coerce").fillna(0).astype(int)

df["amount"] = (
    df["Amount"]
    .astype(str)
    .str.replace(r"[^0-9.-]", "", regex=True)
    .replace("", "0")
    .astype(float)
)

# Normalized status
def normalize_status(s):
    if pd.isna(s):
        return "Unknown"
    s = s.lower()
    if "cancel" in s:
        return "Cancelled"
    if "shipped" in s or "delivered" in s:
        return "Shipped"
    return s.title()

df["status_norm"] = df["Status"].apply(normalize_status)

# B2B to boolean
df["b2b"] = df["B2B"].astype(str).str.upper().replace(
    {"TRUE": True, "FALSE": False}
).fillna(False)

# Fill missing text columns
text_columns = [
    "Style", "SKU", "Category", "Size", "ASIN",
    "Courier Status", "ship-city", "ship-state",
    "ship-postal-code", "ship-country",
    "promotion-ids", "fulfilled-by"
]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].fillna("")

# ==========================================================
# 4. FACT TABLE (STANDARDIZE NAMES)
# ==========================================================
to_load = df.rename(columns={
    "Order ID": "order_id",
    "status_norm": "status",
    "Fulfilment": "fulfilment",
    "Sales Channel": "sales_channel",
    "ship-service-level": "ship_service_level",
    "Style": "style",
    "SKU": "sku",
    "Category": "category",
    "Size": "size",
    "ASIN": "asin",
    "Courier Status": "courier_status",
    "ship-city": "ship_city",
    "ship-state": "ship_state",
    "ship-postal-code": "ship_postal_code",
    "ship-country": "ship_country",
    "promotion-ids": "promotion_ids",
    "fulfilled-by": "fulfilled_by"
})

fact_cols = [
    "order_id", "order_date", "status", "fulfilment", "sales_channel",
    "ship_service_level", "sku", "style", "category", "size", "asin",
    "courier_status", "qty", "currency", "amount",
    "ship_city", "ship_state", "ship_postal_code", "ship_country",
    "promotion_ids", "b2b", "fulfilled_by"
]

to_load = to_load[fact_cols].drop_duplicates(subset=["order_id"])

to_load.to_sql("fact_orders", engine, if_exists="replace", index=False)
print("fact_orders loaded!")

# ==========================================================
# 5. DIM DATE
# ==========================================================
dim_date = pd.DataFrame({"order_date": df["order_date"].dropna().unique()})
dim_date["date_key"] = dim_date["order_date"].dt.strftime("%Y%m%d").astype(int)
dim_date["year"] = dim_date["order_date"].dt.year
dim_date["month"] = dim_date["order_date"].dt.month
dim_date["day"] = dim_date["order_date"].dt.day
dim_date["weekday"] = dim_date["order_date"].dt.day_name()

dim_date.to_sql("dim_date", engine, if_exists="replace", index=False)
print("dim_date loaded!")

# ==========================================================
# 6. DIM PRODUCT
# ==========================================================
dim_product = df[["Style", "SKU", "Category", "Size", "ASIN"]].drop_duplicates()
dim_product = dim_product.rename(columns={
    "Style": "style",
    "SKU": "sku",
    "Category": "category",
    "Size": "size",
    "ASIN": "asin"
})

dim_product["product_key"] = dim_product.index + 1
dim_product.to_sql("dim_product", engine, if_exists="replace", index=False)
print("dim_product loaded!")

# ==========================================================
# 7. DIM REGION
# ==========================================================
dim_region = df[[
    "ship-city", "ship-state", "ship-postal-code", "ship-country"
]].drop_duplicates()

dim_region = dim_region.rename(columns={
    "ship-city": "ship_city",
    "ship-state": "ship_state",
    "ship-postal-code": "ship_postal_code",
    "ship-country": "ship_country"
})

dim_region["region_key"] = dim_region.index + 1
dim_region.to_sql("dim_region", engine, if_exists="replace", index=False)
print("dim_region loaded!")

# ==========================================================
# 8. JOIN DIMENSIONS BACK TO FACT
# ==========================================================
fact_orders = to_load.merge(
    dim_date[["order_date", "date_key"]],
    on="order_date",
    how="left"
)

fact_orders = fact_orders.merge(
    dim_product[["asin", "product_key"]],
    on="asin",
    how="left"
)

fact_orders = fact_orders.merge(
    dim_region,
    on=["ship_city", "ship_state", "ship_postal_code", "ship_country"],
    how="left"
)

fact_orders.to_sql("fact_orders", engine, if_exists="replace", index=False)
print("fact_orders updated with keys!")

print("\n✔✔✔ ETL COMPLETED SUCCESSFULLY ✔✔✔")
