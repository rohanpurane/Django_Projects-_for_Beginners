from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from captcha.fields import CaptchaField


class CaptchaForm(forms.Form):
    captcha = CaptchaField()
 
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'placeholder':'Username', 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'placeholder':'Password', 'class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old_Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus': True, 'placeholder':'Old Password', 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New_Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'placeholder':'New Password', 'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("New_Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'placeholder':'Confirm New Password', 'class':'form-control'}))

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ('fullname', 'your_email', 'subject')
        widgets = {
            'fullname': forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
            'your_email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email'}),
            'subject': forms.Textarea(attrs={'class':'form-control','placeholder':'Subject'}),
        }