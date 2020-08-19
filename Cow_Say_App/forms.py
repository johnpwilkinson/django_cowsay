from django import forms
from Cow_Say_App.models import Cow_Say_What_Model


class Cow_Say_What(forms.Form):
    message = forms.CharField(max_length=85)

