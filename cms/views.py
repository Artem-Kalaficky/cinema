import datetime

from celery.result import AsyncResult
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

from users.models import UserProfile
from users.forms import ChangeUserInfoForm
from main.models import Ticket, Session
from .tasks import send
from .forms import *


# region statistics
@user_passes_test(lambda u: u.is_staff)
def statistics(request):
    films = Ticket.objects.all()
    dates = [(datetime.datetime.now() + datetime.timedelta(days=d)) for d in range(7)]
    sessions = Session.objects.all()
    male = len(films.filter(user__is_male=True))
    female = len(films.filter(user__is_male=False))
    count_cinema_city = []
    count_multiplex = []
    count_sessions_list = []
    for date in dates:
        day = sessions.filter(time__day=date.strftime("%d"))
        count_multiplex.append(len(day.filter(hall__cinema=2)))
        count_cinema_city.append(len(day.filter(hall__cinema=6)))
        count_sessions_list.append(len(day))
    context = {'users': UserProfile.objects.all(),
               'count_users': len(UserProfile.objects.all()),
               'doc': films.filter(sessions__film__name='Доктор Стрэндж: В мультивселенной безумия'),
               'mor': films.filter(sessions__film__name='Морбиус'),
               'spider': films.filter(sessions__film__name='Человек-Паук: Нет пути домой'),
               'venom': films.filter(sessions__film__name='Веном 2'),
               'mutant': films.filter(sessions__film__name='Новые мутанты'),
               'dates': dates,
               'sum_sessions': count_sessions_list,
               'male': male,
               'female': female,
               'male_percent': male / len(films) * 100,
               'female_percent': female / len(films) * 100,
               'count_multiplex': count_multiplex,
               'count_cinema_city': count_cinema_city}
    return render(request, 'cms/pages/statistics.html', context)
# endregion statistics


# region FILM page
@user_passes_test(lambda u: u.is_staff)
def film_list(request):
    current_films = Film.objects.filter(premier_date__lte=datetime.date.today())
    soon_films = Film.objects.filter(premier_date__gt=datetime.date.today())
    context = {'current_films': current_films,
               'soon_films': soon_films}
    return render(request, 'cms/pages/film/film_list.html', context)


@user_passes_test(lambda u: u.is_staff)
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


@user_passes_test(lambda u: u.is_staff)
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
# endregion FILM page


# region CINEMA page
@user_passes_test(lambda u: u.is_staff)
def cinema_list(request):
    cinemas = Cinema.objects.all()
    return render(request, 'cms/pages/cinema/cinema_list.html', {'cinemas': cinemas})


@user_passes_test(lambda u: u.is_staff)
def add_cinema(request):
    base_form = CinemaForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = CinemaGalleryFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.none(),
                                           prefix='gallery_formset')
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


