from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Infos
from django.forms import ModelForm

class Info(ModelForm):
    class Meta:
        model = Infos
        fields = ['age','gender','weight','height']