import pandas as pd
import json

def n_lines(file_name:str=None) -> int: # recebe o nome do arquivo e retorna a quantidade de linhas
    with open(file_name, 'r') as file:
        n_lines = file.readlines()
        file.close()
    return len(n_lines)

def write_json() -> int:
    data = pd.read_csv('data_set.csv') # le o arquivo '.csv'
    data_dict = data.to_dict() # transforma o arquivo em um dict

    with open('data.json', 'w') as file: # guarda os dados em um arquivo '.json'
        file.write(json.dumps(data_dict))
        file.close()
    return n_lines('data_set.csv') # retorna a quantidade de linhas do arquivo '.csv'
