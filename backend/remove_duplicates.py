import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("bike_setup.db")
cursor = conn.cursor()

# Function to remove duplicates while keeping the first entry
def remove_duplicates(table_name, unique_columns):
    print(f"\n🔹 Checking for duplicates in '{table_name}'...")

    # Escape reserved keywords (like "drop") in SQLite using double quotes
    unique_columns = [f'"{col}"' if col.lower() == "drop" else col for col in unique_columns]

    # Construct DELETE query for duplicates
    query = f"""
    DELETE FROM {table_name}
    WHERE id NOT IN (
        SELECT MIN(id) FROM {table_name}
        GROUP BY {', '.join(unique_columns)}
    );
    """

    cursor.execute(query)
    conn.commit()

    # Check if duplicates were removed
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    count = cursor.fetchone()[0]
    print(f"✅ Remaining {table_name} records: {count}")

# Remove duplicates from Frames, Stems, and Handlebars
remove_duplicates("frames", ["make", "size", "reach", "stack", "top_tube"])
remove_duplicates("stems", ["make", "length", "angle"])
remove_duplicates("handlebars", ["make", "width", "reach", '"drop"'])  # Escaped "drop"

# Close the connection
conn.close()
print("\n✅ Duplicate removal completed!")
