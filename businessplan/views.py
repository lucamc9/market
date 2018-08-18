from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
from .forms import BusinessPlanForm
from .models import BusinessPlan
from .utils import try_get_context
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse, Http404
from profiles.models import SMEProfile

class BusinessPlanDetailView(DetailView):

    def get_object(self):
        slug = self.kwargs.get("slug")
        if slug is None:
            raise Http404
        return get_object_or_404(BusinessPlan, slug__iexact=slug)

    def get_context_data(self, *args, **kwargs):
        context = super(BusinessPlanDetailView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = BusinessPlan.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

class BusinessPlanCreateView(LoginRequiredMixin, CreateView):
    template_name = 'forms/bp_create_form.html'
    form_class = BusinessPlanForm

    def get_queryset(self):
        return BusinessPlan.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(BusinessPlanCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(BusinessPlanCreateView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = BusinessPlan.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

class BusinessPlanUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms/bp_update_form.html'
    form_class = BusinessPlanForm

    def get_queryset(self):
        return BusinessPlan.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(BusinessPlanUpdateView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = BusinessPlan.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

class InfoView(LoginRequiredMixin, TemplateView):
    template_name = 'info_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(InfoView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = SMEProfile.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404