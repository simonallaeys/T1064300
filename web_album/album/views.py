# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from django.contrib import auth

#index     
def main_page(request):
	return render_to_response('main_page.html', {'user': request.user})