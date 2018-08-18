'''
All the questions for the DiagnosticsQuestionnaire's model's forms
'''

from django import forms
from django.db import models
import pandas as pd
from django.contrib.staticfiles.templatetags.staticfiles import static
import pickle
from django.conf import settings
import os


class Question:

    def __init__(self, name, area, question, a_1, a_2, a_3, a_4):
        self.name = name
        self.area = area
        self.question = question
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3
        self.a_4 = a_4

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area

    def get_question(self):
        return self.question

    def get_a1(self):
        return self.a_1

    def get_a2(self):
        return self.a_2

    def get_a3(self):
        return self.a_3

    def get_a4(self):
        return self.a_4

    def get_radio_choices(self):
        choices = (
            (1, self.a_1),
            (2, self.a_2),
            (3, self.a_3),
            (4, self.a_4)
        )
        return choices

    def get_model(self):
        return models.IntegerField(choices=self.get_radio_choices(), default=1)

def get_questions_from_db():
    '''

    :return: question dictionary {'sub-area' : questions_list }
    '''
    path_to_db = static('diagnostics_db/Diagnostics_db.csv')
    diagnostics_db = pd.read_csv(path_to_db)
    all_questions = {}
    sub_areas = ['Environmental', 'Social', 'Compliance', 'Finance', 'Legal',
                 'Organisation', 'Staff', 'Competition', 'Marketing', 'Governance',
                 'Management', 'Facilities', 'IT/Technology', 'Processes', 'Procurement']
    for area in sub_areas:
        area_df = diagnostics_db[diagnostics_db['Sub-Area'] == area]
        # Init params
        idx = 0
        questions = []
        for index, row in area_df.iterrows():
            area = area
            if area == 'IT/Technology':
                name = 'ITTechnology' + "_" + str(idx)
            else:
                name = area + "_" + str(idx)
            question = row['Question']
            a_1 = row['Score = 1']
            a_2 = row['Score = 2']
            a_3 = row['Score = 3']
            a_4 = row['Score = 4']
            qs = Question(name, area, question, a_1, a_2, a_3, a_4)
            questions.append(qs)
            idx += 1
        all_questions[area] = questions
    return all_questions

def pickle_questions_db():
    path_to_pickle = static('diagnostics_db/Diagnostics_db.p')
    questions = get_questions_from_db()

    pickle.dump(questions, open(path_to_pickle, 'wb'))

def unpickle_questions_db():
    # path_to_pickle = static('diagnostics_db/Diagnostics_db.p')
    path_to_pickle = os.path.join(settings.STATIC_ROOT, 'diagnostics_db', 'Diagnostics_db.p')
    # path_to_pickle = static('diagnostics_db/Diagnostics_db.p')
    questions = pickle.load(open(path_to_pickle, 'rb'))

    return questions

def get_form_settings(questions):
    fields = []
    labels = {}
    widgets = {}

    for key, values in questions.items():
        for value in values:
            field_name = value.get_name()
            field_label = value.get_question()
            field_widget = forms.RadioSelect()
            fields.append(field_name)
            labels[field_name] = field_label
            widgets[field_name] = field_widget

    return fields, labels, widgets

def get_question_models(questions_dict, sub_area):
    questions = questions_dict[sub_area]
    models = (questions[0].get_model(),)
    for question in questions[1:]:
        model = question.get_model()
        models = models + (model,)
    return models


def get_score_from_diagnostics(diagnostics, area):
    total_score = 0
    if area == 'environmental':
        environmental_list = diagnostics.get_environmental()
        social_list = diagnostics.get_social()
        for score in environmental_list + social_list:
            total_score += score.value_from_object(diagnostics)
    if area == 'finance':
        finance_list = diagnostics.get_finance()
        compliance_list = diagnostics.get_compliance()
        legal_list = diagnostics.get_legal()
        for score in finance_list + compliance_list + legal_list:
            total_score += score.value_from_object(diagnostics)
    if area == 'leadership':
        governance_list = diagnostics.get_governance()
        management_list = diagnostics.get_management()
        for score in governance_list + management_list:
            total_score += score.value_from_object(diagnostics)
    if area == 'operations':
        facilities_list = diagnostics.get_facilities()
        technology_list = diagnostics.get_technology()
        procurement_list = diagnostics.get_procurement()
        processes_list = diagnostics.get_processes()
        for score in facilities_list + technology_list + processes_list + procurement_list:
            total_score += score.value_from_object(diagnostics)
    if area == 'organisation':
        organisation_list = diagnostics.get_organisation()
        staff_list = diagnostics.get_staff()
        for score in organisation_list + staff_list:
            total_score += score.value_from_object(diagnostics)
    if area == 'sales':
        competition_list = diagnostics.get_competition()
        marketing_list = diagnostics.get_marketing()
        for score in competition_list + marketing_list:
            total_score += score.value_from_object(diagnostics)

    return total_score

class Improv:

    def __init__(self, current_percent, previous_percent):
        self.current_percent = current_percent
        self.previous_percent = previous_percent
        self.difference = current_percent - previous_percent

    def get_value(self):
        return abs(self.difference)

    def is_positive(self):
        if self.difference < 0:
            return False
        else:
            return True



