from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Video
from .models import Course


def index(request):
    image = Course.objects.all()
    print(image)
    print("In Index")
    return render(request, 'home.html')


def tutorial(request):

    return render(request, 'tutorial.html')


def course1(request):
    video = Video.objects.all()
    n = len(video)
    print(video)
    print("N is :", n)
    print("hello")
    param = {'video': 'video', 'n': 'n'}
    return render(request, 'index.html', param)