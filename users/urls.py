from django.urls import path

from .views import UserLoginView, UserLogoutView, profile, ChangeUserInfoView, RegisterUserView


urlpatterns = [
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/', ChangeUserInfoView.as_view(), name='account')
]