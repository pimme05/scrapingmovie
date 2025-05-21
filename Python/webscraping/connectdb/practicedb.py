import sqlite3
import pandas as pd

# Connect to the SQLite3 database
conn = sqlite3.connect('STAFF.db')

# === 1. Create and Load Departments Table ===

# Define new table and column headers
table_name = 'Departments'
attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

# Read the CSV file
file_path = '/Users/test/Desktop/IBM coursera/DEPARTMENTS.csv'  # Change this to your actual path
df = pd.read_csv(file_path, names=attribute_list)

# Load data into the database
df.to_sql(table_name, conn, if_exists='replace', index=False)
print(f"'{table_name}' table created and populated from CSV.")

# === 2. Append the given row ===
new_data = {
    'DEPT_ID': [9],
    'DEP_NAME': ['Quality Assurance'],
    'MANAGER_ID': [30010],
    'LOC_ID': ['L0010']
}
df_append = pd.DataFrame(new_data)
df_append.to_sql(table_name, conn, if_exists='append', index=False)
print("New department row appended successfully.")

# === 3. Queries ===

# a. View all entries
query = f"SELECT * FROM {table_name}"
print("\nAll Departments:")
print(pd.read_sql(query, conn))

# b. View only department names
query = f"SELECT DEP_NAME FROM {table_name}"
print("\nDepartment Names:")
print(pd.read_sql(query, conn))

# c. Count total entries
query = f"SELECT COUNT(*) AS Total FROM {table_name}"
print("\nTotal Departments:")
print(pd.read_sql(query, conn))

# Close connection
conn.close()
