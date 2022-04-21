import datetime

from django.shortcuts import render

from main.models import Film


def cms(request):
    return render(request, 'cms/layout/base.html')

def film(request):
    current_films = Film.objects.filter(premier_date__lte=datetime.date.today()).order_by('-premier_date')
    soon_films = Film.objects.filter(premier_date__gt=datetime.date.today()).order_by('-premier_date')
    return render(request, 'cms/pages/film_list.html', {'current_films': current_films, 'soon_films': soon_films})

def add(request):
    return render(request, 'cms/elements/create_film.html')
