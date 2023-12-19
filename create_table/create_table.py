import json

from write_json import write_json


def create_table(file_name: str = None) -> list:
    n_lines = write_json()  # escreve os dados do '.csv' para um '.json'

    with open(file_name, "r") as file:  # pega os dados do arquivo '.json'
        data = json.load(file)

    # gera a tabela com o nome do país e a quantidade produzida
    table = [["Country", "Production (Tons)"]]

    for i in range(n_lines - 1):
        buffer = [data["Country"][f"{i}"], data["Production (Tons)"][f"{i}"]]
        table.append(buffer)

    return table  # retorna a tabela em formato de lista
