import datetime

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from main.models import Film
from .forms import FilmForm, FilmSeoForm


def cms(request):
    return render(request, 'cms/layout/base.html')

def film(request):
    current_films = Film.objects.filter(premier_date__lte=datetime.date.today())
    soon_films = Film.objects.filter(premier_date__gt=datetime.date.today())
    return render(request, 'cms/pages/film_list.html', {'current_films': current_films, 'soon_films': soon_films})


def filmview(request):
    form = FilmForm(request.POST or None)
    form_seo = FilmSeoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid() and form_seo.is_valid():
        form.save()
        return redirect('film')
    else:
        form = FilmForm()
    context = {'form': form,
               'form_seo': form_seo}
    return render(request, 'cms/elements/create_film.html', context)





