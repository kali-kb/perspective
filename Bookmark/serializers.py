from .models import Saved
from rest_framework import serializers

class BookmarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Saved
		fields = '__all__'