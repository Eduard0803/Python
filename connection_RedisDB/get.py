import redis

# abre a conexão com o banco
r = redis.Redis(host="localhost", port=6379, db=0)

# pega os dados da chave 'person:1'
person_cloud = r.hgetall("person:1")

# escreve os dados no console
for key, value in person_cloud.items():
    key = key.decode("utf-8")
    value = value.decode("utf-8")
    print(f"{key}: {value}")
