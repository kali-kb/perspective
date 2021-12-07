from django.shortcuts import render,reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib import messages
from django.core.paginator import Paginator
from annoying.decorators import ajax_request
from Profile.models import Kudos, UserProfile
from Article.forms import ArticleCreationForm, ArticleUpdateForm, SignupForm
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView 
from django.views import View
from django.db.models import Max, Count, Avg
from .serializers import ArticleSerializer
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .decorators import check_recaptcha



'''home view rendering'''
'''top writers'''
#sorted by most followed
#all class based views inherited from View
#follower sorting bug
@check_recaptcha
def signup_view(request):
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get('username')
            message = message.success(request, "Welcome {}".format(username))
            print("welcome {}".format(username))
            return redirect("home")
        else:
            return "Something went wrong try again"
    else:
        form = SignupForm()
    
    return render(request, "sign_up.html", {
     "form": form
    })


@login_required(login_url="/login")
def home_view(request):
    articles=Article.objects.all()
    profile=UserProfile.objects.all()
    user = request.user.userprofile
    #readed_articles
    readed = user.readed.all()
    similar_post = [article.tags.similar_objects() for article in readed][:-1]
    #similar_article = [article.id for article in similar_post]
    #articles_from_followed_writer
    top_article = Article.objects.order_by('-insightful')[:2]
    top_writer = UserProfile.objects.order_by('follows')[:4]
    #top_articles
    context={
    #'similar_article': similar_article,
    'similar_post': similar_post,
    'readed':readed,
    'articles':articles,
    'profile':profile,
    'top_writer':top_writer,
    'top_article':top_article,
    }
    return render(request, 'home.html', context)
	#def get(self,request):
		#rng = [x for x in range(5)]
		#return HttpResponse(rng)
		
	
#def home_view(request):
   # return render(request, 'home.html')


'''blog list'''
def articles(request):
	article = Article.objects.all()
	paginator = Paginator(article, 6) #6 item per page
	page_number = request.GET.get('page')
	print(page_number)
	page_obj = paginator.get_page(page_number)
	context = {'article': article, 'page_obj':page_obj}
	return render(request, 'blog_list.html',context)
	

def article_detail(request, slug, **kwargs):
	u = request.META['HTTP_SEC_FETCH_USER']
	#h = request.SESSION
	print('hello', u[1:])
	#print('hello', h)
	reader=request.user.userprofile
	article_page = Article.objects.get(slug=slug)
	article_page.reader.add(reader)
	context = {
	'article': article_page,
	}
	return render(request, 'blog_details.html', context)
	
#def archive_article(request):
	#Article.archive()
	#return None
	
def article_form_view(request):
    if request.method == 'POST':
        form = ArticleCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            auto_input = form.save(commit=False)
            auto_input.publisher = request.user.userprofile #adds a currently logged in user
            auto_input.save()
            form.save()
            form.save_m2m() #bug here
            return redirect('articles')
    else:
        form = ArticleCreationForm()
    
    return render(request, 'publish_article.html', {'form':form})

		
class UpdateArticleView(UpdateView):
	model = Article
	fields = ['title', 'body']
	template_name = 'publish_article.html'
	#success_url = reverse_lazy('article', args=model.id,)
	
#bug *article obj
def kudos(request):
    try:
        article_id = request.POST.get('Article_id')
    except:
    	return 'No Article'
  
    userprofile = request.user.userprofile
    article = get_object_or_404(Article, id=article_id) #request.POST.get(id='article_id)
    #return None
    k = Kudos.objects.create(user=userprofile, article=article)
    k.save()
    context = {"k": k}
    return HttpResponseRedirect(reverse('article', args=[article.id]))
    #return HttpResponseRedirect(reverse('/home/'))

@ajax_request
def insightful(request, slug):
    article = Article.objects.get(slug=slug)
    profile = request.user.userprofile.id
    article.insightful.add(UserProfile.objects.get(id=profile))
    print(article.pk)
    article.save()
    return HttpResponseRedirect(reverse('article', args=[article.slug]))
    
'''writer of current post'''
def writer(request, pk):
	article = get_object_or_404(Article, pk=pk)
	writer=UserProfile.objects.get(pk=article.publisher.id)
	context={'writer':writer}
	return render(request, 'writer.html', context)

'''follow writer'''
@ajax_request
def follow(request, id):
    followed=False
    followee = get_object_or_404(UserProfile, id=id)
    profile=request.user.userprofile
    followee.follower.add(UserProfile.objects.get(id=profile.id))
    followee.save()
    followed=True
    if followee.follower.filter(id=followee.id).exists():
        followee.follower.remove(UserProfile.objects.get(id=profile.id))
        followed=False
        context_dict={
	    'followed':followed
	    }
        return response(context)
    return HttpResponseRedirect(reverse('writer', args=str(id)))

def archive_article(request, pk):
	article = Article.objects.get(pk=pk)
	article.archive()
	messages.success(request, 'successfully archived')
	return HttpResponseRedirect(reverse('article', args=str(pk)))


'''CRUD api_views'''

#GET/READ
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,)) #permission for fbv views
def article_list(request):
	article = Article.objects.all()
	serializer = ArticleSerializer(article, many=True)
	return Response(serializer.data)

#GET/READ
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def article_detail_api(request, pk):
	#get model query
	#serialize
	#return serialized data
	article = Article.objects.get(pk=pk)
	serializer = ArticleSerializer(article, many=False)
	return Response(serializer.data)
	
#CREATE
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def article_create_api(request):
	#get model query
	#serialize
	#return serialized data
	article = Article.objects.all()
	if request.method == 'POST':
		serializer = ArticleSerializer(article, request.data)
		if serializer.valid():
			serializer.save()
			return Response(status=HTTP_201_CREATED)
	return Response(serializer.data)



#UPDATE
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def article_update_api(request, pk):
	article = Article.objects.get(pk=pk)
	serializer = ArticleSerializer(article, data=request.data, instance=data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


#DELETE
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def article_delete_api(request, pk):
	#get model query
	#serialize
	#return serialized data
	article = Article.objects.get(pk=pk)
	article.delete()
	
	return Response('Deleted Successfully')
	
	




	
	
	
	

	

