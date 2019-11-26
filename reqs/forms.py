from django import forms
from .models import RequestForsto


class RequestForstoForm(forms.ModelForm):
    class Meta:
        model = RequestForsto
        fields = ['phone',
                  'client_name',
                  'car_model',
                  'vin',
                  'description',
                  ]
        labels = {'phone':       'Телефон клиента',
                  'client_name': 'Имя клиента',
                  'car_model':   'Модель автомобиля',
                  'vin':         'VIN автомобиля',
                  'description': 'Содержание заказа',
                  }
        widgets = {'description': forms.Textarea(attrs={'cols': 40}),
                   'car_model': forms.TextInput(attrs={'size': 40}),
                   'vin': forms.TextInput(attrs={'size': 20}),
                   'client_name': forms.TextInput(attrs={'size': 40}),
                   'phone': forms.TextInput(attrs={'size': 10}),
                   }