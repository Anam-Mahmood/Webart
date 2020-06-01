from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}
    ))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=255, widget=forms.TextInput(
        attrs={'class': 'string optional', 'placeholder': 'First Name'}
    ))
    last_name = forms.CharField(required=True, max_length=255, widget=forms.TextInput(
        attrs={'class': 'string optional', 'placeholder': 'Last Name'}
    ))
    username = forms.CharField(required=True, max_length=255, widget=forms.TextInput(
        attrs={'class': 'string optional', 'placeholder': 'Username'}
    ))
    email = forms.EmailField(required=True, max_length=255, widget=forms.TextInput(
        attrs={'class': 'string optional', 'placeholder': 'E-mail Address'}
    ))
    password1 = forms.CharField(required=True, max_length=255, widget=forms.PasswordInput(
        attrs={'class': 'string optional', 'placeholder': 'Password'}
    ))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'string optional', 'placeholder': 'Password Confirmation'}
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']

        if commit:
            user.save()

        return user