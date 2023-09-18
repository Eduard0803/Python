from connection import conn

def upload_data(name: str=None, age: int=None, email: str=None, password:str=None) -> None:
    
    cur = conn.cursor()
    sql_command = '''CREATE TABLE IF NOT EXISTS test (id INT, name VARCHAR(255), age INT, email VARCHAR(255), password VARCHAR(255));'''
    cur.execute(sql_command)

    cur.execute("SELECT COUNT(*) FROM test;")
    less_id = cur.fetchone()[0]

    # insert the data in bank
    base_command = "INSERT INTO test VALUES ('{}', '{}', '{}', '{}', '{}')"
    sql_command = base_command.format(less_id, name, age, email, password)
    cur.execute(sql_command)
    conn.commit()
    cur.close()

if __name__ == '__main__':
    upload_data('Test', 0, 'example@gmail.com', '12345678')
