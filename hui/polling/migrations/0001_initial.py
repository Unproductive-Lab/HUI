# Generated by Django 5.1.3 on 2024-11-14 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='Имя')),
                ('thefuckingthing', models.TextField(verbose_name='Проблема')),
            ],
        ),
    ]