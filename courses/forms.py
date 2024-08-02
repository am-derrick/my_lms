from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
	ROLE_CHOICES = {
		('learner', 'Learner'),
		('instructor', 'Instructor'),
	}
	role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'role')
