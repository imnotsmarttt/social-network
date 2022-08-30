from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        labels = {'content': ''}

        widgets = {
            'content': forms.TextInput(attrs={
                'class': '', 'placeholder': 'Сообщение', 'id': ''
            })
        }
