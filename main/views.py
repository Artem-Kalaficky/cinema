import datetime

from django.shortcuts import render

from .models import Page, Banner, Slide, Carousel, Film


NOW = datetime.datetime.now()
def m(month):
    out = ''
    if month == 'January': out = 'января'
    if month == 'December': out = 'декабря'
    if month == 'February': out = 'февраля'
    if month == 'March': out = 'марта'
    if month == 'April': out = 'апреля'
    if month == 'May': out = 'мая'
    if month == 'June': out = 'июня'
    if month == 'July': out = 'июля'
    if month == 'August': out = 'августа'
    if month == 'September': out = 'сентября'
    if month == 'October': out = 'октября'
    if month == 'November': out = 'ноября'
    return out


def main(request):
    day = NOW.strftime("%d ") + m(NOW.strftime("%B"))
    current_films = Film.objects.filter(premier_date__lte=datetime.date.today())
    soon_films = Film.objects.filter(premier_date__gt=datetime.date.today())
    main_page = Page.objects.get(is_main=True)
    banner = Banner.objects.get()
    top_carousel = Carousel.objects.get(is_main=True)
    top_slides = Slide.objects.filter(is_main=True)
    bottom_carousel = Carousel.objects.get(is_main=False)
    bottom_slides = Slide.objects.filter(is_main=False)
    context = {'main_page': main_page,
               'banner': banner,
               'top_slides': top_slides,
               'top_carousel': top_carousel,
               'bottom_carousel': bottom_carousel,
               'bottom_slides': bottom_slides,
               'day': day,
               'current_films': current_films,
               'soon_films': soon_films}
    return render(request, 'main/pages/index.html', context)


