def main():
    import requests
    url = 'http://127.0.0.1:8000/person/'

    op = int(input('''
        1 - Create new register\n
        2 - Read a register\n
        3 - Update a register\n
        4 - Delete a register\n
        \nChoose the option: '''))

    if op > 4 or op < 1:
        print('Invalid Option\n')
        return
    email = input('Insert the E-mail: ')
    if op == 1:
        name = input('Insert the Name: ')
        age = int(input('Insert the Age: '))

        data = {}
        data['name'] = name
        data['email'] = email
        data['age'] = age
        response = requests.post(url, json=data)
    elif op == 2:
        response = requests.get(url + f'{email}/')
    elif op == 3:
        name = input('Insert the Name: ')
        age = int(input('Insert the Age: '))

        data = {}
        data['name'] = name
        data['email'] = email
        data['age'] = age
        response = requests.put(url, json=data)
    elif op == 4:
        response = requests.delete(url + f'{email}/')
    print('\n', response.json(), '\n')

if __name__ == '__main__':
    main()
