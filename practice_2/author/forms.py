from django import forms
from .models import Author
from django.forms.widgets import NumberInput

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))