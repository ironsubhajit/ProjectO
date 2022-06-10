from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordResetView, PasswordResetConfirmView,
    PasswordResetDoneView, PasswordResetCompleteView
)

from . import (
    views as acc_views,
    forms as acc_form
)


app_name = 'accounts'

urlpatterns = [
    path('signup/', acc_views.SignupView.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html',
            authentication_form=acc_form.UserLoginForm
        ),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'password-reset/',
        PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            success_url=reverse_lazy('accounts:password_reset_done'),
            email_template_name='accounts/password_reset_email.html'
        ),
        name="password_reset",

    ),
    path(
        'password-reset/done',
        PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'),
        name="password_reset_done"
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=reverse_lazy('accounts:password_reset_complete')
        ),
        name="password_reset_confirm"
    ),
    path(
        'password-reset-complete/',
        PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path('profile/', acc_views.profile, name="profile"),
    path('update/profile/', acc_views.profile_update, name="update_profile"),
]
