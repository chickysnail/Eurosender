from email.message import EmailMessage
import ssl
import smtplib
import config

def send(balance):
    em = EmailMessage()
    em["From"] = config.sender
    em["To"] = config.reciever
    em["Subject"] = config.title
    em.set_content(config.content_sample.format(balance))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(config.sender, config.mailPwd)
        smtp.sendmail(config.sender, config.reciever, em.as_string())