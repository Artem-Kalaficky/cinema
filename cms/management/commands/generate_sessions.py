import random
import datetime

from django.core.management.base import BaseCommand

from main.models import Hall, Film, Session


class Command(BaseCommand):
    help = 'Generate sessions for 1 week'

    def handle(self, *args, **kwargs):
        halls = Hall.objects.all()
        films = Film.objects.filter(premier_date__lte=datetime.datetime.now())
        costs = [65, 75, 85]
        dates = []
        hours = [8, 10, 12, 14, 16, 18]
        month = int(datetime.datetime.now().strftime("%m"))
        for date in [(datetime.datetime.now() + datetime.timedelta(days=d)).strftime("%d") for d in range(7)]:
            dates.append(int(date))
        for day in dates:
            for i in range(len(halls)):
                Session.objects.create(hall=halls[i], film=random.choice(films),
                                       time=datetime.datetime(2022, month, day, hours[i], 0, tzinfo=datetime.timezone.utc),
                                       cost=random.choice(costs))
        self.stdout.write("Сеансы сгенерированы!")
