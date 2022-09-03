from django import forms

from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        labels = {
            'title': 'Заголовок',
            'body': 'Текст',
            'image': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 12
            }),
        }