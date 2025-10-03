import sqlite3
import matplotlib.pyplot as plt
#Connect to SQLite
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
#Create Sales table (only if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    unit_price REAL
)
""")
#Insert some sample data 
sample_data = [
    ("Apple", 10, 2.5),
    ("Banana", 20, 1.5),
    ("Mango", 15, 3.0)
]
cursor.executemany("INSERT INTO Sales (product, quantity, unit_price) VALUES (?, ?, ?)", sample_data)
conn.commit()
#Run the SQL query
query = """
SELECT 
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_revenue
FROM Sales
"""
cursor.execute(query)
row = cursor.fetchone()
total_quantity, total_revenue = row
#Print results
print("Sales Summary:")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Total Revenue: {total_revenue}")
#Bar Chart
labels = ['Total Quantity', 'Total Revenue']
values = [total_quantity, total_revenue]

plt.bar(labels, values, color=['skyblue', 'lightgreen'])
plt.title("Sales Summary")
plt.ylabel("Values")
plt.show()
# close Connection.
cursor.close()
conn.close()
