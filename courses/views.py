from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, LoginForm
from .models import User

def signup(request):
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
# login(request, user)
			return redirect('login')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			role = form.cleaned_data.get('role')
			if role == 'learner':
				user.is_learner = True
			elif role == 'mentor':
				user.is_mentor = True
			user.save()
			login(request, user)
			if user == 'learner':
				return redirect('learner_dashboard')
			elif user == 'mentor':
				return redirect('mentor_dashbaord')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})

def learner_dashboard(request):
	return render(request, 'learner_dashboard.html')

def mentor_dashboard(request):
	return render(request, 'mentor_dashboard.html')
