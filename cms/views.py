import datetime

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from main.models import Film
from .forms import FilmForm


def cms(request):
    return render(request, 'cms/layout/base.html')

def film(request):
    current_films = Film.objects.filter(premier_date__lte=datetime.date.today())
    soon_films = Film.objects.filter(premier_date__gt=datetime.date.today())
    return render(request, 'cms/pages/film_list.html', {'current_films': current_films, 'soon_films': soon_films})

# def add(request):
#     return render(request, 'cms/elements/create_film.html')


class FilmCreateViev(CreateView):
    template_name = 'cms/elements/create_film.html'
    form_class = FilmForm
    success_url = reverse_lazy('film')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

