import pandas as pd
import os
from django.conf import settings


excel = pd.ExcelFile(os.path.join(settings.STATIC_ROOT, 'master_db', 'Diagnostic Data Room Merged.xlsx'))
database_qs = excel.parse(excel.sheet_names[1])

def get_diligence():
    diligence = database_qs[database_qs.Where == 'Due Diligence']
    diligence = diligence[['Where', 'Area', 'Sub-Area', 'Question']]
    return diligence

def get_diligence_form():
    fields = []
    labels = {}

    diligence_db = get_diligence()
    idx = 0
    for question in list(diligence_db['Question']):
        question_name = 'question_' + str(idx)
        fields.append(question_name)
        labels[question_name] = question
        idx += 1

    return fields, labels

