from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import DiligenceRoomForm
from .models import DiligenceRoom
from businessplan.utils import try_get_context
from django.http import Http404
from django.shortcuts import get_object_or_404


User = get_user_model()

class DiligenceRoomDetailView(DetailView):

    def get_object(self):
        slug = self.kwargs.get("slug")
        if slug is None:
            raise Http404
        return get_object_or_404(DiligenceRoom, slug__iexact=slug)

    def get_context_data(self, *args, **kwargs):
        context = super(DiligenceRoomDetailView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = DiligenceRoom.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

class DiligenceRoomCreateView(LoginRequiredMixin, CreateView):
    template_name = 'forms/diligence_create_form.html'
    form_class = DiligenceRoomForm

    def get_queryset(self):
        return DiligenceRoom.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(DiligenceRoomCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(DiligenceRoomCreateView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = DiligenceRoom.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

class DiligenceRoomUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'forms/diligence_update_form.html'
    form_class = DiligenceRoomForm

    def get_queryset(self):
        return DiligenceRoom.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(DiligenceRoomUpdateView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = DiligenceRoom.objects.get(slug=slug).get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context