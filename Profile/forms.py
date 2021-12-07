from django import forms
from .models import UserProfile



class ProfileCreationForm(forms.ModelForm):
	class Meta:
		
		model = UserProfile
		fields = '__all__'
		exclude = ['follower','user']
		#fields = ['name','user','bio']
	 
	
	
#class ProfileUpdateForm(forms.ModelForm):