from django import forms
from .models import MadlibFields


class MadlibForm(forms.ModelForm):
    class Meta(object):
        model = MadlibFields
        fields = ['adjective', 'verb', 'adjective2', 'adverb', 'place', 'name', 'animal']

        widgets = {
            'adjective': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'verb': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'verb that ends with ing'
                }
            ), 'adjective2': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'adverb': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'place': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ), 'animal': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }
