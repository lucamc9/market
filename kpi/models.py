from django.db import models
from django.conf import settings
from profiles.utils import sme_choices
import datetime
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from .utils import is_year, get_period_verbose
import os

User = settings.AUTH_USER_MODEL

def get_upload_path(instance, filename):
    if is_year(filename):
        return os.path.join('Yearly', filename)
    else:
        return os.path.join('Monthly', filename)

class ExcelTemplate(models.Model):
    PERIODS = (('y', 'Year'), ('m', 'Month'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.FileField(blank=True, null=True, upload_to=get_upload_path)
    period = models.CharField(max_length=10, choices=PERIODS, default='y')
    period_verbose = models.CharField(max_length=20, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('kpi:demo')

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_user(self):
        return self.user

    def get_template(self):
        return self.template

    def get_period(self):
        return self.period

    def get_period_verbose(self):
        return self.period_verbose


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if is_year(instance.template.name):
        instance.period = 'y'
    else:
        instance.period = 'm'
    if not instance.period_verbose:
        instance.period_verbose = get_period_verbose(instance)

pre_save.connect(pre_save_receiver, sender=ExcelTemplate)
