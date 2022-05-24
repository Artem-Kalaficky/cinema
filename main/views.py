from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .models import Page, Banner, Slide
from users.models import UserProfile


def main(request):
    main_page = Page.objects.get(is_main=True)
    banner = Banner.objects.get()
    top_slides = Slide.objects.filter(is_main=True)
    context = {'main_page': main_page,
               'banner': banner,
               'top_slides': top_slides}
    return render(request, 'main/pages/index.html', context)


