from .models import Article
from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
	tags = TagListSerializerField()
	#manual fields
	class Meta:
		model = Article
		fields = ['id','title', 'body', 'date', 'publisher', 'edited', 'reader', 'insightful', 'slug', 'readtime', 'tags'] #taggablemanager() not serializable