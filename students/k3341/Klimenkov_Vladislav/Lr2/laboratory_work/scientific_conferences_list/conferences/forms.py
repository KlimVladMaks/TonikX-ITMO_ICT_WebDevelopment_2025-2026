from django import forms
from .models import Presentation


class RegisterPresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ['topic', 'description']
