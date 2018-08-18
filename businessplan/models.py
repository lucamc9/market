from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from django.urls import reverse
import os

User = settings.AUTH_USER_MODEL

def get_upload_path_bp(instance, filename):
    return os.path.join('BPlans', filename)

class BusinessPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.TextField(max_length=1500, blank=True, null=True)
    qualifications = models.CharField(max_length=1500, blank=True, null=True)
    exit = models.CharField(max_length=1500, blank=True, null=True)
    summary = models.CharField(max_length=1500, blank=True, null=True)
    competitors = models.CharField(max_length=1500, blank=True, null=True)
    customers = models.CharField(max_length=1500, blank=True, null=True)
    market = models.CharField(max_length=1500, blank=True, null=True)
    problem = models.CharField(max_length=1500, blank=True, null=True)
    solution = models.CharField(max_length=1500, blank=True, null=True)
    strategy = models.CharField(max_length=1500, blank=True, null=True)
    advantages = models.CharField(max_length=1500, blank=True, null=True)
    plan = models.FileField(blank=True, null=True, upload_to=get_upload_path_bp)
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('businessplan:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

    def get_model(self):
        return self.model

    def get_qualifications(self):
        return self.qualifications

    def get_exit(self):
        return self.exit

    def get_summary(self):
        return self.summary

    def get_competitors(self):
        return self.competitors

    def get_customers(self):
        return self.customers

    def get_market(self):
        return self.market

    def get_problem(self):
        return self.problem

    def get_solution(self):
        return self.solution

    def get_strategy(self):
        return self.strategy

    def get_advantages(self):
        return self.advantages

    def get_plan(self):
        return self.plan

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=BusinessPlan)
