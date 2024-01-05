from django import forms
from django.forms import Form
from .models import Screen
from django.forms import ModelForm
from .models import Users


class Gamer(forms.Form):
    name=forms.CharField(max_length=50)
    number_of_hours=forms.IntegerField(max_value=10,min_value=1,step_size=1)

    if (Screen.active):
        screens=forms.ModelMultipleChoiceField(queryset=Screen.objects.all())


class UserForm(ModelForm):
    class Meta:
        model=Users
        fields=["name","password"]


class SignupForm(ModelForm):
    class Meta:
        model=Users
        fields=["name","email","econtact","password","password_retype"]



