from django import forms
from django.forms import widgets

class GuestbookEntryForm(forms.Form):
    author = forms.CharField(
        max_length=50, required=True, label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя автора'})
    )
    email = forms.EmailField(
        max_length=50, required=True, label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    content = forms.CharField(
        max_length=2000, required=True, label='Текст',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

class SearchForm(forms.Form):
    query = forms.CharField(required=False, label='Поиск по имени')