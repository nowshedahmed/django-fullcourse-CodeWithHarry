from django.shortcuts import render
from django.http import HttpResponse

# Create your views  here. of shop folder




def indexshop(request):
    return render(request,'shop/indexshop.html')


def about(request):
    return render(request,'shop/aboutsp.html')

def contract(request):
    return render(request,'shop/contrtsp.html')

def tracker(request):
    return render(request,'shop/tractsp.html')

def search(request):
    return render(request,'shop/serchsp.html')

def prodviews(request):
    return render(request,'shop/prodviewsp.html')

def cheackout(request):
    return render(request,'shop/chekoutsp.html')










