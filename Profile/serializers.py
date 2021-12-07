from .models import UserProfile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = UserProfile
		fields = '__all__'