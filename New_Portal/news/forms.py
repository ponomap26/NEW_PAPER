from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    title = forms.CharField(min_length=15)

    class Meta:
        model = Post
        fields = ['categoryType', 'author', 'category', 'title', 'text']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("description")
        if title is not None and len(title) > 15:
            raise ValidationError({
                "Название ": "Название не может быть больше 20 символов."
            })

        return cleaned_data


class NewsDelete(forms.ModelForm):

    class Meta:
        model = Post
        fields = []


class NewsEdit(forms.ModelForm):
    title = forms.CharField(min_length=15)

    class Meta:
        model = Post
        fields = ['categoryType',  'category', 'title', 'text']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("description")
        if title is not None and len(title) > 15:
            raise ValidationError({
                "Название ": "Название не может быть больше 15 символов."
            })

        return cleaned_data
