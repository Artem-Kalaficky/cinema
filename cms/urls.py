from django.urls import path

from .views import cms, film, FilmCreateViev


urlpatterns = [
    path('', cms, name='cms'),
    path('film/add/', FilmCreateViev.as_view(), name='add'),
    path('film/', film, name='film'),
]