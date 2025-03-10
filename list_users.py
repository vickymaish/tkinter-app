import sqlite3

# Connect to the database
db = sqlite3.connect('admin.db')

# Create a cursor object
cursor = db.cursor()

# Execute a query to retrieve all user IDs and passwords
cursor.execute("SELECT User_ID, Password FROM adm")

# Fetch all results
users = cursor.fetchall()

# Print the results
for user in users:
    print(f"User ID: {user[0]}, Password: {user[1]}")

# Close the database connection
db.close()