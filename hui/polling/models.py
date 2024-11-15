from django.db import models


class Issue(models.Model):
    fio = models.CharField("Имя\Фамилия\Кабинет", max_length=100)
    thefuckingthing = models.TextField("Опишите, пожалуйста, вашу проблему")
    def __str__(self):
        return self.fio
# Create your models here.
