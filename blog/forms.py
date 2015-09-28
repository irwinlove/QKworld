from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from blog.models import UserProfile
class Userform(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=('username','email','password')
class UserProfileForm(ModelForm):
	class Meta:
		model=UserProfile
		fields=('website','picture')
