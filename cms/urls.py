from django.urls import path

from .views import cms, film_list, add_film


urlpatterns = [
    path('', cms, name='cms'),
    path('film/add/', add_film, name='add'),
    path('film/', film_list, name='film'),
]