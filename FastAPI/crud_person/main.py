import requests
import json

url_create = 'http://127.0.0.1:8000/create/{}/{}/'
url_read = 'http://127.0.0.1:8000/read/{}/{}/'

def create(name:str=None, age:int=None):
    if name is None or age is None:
        return None
    
    response = requests.post(url_create.format(name, age))
    return json.loads(response.text)

def read(name:str=None, age:int=None):
    if name is None or age is None:
        return None
    
    response = requests.get(url_read.format(name, age))
    return json.loads(response.text)

op = int(input('1 - Create new register\n2 - Read a register\n\nChoose the option: '))

n = input('Insert the Name: ')
a = int(input('Insert the Age: '))

if op == 1:
    data = create(n, a)
    print('\n', data)

elif op == 2:
    data = read(n, a)
    print('\n', data)
