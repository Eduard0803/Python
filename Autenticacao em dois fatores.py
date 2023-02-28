from twilio.rest import Client
import string
import random

account_sid = 'your_id'
auth_token = 'your_token'
numero_twilio = 'your_number_twilio' #seu número da twilio
meu_numero = 'number' #número que receberá a ligação

print("\t\tLogin\n")

email = input("Digite o seu e-mail: ")
senha = input("Digite a sua senha: ")

if email == "teste@gmail.com":
    if senha == "password":

        print("Você receberá um código  por chamada telefonica\n")

        def random_generator(size=5, chars=string.ascii_uppercase + string.digits): # Função que gera os códigos de autenticação
            return ''.join(random.choice(chars) for _ in range(size))

        texto = random_generator()
        print(f"Código criado\nCódigo: {texto}")

        cliente = Client(account_sid, auth_token) # Parte respónsavel por fazer a ligação ao usuario

        mensagem = f"""
        <Response>
        <Say language="pt-BR">
        o seu código de autenticação é: {texto[0]}          {texto[1]}          {texto[2]}          {texto[3]}          {texto[4]} 
        repetindo o seu código de autenticação é: {texto[0]}          {texto[1]}          {texto[2]}          {texto[3]}          {texto[4]}
        </Say>
        </Response>
        """

        ligacao = cliente.calls.create(
            to=meu_numero,
            from_=numero_twilio,
            twiml=mensagem
        )

        aut = input("Digite o código que recebeu na chamada telefonica: ") # Pede a entrada do código ao usuario

        if aut == texto: # Faz a comparação entre o código de autenticação gerado e o código inserido pelo usuario
            print("Usuario autenticado\n")
        else:
            print("Erro na autenticacao\n")
    else:
        print("Erro na autenticacao\n")
else:
    print("Erro na autenticacao\n")
