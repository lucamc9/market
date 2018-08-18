from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .utils import code_generator
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False,
                    is_investor=False, is_sme=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.investor = is_investor
        user_obj.sme = is_sme
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=False)  # can login
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    staff = models.BooleanField(default=False) # staff non-superuser
    admin = models.BooleanField(default=False) # superuser
    investor = models.BooleanField(default=False) # for investors
    sme = models.BooleanField(default=False) # for smes
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def send_activation_email(self):
        if not self.active:
            self.activation_key = code_generator()  # 'somekey' #gen key
            self.save()
            # path_ = reverse()
            path_ = reverse('activate', kwargs={"code": self.activation_key})
            full_path = "https://challengesmarketplace.co.uk" + path_
            subject = 'Activate your Marketplace account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'Activate your account here: %s' % full_path
            recipient_list = [self.email]
            html_message = '<p>Activate your account here: %s </p>' % full_path
            print(html_message)
            sent_mail = send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
                html_message=html_message)
            # sent_mail = False
            return sent_mail

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_investor(self):
        return self.investor

    @property
    def is_sme(self):
        return self.sme

    def get_key(self):
        return self.activation_key



