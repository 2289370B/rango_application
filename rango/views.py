from django.shortcuts import render

from django.http import HttpResponse

# index view
def index(request):
	return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

# about view
def about(request):
	return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>Index</a>")