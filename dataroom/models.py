from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from django.urls import reverse
import os

User = settings.AUTH_USER_MODEL

def get_upload_path(instance, filename):
    return os.path.join(instance.sub_area, filename)

class Accordion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_absolute_url(self):
        return reverse('accordion:detail', kwargs={'slug': self.slug})

    def get_user(self):
        return self.user

class AccordionFileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accordion = models.ForeignKey(Accordion, on_delete=models.CASCADE, default=1)
    label = models.CharField(max_length=1500, default='None')
    file = models.FileField(upload_to=get_upload_path)
    sub_area = models.CharField(max_length=100, default='None')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_user(self):
        return self.user

    def get_file(self):
        return self.file

    def get_label(self):
        return self.label

    def get_sub_area(self):
        return self.sub_area

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Accordion)