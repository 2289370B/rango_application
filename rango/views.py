from django.shortcuts import render
from django.http import HttpResponse


# index view
def index(request):
   context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
   return render(request,'rango/index.html',context=context_dict)

# about view
def about(request):
	return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>Index</a>")