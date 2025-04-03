from django.urls import path
from .views import index, city_detail

urlpatterns = [
    path('', index, name='main_page'),
    path('city/<int:city_id>/', city_detail, name='city_detail'),
]