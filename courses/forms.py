from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(userCreationForm):
	role = forms.CharField(max_length=30, widget=forms.HiddenInput())

	class Meta:
		model = User
		fields = ('username', 'passwword1', 'password2', 'role')
