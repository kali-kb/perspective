from django.shortcuts import render, reverse, redirect
from .models import UserProfile
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, FormView, CreateView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect, FileResponse
from .forms import ProfileCreationForm
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import ProfileSerializer


#class ProfileView(TemplateView):
	#profile = Profile.objects.get(id=1)
	#template_name = 'userprofile/profile.html'
	
	#@property
	#def get_ip():
		#ip = request.META['REMOTE_ADDR']
		#return ip
def profile_view(request):
	profile = UserProfile.objects.get(id=request.user.id)
	context = {'profile': profile}
	return render(request, 'profile.html', context)

def open_img(self, profile_id):
	obj = UserProfile.objects.get(id=profile_id)
	img = obj.image
	return FileResponse(open('img', 'rb'))

def profile_creation_view(request):
    if request.method == 'POST':
        form = ProfileCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            user = form.cleaned_data['user']
            bio = form.cleaned_data['bio']
            #userprofile.save()
            #form = ProfileCreationForm(data=request.POST, files=request.FILES)
            obj = form.save(commit=False)
            obj.user=request.user.userprofile
            obj.save()
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = ProfileCreationForm()
    
    return render(request, 'create_profile.html', {'form':form })

def profile_update(request, pk):
	obj = request.user.userprofile
	#update form on a given object instance --> profile
	form = ProfileCreationForm(data=request.POST or None, files=request.FILES, instance=obj) #instance = obj
	if form.is_valid():
		form.save()
		return redirect('profile')
	else:
		form = ProfileCreationForm()
	# update.html with form==post method
	return render(request, 'edit_profile.html', context={'form':form})
			
	
class ProfileUpdateView(UpdateView):
	model = UserProfile
	fields = ['name', 'image', 'bio']
	

class CreateProfileFormView(CreateView):
	model = UserProfile
	form_class = ProfileCreationForm
	#context_object_name = 'form
	template_name = 'create_profile.html'
	
class ListProfileApiView(ListAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = ProfileSerializer


class CreateProfileApiView(CreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = ProfileSerializer


class UpdateProfileApiView(UpdateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = ProfileSerializer
	

class DeleteProfileAPIView(DestroyAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = ProfileSerializer
	
	
#class UpdateProfileViewFormView(UpdateView)



#class UpdateFormView(UpdateView):
