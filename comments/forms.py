from django import forms

from .models import CommentModel


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content']