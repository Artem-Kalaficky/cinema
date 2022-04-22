from django.urls import path

from .views import cms, film, filmview


urlpatterns = [
    path('', cms, name='cms'),
    path('film/add/', filmview, name='add'),
    path('film/', film, name='film'),
]