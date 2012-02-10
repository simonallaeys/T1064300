# Create your views here.
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

#registration page
def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
 
    return render_to_response("registration/register.html",  {'form': form,  })


#override logout and redirect to main page
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')