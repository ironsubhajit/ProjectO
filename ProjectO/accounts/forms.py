from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


from .models import Profile


# new user create form
class UserCreateForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control bg-white border-left-0 border-md'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'

        self.fields['first_name'].widget.attrs['class'] = 'form-control bg-white border-left-0 border-md'
        self.fields['first_name'].widget.attrs['id'] = 'first_name'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'

        self.fields['last_name'].widget.attrs['class'] = 'form-control bg-white border-left-0 border-md'
        self.fields['last_name'].widget.attrs['id'] = 'last_name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

        self.fields['email'].widget.attrs['class'] = 'form-control bg-white border-left-0 border-md'
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'

        self.fields['password1'].widget.attrs['class'] = 'form-control bg-white border-left-0 border-md'
        self.fields['password1'].widget.attrs['id'] = 'password'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = 'form-control bg-white border-left-0 border-md'
        self.fields['password2'].widget.attrs['id'] = 'passwordConfirmation'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    def username_clean(self):
        username = self.cleaned_data.get('username').lower()
        new_user = get_user_model().objects.filter(username=username)
        if new_user.count():
            raise ValidationError("User Already Exist!")
        return username

    def email_clean(self):
        email = self.cleaned_data.get('email').lower()
        new_user_email = get_user_model().objects.filter(email=email)
        if new_user_email.count():
            raise ValidationError("Email Already Exist!")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "The two password fields didn't match.",
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        return user


# login form
class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['id'] = 'password'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class UserUpdateForm(forms.ModelForm):
    """user information update form"""

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        fields = ("first_name", "last_name", "email")
        model = get_user_model()
    
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control bg-dark text-white site__input_field'
        self.fields['first_name'].widget.attrs['id'] = 'first_name_input'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'

        self.fields['last_name'].widget.attrs['class'] = 'form-control bg-dark text-white site__input_field'
        self.fields['last_name'].widget.attrs['id'] = 'last_name_input'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

        self.fields['email'].widget.attrs['class'] = 'form-control bg-dark text-white site__input_field'
        self.fields['email'].widget.attrs['id'] = 'email_input'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        

class ProfileUpdateForm(forms.ModelForm):
    """Profile update form"""
    profile_description = forms.CharField(max_length=500)
    collage_name = forms.CharField(max_length=200)

    class Meta:
        model = Profile
        fields = ("profile_image", "profile_description", "collage_name")
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        self.fields['profile_description'].widget.attrs['class'] = 'form-control bg-dark text-white site__input_field'
        self.fields['profile_description'].widget.attrs['id'] = 'profile_description_input'
        self.fields['profile_description'].widget.attrs['placeholder'] = 'Description'
        
        self.fields['collage_name'].widget.attrs['class'] = 'form-control bg-dark text-white site__input_field'
        self.fields['collage_name'].widget.attrs['id'] = 'collage_name_input'
        self.fields['collage_name'].widget.attrs['placeholder'] = 'Collage Name'
        
        self.fields['profile_image'].widget.attrs['class'] = 'form-control-file bg-dark text-white site__input_field'
        self.fields['profile_image'].widget.attrs['id'] = 'profile_image_input'
