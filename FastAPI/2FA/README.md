# 2FA Authentication

para o funcionamento execute o código `pip install -r requirements.txt` no terminal  

preencha as linhas 9, 10, 11 do arquivo [main.py](main.py) com seus dados  

por fim execute o código `uvicorn main:app --reload` no terminal  

- Pages:
    - [`/`](pages/home.html) - home page
    - [`/input`](pages/input.html) - receive the user's data and send the authentication code 
    - `/verify` - check the code and render the page [success](pages/succes.html) or [error](pages/error.html)
