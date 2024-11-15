from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import IssueForm
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.conf import settings

def index(request):
    error = ""
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():

            try:
                form.save()

                return redirect('success')
            except Exception:
                return HttpResponse("Найден некорректный заголовок")

        else:
            error = "Ошибка заполнения!"

    form = IssueForm()
    data = {
        "form": form,
        "error": error
    }
    return render(request, 'polling/index.html', data)


def success(request):
    return render(request, 'polling/success.html')


def test(request):
    return HttpResponse("<h4>ТЕСТ,ТЕСТ. СЕРВЕР ПОДНЯТ!</h4>")
# Create your views here.
