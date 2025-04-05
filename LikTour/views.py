from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
from .forms import *

def index(request):
    countries = CountryTour.objects.prefetch_related('cities').all()
    country_city_map = {}
    for country_tour in countries:
        country_name = country_tour.country
        if country_name not in country_city_map:
            country_city_map[country_name] = {
                'photo': country_tour.country_photo.url if country_tour.country_photo else None,
                'cities': []
            }
        country_city_map[country_name]['cities'].extend(country_tour.cities.all())

    news_list = News.objects.select_related('news')[:3]
    banners = Banner.objects.all()  # Получаем все баннеры

    question_form = QuestionForm(request.POST or None)
    
    if request.method == 'POST':
        if question_form.is_valid():
            question_form.save()
            return redirect('main_page')
    
    context = {
        'country_city_map': country_city_map,
        'form': question_form,
        'news_list': news_list,
        'banners': banners  # Добавляем баннеры в контекст
    }
    return render(request, 'LikTour/index.html', context)

def city_detail(request, city_id):
    city = get_object_or_404(Cities, id=city_id)
    country_tour = CountryTour.objects.filter(cities=city).first()  # Получаем объект CountryTour

    # Инициализируем форму один раз
    form = SmallContactForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main_page')
    
    context = {
        'city': city,
        'country': country_tour.country if country_tour else 'Не указана страна',
        'form': form
    }
    return render(request, 'LikTour/city_detail.html', context)

def all_tours(request):
    countries = CountryTour.objects.prefetch_related('cities').all()
    country_city_map = {}

    for country_tour in countries:
        country_name = country_tour.country
        if country_name not in country_city_map:
            country_city_map[country_name] = {
                'photo': country_tour.country_photo.url if country_tour.country_photo else None,
                'cities': []
            }
        country_city_map[country_name]['cities'].extend(country_tour.cities.all())
    
    context = {
        'country_city_map': country_city_map
    }

    return render(request, 'LikTour/properties.html', context)

def all_news(request):
    news_list = News.objects.select_related('news').all()
    context = {
        'news_list': news_list
    }

    return render(request, 'LikTour/all-news.html', context)

def news_detail(request, news_id):
    news_page = get_object_or_404(AboutNewsPage, id=news_id)
    context = {
        'news_page': news_page
    }
    return render(request, 'LikTour/news-detail.html', context)

def about_us(request):
    return render(request, 'LikTour/property-details.html')

def contact_with_us(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact_with_us')
    
    context = {
        'form': form
    }
    return render(request, 'LikTour/contact.html', context)

def our_policy(request):
    return render(request, 'LikTour/policy.html')

def agreement(request):
    return render(request, 'LikTour/agreement.html')