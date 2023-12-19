import psycopg2

# creat the data bank connection
conn = psycopg2.connect(
    host="google_cloud_ip",
    port="5432",
    dbname="postgres",
    user="postgres",
    password="your_password",
)
