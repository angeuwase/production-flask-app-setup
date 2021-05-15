from flask_mail import Message
from . import mail, celery
from flask import current_app

@celery.task(name='app.tasks.send_celery_email')
def send_celery_email(message_data):
    app = current_app._get_current_object()
    message = Message(subject=message_data['subject'],
                    recipients=[message_data['recipients']],
                    body=message_data['body'],
                    sender=app.config['MAIL_DEFAULT_SENDER'])

    mail.send(message)

   

