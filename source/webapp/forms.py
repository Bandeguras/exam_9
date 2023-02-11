from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Ad


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


class AdDeleteForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data['title']
        if self.instance.title != title:
            raise ValidationError('Названия не совпадают')
        return title