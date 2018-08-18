from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from profiles.utils import unique_slug_generator
from django.conf import settings
from .utils import get_diligence_form


User = settings.AUTH_USER_MODEL

# Horrible way to do it, must delve deep into dynamic model field assignment [TEMPORARY]
class DiligenceRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_0 = models.CharField(max_length=1500, blank=True, null=True)
    question_1 = models.CharField(max_length=1500, blank=True, null=True)
    question_2 = models.CharField(max_length=1500, blank=True, null=True)
    question_3 = models.CharField(max_length=1500, blank=True, null=True)
    question_4 = models.CharField(max_length=1500, blank=True, null=True)
    question_5 = models.CharField(max_length=1500, blank=True, null=True)
    question_6 = models.CharField(max_length=1500, blank=True, null=True)
    question_7 = models.CharField(max_length=1500, blank=True, null=True)
    question_8 = models.CharField(max_length=1500, blank=True, null=True)
    question_9 = models.CharField(max_length=1500, blank=True, null=True)
    question_10 = models.CharField(max_length=1500, blank=True, null=True)
    question_11 = models.CharField(max_length=1500, blank=True, null=True)
    question_12 = models.CharField(max_length=1500, blank=True, null=True)
    question_13 = models.CharField(max_length=1500, blank=True, null=True)
    question_14 = models.CharField(max_length=1500, blank=True, null=True)
    question_15 = models.CharField(max_length=1500, blank=True, null=True)
    question_16 = models.CharField(max_length=1500, blank=True, null=True)
    question_17 = models.CharField(max_length=1500, blank=True, null=True)
    question_18 = models.CharField(max_length=1500, blank=True, null=True)
    question_19 = models.CharField(max_length=1500, blank=True, null=True)
    question_20 = models.CharField(max_length=1500, blank=True, null=True)
    question_21 = models.CharField(max_length=1500, blank=True, null=True)
    question_22 = models.CharField(max_length=1500, blank=True, null=True)
    question_23 = models.CharField(max_length=1500, blank=True, null=True)
    question_24 = models.CharField(max_length=1500, blank=True, null=True)
    question_25 = models.CharField(max_length=1500, blank=True, null=True)
    question_26 = models.CharField(max_length=1500, blank=True, null=True)
    question_27 = models.CharField(max_length=1500, blank=True, null=True)
    question_28 = models.CharField(max_length=1500, blank=True, null=True)
    question_29 = models.CharField(max_length=1500, blank=True, null=True)
    question_30 = models.CharField(max_length=1500, blank=True, null=True)
    question_31 = models.CharField(max_length=1500, blank=True, null=True)
    question_32 = models.CharField(max_length=1500, blank=True, null=True)
    question_33 = models.CharField(max_length=1500, blank=True, null=True)
    question_34 = models.CharField(max_length=1500, blank=True, null=True)
    question_35 = models.CharField(max_length=1500, blank=True, null=True)
    question_36 = models.CharField(max_length=1500, blank=True, null=True)
    question_37 = models.CharField(max_length=1500, blank=True, null=True)
    question_38 = models.CharField(max_length=1500, blank=True, null=True)
    question_39 = models.CharField(max_length=1500, blank=True, null=True)
    question_40 = models.CharField(max_length=1500, blank=True, null=True)
    question_41 = models.CharField(max_length=1500, blank=True, null=True)
    question_42 = models.CharField(max_length=1500, blank=True, null=True)
    question_43 = models.CharField(max_length=1500, blank=True, null=True)
    question_44 = models.CharField(max_length=1500, blank=True, null=True)
    question_45 = models.CharField(max_length=1500, blank=True, null=True)
    question_46 = models.CharField(max_length=1500, blank=True, null=True)
    question_47 = models.CharField(max_length=1500, blank=True, null=True)
    question_48 = models.CharField(max_length=1500, blank=True, null=True)
    question_49 = models.CharField(max_length=1500, blank=True, null=True)
    question_50 = models.CharField(max_length=1500, blank=True, null=True)
    question_51 = models.CharField(max_length=1500, blank=True, null=True)
    question_52 = models.CharField(max_length=1500, blank=True, null=True)
    question_53 = models.CharField(max_length=1500, blank=True, null=True)
    question_54 = models.CharField(max_length=1500, blank=True, null=True)
    question_55 = models.CharField(max_length=1500, blank=True, null=True)
    question_56 = models.CharField(max_length=1500, blank=True, null=True)
    question_57 = models.CharField(max_length=1500, blank=True, null=True)
    question_58 = models.CharField(max_length=1500, blank=True, null=True)
    question_59 = models.CharField(max_length=1500, blank=True, null=True)
    question_60 = models.CharField(max_length=1500, blank=True, null=True)
    question_61 = models.CharField(max_length=1500, blank=True, null=True)
    question_62 = models.CharField(max_length=1500, blank=True, null=True)
    question_63 = models.CharField(max_length=1500, blank=True, null=True)
    question_64 = models.CharField(max_length=1500, blank=True, null=True)
    question_65 = models.CharField(max_length=1500, blank=True, null=True)
    question_66 = models.CharField(max_length=1500, blank=True, null=True)
    question_67 = models.CharField(max_length=1500, blank=True, null=True)
    question_68 = models.CharField(max_length=1500, blank=True, null=True)
    question_69 = models.CharField(max_length=1500, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('diligence:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user.__str__()

    def get_user(self):
        return self.user

    def get_all_questions(self):
        return [self.question_0, self.question_1, self.question_2, self.question_3,
                self.question_4, self.question_5, self.question_6, self.question_7,
                self.question_8, self.question_9, self.question_10, self.question_11,
                self.question_12, self.question_13, self.question_14, self.question_15,
                self.question_16, self.question_17, self.question_18, self.question_19,
                self.question_20, self.question_21, self.question_22, self.question_23,
                self.question_24, self.question_25, self.question_26, self.question_27,
                self.question_28, self.question_29, self.question_30, self.question_31,
                self.question_32, self.question_33, self.question_34, self.question_35,
                self.question_36, self.question_37, self.question_38, self.question_39,
                self.question_40, self.question_41, self.question_42, self.question_43,
                self.question_44, self.question_45, self.question_46, self.question_47,
                self.question_48, self.question_49, self.question_50, self.question_51,
                self.question_52, self.question_53, self.question_54, self.question_55,
                self.question_56, self.question_57, self.question_58, self.question_59,
                self.question_60, self.question_61, self.question_62, self.question_63,
                self.question_64, self.question_65, self.question_66, self.question_67,
                self.question_68, self.question_69]

    def get_detail_questions(self):
        fields, labels = get_diligence_form()
        all_questions = self.get_all_questions()
        detail_format = []
        idx = 0
        for field in fields:
            label = labels[field]
            detail_format.append((all_questions[idx], label))
            idx += 1
        return detail_format


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=DiligenceRoom)