from django import forms
from member.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class UserLoginForm(forms.Form):
    username = forms.CharField(label='帳號', error_messages={'required': '請輸入帳號'})
    password = forms.CharField(label='密碼', widget=forms.PasswordInput(), error_messages={'required': '請輸入密碼'})
    next_url = forms.CharField(required=False, widget=forms.HiddenInput())