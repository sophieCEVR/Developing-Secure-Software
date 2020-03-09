# project/email.py
from flask_mail import Message
from . import mail, app


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='justJackverify@gmail.com',
    )
    mail.send(msg)

