import datetime

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView

from .models import Page, Banner, Slide, Carousel, Film, Cinema, Hall, Session, NewsOrProm, Contact


def main(request):
    context = {'main_page': Page.objects.get(is_main=True),
               'banner': Banner.objects.get(),
               'top_slides': Slide.objects.filter(is_main=True),
               'top_carousel': Carousel.objects.get(is_main=True),
               'bottom_carousel': Carousel.objects.get(is_main=False),
               'bottom_slides': Slide.objects.filter(is_main=False),
               'day': timezone.now(),
               'current_films': Film.objects.filter(premier_date__lte=datetime.date.today()),
               'soon_films': Film.objects.filter(premier_date__gt=datetime.date.today()),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False)}
    return render(request, 'main/pages/index.html', context)


# region POSTER/SOON
def poster(request):
    context = {'current_films': Film.objects.filter(premier_date__lte=datetime.date.today()),
               'soon_films': Film.objects.filter(premier_date__gt=datetime.date.today()),
               'main_page': Page.objects.get(is_main=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False)}
    return render(request, 'main/pages/poster.html', context)


def soon(request):
    context = {'soon_films': Film.objects.filter(premier_date__gt=datetime.date.today()),
               'main_page': Page.objects.get(is_main=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False),
               'current_films': Film.objects.filter(premier_date__lte=datetime.date.today())}
    return render(request, 'main/pages/soon.html', context)
# endregion POSTER/SOON


# region CINEMAS
def cinemas(request):
    context = {'cinemas': Cinema.objects.all(),
               'main_page': Page.objects.get(is_main=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False)}
    return render(request, 'main/pages/cinemas/cinemas.html', context)


class DetailCinemaView(DetailView):
    model = Cinema
    template_name = 'main/pages/cinemas/cinema.html'

    def get_context_data(self, **kwargs):
        context = super(DetailCinemaView, self).get_context_data(**kwargs)
        context['main_page'] = Page.objects.get(is_main=True)
        context['images'] = self.object.images.all()
        halls = Hall.objects.filter(cinema=self.kwargs['pk'])
        idx = []
        for hall in halls:
            idx.append(hall.id)
        context['sessions'] = Session.objects.filter(hall_id__in=idx)
        context['halls'] = halls
        context['count_halls'] = len(halls)
        context['pages'] = Page.objects.filter(is_main=False, is_base=True, is_contact=False)
        return context


class DetailHallView(DetailView):
    model = Hall
    template_name = 'main/pages/cinemas/hall.html'

    def get_context_data(self, **kwargs):
        context = super(DetailHallView, self).get_context_data(**kwargs)
        context['main_page'] = Page.objects.get(is_main=True)
        context['sessions'] = Session.objects.filter(hall=self.kwargs['pk'])
        context['images'] = self.object.images.all()
        context['pages'] = Page.objects.filter(is_main=False, is_base=True, is_contact=False)
        return context
# endregion CINEMAS


# region PROMOTIONS
def promotions(request):
    context = {'main_page': Page.objects.get(is_main=True),
               'promotions': NewsOrProm.objects.filter(type=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False)}
    return render(request, 'main/pages/promotions/promotions.html', context)


def concrete_promotion(request, promotion_id):
    context = {'main_page': Page.objects.get(is_main=True),
               'promotion': get_object_or_404(NewsOrProm, pk=promotion_id),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False)}
    return render(request, 'main/pages/promotions/promotion.html', context)
# endregion PROMOTIONS


# region PAGES
def about_cinema(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    context = {'main_page': Page.objects.get(is_main=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False),
               'page': page,
               'images': page.images.all()}
    return render(request, 'main/pages/pages/about_cinema_pages.html', context)


def news(request):
    context = {'main_page': Page.objects.get(is_main=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False),
               'news': NewsOrProm.objects.filter(type=False)}
    return render(request, 'main/pages/pages/news.html', context)


def concrete_news(request, news_id):
    context = {'main_page': Page.objects.get(is_main=True),
               'news': get_object_or_404(NewsOrProm, pk=news_id),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False)}
    return render(request, 'main/pages/pages/concrete_news.html', context)


def mobile_app(request):
    context = {'main_page': Page.objects.get(is_main=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False)}
    return render(request, 'main/pages/pages/mobile_app.html', context)


def contacts(request):
    context = {'main_page': Page.objects.get(is_main=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False),
               'contact_page': Page.objects.filter(is_contact=True),
               'contacts': Contact.objects.all()}
    return render(request, 'main/pages/pages/contacts.html', context)
# endregion PAGES


# region SESSIONS
def sessions(request):
    halls = Hall.objects.filter(cinema=6)
    idx = []
    for hall in halls:
        idx.append(hall.id)
    sessions = Session.objects.filter(hall_id__in=idx)
    context = {'main_page': Page.objects.get(is_main=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False),
               'cinemas': Cinema.objects.all(),
               'dates': [(datetime.datetime.now() + datetime.timedelta(days=d)).strftime("%m.%d.%Y") for d in range(7)],
               'date_now': datetime.datetime.now(),
               'films': Film.objects.all(),
               'halls': Hall.objects.all(),
               'sessions': sessions}
    return render(request, 'main/pages/sessions.html', context)
# endregion SESSIONS