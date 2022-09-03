from django import forms

from .models import CommentModel


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content']
        labels = {
            'content': ''
        }

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 2
            })
        }
