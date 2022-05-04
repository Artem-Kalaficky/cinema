from django.urls import path

from .views import cms, film_list, add_film, edit_film


urlpatterns = [
    path('', cms, name='cms'),
    path('film/<int:film_id>/edit/', edit_film, name='edit'),
    path('film/add/', add_film, name='add'),
    path('film/', film_list, name='film'),
]