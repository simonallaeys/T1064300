# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login

#override logout and redirect to main page
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')