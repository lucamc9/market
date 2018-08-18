from .models import BusinessPlan
from diagnostics.models import Diagnostics
from profiles.models import SMEProfile, StaffProfile
from dataroom.models import Accordion
from diligence.models import DiligenceRoom
from kpi.models import ExcelTemplate
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser

# def try_get_context(context, slug, request_user):
#     # Get full context
#
#     try:
#         bp = BusinessPlan.objects.get(slug=slug)
#         context['bp'] = bp
#     except BusinessPlan.DoesNotExist:
#         context['bp'] = None
#     try:
#         diag = Diagnostics.objects.filter(slug=slug)[0]
#         context['diag'] = diag
#     except:
#         context['diag'] = None
#     try:
#         profile = SMEProfile.objects.get(user=request_user)
#         context['smeprofile'] = profile
#     except SMEProfile.DoesNotExist:
#         context['smeprofile'] = None
#     try:
#         profile = StaffProfile.objects.get(user=request_user)
#         context['staffprofile'] = profile
#     except StaffProfile.DoesNotExist:
#         context['staffprofile'] = None
#     try:
#         accordion = Accordion.objects.get(slug=slug)
#         context['accordion'] = accordion
#     except:
#         context['accordion'] = None
#     try:
#         diligence = DiligenceRoom.objects.get(slug=slug)
#         context['diligence'] = diligence
#     except:
#         context['diligence'] = None
#     try:
#         graph_data = GraphData.objects.filter(user=request_user)[0]
#         context['kpi'] = graph_data
#     except:
#         context['kpi'] = None
#
#
#     return context

# Old version

def try_get_context(context, request_user):
    #
    #if isinstance(request_user, SimpleLazyObject):
    #     context['bp'] = None
    #     context['diag'] = None
    #     context['smeprofile'] = None
    #     context['staffprofile'] = None
    #     context['accordion'] = None
    #     context['diligence'] = None
    #     context['kpi'] = None
    # else:

    try:
        bp = BusinessPlan.objects.get(user=request_user)
        context['bp'] = bp
    except BusinessPlan.DoesNotExist:
        context['bp'] = None
    try:
        diag = Diagnostics.objects.filter(user=request_user).first()
        context['diag'] = diag
    except:
        context['diag'] = None
    try:
        profile = SMEProfile.objects.get(user=request_user)
        context['smeprofile'] = profile
    except SMEProfile.DoesNotExist:
        context['smeprofile'] = None
    try:
        profile = StaffProfile.objects.get(user=request_user)
        context['staffprofile'] = profile
    except StaffProfile.DoesNotExist:
        context['staffprofile'] = None
    try:
        accordion = Accordion.objects.filter(user=request_user).first()
        context['accordion'] = accordion
    except:
        context['accordion'] = None
    try:
        diligence = DiligenceRoom.objects.get(user=request_user)
        context['diligence'] = diligence
    except:
        context['diligence'] = None
    try:
        graph_data = ExcelTemplate.objects.filter(user=request_user)
        if graph_data.count() < 2:
            context['kpi'] = None
        else:
            context['kpi'] = graph_data
    except:
        context['kpi'] = None
    # print(context['kpi'])
    # print(context['smeprofile'])

    return context




