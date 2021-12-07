from django.urls import path
from .views import profile_view, CreateProfileFormView, profile_creation_view, ProfileUpdateView, profile_update, ListProfileApiView, CreateProfileApiView, UpdateProfileApiView, DeleteProfileAPIView

urlpatterns = [
    #path('profile', ProfileView.as_view(), name='profile'),
    path('profile_list_api/', ListProfileApiView.as_view(), name='profile-list-api'),
    path('profile_create_api/', CreateProfileApiView.as_view(), name='profile-create-api'),
    path('profile_update_api/<id>', UpdateProfileApiView.as_view(), name='profile-update-api'),
    path('profile_delete_api/<id>', DeleteProfileAPIView.as_view(), name='profile-delete-api'),
    path('profile/', profile_view, name='profile'),
    path('<pk>/update/', profile_update, name='update_profile'),
    path('create-profile', profile_creation_view, name='profile_form')
    #path('profile-create/', CreateProfileFormView.as_view(), name='profile_form')
]