import pyodbc

# Replace these with your own server details
server = "your_server_name"
database = "your_database_name"
username = "your_username"
password = "your_password"

# Connection string with driver and port (optional)
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
  # Connect to the SQL Server
  connection = pyodbc.connect(connection_string)

  # Print a success message
  print("Connection established successfully!")

except pyodbc.Error as err:
  # Print an error message if connection fails
  print("Error connecting to the server:", err)

finally:
  # Close the connection if it was successful
  if connection:
    connection.close()
    print("Connection closed.")
