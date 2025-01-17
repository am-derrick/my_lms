from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	is_learner = models.BooleanField(default=False)
	is_mentor = models.BooleanField(default=False)
