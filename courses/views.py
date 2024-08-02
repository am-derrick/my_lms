from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from .models import User

def signup(request, role):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			role = form.cleaned_data.get('role')
			if role == 'learner':
				user.is_learner = True
			elif role == 'mentor':
				user.is_mentor = True
			user.save()
			login(request, user)
			return redirect('login')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
