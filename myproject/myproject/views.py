from django.http import HttpResponse

def homepage(request):
    return HttpResponse('hello world, welcome to the home page')

def aboutpage(request):
    return HttpResponse('welcome to the about page')