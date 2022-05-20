from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from main.models import Page


class UserLoginView(LoginView):
    template_name = 'users/login.html'


@login_required()
def profile(request):
    main_page = Page.objects.get(is_main=True)
    context = {'main_page': main_page}
    return render(request, 'users/profile.html', context)
