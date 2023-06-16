from tabulate import tabulate
from connector import conn

cur = conn.cursor()
cur.execute("SELECT * FROM users;")
datas = cur.fetchall()
table = [['id', 'name', 'age']]

for data_person in datas:
    buffer = [data_person[0], data_person[1], data_person[2]]
    table.append(buffer)
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

conn.close()
