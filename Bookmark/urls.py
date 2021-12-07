from django.urls import path
from .views import bookmarks, saved_article, ListBookmarksAPIView

urlpatterns = [
   path('bookmarks_list_api/', ListBookmarksAPIView.as_view(), name='profile_api_list'),
   path('bookmarks/', bookmarks, name='read_later'),
   path('saved_article/', saved_article, name='saved-article')
]