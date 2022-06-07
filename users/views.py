from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy


from .models import UserProfile
from .forms import ChangeUserInfoForm, RegisterUserForm
from main.models import Page


class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        if not self.request.user.is_ru:
            lang = '/uk/'
        else:
            lang = '/ru/'
        return HttpResponseRedirect(lang)


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
    success_url = None

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.user_id)
        self.user_lang = obj.is_ru
        return obj

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if self.user_lang:
            self.success_url = '/ru/users/accounts/'
        else:
            self.success_url = '/uk/users/accounts/'
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ChangeUserInfoView, self).get_context_data(**kwargs)
        main_page = Page.objects.get(is_main=True)
        context['main_page'] = main_page
        context['pages'] = Page.objects.filter(is_main=False, is_base=True, is_contact=False)
        context['contact_page'] = Page.objects.filter(is_contact=True)
        return context


class RegisterUserView(CreateView):
    model = UserProfile
    template_name = 'users/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main')

