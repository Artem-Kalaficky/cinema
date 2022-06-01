from django.template.loader import render_to_string

from cinema.settings import EMAIL_HOST_USER
from cinema.celery import *


# html_message = render_to_string('')


@app.task
def add(recipients):
    return send_mail('Django mail', 'This e-mail was sent with Django.', EMAIL_HOST_USER, recipients,
                     fail_silently=False)
