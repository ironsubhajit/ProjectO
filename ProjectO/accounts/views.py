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


@login_required
def profile_update(request):
    """user profile update page view"""
    if request.method == 'POST':
        user_update_form = acc_form.UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = acc_form.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # print(f"user_update_form.is_valid() ========================================> {user_update_form.is_valid()}")
        # print(f"user_update_form.is_bound() ========================================> {user_update_form.is_bound}")
        # print(f"user_update_form.errors() ========================================> {user_update_form.errors}")

        print(f"profile_update_form.is_valid() ========================================> {profile_update_form.is_valid()}")

        if user_update_form.is_valid() and profile_update_form.is_valid():
            # print(f"========================================> Inside valid")

            user_update_form.save()

            # print(f"========================================> user update validated")

            profile_update_form.save()

            # print(f"========================================> profile update validated")

            return redirect('accounts:profile')
    else:
        user_update_form = acc_form.UserUpdateForm(instance=request.user)
        profile_update_form = acc_form.ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }

    return render(request, 'accounts/user_update_page.html', context=context)

