from django import forms
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