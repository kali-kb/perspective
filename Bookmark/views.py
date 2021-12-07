from django.shortcuts import render
from .models import Saved
from django.contrib.auth.models import User
from Article.models import Article
from .serializers import BookmarkSerializer
from rest_framework.generics import ListAPIView


def bookmarks(request):
	profile = request.user.userprofile
	bookmark = Saved.objects.filter(profile__id=profile.id)
	context={"bookmark": bookmark}
	return render(request, 'read_later.html', context)

#cached obj
def saved_article(request):
	profile = request.user.userprofile
	saved= Saved.objects.get(id=request.POST.get('id'))
	article=Article.objects.get(id=saved.article.id)
	context={
	'article': article
	}
	return render(request, 'saved_article.html', context)
	
class ListBookmarksAPIView(ListAPIView):
	queryset = Saved.objects.all()
	serializer_class = BookmarkSerializer

	