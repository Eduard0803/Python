### 2FA Authentication

preencha as linhas 9, 10, 11 do arquivo [main.py](main.py) com seus dados  

para instalar as depedencias:

```
make install
```

para iniciar o servidor:

```
make start
```

para encerrar o servidor:

```
make stop
```

- Pages:
    - [`/`](pages/home.html) - home page
    - [`/input`](pages/input.html) - receive the user's data and send the authentication code 
    - `/verify` - check the code and render the page [success](pages/succes.html) or [error](pages/error.html)

