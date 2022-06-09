from django.core.mail import send_mail

from cinema.celery import *


@app.task
def send(recipients, html_message):
    state = 0
    current = 0

    for recipient in recipients:
        list_of_recipient = [recipient]
        send_mail('Django mail', 'This e-mail was sent with Django.', None, list_of_recipient, fail_silently=False,
                  html_message=html_message)
        current += 1
        state = (current / len(recipients)) * 100
        print(f"{int(state)}%")
    return 'task end'
