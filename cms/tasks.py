from django.core.mail import send_mail

from cinema.celery import *


@app.task
def send(recipients, html_message):
    return send_mail('Django mail', 'This e-mail was sent with Django.', None, recipients,
                     fail_silently=False, html_message=html_message)
