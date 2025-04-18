from django.db import models
from django.urls import reverse_lazy
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Cities(models.Model):
    name = models.CharField(max_length=30, verbose_name = 'Название города')
    description = models.TextField(max_length=340, verbose_name='Описание города')
    cuisine = models.TextField(max_length=340, verbose_name='Кухня')
    photo_cuisine = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография кухни страны/города')
    what_to_see = models.TextField(max_length=340, verbose_name='Что посмотреть')
    photo_what_to_see = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография достопремичательностей страны/города')
    when_is_the_season = models.TextField(max_length=340, verbose_name='Когда сезон?')
    photo_when_is_the_season = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Фото сезона страны/города')
    city_photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография города')
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class CountryTour(models.Model):
    country = models.CharField(max_length=30, verbose_name='Название страны')
    country_photo = models.ImageField(upload_to='image/%Y/%m/%d', blank=True, null=True, verbose_name='Картинка страны')
    cities = models.ManyToManyField(Cities, blank=True, verbose_name='Названия городов')  # Убрано null=True

    def __str__(self):
        return f"{self.country} -- {', '.join(city.name for city in self.cities.all())}"
    
    class Meta:
        verbose_name = 'Страна и её города'
        verbose_name_plural = 'Страны и их города'
    
class ContactForm(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Имя')
    telephone_number = PhoneNumberField(region='RU', verbose_name='Номер телефона')
    email = models.EmailField(max_length=50, blank=False, null=False, verbose_name='Электронная почта')
    message_subject = models.CharField(max_length=50, blank=False, null=False, verbose_name='Тема сообщения')
    message = models.TextField(max_length=1200, null=False, blank=False, verbose_name='Сообщение')

    def __str__(self):
        return f"{self.name} -- {self.message}"
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class SmallContactForm(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Имя')
    telephone_number = PhoneNumberField(region='RU', verbose_name='Номер телефона')
    country = models.ForeignKey(CountryTour, on_delete=models.CASCADE, verbose_name='Страна')
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, verbose_name='Город')

    def __str__(self):
        return f"{self.name} -- {self.telephone_number}"
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class AboutNewsPage(models.Model):
    title = models.CharField(max_length=45, verbose_name='Заголовок новости в отдельной странице')
    first_title = models.CharField(max_length=45, blank=True, default='', verbose_name='Заголовок первого блока')
    first_info = models.TextField(max_length=340, verbose_name='Первый блок с новостью')
    first_info_phoro = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография для 1 блока с новостью на странице')
    second_title = models.CharField(max_length=45, blank=True, default='', verbose_name='Заголовок второго блока')
    second_info = models.TextField(max_length=340, verbose_name='Второй блок с новостью')
    second_info_photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография для 2 блока с новостью на странице')
    third_title = models.CharField(max_length=45, blank=True, default='', verbose_name='Заголовок третьего блока')
    third_info = models.TextField(max_length=340, verbose_name='Третий блок с новостью')
    third_info_photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография для 3 блока с новостью на странице')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость отдельно'
        verbose_name_plural = 'Новости отдельно'

class News(models.Model):
    title = models.CharField(max_length=45, verbose_name='Заголовок новости')
    description = models.TextField(max_length=145, verbose_name='Описание новости')
    news = models.ForeignKey(AboutNewsPage, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Новость')
    is_pinned = models.BooleanField(default=False, verbose_name='Закрепить новость')  # Новое поле

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = 'Новость блоком'
        verbose_name_plural = 'Новости блоком'

    # Ограничение: не более 3 закреплённых новостей
    def save(self, *args, **kwargs):
        if self.is_pinned:
            pinned_count = News.objects.filter(is_pinned=True).exclude(id=self.id).count()
            if pinned_count >= 3:
                raise ValueError("Нельзя закрепить больше 3 новостей.")
        super().save(*args, **kwargs)

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок баннера')
    subtitle = models.CharField(max_length=100, verbose_name='Подзаголовок баннера', blank=True)
    image = models.ImageField(upload_to='banners/%Y/%m/%d', verbose_name='Изображение баннера')
    link = models.URLField(max_length=200, blank=True, verbose_name='Ссылка на подробности')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['order']



