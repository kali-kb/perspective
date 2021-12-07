from django.urls import path, include
#from .views import ArticleViewSet
#from rest_framework import routers
#from django.contrib.auth import views as auth_views
from .views import (
          signup_view,
          home_view,
          articles,
          article_list,
          article_detail,
          kudos,
          article_form_view,
          UpdateArticleView,
          insightful,
          writer,
          follow,
          archive_article,
          article_detail_api,
          article_list,
          article_delete_api,
          article_update_api
          
)

#router = routers.DefaultRouter() 
#router.register(r'article_api', ArticleViewSet)

#home_view
urlpatterns = [
    #path('', include(router.urls)),
    """
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    """
    path('sign_up', signup_view, name="sign-up"),
    path('article_update_api/<pk>', article_update_api, name='article-delete-api'),
    path('article_delete_api/<pk>', article_delete_api, name='delete_api'),
    path('articles_list', article_list, name='article-list'),
    path('article_detail/<pk>', article_detail_api, name='article-detail-api'),
    path('home/', home_view, name='homeview'),
    path('articles/', articles, name='articles'),
    path('publish-article/', article_form_view, name='publish-article'),
    path('article/<str:slug>/', article_detail, name='article'),
    path('<pk>/update_article/',UpdateArticleView.as_view(), name='update_article'),
    path('kudos/', kudos, name='kudos_add'),
    path('insightful/<str:slug>', insightful, name='insightful'),
    path('archive/<pk>', archive_article, name='archive'),
    path('writer/<pk>', writer, name='writer'),
    path('follow-writer/<id>', follow, name='follow')
]