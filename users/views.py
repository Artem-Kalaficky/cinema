from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import UserProfile
from .forms import ChangeUserInfoForm, RegisterUserForm
from main.models import Page


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('main')


class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('main')


@login_required()
def profile(request):
    main_page = Page.objects.get(is_main=True)
    context = {'main_page': main_page}
    return render(request, 'users/profile.html', context)


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'main/pages/account.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('account')
    success_message = 'Данные пользователя успешно изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

    def get_context_data(self, **kwargs):
        context = super(ChangeUserInfoView, self).get_context_data(**kwargs)
        main_page = Page.objects.get(is_main=True)
        context['main_page'] = main_page
        return context


class RegisterUserView(CreateView):
    model = UserProfile
    template_name = 'users/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main')

