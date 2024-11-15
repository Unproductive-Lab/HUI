from .models import Issue
from django.forms import ModelForm, TextInput, Textarea


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['fio', 'thefuckingthing']

        widgets = {
            "fio": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя\Фамилия\Кабинет"
            }),
            "thefuckingthing": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Опишите, пожалуйста, вашу проблему",
                "rows": "5"
            })

        }
