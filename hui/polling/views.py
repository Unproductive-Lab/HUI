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
            subject = "[НОВАЯ ЗАЯВКА]"
            body = {
                'name': form.cleaned_data['fio'],
                'issue': form.cleaned_data['thefuckingthing'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject,message,
                        settings.EMAIL_HOST_USER,
                            [settings.EMAIL_RECIPIENT],
                          auth_user=settings.EMAIL_HOST_USER,
                          auth_password=settings.EMAIL_HOST_PASSWORD
                          )

                return redirect('success')
            except BadHeaderError:
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
