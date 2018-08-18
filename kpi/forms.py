from django import forms
from django.contrib.auth import get_user_model
from .models import ExcelTemplate

User = get_user_model()

class ExcelTemplateForm(forms.ModelForm):
    class Meta:
        model = ExcelTemplate
        fields = ['template']
