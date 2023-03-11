import win32com.client as win32

remetente = 'eduardobelarmino45@gmail.com'
assunto = 'form result'

with open('body.txt', 'r') as file:
    body_email = file.read()

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

email.To = f"{remetente}"
email.Subject = f"{assunto}"
email.HTMLBody = f"""
<p>{body_email}</p>
"""
email.Send()

