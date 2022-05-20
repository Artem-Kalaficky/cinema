from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .models import Page, Banner
from users.models import UserProfile


def main(request):
    main_page = Page.objects.get(is_main=True)
    banner = Banner.objects.get()
    context = {'main_page': main_page,
               'banner': banner}
    return render(request, 'main/pages/index.html', context)


