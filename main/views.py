import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView


from .models import Page, Banner, Slide, Carousel, Film, Cinema, Hall, Session, NewsOrProm, Contact
from .serializers import serialize

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
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:

        if request.method == 'GET':
            response = {}
            cinema_id = request.GET.get('cinema_id')
            print(cinema_id)
            hall_id = request.GET.get('hall_id')
            film = request.GET.get('film')
            date = int(datetime.datetime.now().strftime("%d.%m.%Y").split('.')[0])
            type_2d = True if request.GET.get('2d') == 'true' else False
            type_3d = True if request.GET.get('3d') == 'true' else False
            type_imax = True if request.GET.get('imax') == 'true' else False
            sessions = Session.objects.filter(time__day=date)
            if cinema_id != 'false':
                halls = Hall.objects.filter(cinema=cinema_id)
                idx = []
                for hall in halls:
                    idx.append(hall.id)
                sessions = sessions.filter(hall_id__in=idx)
            print(sessions)
            # if cinema_id is not None:
            #     halls = Hall.objects.filter(cinema=cinema_id)
            #     response['halls'] = json.loads(json.dumps([{'hall_id': hall.id, 'hall': hall.hall_number} for hall in halls]))
            #     idx = []
            #     for hall in halls:
            #         idx.append(hall.id)
            #         response['json_data'] = serialize(Session.objects.filter(hall_id__in=idx, film__type_2d=type_2d, film__type_3d=type_3d, film__type_imax=type_imax))
            #     if hall_id is not None:
            #         response['json_data'] = serialize(Session.objects.filter(hall_id=hall_id, hall__cinema=cinema_id))
            #         if film is not None:
            #             response['json_data'] = serialize(Session.objects.filter(hall_id=hall_id, hall__cinema=cinema_id, film__name=film))
            return JsonResponse({}, status=200)

    context = {'main_page': Page.objects.get(is_main=True),
               'pages': Page.objects.filter(is_main=False, is_base=True, is_contact=False),
               'cinemas': Cinema.objects.all(),
               'dates': [(datetime.datetime.now() + datetime.timedelta(days=d)).strftime("%d.%m.%Y") for d in range(7)],
               'date_now': datetime.datetime.now(),
               'films': Film.objects.all(),
               'halls': Hall.objects.all(),
               'sessions': Session.objects.all()}
    return render(request, 'main/pages/sessions.html', context)
# endregion SESSIONS

# if cinema_id:
#     if cinema_id != 'all':
#         halls = Hall.objects.filter(cinema=cinema_id)
#         response['halls'] = json.loads(json.dumps([{'hall_id': hall.id, 'hall': hall.hall_number} for hall in halls]))
#     if cinema_id == 'all':
#         halls = Hall.objects.all()
# if hall_id:
#     if hall_id != 'all':
#         idx.append(hall_id)
# if halls:
#     idx = []
#     for hall in halls:
#         idx.append(hall.id)
# int(request.GET.get('date').split('.')[0]) or