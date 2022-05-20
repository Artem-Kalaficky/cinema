from django.urls import path

from .views import UserLoginView, profile


urlpatterns = [
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),

]