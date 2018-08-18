from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from django.urls import reverse
from .utils import unpickle_questions_db, get_question_models, get_questions_from_db, get_score_from_diagnostics, Improv
from django.utils.text import slugify


User = settings.AUTH_USER_MODEL

class Diagnostics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    environmental = models.IntegerField(null=True, blank=True)
    leadership = models.IntegerField(null=True, blank=True)
    finance = models.IntegerField(null=True, blank=True)
    operations = models.IntegerField(null=True, blank=True)
    organisation = models.IntegerField(null=True, blank=True)
    sales = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('diagnostics:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

    # Organisation
    def get_organisation(self):
        return self.organisation

    def get_organisation_total(self):
        return 120

    def get_organisation_percent(self):
        return int(self.organisation * 100 / self.get_organisation_total())

    # Operations
    def get_operations(self):
        return self.operations

    def get_operations_total(self):
        return 96

    def get_operations_percent(self):
        return int(self.operations * 100 / self.get_operations_total())

    # Finance
    def get_finance(self):
        return self.finance

    def get_finance_total(self):
        return 108

    def get_finance_percent(self):
        return int(self.finance * 100 / self.get_finance_total())

    # Sales
    def get_sales(self):
        return self.sales

    def get_sales_total(self):
        return 44

    def get_sales_percent(self):
        return int(self.sales * 100 / self.get_sales_total())

    # Environmental
    def get_environmental(self):
        return self.environmental

    def get_environmental_total(self):
        return 16

    def get_environmental_percent(self):
        return int(self.environmental * 100 / self.get_environmental_total())

    # Leadership
    def get_leadership(self):
        return self.leadership

    def get_leadership_total(self):
        return 76

    def get_leadership_percent(self):
        return int(self.leadership * 100 / self.get_leadership_total())

    # Total
    def get_total(self):
        return self.total

    def get_real_total(self):
        return self.get_organisation_total() + self.get_environmental_total() + self.get_finance_total() \
               + self.get_leadership_total() + self.get_operations_total() + self.get_sales_total()

    def get_total_percent(self):
        return int(self.total * 100 / self.get_real_total())

    def get_all_percents(self):
        return [self.get_environmental_percent(), self.get_leadership_percent(), self.get_finance_percent(),
                self.get_operations_percent(), self.get_organisation_percent(), self.get_sales_percent(),
                self.get_total_percent()]

    def there_is_improvement(self):
        if len(Diagnostics.objects.filter(user=self.user)) > 1:
            return True
        else:
            return False

    def get_improvements_previous(self):
        previous_diag = Diagnostics.objects.filter(user=self.user)[1]
        improv_environment = Improv(self.get_environmental_percent(), previous_diag.get_environmental_percent())
        improv_finance = Improv(self.get_finance_percent(), previous_diag.get_finance_percent())
        improv_leadership = Improv(self.get_leadership_percent(), previous_diag.get_leadership_percent())
        improv_operations = Improv(self.get_operations_percent(), previous_diag.get_operations_percent())
        improv_organisation = Improv(self.get_organisation_percent(), previous_diag.get_organisation_percent())
        improv_sales = Improv(self.get_sales_percent(), previous_diag.get_sales_percent())
        improv_total = Improv(self.get_total_percent(), previous_diag.get_total_percent())

        return [improv_environment, improv_finance, improv_leadership,
                improv_operations, improv_organisation, improv_sales, improv_total]


    def get_improvements_first(self):
        previous_diag = Diagnostics.objects.filter(user=self.user).last()

        improv_environment = Improv(self.get_environmental_percent(), previous_diag.get_environmental_percent())
        improv_finance = Improv(self.get_finance_percent(), previous_diag.get_finance_percent())
        improv_leadership = Improv(self.get_leadership_percent(), previous_diag.get_leadership_percent())
        improv_operations = Improv(self.get_operations_percent(), previous_diag.get_operations_percent())
        improv_organisation = Improv(self.get_organisation_percent(), previous_diag.get_organisation_percent())
        improv_sales = Improv(self.get_sales_percent(), previous_diag.get_sales_percent())
        improv_total = Improv(self.get_total_percent(), previous_diag.get_total_percent())

        return [improv_environment, improv_finance, improv_leadership,
                improv_operations, improv_organisation, improv_sales, improv_total]


class DiagnosticsQuestionnaire(models.Model):
    # Retrieve questions
    questions = unpickle_questions_db()
    # Standard models
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Environmental
    Environmental_0, Environmental_1 = get_question_models(questions, 'Environmental')
    environmental_list = [Environmental_0, Environmental_1]
    # Social
    Social_0, Social_1 = get_question_models(questions, 'Social')
    social_list = [Social_0, Social_1]
    # Competition
    Competition_0, Competition_1, Competition_2 = get_question_models(questions, 'Competition')
    competition_list = [Competition_0, Competition_1, Competition_2]
    # Procurement
    Procurement_0, Procurement_1, Procurement_2, Procurement_3 = get_question_models(questions, 'Procurement')
    procurement_list = [Procurement_0, Procurement_1, Procurement_2, Procurement_3]
    # Compliance
    Compliance_0, Compliance_1, Compliance_2, Compliance_3 = get_question_models(questions, 'Compliance')
    compliance_list = [Compliance_0, Compliance_1, Compliance_2, Compliance_3]
    # Legal
    Legal_0, Legal_1, Legal_2, Legal_3 = get_question_models(questions, 'Legal')
    legal_list = [Legal_0, Legal_1, Legal_2, Legal_3]
    # Facilities
    Facilities_0, Facilities_1, Facilities_2, Facilities_3, Facilities_4 = get_question_models(questions, 'Facilities')
    facilities_list = [Facilities_0, Facilities_1, Facilities_2, Facilities_3, Facilities_4]
    # Processes
    Processes_0, Processes_1, Processes_2, Processes_3, Processes_4, \
    Processes_5, Processes_6 = get_question_models(questions, 'Processes')
    processes_list = [Processes_0, Processes_1, Processes_2, Processes_3, Processes_4, Processes_5, Processes_6]
    # Governance
    Governance_0, Governance_1, Governance_2, Governance_3, Governance_4, \
    Governance_5, Governance_6 = get_question_models(questions, 'Governance')
    governance_list = [Governance_0, Governance_1, Governance_2,
                       Governance_3, Governance_4, Governance_5, Governance_6]
    # IT Technologies
    ITTechnology_0, ITTechnology_1, ITTechnology_2, ITTechnology_3, \
    ITTechnology_4, ITTechnology_5, ITTechnology_6, \
    ITTechnology_7 = get_question_models(questions, 'IT/Technology')
    technology_list = [ITTechnology_0, ITTechnology_1, ITTechnology_2, ITTechnology_3,
                       ITTechnology_4, ITTechnology_5, ITTechnology_6, ITTechnology_7]
    # Marketing
    Marketing_0, Marketing_1, Marketing_2, Marketing_3, Marketing_4, Marketing_5, \
    Marketing_6, Marketing_7 = get_question_models(questions, 'Marketing')
    marketing_list = [Marketing_0, Marketing_1, Marketing_2, Marketing_3,
                      Marketing_4, Marketing_5, Marketing_6, Marketing_7]
    # Management
    Management_0, Management_1, Management_2, Management_3, Management_4, Management_5, \
    Management_6, Management_7, Management_8, Management_9, Management_10, \
    Management_11 = get_question_models(questions, 'Management')
    management_list = [Management_0, Management_1, Management_2, Management_3, Management_4, Management_5,
                       Management_6, Management_7, Management_8, Management_9, Management_10, Management_11]
    # Organisation
    Organisation_0, Organisation_1, Organisation_2, Organisation_3, Organisation_4, \
    Organisation_5, Organisation_6, Organisation_7, Organisation_8, Organisation_9, \
    Organisation_10, Organisation_11, Organisation_12, Organisation_13, \
    Organisation_14 = get_question_models(questions, 'Organisation')
    organisation_list = [Organisation_0, Organisation_1, Organisation_2, Organisation_3, Organisation_4,
                         Organisation_5, Organisation_6, Organisation_7, Organisation_8, Organisation_9,
                         Organisation_10, Organisation_11, Organisation_12, Organisation_13, Organisation_14]
    # Staff
    Staff_0, Staff_1, Staff_2, Staff_3, Staff_4, Staff_5, Staff_6, Staff_7, Staff_8, Staff_9, \
    Staff_10, Staff_11, Staff_12, Staff_13, Staff_14 = get_question_models(questions, 'Staff')
    staff_list = [Staff_0, Staff_1, Staff_2, Staff_3, Staff_4, Staff_5, Staff_6, Staff_7,
                  Staff_8, Staff_9, Staff_10, Staff_11, Staff_12, Staff_13, Staff_14]
    # Finance
    Finance_0, Finance_1, Finance_2, Finance_3, Finance_4, \
    Finance_5, Finance_6, Finance_7, Finance_8, Finance_9, \
    Finance_10, Finance_11, Finance_12, Finance_13, \
    Finance_14, Finance_15, Finance_16, Finance_17, Finance_18 = get_question_models(questions, 'Finance')
    finance_list = [Finance_0, Finance_1, Finance_2, Finance_3, Finance_4, Finance_5,
                    Finance_6, Finance_7, Finance_8, Finance_9, Finance_10, Finance_11,
                    Finance_12, Finance_13, Finance_14, Finance_15, Finance_16, Finance_17, Finance_18]

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_absolute_url(self):
        return reverse('diagnostics:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

    def get_organisation(self):
        return self.organisation_list

    def get_management(self):
        return self.management_list

    def get_environmental(self):
        return self.environmental_list

    def get_social(self):
        return self.social_list

    def get_legal(self):
        return self.legal_list

    def get_processes(self):
        return self.processes_list

    def get_finance(self):
        return self.finance_list

    def get_staff(self):
        return self.staff_list

    def get_marketing(self):
        return self.marketing_list

    def get_technology(self):
        return self.technology_list

    def get_facilities(self):
        return self.facilities_list

    def get_competition(self):
        return self.competition_list

    def get_procurement(self):
        return self.procurement_list

    def get_governance(self):
        return self.governance_list

    def get_compliance(self):
        return self.compliance_list


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def calculate_scores(sender, instance, *args, **kwargs):
    # Function to calculate Diagnostics scores from the questionnaire
    user = instance.get_user()

    # Get scores for each section
    environmental = get_score_from_diagnostics(instance, 'environmental')
    leadership = get_score_from_diagnostics(instance, 'leadership')
    finance = get_score_from_diagnostics(instance, 'finance')
    operations = get_score_from_diagnostics(instance, 'operations')
    organisation = get_score_from_diagnostics(instance, 'organisation')
    sales = get_score_from_diagnostics(instance, 'sales')
    total = environmental + leadership + finance + operations + organisation + sales
    # Create and save model
    diagnostics = Diagnostics(user=user, slug=instance.slug, environmental=environmental,
                              leadership=leadership, finance=finance, operations=operations,
                              organisation=organisation, sales=sales, total=total)

    diagnostics.save()

pre_save.connect(pre_save_receiver, sender=DiagnosticsQuestionnaire)
post_save.connect(calculate_scores, sender=DiagnosticsQuestionnaire)



