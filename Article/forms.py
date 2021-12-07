from .models import Article
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#body
#publisher
class ArticleCreationForm(forms.ModelForm):
	#title = forms.Charfield()
	#body = forms.Textarea()
	
	class Meta:
		model = Article
		fields = ['title','body', 'tags']
		
		
class ArticleUpdateForm(forms.ModelForm):
	class Meta:
		model = Article
		exclude = ['publisher']
		
class SignupForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]
		
	