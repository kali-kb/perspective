from django.db import models
from django.shortcuts import reverse
#from blog.models #import #Blog
#from django_quill.fields import QuillField
from django import apps
from django.conf import settings
from django.contrib.auth.models import User
#class #Careers(models.#Model):ĺ
	#CAREERS = (
    #('Software engineer','software engineer'),
#)

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200)
    #bio = QuillField(
    #max_length=350, help_text='optional',
    #blank=True,null=True, verbose_name='Bio'
    #)
    follower = models.ManyToManyField(to='Profile.UserProfile', verbose_name='Follower', related_query_name='follows')
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(
    upload_to='profile_pic/', verbose_name='Profile Picture',
    blank=True
    )
    
    bio = models.TextField(max_length=100)
    books = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    
    def get_success_url(self):
        return reverse('profile', args=self.pk)


class Kudos(models.Model):
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    article = models.ForeignKey('Article.Article', related_name='kudos', on_delete=models.CASCADE) 
    
    def __str__(self):
        return 'liked {}'.format(self.article)


#bio = QuillField(
    #max_length=350, help_text='optional',
    #blank=True,null=True, verbose_name='Bio'
    #)
#career = model.IntegerField(choices=CAREERS,default='None', max_length=200)
	#career = modelmultiplechoicefield(queryset=None)