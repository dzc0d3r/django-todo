from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'add new Todo'}))
    complete = forms.CharField(widget=forms.CheckboxInput(
        attrs={'class': 'checky'}))

    class Meta:
        model = Task
        fields = '__all__'