@user_passes_test(lambda u: u.is_staff)
def edit_cinema(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    halls = Hall.objects.filter(cinema=cinema_id)
    seo = cinema.seo
    base_form = CinemaForm(request.POST or None, request.FILES or None, instance=cinema, prefix='base_form')
    gallery_formset = CinemaGalleryFormSet(request.POST or None, request.FILES or None, queryset=cinema.images.all(),
                                           prefix='gallery_formset')
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
# endregion CINEMA page


# region HALL page
@user_passes_test(lambda u: u.is_staff)
def add_hall(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    base_form = HallForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = HallGalleryFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.none(),
                                         prefix='gallery_formset')
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


@user_passes_test(lambda u: u.is_staff)
def edit_hall(request, cinema_id, hall_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    hall = get_object_or_404(Hall, pk=hall_id)
    seo = hall.seo
    base_form = HallForm(request.POST or None, request.FILES or None, instance=hall, prefix='base_form')
    gallery_formset = HallGalleryFormSet(request.POST or None, request.FILES or None, queryset=hall.images.all(),
                                         prefix='gallery_formset')
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
# endregion HALL page


# region NEWS page
@user_passes_test(lambda u: u.is_staff)
def news_list(request):
    newss = NewsOrProm.objects.filter(type=False)
    return render(request, 'cms/pages/news/news_list.html', {'newss': newss})


@user_passes_test(lambda u: u.is_staff)
def add_news(request):
    base_form = NPForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = NPGalleryFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.none(),
                                       prefix='gallery_formset')
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


@user_passes_test(lambda u: u.is_staff)
def edit_news(request, news_id):
    news = get_object_or_404(NewsOrProm, pk=news_id)
    seo = news.seo
    base_form = NPForm(request.POST or None, request.FILES or None, instance=news, prefix='base_form')
    gallery_formset = NPGalleryFormSet(request.POST or None, request.FILES or None, queryset=news.images.all(),
                                       prefix='gallery_formset')
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
# endregion NEWS page


# region PROMOTION page
@user_passes_test(lambda u: u.is_staff)
def promotion_list(request):
    promotions = NewsOrProm.objects.filter(type=True)
    return render(request, 'cms/pages/promotion/promotion_list.html', {'promotions': promotions})


@user_passes_test(lambda u: u.is_staff)
def add_promotion(request):
    base_form = NPForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = NPGalleryFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.none(),
                                       prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            promotion = base_form.save(commit=False)
            promotion.seo = seo_form.instance
            promotion.save()
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    promotion.images.add(image)
        return redirect('promotion')
    context = {'base_form': base_form,
               'gallery_formset': gallery_formset,
               'seo_form': seo_form}
    return render(request, 'cms/pages/promotion/create_promotion.html', context)


@user_passes_test(lambda u: u.is_staff)
def edit_promotion(request, promotion_id):
    promotion = get_object_or_404(NewsOrProm, pk=promotion_id)
    seo = promotion.seo
    base_form = NPForm(request.POST or None, request.FILES or None, instance=promotion, prefix='base_form')
    gallery_formset = NPGalleryFormSet(request.POST or None, request.FILES or None, queryset=promotion.images.all(),
                                       prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, instance=seo, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            promotion = base_form.save(commit=False)
            promotion.seo = seo_form.instance
            promotion.save()
            gallery_formset.save(commit=False)
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    promotion.images.add(image)
            for form in gallery_formset.deleted_objects:
                form.delete()
            gallery_formset.save_m2m()
        return redirect('promotion')
    context = {'promotion': promotion,
               'base_form': base_form,
               'seo_form': seo_form,
               'gallery_formset': gallery_formset}
    return render(request, 'cms/pages/promotion/edit_promotion.html', context)


def delete_promotion(request, promotion_id):
    promotion = get_object_or_404(NewsOrProm, pk=promotion_id)
    if request.method == 'POST':
        promotion.delete()
        return redirect('promotion')
    else:
        context = {'promotion': promotion}
        return render(request, 'cms/pages/promotion/promotion_confirm_delete.html', context)
# endregion PROMOTION page


# region PAGES page
@user_passes_test(lambda u: u.is_staff)
def pages_list(request):
    pages = Page.objects.filter(is_main=False, is_contact=False)
    main_page = Page.objects.filter(is_main=True)
    contact_page = Page.objects.filter(is_contact=True)
    context = {'pages': pages,
               'main_page': main_page,
               'contact_page': contact_page}
    return render(request, 'cms/pages/pages/pages_list.html', context)


@user_passes_test(lambda u: u.is_staff)
def add_page(request):
    base_form = PageForm(request.POST or None, request.FILES or None, prefix='base_form')
    gallery_formset = PageGalleryFormSet(request.POST or None, request.FILES or None,
                                         queryset=Image.objects.none(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            page = base_form.save(commit=False)
            page.seo = seo_form.instance
            page.save()
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    page.images.add(image)
        return redirect('pages')
    context = {'base_form': base_form,
               'gallery_formset': gallery_formset,
               'seo_form': seo_form}
    return render(request, 'cms/pages/pages/create_page.html', context)


@user_passes_test(lambda u: u.is_staff)
def edit_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    seo = page.seo
    base_form = PageForm(request.POST or None, request.FILES or None, instance=page, prefix='base_form')
    gallery_formset = PageGalleryFormSet(request.POST or None, request.FILES or None,
                                         queryset=page.images.all(), prefix='gallery_formset')
    seo_form = SeoForm(request.POST or None, instance=seo, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid() and gallery_formset.is_valid():
            seo_form.save()
            page = base_form.save(commit=False)
            page.seo = seo_form.instance
            page.save()
            gallery_formset.save(commit=False)
            for form in gallery_formset:
                if form.is_valid() and form.cleaned_data:
                    image = form.save()
                    page.images.add(image)
            for form in gallery_formset.deleted_objects:
                form.delete()
            gallery_formset.save_m2m()
        return redirect('pages')
    context = {'page': page,
               'base_form': base_form,
               'seo_form': seo_form,
               'gallery_formset': gallery_formset}
    return render(request, 'cms/pages/pages/edit_page.html', context)


@user_passes_test(lambda u: u.is_staff)
def edit_main_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    seo = page.seo
    base_form = PageForm(request.POST or None, request.FILES or None, instance=page, prefix='base_form')
    seo_form = SeoForm(request.POST or None, instance=seo, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid():
            seo_form.save()
            page = base_form.save(commit=False)
            page.seo = seo_form.instance
            page.save()
        return redirect('pages')
    context = {'page': page,
               'base_form': base_form,
               'seo_form': seo_form}
    return render(request, 'cms/pages/pages/edit_main_page.html', context)


@user_passes_test(lambda u: u.is_staff)
def edit_contact_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    seo = page.seo
    base_form = PageForm(request.POST or None, request.FILES or None, instance=page, prefix='base_form')
    contact_formset = ContactFormSet(request.POST or None, request.FILES or None,
                                     queryset=Contact.objects.all(), prefix='contact_formset')
    seo_form = SeoForm(request.POST or None, instance=seo, prefix='seo_form')
    if request.method == 'POST':
        if base_form.is_valid() and seo_form.is_valid() and contact_formset.is_valid():
            seo_form.save()
            page = base_form.save(commit=False)
            page.seo = seo_form.instance
            for form in contact_formset:
                if form.is_valid() and form.cleaned_data:
                    form.save()
            page.save()
        return redirect('pages')
    context = {'page': page,
               'base_form': base_form,
               'seo_form': seo_form,
               'contact_formset': contact_formset}
    return render(request, 'cms/pages/pages/edit_contact_page.html', context)


def delete_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    if request.method == 'POST':
        page.delete()
        return redirect('pages')
    else:
        context = {'page': page}
        return render(request, 'cms/pages/pages/page_confirm_delete.html', context)
# endregion PAGES page


# region BANNERS page
@user_passes_test(lambda u: u.is_staff)
def banner_list(request):
    top_carousel = get_object_or_404(Carousel, is_main=True)
    bottom_carousel = get_object_or_404(Carousel, is_main=False)
    queryset = Slide.objects.filter(is_main=True)
    queryset1 = Slide.objects.filter(is_main=False)
    base_form = CarouselForm(request.POST or None, request.FILES or None, instance=top_carousel, prefix='base_form')
    base_form1 = CarouselForm(request.POST or None, request.FILES or None, instance=bottom_carousel,
                              prefix='base_form1')
    top_carousel_formset = SlideFormSet(request.POST or None, request.FILES or None,
                                        queryset=queryset, prefix='top_carousel_formset')
    bottom_carousel_formset = SlideFormSet(request.POST or None, request.FILES or None,
                                           queryset=queryset1, prefix='bottom_carousel_formset')
    banner = get_object_or_404(Banner)
    banner_form = BannerForm(request.POST or None, request.FILES or None, instance=banner, prefix='banner_form')
    if request.method == 'POST':
        if base_form.is_valid() and top_carousel_formset.is_valid():
            base_form.save()
            top_carousel_formset.save(commit=False)
            for form in top_carousel_formset:
                if form.is_valid() and form.cleaned_data:
                    form.save()
            for form in top_carousel_formset.deleted_objects:
                form.delete()
            top_carousel_formset.save()

        elif base_form1.is_valid() and bottom_carousel_formset.is_valid():
            base_form1.save()
            bottom_carousel_formset.save(commit=False)
            for form in top_carousel_formset:
                if form.is_valid() and form.cleaned_data:
                    form.save()
            for form in bottom_carousel_formset.deleted_objects:
                form.delete()
            bottom_carousel_formset.save()

        elif banner_form.is_valid():
            banner_form.save()

        return redirect('banners')

    context = {'top_carousel': top_carousel,
               'base_form': base_form,
               'top_carousel_formset': top_carousel_formset,
               'base_form1': base_form1,
               'bottom_carousel_formset': bottom_carousel_formset,
               'banner_form': banner_form,
               'banner': banner}
    return render(request, 'cms/pages/banners/banners_list.html', context)
# endregion BANNERS page


# region USERS page
class UsersView(LoginRequiredMixin, ListView):
    template_name = 'cms/pages/users/users_list.html'

    def get_queryset(self):
        return UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        context['users'] = UserProfile.objects.filter(is_staff=False)
        return context


class UsersEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ChangeUserInfoForm
    template_name = 'cms/pages/users/edit_user.html'
    success_url = reverse_lazy('users')

    def get_context_data(self, **kwargs):
        context = super(UsersEditView, self).get_context_data(**kwargs)
        context['users'] = UserProfile.objects.filter(is_staff=False)
        return context


class UsersDeleteView(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('users')

    def get_context_data(self, **kwargs):
        context = super(UsersDeleteView, self).get_context_data(**kwargs)
        context['users'] = UserProfile.objects.filter(is_staff=False)
        return context
# endregion USERS page


# region MAILING page
@user_passes_test(lambda u: u.is_staff)
def mailing(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            recipients = request.POST.get('emails').split(',')
            id_template = request.POST.get('id_template')
            file = request.FILES.get('file')
            if file:
                html_message = file.read().decode()
                task = send.delay(recipients, html_message)
                mail = Mailing(letter=file)
                mail.save()
                return JsonResponse({'task_id': task.task_id}, status=200)
            else:
                html_message = get_object_or_404(Mailing, pk=int(id_template)).letter.read().decode()
                task = send.delay(recipients, html_message)
                return JsonResponse({'task_id': task.task_id}, status=200)
    context = {'users': UserProfile.objects.filter(is_staff=False),
               'templates': Mailing.objects.all().order_by('-id')[:5],
               'file_form': EmailForm(request.POST or None, request.FILES or None, prefix='file_form')}
    return render(request, 'cms/pages/mailing/mailing.html', context)


def task_progress(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            task_id = request.GET.get('task_id')
            task = AsyncResult(task_id)
            if task.state == 'FAILURE' or task.state == 'PENDING':
                response = {
                    'progression': '0'
                }
                return JsonResponse(response, status=200)
            else:
                current = task.info.get('current', 0)
                total = task.info.get('total', 1)
                progression = int((int(current) / int(total)) * 100)
                response = {
                    'progression': progression
                }
                return JsonResponse(response, status=200)


class EmailDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing')
# endregion MAILING page
