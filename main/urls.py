from django.urls import path

from .views import main, poster, soon, cinemas, DetailCinemaView, DetailHallView, promotions


urlpatterns = [
    path('', main, name='main'),
    path('poster/', poster, name='poster'),
    path('soon/', soon, name='soon'),
    # cinemas
    path('cinemas/cinema/<int:pk>/', DetailCinemaView.as_view(), name='concrete_cinema'),
    path('cinemas/cinema/hall/<int:pk>', DetailHallView.as_view(), name='concrete_hall'),
    path('cinemas/', cinemas, name='cinemas'),
    # promotions
    path('promotions/', promotions, name='promotions'),
]