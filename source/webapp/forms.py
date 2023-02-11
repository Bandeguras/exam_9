from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Ad, Comment


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['photo', 'title', 'description', 'category', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'content': {
                'required': 'Поле должно быть заполнено'
            }
        }


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти', widget=widgets.TextInput(attrs={'class': "form-control w-25"}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']