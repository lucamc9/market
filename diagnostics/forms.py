from django import forms
from .models import DiagnosticsQuestionnaire
from .utils import get_form_settings, unpickle_questions_db, get_questions_from_db
from django.contrib.staticfiles.templatetags.staticfiles import static


questions = unpickle_questions_db()

class DiagnosticsForm(forms.ModelForm):
    class Meta:
        model = DiagnosticsQuestionnaire
        fields, labels, widgets = get_form_settings(questions)