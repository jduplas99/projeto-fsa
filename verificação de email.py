import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

def validar_formato_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao, email) is not None

def enviar_email_teste(email_destino, email_origem, senha, servidor_smtp, porta_smtp):
    try:
        # Criação da mensagem de email
        mensagem = MIMEMultipart()
        mensagem['From'] = email_origem
        mensagem['To'] = email_destino
        mensagem['Subject'] = 'Teste de Validação de Email'
        corpo = 'Este é um email de teste para validação de email.'
        mensagem.attach(MIMEText(corpo, 'plain'))

        # Conectando ao servidor SMTP
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()
        servidor.login(email_origem, senha)
        servidor.sendmail(email_origem, email_destino, mensagem.as_string())
        servidor.quit()
        return True
    except smtplib.SMTPAuthenticationError as e:
        print(f'Erro de autenticação ao enviar email: {e}')
        if "5.7.8" in str(e):
            print("Possíveis soluções:")
            print("1. Verifique se o email e a senha estão corretos.")
            print("2. Se você tiver autenticação em duas etapas ativada, use uma senha de aplicativo.")
            print("3. Ative 'Acesso a aplicativos menos seguros' na sua conta do Google.")
        return False
    except Exception as e:
        print(f'Erro ao enviar email: {e}')
        return False

def validar_email(email_destino, email_origem, senha, servidor_smtp, porta_smtp):
    if not validar_formato_email(email_destino):
        return False, "Formato de email inválido"
    if enviar_email_teste(email_destino, email_origem, senha, servidor_smtp, porta_smtp):
        return True, "Email válido e teste enviado com sucesso"
    else:
        return False, "Falha ao enviar email de teste"

# Exemplo de uso
print("Escolha o serviço de email:")
print("1. Gmail")
print("2. Outlook/Hotmail")
print("3. Yahoo")
escolha = input("Digite o número correspondente ao serviço de email: ")

if escolha == '1':
    servidor_smtp = 'smtp.gmail.com'
    porta_smtp = 587
elif escolha == '2':
    servidor_smtp = 'smtp.office365.com'
    porta_smtp = 587
elif escolha == '3':
    servidor_smtp = 'smtp.mail.yahoo.com'
    porta_smtp = 587
else:
    print("Escolha inválida!")
    exit()

email_origem = input('Digite seu email de origem: ')
senha = getpass('Digite sua senha de email: ')
email_destino = input('Digite o email de destino para validação: ')

valido, mensagem = validar_email(email_destino, email_origem, senha, servidor_smtp, porta_smtp)
print(mensagem)
