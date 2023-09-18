from connection import conn

def get_data(email: str=None, password:str=None) -> list:

    cur = conn.cursor()
    sql_command = '''CREATE TABLE IF NOT EXISTS test (id INT, name VARCHAR(255), age INT, email VARCHAR(255), password VARCHAR(255));'''
    cur.execute(sql_command)

    base_command = "SELECT name, age, email, password FROM test WHERE email = '{}' AND password = '{}';"
    sql_command = base_command.format(email, password)
    cur.execute(sql_command)

    return cur.fetchone()

if __name__ == '__main__':
    result = get_data('example@gmail.com', '12345678')
    print(result)
