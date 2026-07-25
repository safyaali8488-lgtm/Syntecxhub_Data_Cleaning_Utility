import pandas as pd

# -------------------------------
# Step 1: Read Dataset
# -------------------------------
file_path = "data/dirty_data.csv"

df = pd.read_csv(file_path)

print("\nOriginal Dataset:")
print(df)

# -------------------------------
# Step 2: Standardize Column Names
# -------------------------------
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

print("\nColumn Names Standardized:")
print(df.columns)

# -------------------------------
# Step 3: Remove Duplicate Rows
# -------------------------------
duplicate_count = df.duplicated().sum()

df = df.drop_duplicates()

print(f"\nDuplicate Rows Removed: {duplicate_count}")

# -------------------------------
# Step 4: Handle Missing Values
# -------------------------------

# Fill missing age with average age
df["age"] = df["age"].fillna(df["age"].mean())

# Fill missing city with "Unknown"
df["city"] = df["city"].fillna("Unknown")

# Fill missing salary with average salary
df["salary"] = df["salary"].fillna(df["salary"].mean())

print("\nMissing Values Handled.")

# -------------------------------
# Step 5: Convert Date Column
# -------------------------------
df["join_date"] = pd.to_datetime(
    df["join_date"],
    format="mixed",
    errors="coerce"
)

print("\nDate Column Converted.")

# -------------------------------
# Step 6: Save Clean Dataset
# -------------------------------
output_file = "output/cleaned_data.csv"

df.to_csv(output_file, index=False)

print(f"\nCleaned dataset saved as {output_file}")

# -------------------------------
# Step 7: Create Cleaning Log
# -------------------------------

log = f"""
DATA CLEANING REPORT
====================

Original Rows : {len(pd.read_csv(file_path))}
Final Rows    : {len(df)}

Duplicate Rows Removed : {duplicate_count}

Missing Values Remaining
------------------------
{df.isnull().sum()}

Column Names
------------
{list(df.columns)}
"""

with open("cleaning_log.txt", "w") as file:
    file.write(log)

print("\nCleaning log created successfully.")

# -------------------------------
# Step 8: Display Final Dataset
# -------------------------------

print("\nFinal Clean Dataset:")
print(df)