from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def welcome(request):
    return HttpResponse('hello world')


def debug(request):
    print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    return render(request, 'home.html', {'name': 'Welcome to Posts'})


def method(request):
    if request.method != "POST":
        return HttpResponse('Invalid Request Method')
    return JsonResponse({
        'success': True
    })
