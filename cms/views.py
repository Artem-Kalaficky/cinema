import datetime

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from main.models import Film, Image, Seo
from .forms import FilmForm, FilmSeoFormSet, FilmGalleryFormSet


def cms(request):
    return render(request, 'cms/layout/base.html')

def film_list(request):
    current_films = Film.objects.filter(premier_date__lte=datetime.date.today())
    soon_films = Film.objects.filter(premier_date__gt=datetime.date.today())
    return render(request, 'cms/pages/film_list.html', {'current_films': current_films, 'soon_films': soon_films})


def add_film(request):
    base_form = FilmForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = FilmGalleryFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.none(), prefix='gallery_formset')
    seo_formset = FilmSeoFormSet(request.POST or None, queryset=Seo.objects.none(), prefix='seo_formset')

    if request.method == 'POST' and base_form.is_valid() and gallery_formset.is_valid() and seo_formset.is_valid():
        base_form.save()
        gallery_formset.save()
        seo_formset.save()
        return redirect('film')

    context = {'base_form': base_form,
               'gallery_formset': gallery_formset,
               'seo_formset': seo_formset}
    return render(request, 'cms/elements/create_film.html', context)





