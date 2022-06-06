import datetime

from django.shortcuts import render
from django.utils import timezone

from .models import Page, Banner, Slide, Carousel, Film


def main(request):
    context = {'main_page': Page.objects.get(is_main=True),
               'banner': Banner.objects.get(),
               'top_slides': Slide.objects.filter(is_main=True),
               'top_carousel': Carousel.objects.get(is_main=True),
               'bottom_carousel': Carousel.objects.get(is_main=False),
               'bottom_slides': Slide.objects.filter(is_main=False),
               'day': timezone.now(),
               'current_films': Film.objects.filter(premier_date__lte=datetime.date.today()),
               'soon_films': Film.objects.filter(premier_date__gt=datetime.date.today())}
    return render(request, 'main/pages/index.html', context)


def poster(request):
    context = {'current_films': Film.objects.filter(premier_date__lte=datetime.date.today()),
               'soon_films': Film.objects.filter(premier_date__gt=datetime.date.today()),
               'main_page': Page.objects.get(is_main=True)}
    return render(request, 'main/pages/poster.html', context)


def soon(request):
    context = {'current_films': Film.objects.filter(premier_date__lte=datetime.date.today()),
               'soon_films': Film.objects.filter(premier_date__gt=datetime.date.today()),
               'main_page': Page.objects.get(is_main=True)}
    return render(request, 'main/pages/soon.html', context)
