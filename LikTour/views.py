from django.shortcuts import render, get_object_or_404, redirect
from .models import CountryTour, Cities, SmallContactForm
from django.contrib import messages

def index(request):
    countries = CountryTour.objects.select_related('city').all()
    country_city_map = {}
    for country_tour in countries:
        country_name = country_tour.country
        if country_name not in country_city_map:
            country_city_map[country_name] = {
                'photo': country_tour.country_photo.url if country_tour.country_photo else None,
                'cities': []
            }
        country_city_map[country_name]['cities'].append(country_tour.city)

    context = {
        'country_city_map': country_city_map,
    }
    return render(request, 'LikTour/index.html', context)

def city_detail(request, city_id):
    city = get_object_or_404(Cities, id=city_id)
    country = CountryTour.objects.filter(city=city).first()  # Получаем страну для города
    context = {
        'city': city,
        'country': country.country if country else 'Не указана страна',
    }
    return render(request, 'LikTour/city_detail.html', context)