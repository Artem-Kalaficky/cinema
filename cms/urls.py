from django.urls import path

from .views import *


urlpatterns = [
    #films
    path('', cms, name='cms'),
    path('film/<int:film_id>/delete/', delete_film, name='delete_film'),
    path('film/<int:film_id>/edit/', edit_film, name='edit_film'),
    path('film/add/', add_film, name='add_film'),
    path('film/', film_list, name='film'),
    #cinemas
    path('cinema/<int:cinema_id>/<int:hall_id>/delete-hall/', delete_hall, name='delete_hall'),
    path('cinema/<int:cinema_id>/<int:hall_id>/edit-hall/', edit_hall, name='edit_hall'),
    path('cinema/<int:cinema_id>/add-hall/', add_hall, name='add_hall'),
    #halls of cinema
    path('cinema/<int:cinema_id>/delete/', delete_cinema, name='delete_cinema'),
    path('cinema/<int:cinema_id>/edit/', edit_cinema, name='edit_cinema'),
    path('cinema/add/', add_cinema, name='add_cinema'),
    path('cinema/', cinema_list, name='cinema'),
    #news
    path('news/<int:news_id>/delete/', delete_news, name='delete_news'),
    path('news/<int:news_id>/edit/', edit_news, name='edit_news'),
    path('news/add/', add_news, name='add_news'),
    path('news/', news_list, name='news'),
    #promotion
    path('promotion/<int:promotion_id>/delete/', delete_promotion, name='delete_promotion'),
    path('promotion/<int:promotion_id>/edit/', edit_promotion, name='edit_promotion'),
    path('promotion/add/', add_promotion, name='add_promotion'),
    path('promotion/', promotion_list, name='promotion'),
    #pages
    path('pages/<int:page_id>/delete/', delete_page, name='delete_page'),
    path('pages/<int:page_id>/edit-main/', edit_main_page, name='edit_main_page'),
    path('pages/<int:page_id>/edit-contacts/', edit_contact_page, name='edit_contact_page'),
    path('pages/<int:page_id>/edit/', edit_page, name='edit_page'),
    path('pages/add/', add_page, name='add_page'),
    path('pages/', pages_list, name='pages'),
    #banners
    path('banners-sliders/', banner_list, name='banners'),

]