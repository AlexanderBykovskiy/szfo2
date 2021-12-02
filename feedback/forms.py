from django import forms
from django.core.exceptions import ValidationError
import re

from .models import *


# Форма обратной связи
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['name', 'phone_number', 'email', 'message', 'accept_processing']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3})
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        reg_tpl = '^[\+]?[0-9]*$'
        if not re.match(reg_tpl, phone_number):
            raise ValidationError('Номер телефона может содержать только цифры и знак "+"')
        return phone_number

    def clean_accept_processing(self):
        accept_processing = self.cleaned_data['accept_processing']
        if not accept_processing:
            raise ValidationError('Без Вашего разрешения мы не можем принять персональные данные')
        return accept_processing
