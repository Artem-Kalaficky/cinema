from django.urls import path

from .views import cms


urlpatterns = [
    path('', cms, name='cms')
]