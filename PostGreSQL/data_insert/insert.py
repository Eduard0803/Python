from connector import conn
from faker import Faker

cur = conn.cursor()
fake = Faker(locale="pt-br")

sql_command = (
    """CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(255), age INT);"""
)
cur.execute(sql_command)

base_command = """INSERT INTO users (id, name, age) VALUES ('{}', '{}', '{}')"""

cur.execute("SELECT COUNT(*) FROM users;")
less_id = cur.fetchone()[0]

for i in range(5):
    name = fake.name()
    age = fake.random_int(min=15, max=70)
    sql_command = base_command.format(less_id, name, age)
    cur.execute(sql_command)
    less_id += 1

conn.commit()
conn.close()
