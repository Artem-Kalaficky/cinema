from django.urls import path

from .views import main, poster, soon, cinemas, DetailCinemaView


urlpatterns = [
    path('', main, name='main'),
    path('poster/', poster, name='poster'),
    path('soon/', soon, name='soon'),
    # cinemas
    path('cinemas/<int:pk>/cinema', DetailCinemaView.as_view(), name='concrete_cinema'),
    path('cinemas/', cinemas, name='cinemas'),
]