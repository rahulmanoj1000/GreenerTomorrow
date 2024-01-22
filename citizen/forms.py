from django import forms
from .models import CitizenInput

class CitizenForm(forms.ModelForm):
    class Meta:
        model = CitizenInput
        fields = ['name','image','address','email']