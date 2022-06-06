from django.urls import path

from .views import main, poster, soon


urlpatterns = [
    path('', main, name='main'),
    path('poster/', poster, name='poster'),
    path('soon/', soon, name='soon'),
]