import smtplib
import ssl
import os


def send_inquiry(message):
    """
    Receives a message from the contact page and sends an email when user
    hits submit.
    :param message:
    :return:
    """
    host = "smtp.gmail.com"
    port = 465

    username = "j.d.land.16@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "j.d.land.16@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
