import smtplib

USER_EMAIL = ''
USER_PASSWORD = ''
HOST = 'smtp.gmail.com'
PORT = 587


def send_email(to_email, message):
    email_body = f'''Subject: Email de comunicação de agendamento

Olá {to_email},

{message}

Obrigado,
Conta de teste.'''
    
    server = smtplib.SMTP(HOST, PORT)
    status_code, response = server.ehlo()
    print(f"== Echoing the server: {status_code} {response}")

    print(server.starttls())

    status_code, response = server.login(USER_EMAIL, USER_PASSWORD)
    print(f'== Logging in: {status_code}, {response}')

    server.sendmail(USER_EMAIL, to_email, email_body.encode('utf-8'))
    print('=== Email enviado com sucesso')

    server.quit()

