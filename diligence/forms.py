from django import forms
from .models import DiligenceRoom
from .utils import get_diligence_form

class DiligenceRoomForm(forms.ModelForm):
    class Meta:
        model = DiligenceRoom
        fields, labels = get_diligence_form()
