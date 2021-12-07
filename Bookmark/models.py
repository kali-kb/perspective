from django.db import models
from django import apps
from Profile.models import UserProfile

class Saved(models.Model):
	profile = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='saved')
	article = models.ForeignKey(to='Article.Article', on_delete=models.CASCADE, related_name='saved') #related_name
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return '{}'.format(self.article)