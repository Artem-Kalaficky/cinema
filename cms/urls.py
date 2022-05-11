from django.urls import path

from .views import *


urlpatterns = [
    path('', cms, name='cms'),
    path('film/<int:film_id>/delete/', delete_film, name='delete_film'),
    path('film/<int:film_id>/edit/', edit_film, name='edit_film'),
    path('film/add/', add_film, name='add_film'),
    path('film/', film_list, name='film'),
    path('cinema/<int:cinema_id>/add-hall/', add_hall, name='add_hall'),
    path('cinema/<int:cinema_id>/delete/', delete_cinema, name='delete_cinema'),
    path('cinema/<int:cinema_id>/edit/', edit_cinema, name='edit_cinema'),
    path('cinema/add/', add_cinema, name='add_cinema'),
    path('cinema/', cinema_list, name='cinema'),
]