from django.urls import path

from .views import *


urlpatterns = [
    path('', cms, name='cms'),
    path('film/<int:film_id>/delete/', delete_film, name='delete_film'),
    path('film/<int:film_id>/edit/', edit_film, name='edit_film'),
    path('film/add/', add_film, name='add_film'),
    path('film/', film_list, name='film'),
    path('cinema/', cinema_list, name='cinema'),
    path('cinema/add/', add_cinema, name='add_cinema'),
]