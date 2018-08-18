from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .forms import SMEForm, StaffForm
from .models import SMEProfile, StaffProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from businessplan.utils import try_get_context
from .utils import add_filter_choices, filter_search
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

User = get_user_model()

class SMEProfileDetailView(DetailView):

    def get_object(self):
        slug = self.kwargs.get("slug")
        if slug is None:
            raise Http404
        return get_object_or_404(SMEProfile, slug__iexact=slug)

    def get_context_data(self, *args, **kwargs):
        context = super(SMEProfileDetailView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('query')
        qs = SMEProfile.objects.search(query)
        if qs.exists():
            context['smes'] = qs
        slug = self.kwargs.get("slug")
        if slug:
            user = SMEProfile.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context


class StaffProfileDetailView(DetailView):
    def get_queryset(self):
        return StaffProfile.objects.filter(user=self.request.user)

class SMEProfileCreateView(LoginRequiredMixin, CreateView):
    template_name = 'forms/create_form.html'
    form_class = SMEForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not self.request.user.is_staff:
            obj.user = self.request.user
        obj.save()
        return super(SMEProfileCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(SMEProfileCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create a basic profile"
        full_context = try_get_context(context, self.request.user)
        return full_context

# @login_required
# def smeprofile_create(request):
#     if request.method == 'GET':
#         form = SMEForm()
#         return render(request, 'forms/create_form.html', {'form':form})
#     elif request.method == 'POST':
#         import pdb;pdb.set_trace()
#         form = SMEForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             if not request.user.is_staff:
#                 obj.user = request.user
#             obj.save()
#             return HttpResponseRedirect(obj.get_absolute_url())
#         else:
#             return render(request, 'forms/create_form.html', {'form': form})


class StaffProfileCreateView(LoginRequiredMixin, CreateView):
    template_name = 'forms/create_form.html'
    form_class = StaffForm

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(StaffProfileCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(StaffProfileCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create a basic profile"
        return context

class SMEProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms/update_form.html'
    form_class = SMEForm

    def get_queryset(self):
        return SMEProfile.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(SMEProfileUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Update Profile"
        return context

class StaffProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms/update_form.html'
    form_class = StaffForm

    def get_queryset(self):
        return StaffProfile.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(StaffProfileUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Update Profile"
        return context

class SearchSMEView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/base_search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchSMEView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('query')
        qs = SMEProfile.objects.search(query)
        qs = filter_search(self, qs)
        if qs.exists():
            context['smes'] = qs
        slug = self.kwargs.get("slug")
        if slug:
            user = SMEProfile.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        full_context = add_filter_choices(full_context, user)
        return full_context

class HomePageView(TemplateView):
    template_name = 'base_home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        return context

class HomeActivateView(TemplateView):
    template_name = 'base_home_activate.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeActivateView, self).get_context_data(*args, **kwargs)
        return context