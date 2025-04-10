import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("bike_setup.db")
cursor = conn.cursor()

# Function to check and display table data
def check_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    if rows:
        print(f"\n✅ Found these in '{table_name}':")
        for row in rows:
            print(row)
    else:
        print(f"\n❌ No data found in the '{table_name}' table.")

# Check Frames Table
check_table("frames")

# Check Stems Table
check_table("stems")

# Check Handlebars Table
check_table("handlebars")

# Close the connection
conn.close()
