import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from main.models import Film, Image, Cinema, Hall, NewsOrProm
from .forms import *


def cms(request):
    return render(request, 'cms/layout/base.html')

# region FILM PAGE
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
    film = get_object_or_404(Film, pk=film_id)
    seo = film.seo
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
    film = get_object_or_404(Film, pk=film_id)
    if request.method == 'POST':
        film.delete()
        return redirect('film')
    else:
        context = {'film': film}
        return render(request, 'cms/pages/film/film_confirm_delete.html', context)
# endregion FILM PAGE

# region CINEMA PAGE
def cinema_list(request):
    cinemas = Cinema.objects.all()
    return render(request, 'cms/pages/cinema/cinema_list.html', {'cinemas': cinemas})


def add_cinema(request):
    base_form = CinemaForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = CinemaGalleryFormSet(request.POST or None, request.FILES or None,
                                         queryset=Image.objects.none(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and gallery_formset.is_valid() and seo_form.is_valid():
            seo_form.save()
            cinema = base_form.save(commit=False)
            cinema.seo = seo_form.instance
            cinema.save()
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    cinema.images.add(image)
        return redirect('cinema')
    context = {'base_form': base_form,
               'gallery_formset': gallery_formset,
               'seo_form': seo_form}
    return render(request, 'cms/pages/cinema/create_cinema.html', context)


def edit_cinema(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    halls = Hall.objects.filter(cinema=cinema_id)
    seo = cinema.seo
    base_form = CinemaForm(request.POST or None, request.FILES or None, instance=cinema, prefix='base_form')
    gallery_formset = CinemaGalleryFormSet(request.POST or None, request.FILES or None,
                                         queryset=cinema.images.all(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, instance=seo, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            cinema = base_form.save(commit=False)
            cinema.seo = seo_form.instance
            cinema.save()
            gallery_formset.save(commit=False)
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    cinema.images.add(image)
            for form in gallery_formset.deleted_objects:
                form.delete()
            gallery_formset.save_m2m()
        return redirect('cinema')
    context = {'cinema': cinema,
               'halls': halls,
               'base_form': base_form,
               'seo_form': seo_form,
               'gallery_formset': gallery_formset}
    return render(request, 'cms/pages/cinema/edit_cinema.html', context)


def delete_cinema(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    if request.method == 'POST':
        cinema.delete()
        return redirect('cinema')
    else:
        context = {'cinema': cinema}
        return render(request, 'cms/pages/cinema/cinema_confirm_delete.html', context)
# endregion CINEMA PAGE

# region HALL PAGE
def add_hall(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    base_form = HallForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = HallGalleryFormSet(request.POST or None, request.FILES or None,
                                           queryset=Image.objects.none(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and gallery_formset.is_valid() and seo_form.is_valid():
            seo_form.save()
            hall = base_form.save(commit=False)
            hall.seo = seo_form.instance
            hall.cinema = cinema
            hall.save()
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    hall.images.add(image)
        return redirect('edit_cinema', cinema_id)
    context = {'cinema': cinema,
               'base_form': base_form,
               'gallery_formset': gallery_formset,
               'seo_form': seo_form}
    return render(request, 'cms/pages/hall/create_hall.html', context)


def edit_hall(request, cinema_id, hall_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    hall = get_object_or_404(Hall, pk=hall_id)
    seo = hall.seo
    base_form = HallForm(request.POST or None, request.FILES or None, instance=hall, prefix='base_form')
    gallery_formset = HallGalleryFormSet(request.POST or None, request.FILES or None,
                                           queryset=hall.images.all(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, instance=seo, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            hall = base_form.save(commit=False)
            hall.seo = seo_form.instance
            hall.save()
            gallery_formset.save(commit=False)
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    hall.images.add(image)
            for form in gallery_formset.deleted_objects:
                form.delete()
            gallery_formset.save_m2m()
        return redirect('edit_cinema', cinema_id)
    context = {'cinema': cinema,
               'hall': hall,
               'base_form': base_form,
               'gallery_formset': gallery_formset,
               'seo_form': seo_form}
    return render(request, 'cms/pages/hall/edit_hall.html', context)


def delete_hall(request, cinema_id, hall_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    hall = get_object_or_404(Hall, pk=hall_id)

    if request.method == 'POST':
        hall.delete()
        return redirect('edit_cinema', cinema_id)
    else:
        context = {'cinema': cinema,
                   'hall': hall}
        return render(request, 'cms/pages/hall/hall_confirm_delete.html', context)
# endregion HALL PAGE

# region NEWS PAGE
def news_list(request):
    newss = NewsOrProm.objects.filter(type=False)
    return render(request, 'cms/pages/news/news_list.html', {'newss': newss})


def add_news(request):
    base_form = NPForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = NPGalleryFormSet(request.POST or None, request.FILES or None,
                                         queryset=Image.objects.none(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            news = base_form.save(commit=False)
            news.seo = seo_form.instance
            news.save()
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    news.images.add(image)
        return redirect('news')
    context = {'base_form': base_form,
               'gallery_formset': gallery_formset,
               'seo_form': seo_form}
    return render(request, 'cms/pages/news/create_news.html', context)


def edit_news(request, news_id):
    news = get_object_or_404(NewsOrProm, pk=news_id)
    seo = news.seo
    base_form = NPForm(request.POST or None, request.FILES or None, instance=news, prefix='base_form')
    gallery_formset = NPGalleryFormSet(request.POST or None, request.FILES or None,
                                         queryset=news.images.all(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, instance=seo, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            news = base_form.save(commit=False)
            news.seo = seo_form.instance
            news.save()
            gallery_formset.save(commit=False)
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    news.images.add(image)
            for form in gallery_formset.deleted_objects:
                form.delete()
            gallery_formset.save_m2m()
        return redirect('news')
    context = {'news': news,
               'base_form': base_form,
               'seo_form': seo_form,
               'gallery_formset': gallery_formset}
    return render(request, 'cms/pages/news/edit_news.html', context)


def delete_news(request, news_id):
    news = get_object_or_404(NewsOrProm, pk=news_id)
    if request.method == 'POST':
        news.delete()
        return redirect('news')
    else:
        context = {'news': news}
        return render(request, 'cms/pages/news/news_confirm_delete.html', context)
# endregion NEWS PAGE



