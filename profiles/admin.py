from django.contrib import admin
from .models import SMEProfile, InvestorProfile, StaffProfile

admin.site.register(SMEProfile)
admin.site.register(StaffProfile)
admin.site.register(InvestorProfile)
