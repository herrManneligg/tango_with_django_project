from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
    context_dict = {'boldmessage': 'This tutorial has been put together by Pablo Berjon.'}
    return render(request, 'rango/about.html', context=context_dict)
