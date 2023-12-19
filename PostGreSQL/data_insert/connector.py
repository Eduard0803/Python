import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="postgres",
    user="postgres",
    password="YOUR_PASSWORD",
)
