import pandas as pd
import os

# -------------------
# Paths to data
# -------------------
data_folder = os.path.join(os.path.dirname(__file__), "../data")
hierarchy_path = os.path.join(data_folder, "PlantsHierarchy_DIM.csv")
fact_path = os.path.join(data_folder, "Plants_FACT.csv")
accounts_path = os.path.join(data_folder, "Accounts_DIM.csv")

# Load datasets
hierarchy_dim = pd.read_csv(hierarchy_path)
fact = pd.read_csv(fact_path)
accounts_dim = pd.read_csv(accounts_path)

# Inspect datasets
print("---- Plants Hierarchy ----")
print(hierarchy_dim.info())
print(hierarchy_dim.head())

print("\n---- Plants Fact ----")
print(fact.info())
print(fact.head())

print("\n---- Accounts ----")
print(accounts_dim.info())
print(accounts_dim.head())

# Data Cleaning
# ------------------
# Convert Date_Time to datetime
fact["Date_Time"] = pd.to_datetime(fact["Date_Time"], dayfirst=True, errors="coerce")

# Fill missing Account_id in Accounts_DIM
accounts_dim["Account_id"] = accounts_dim["Account_id"].fillna("Unknown")

# Strip whitespace from string columns
for df in [hierarchy_dim, fact, accounts_dim]:
    str_cols = df.select_dtypes(["object"]).columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

# ------------------------
# Create KPIs
# ------------------------
fact["Gross_Profit"] = fact["Sales_USD"] - fact["COGS_USD"]
fact["Profit_Margin"] = fact["Gross_Profit"] / fact["Sales_USD"] * 100

# ------------------------
# Merge datasets for Power BI
# ------------------------
# Merge Fact + Product hierarchy
fact_full = fact.merge(
    hierarchy_dim, left_on="Product_id", right_on="Product_Name_id", how="left"
)

# Merge with Accounts
fact_full = fact_full.merge(accounts_dim, on="Account_id", how="left")

# Export cleaned dataset
# ------------------------
output_path = os.path.join(data_folder, "Plants_Dashboard_Cleaned.csv")
fact_full.to_csv(output_path, index=False)
print(f"\nCleaned dataset saved as '{output_path}'")
