import smtplib
import email.message
from email_data import email_data

def send_email(user_name:str=None, user_email:str=None, user_phone:str=None, user_message:str=None) -> None:
    email_body = email_data['email_body'].format(user_name, user_email, user_phone, user_message)
    msg = email.message.Message()
    msg['Subject'] = email_data['email_subject']
    msg['From'] = email_data['your_email']
    msg['To'] = user_email
    password = email_data['email_password']
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

if __name__ == '__main__':
    send_email('name example', 'example@gmail.com', '61900000000', 'example message')
