from django.core.mail import send_mail

from cinema.celery import *


@app.task(bind=True)
def send(self, recipients, html_message):
    print('Start')
    for i in range(len(recipients)):
        send_mail('Рассылка CinemaCMS', 'Это письмо пришло от CinemaCMS', None, [recipients[i]], fail_silently=False,
                  html_message=html_message)
        self.update_state(state='PROGRESS', meta={'current': i+1, 'total': len(recipients)})
    print('End')
    return {'current': 100, 'total': 100}
