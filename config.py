import pymysql

DB_HOST = "localhost"  # Change if using a remote database
DB_USER = "root"  # Replace with actual MySQL username
DB_PASSWORD = "your_password"  # Replace with actual MySQL password
DB_NAME = "bank_management"  # Ensure this database exists in MySQL

def get_db_connection():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

