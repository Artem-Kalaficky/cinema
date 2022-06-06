import datetime

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView

from .models import Page, Banner, Slide, Carousel, Film, Cinema, Hall, Session


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


def cinemas(request):
    context = {'cinemas': Cinema.objects.all(),
               'main_page': Page.objects.get(is_main=True)}
    return render(request, 'main/pages/cinemas/cinemas.html', context)


class DetailCinemaView(DetailView):
    model = Cinema
    template_name = 'main/pages/cinemas/cinema.html'

    def get_context_data(self, **kwargs):
        context = super(DetailCinemaView, self).get_context_data(**kwargs)
        context['main_page'] = Page.objects.get(is_main=True)
        context['images'] = get_object_or_404(Cinema, pk=self.kwargs['pk']).images.all()
        halls = Hall.objects.filter(cinema=self.kwargs['pk'])
        idx = []
        for hall in halls:
            idx.append(hall.id)
        context['sessions'] = Session.objects.filter(hall_id__in=idx)
        context['halls'] = halls
        context['count_halls'] = len(halls)
        return context
