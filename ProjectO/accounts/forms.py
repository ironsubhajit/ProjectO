from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# new user create form
class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

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


# login form
class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control bg-white border-left-0 border-md'
        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'

        self.fields['password'].widget.attrs['class'] = 'form-control bg-white border-left-0 border-md'
        self.fields['password'].widget.attrs['id'] = 'password'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
