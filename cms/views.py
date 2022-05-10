import datetime

from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from main.models import Film, Image, Seo
from .forms import FilmForm, SeoForm, FilmGalleryFormSet


def cms(request):
    return render(request, 'cms/layout/base.html')

# FILM PAGE-------------------------------------------------------------------------------------------------------------
def film_list(request):
    current_films = Film.objects.filter(premier_date__lte=datetime.date.today())
    soon_films = Film.objects.filter(premier_date__gt=datetime.date.today())
    context = {'current_films': current_films,
               'soon_films': soon_films}
    return render(request, 'cms/pages/film/film_list.html', context)


def add_film(request):
    base_form = FilmForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = FilmGalleryFormSet(request.POST or None, request.FILES or None,
                                         queryset=Image.objects.none(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, prefix='seo_form')
    if request.method == 'POST':

        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            film = base_form.save(commit=False)
            film.seo = seo_form.instance
            film.save()
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    film.images.add(image)

        return redirect('film')

    context = {'base_form': base_form,
               'gallery_formset': gallery_formset,
               'seo_form': seo_form}
    return render(request, 'cms/pages/film/create_film.html', context)


def edit_film(request, film_id):
    film = Film.objects.get(pk=film_id)
    seo = Seo.objects.get(pk=film_id)
    base_form = FilmForm(request.POST or None, request.FILES or None, instance=film, prefix='base_form')
    gallery_formset = FilmGalleryFormSet(request.POST or None, request.FILES or None,
                                         queryset=film.images.all(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, instance=seo, prefix='seo_form')
    if request.method == 'POST':

        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            film = base_form.save(commit=False)
            film.seo = seo_form.instance
            film.save()
            gallery_formset.save(commit=False)
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    film.images.add(image)
            for form in gallery_formset.deleted_objects:
                form.delete()
            gallery_formset.save_m2m()
        return redirect('film')

    context = {'film': film,
               'base_form': base_form,
               'seo_form': seo_form,
               'gallery_formset': gallery_formset}
    return render(request, 'cms/pages/film/edit_film.html', context)


def delete_film(request, film_id):
    film = Film.objects.get(pk=film_id)
    if request.method == 'POST':
        film.delete()
        return redirect('film')
    else:
        context = {'film': film}
        return render(request, 'cms/pages/film/film_confirm_delete.html', context)





