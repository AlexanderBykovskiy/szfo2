from django import forms
from django.core.exceptions import ValidationError

from .models import *


# Форма обратной связи
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['name', 'phone_number', 'email', 'message']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number != '*':
            raise ValidationError('Номер телефона может содержать только цифры')
        return phone_number

