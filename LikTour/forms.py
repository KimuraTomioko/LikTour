from django import forms
from .models import ContactForm, SmallContactForm
from phonenumber_field.formfields import PhoneNumberField as FormPhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget

class QuestionForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = (
            'name',
            'telephone_number',
            'email',
            'message_subject',
            'message'
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ваше имя...'}),
            'telephone_number': RegionalPhoneNumberWidget(attrs={'class': 'form-control', 'placeholder':'Ваш номер телефона...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Ваш email...'}),
            'message_subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Тема сообщения...'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Ваше сообщение...'}),
        }

class SmallContactForm(forms.ModelForm):
    class Meta:
        model = SmallContactForm
        fields = (
            'name', 
            'email'
            )
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ваша электронная почта'})
        }