import redis

# abre a conexão com o banco
r = redis.Redis(host='localhost', port=6379, db=0)

# define os dados da pessoa
person_1 = {
   'name': 'name example',
   'age': 0,
   'phone_number': '+55 (61) 00000-0000',
   'city': 'Brasilia'
}

# insere os dados da pessoa no banco e atribui a chave 'person:1'
for key, value in person_1.items():
    r.hset("person:1", key, value)
