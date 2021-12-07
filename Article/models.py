from django.db import models
from django.shortcuts import reverse
from Profile.models import UserProfile, Kudos
import os
import sys
from django.utils.text import slugify
#from django_quill.fields import QuillField
from taggit.managers import TaggableManager
from django import apps



class Article(models.Model):
    title = models.CharField(max_length=50)
	#body = QuillField(max_length=50000, blank=False) #max_length(50000)
    body = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(
    'Profile.UserProfile',
    on_delete=models.CASCADE, related_name='article',
    verbose_name='Publisher',null=True
    )
    edited = models.DateTimeField(auto_now=True)
    #readers = models.PositiveIntegerField(default=0)
    reader = models.ManyToManyField(to=UserProfile, related_name='readed', related_query_name='readed_users', blank=True)
    insightful = models.ManyToManyField(to=UserProfile, related_name='+',verbose_name='Insightful', blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    readtime = models.IntegerField(default=0)
    tags = TaggableManager()
	#collab
	#blogthread
	
    def get_absolute_url(self):
        return reverse('article', kwargs={'id': self.id},)
    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.readtime = len(self.body)//265
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    
    
    def archive(self, *args, **kwargs):
        body = self.body
        try:
           with open('{}.txt'.format(self.title), 'x') as archive:
              archive.write(body)
        except:
           pass #custom error view
	
	#add reader

		

'''
class Followers()
   follower
   followee
'''