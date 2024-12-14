import psycopg2

try:
    connection = psycopg2.connect(
        dbname="mydb",
        user="postgres",
        password="1234",
        host="localhost",
        port=5432
    )
    print("Database connection successful!")
except Exception as e:
    print(f"Error: {e}")
