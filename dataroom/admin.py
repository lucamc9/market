from django.contrib import admin
from .models import Accordion, AccordionFileModel

admin.site.register(AccordionFileModel)
admin.site.register(Accordion)


