from django.urls import path

from .views import cms, film, add


urlpatterns = [
    path('', cms, name='cms'),
    path('film/add/', add, name='add'),
    path('film/', film, name='film'),
]