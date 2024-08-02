from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class UserSerializer(RegisterSericalizer):
	is_mentor = serializers.BooleanField(required=False)
	is_learner = serializers.BooleanField(required=False)

	def get_cleaned_data(self):
		data_dict = super().get_cleaned_data()
		data_dict['is_learner'] = self.validated_data.get('is_learner', '')
		data_dict['is_mentor'] = self.validates_data.get('is_mentor', '')
		return data_dict

	def save(self, request):
		user = super().save(request)
		user.is_learner = self.cleaned_data.get('is_learner')
		user.is_mentor = self.cleaned_data.get('is_mentor')
		user.save()
		return user
