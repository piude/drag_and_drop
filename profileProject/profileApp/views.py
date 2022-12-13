from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created successfully for user {username}')
			return redirect('profileApp:profile_list')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form':form})


def profile_list(request):
	context = {}
	context['profiles'] = Profile.objects.all()
	return render(request, 'profile_list.html', context)

def profile_detail(request, id):
	context = {}
	context['profile'] = Profile.objects.get(id=id)
	return render(request, 'profile_detail.html', context)

def edit_profile(request, id):
	context = {}
	obj = get_object_or_404(Profile, id=id)
	form = ProfileForm(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
		return redirect('profileApp:profile_list')
	context['form'] = form
	return render(request, 'edit_profile.html', context)
