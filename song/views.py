from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/admin">Admin page</a>')

