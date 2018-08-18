from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView, DetailView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from .forms import LoginForm, RegisterForm, AccountTypeForm
from accounts.models import User
from django.urls import reverse
from profiles.models import SMEProfile

def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        qs = User.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            account = qs.first()
            if not account.active:
                account.active = True
                account.activation_key = None
                account.save()
                return redirect("/login")
    return redirect("/login")

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = '/activation/'

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            elif user.is_staff:
                return redirect('/search-companies/')
            elif user.is_sme:
                try:
                    sme_profile = SMEProfile.objects.get(user=user)
                    return redirect(sme_profile.get_absolute_url())
                except SMEProfile.DoesNotExist:
                    return redirect('/profile/sme/create')
            else:
                return redirect('/account/')
        return super(LoginView, self).form_invalid(form)

class AccountTypeView(FormView):
    form_class = AccountTypeForm
    template_name = 'accounts/acc_type.html'

    def form_valid(self, form):
        user = self.request.user
        user_choice = form.cleaned_data.get('account_type')
        if user_choice == 'sme':
            user.sme = True
            user.save()
            return redirect('/profile/sme/create')
        else:
            user.staff = True
            user.save()
            return redirect('/profile/staff/create')
        return super(AccountTypeView, self).form_invalid(form)