from django.views.generic import DetailView, FormView, UpdateView, TemplateView
from businessplan.utils import try_get_context
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ExcelTemplate
from accounts.models import User # temporary solution
from .utils import get_business_graph_data, get_follower_graph_data, add_graph_data_follower
from .forms import ExcelTemplateForm
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# class KPIHomeView(LoginRequiredMixin, FormView):
#     template_name = 'home_view.html'
#     form_class = ExcelTemplateForm
#
#     def get_queryset(self):
#         return ExcelTemplate.objects.filter(user=self.request.user)
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.user = self.request.user
#         return super(KPIHomeView, self).form_valid(form)
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(KPIHomeView, self).get_context_data(*args, **kwargs)
#         slug = self.kwargs.get("slug")
#         if slug:
#             user = ExcelTemplate.objects.get(slug=slug).get_user()
#         else:
#             user = self.request.user
#         full_context = try_get_context(context, user)
#         return full_context
#
#     def get_success_url(self):
#         kpis = ExcelTemplate.objects.filter(user=self.request.user)
#         if kpis.count() > 1:
#             return reverse('kpi:detail-follower', kwargs={'slug': kpis.first().slug})
#         else:
#             return redirect('/kpi/')

@login_required
def kpi_home(request):
    if request.method == "GET":
        form = ExcelTemplateForm()
        context = try_get_context({}, request.user)
        context['form'] = form
        return render(request, 'home_view.html', context)
    elif request.method == 'POST':
        file = request.FILES['template']
        template = ExcelTemplate(user=request.user, template=file)
        template.save()
        # If user has less than 2 KPIs uploaded redirect to same page
        kpis = ExcelTemplate.objects.filter(user=request.user)
        if kpis.count() < 2:
            return redirect('/kpi/')
        else:
            return HttpResponseRedirect(reverse('kpi:detail-follower', kwargs={'slug': kpis.first().slug}))

class KPIFollowerView(LoginRequiredMixin, TemplateView):
    template_name = 'follower_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(KPIFollowerView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = ExcelTemplate.objects.filter(slug=slug).first().get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        yearly_excel = ExcelTemplate.objects.filter(user=user, period='y').first()
        full_context = add_graph_data_follower(full_context, yearly_excel.template.file)
        return full_context

    # def get(self, request, *args, **kwargs):
    #     response = super(KPIDemoView, self).get(request, *args, **kwargs)
    #     response['X_EMAIL'] = request.user.email
    #     print(response['X_EMAIL'])
    #     return response

class KPIBusinessView(LoginRequiredMixin, TemplateView):
    template_name = 'business_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(KPIBusinessView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            user = ExcelTemplate.objects.filter(slug=slug).first().get_user()
        else:
            user = self.request.user
        full_context = try_get_context(context, user)
        return full_context

@login_required
def get_data_follower(request, *args, **kwargs):
    slug = kwargs.get("slug")
    if slug:
        user = ExcelTemplate.objects.filter(slug=slug).first().get_user()
    else:
        user = request.user
    yearly_excel = ExcelTemplate.objects.filter(user=user, period='y').first()
    monthly_excels = ExcelTemplate.objects.filter(user=user, period='m')
    print(get_follower_graph_data(yearly_excel, monthly_excels))
    return JsonResponse(get_follower_graph_data(yearly_excel, monthly_excels))

@login_required
def get_data_business(request, *args, **kwargs):
    slug = kwargs.get("slug")
    if slug:
        user = ExcelTemplate.objects.filter(slug=slug).first().get_user()
    else:
        user = request.user
    yearly_excel = ExcelTemplate.objects.filter(user=user, period='y').first()
    monthly_excels = ExcelTemplate.objects.filter(user=user, period='m')
    print(get_business_graph_data(yearly_excel, monthly_excels, user))
    return JsonResponse(get_business_graph_data(yearly_excel, monthly_excels, user))

# def prueba(request):
#     return render(request, "kpi/business_view.html")

# Not using REST for now: this project has custom user and can't get the email from headers
# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []
#
#     def get(self, request, format=None):
#         temporary_user = User.objects.get(email='lemac_cw@lemac.com') # temporary solution
#         print(request.META.get('HTTP_X_EMAIL'))
#         gross_and_nets = GrossAndNet.objects.filter(user=temporary_user)
#         years = []
#         gross_values = []
#         net_values = []
#         for gn in gross_and_nets:
#             years.append(gn.get_year())
#             gross_values.append(gn.get_gross())
#             net_values.append(gn.get_net())
#         data = {
#             "labels": years,
#             "gross_values": gross_values,
#             "net_values": net_values,
#         }
#         return Response(data)




