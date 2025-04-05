from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('city/<int:city_id>/', city_detail, name='city_detail'),
    path('all-tours/', all_tours, name='properties'),
    path('all-news/', all_news, name='all_news'),
    path('news/<int:news_id>', news_detail, name='news_detail'),
    path('about-us/', about_us, name='about_us'),
    path('contact-us/', contact_with_us, name='contact_with_us'),
    path('policy/', our_policy, name='our_policy'),
    path('agreement/', agreement, name='agreement')
]