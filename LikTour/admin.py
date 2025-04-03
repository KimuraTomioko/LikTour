from django.contrib import admin
from .models import * 

@admin.register(Cities)
class AdminCities(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    list_filter = ('name',)

@admin.register(CountryTour)
class AdminCountryTour(admin.ModelAdmin):
    list_display = ('country', 'city')
    list_display_links = ('country',)
    list_filter = ('country',)

@admin.register(ContactForm)
class AdminContactForm(admin.ModelAdmin):
    list_display = ('name', 'telephone_number', 'email', 'message_subject', 'message')
    list_display_links = ('name',)
    list_filter = ('name',)

@admin.register(SmallContactForm)
class AdminSmallContactForm(admin.ModelAdmin):
    list_display = ('name', 'telephone_number')
    list_display_links = ('name',)
    list_filter = ('name',)


    