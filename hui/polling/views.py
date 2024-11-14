from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'polling/index.html')


def success(request):
    return render(request, 'polling/success.html')


def test(request):
    return HttpResponse("<h4>ТЕСТ,ТЕСТ. СЕРВЕР ПОДНЯТ!</h4>")
# Create your views here.
