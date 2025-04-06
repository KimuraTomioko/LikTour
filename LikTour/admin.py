from django.contrib import admin
from .models import * 

@admin.register(Cities)
class AdminCities(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    list_filter = ('name',)

@admin.register(CountryTour)
class AdminCountryTour(admin.ModelAdmin):
    list_display = ('country', 'get_cities')
    list_display_links = ('country',)
    list_filter = ('country',)
    filter_horizontal = ('cities',)

    def get_cities(self, obj):
        return ', '.join(city.name for city in obj.cities.all())
    get_cities.short_description = 'Города'

@admin.register(ContactForm)
class AdminContactForm(admin.ModelAdmin):
    list_display = ('name', 'telephone_number', 'email', 'message_subject', 'message')
    list_display_links = ('name',)
    list_filter = ('name',)

@admin.register(SmallContactForm)
class AdminSmallContactForm(admin.ModelAdmin):
    list_display = ('name', 'telephone_number', 'country', 'city')
    list_display_links = ('name',)
    list_filter = ('name',)

@admin.register(AboutNewsPage)
class AdminAboutNewsPage(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    list_filter = ('title',)

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'order')
    list_editable = ('order',)
    ordering = ('order',)