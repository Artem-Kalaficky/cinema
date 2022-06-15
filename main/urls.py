from django.urls import path

from .views import main, poster, soon, cinemas, DetailCinemaView, DetailHallView, promotions, concrete_promotion, \
    about_cinema, news, concrete_news, mobile_app, contacts, sessions, film_card


urlpatterns = [
    path('', main, name='main'),
    path('poster/', poster, name='poster'),
    path('soon/', soon, name='soon'),
    # cinemas
    path('cinemas/cinema/<int:pk>/', DetailCinemaView.as_view(), name='concrete_cinema'),
    path('cinemas/cinema/hall/<int:pk>', DetailHallView.as_view(), name='concrete_hall'),
    path('cinemas/', cinemas, name='cinemas'),
    # promotions
    path('promotions/<int:promotion_id>', concrete_promotion, name='concrete_promotion'),
    path('promotions/', promotions, name='promotions'),
    # about cinema pages
    path('about-cinema/<int:page_id>/', about_cinema, name='about_cinema'),
    path('news/<int:news_id>', concrete_news, name='concrete_news'),
    path('news/', news, name='about_news'),
    path('mobile_app/', mobile_app, name='mobile_app'),
    path('contacts/', contacts, name='about_contacts'),
    # sessions
    path('sessions/', sessions, name='sessions'),
    # film card
    path('film/<int:film_id>/', film_card, name='film_card')
]