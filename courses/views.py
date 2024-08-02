from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from .models import User

def signup(request, role):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			if form.cleaned_data['role'] == 'learner':
				user.is_learner = True
			elif form.cleaned_data['role'] == 'mentor':
				user.is_mentor = True
			user.save()
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm(initial={'role': role})
	return render(request, 'courses/signup.html', {'form': form, 'role': role})
