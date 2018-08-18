from django import forms
from django.contrib.auth import get_user_model
# from .models import Compliance
from .utils import get_dataroom_questions
import pandas as pd

User = get_user_model()

class DataRoomForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.sub_area = kwargs.pop('sub_area')
        super(DataRoomForm, self).__init__(*args, **kwargs)
        self.dataroom_db = get_dataroom_questions(self.sub_area)
        self.questions_dict = {}
        for i, question in enumerate(list(self.dataroom_db['Question'])):
            field_name = self.sub_area + '_' + str(i)
            self.fields[field_name] = forms.FileField(required=False,
                                                      widget=forms.ClearableFileInput(attrs={'multiple': True}),
                                                      label=question)
            self.questions_dict[field_name] = question

    def get_model_questions(self):
        return self.questions_dict
