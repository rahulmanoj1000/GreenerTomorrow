from django import forms
from .models import WorkMan

class WorkManRegisterForm(forms.ModelForm):
    class Meta:
        model = WorkMan
        fields = ['name','password']
        
class WorkManLogin(forms.ModelForm):
    class Meta:
        model = WorkMan
        fields = ['name','password']