import psycopg2

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    dbname='postgres',
    user='postgres',
    password='your_password'
)

# Criar um cursor
cur = conn.cursor()

sql_commands = [
    "CREATE TABLE users (name VARCHAR(255), age INT, phone_number VARCHAR(255), city VARCHAR(255));", # Define o nome e datatypes das colunas e cria a tabela
    "DROP TABLE users;", # exclui a tabela
    "ALTER TABLE users ADD nova_column data_type;", # insere uma nova coluna na tabela
    "INSERT INTO users (name, age, phone_number, city) VALUES ('name example', 0, '+55 (61) 90000-0000', 'Brasília');", # insere um novo dado na tabela
    "SELECT * FROM users;" # retorna uma lista de users com os valores
    "UPDATE users SET name = 'name example' WHERE condição;", # atualiza os dados da tabela quando a condição é satisfeita
    "DELETE FROM users WHERE condição;" # remove dados da tabela quando a condição é satisfeita
]

# Executar o comando SQL
cur.execute(sql_commands[3])
conn.commit()

# Fechar o cursor e a conexão
cur.close()
conn.close()
