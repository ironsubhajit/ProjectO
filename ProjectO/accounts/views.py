from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import forms as acc_form


class SignupView(CreateView):
    form_class = acc_form.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


@login_required
def profile(request):
    """user profile page view"""
    return render(request, 'accounts/user_profile.html')
