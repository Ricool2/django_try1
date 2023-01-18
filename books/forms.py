from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
    
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "author", "text", "date"]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control'
            })
        }