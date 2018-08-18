import pandas as pd
import os
from django.conf import settings
from .models import AccordionFileModel

dataroom_db = pd.read_csv(os.path.join(settings.STATIC_ROOT, 'dataroom_db', 'Dataroom_db.csv'))

def get_dataroom_areas():
    return [str(x) for x in dataroom_db['Area'].unique()]

def get_dataroom_sub_areas(area):
    return [str(x) for x in dataroom_db[dataroom_db['Area'] == area]['Sub-Area'].unique()]

def get_dataroom_questions(area):

    if area == 'Technology':
        area = 'IT/Technology'
    elif area == 'Company':
        area = 'General Company Info'

    return dataroom_db[dataroom_db['Sub-Area'] == area]

class AccordionQuestion:

    def __init__(self, question, user, collapse):
        self.question = question
        self.user = user
        self.collapse = collapse

    def get_question(self):
        return self.question

    def get_files(self):
        models = AccordionFileModel.objects.filter(label=self.question)
        files = []
        for model in models:
            files.append(model.get_file())
        return files

    def get_collapse(self):
        return self.collapse

class AccordionSubArea:

    def __init__(self, sub_area, user, collapse):
        self.sub_area = sub_area
        self.user = user
        self.collapse = collapse

    def clean_area(self, area):
        if area == 'IT/Technology':
            area = 'Technology'
        elif area == 'General Company Info':
            area = 'Company'
        return area

    def get_sub_area(self):
        return self.sub_area

    def get_questions(self):
        accordion_questions = []
        questions = AccordionFileModel.objects.filter(user=self.user, sub_area=self.clean_area(self.sub_area))
        question_collapse = self.collapse + 1
        prev_label = None
        for question in questions:
            label = question.get_label()
            if label != prev_label:
                accordion_question = AccordionQuestion(label, self.user, question_collapse)
                accordion_questions.append(accordion_question)
                question_collapse += 1
            prev_label = label
        return accordion_questions

    def get_collapse(self):
        return self.collapse

    def get_last_collapse(self):
        return self.collapse + len(self.get_questions())

    def has_questions(self):
        has_questions = False
        if self.get_questions():
            has_questions = True
        return has_questions

class AccordionArea:

    def __init__(self, area, user, collapse):
        self.area = area
        self.user = user
        self.collapse = collapse

    def get_area(self):
        return self.area

    def get_sub_areas(self):
        accordion_subs = []
        sub_area_collapse = self.collapse + 1
        for sub_area in get_dataroom_sub_areas(self.area):
            accordion_sub = AccordionSubArea(sub_area, self.user, sub_area_collapse)
            accordion_subs.append(accordion_sub)
            sub_area_collapse = accordion_sub.get_last_collapse() + 1
        return accordion_subs

    def get_collapse(self):
        return self.collapse

    def get_last_collapse(self):
        sub_areas = self.get_sub_areas()
        return sub_areas[-1].get_last_collapse()

    def has_questions(self):
        has_questions = False
        for sub_area in self.get_sub_areas():
            if sub_area.has_questions():
                has_questions = True
        return has_questions


def add_accordion_context(context, request_user):
    area_names = get_dataroom_areas()
    accordions = []
    collapse = 1
    for area in area_names:
        accordion = AccordionArea(area, request_user, collapse)
        accordions.append(accordion)
        collapse = int(accordion.get_last_collapse()) + 1

    context['accordions'] = accordions
    return context
