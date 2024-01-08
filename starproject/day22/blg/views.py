from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.




def indexblg(request):
    return HttpResponse("<h1>welcome to blg</h1>")
