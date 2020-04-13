from django.db import models
from django.contrib.auth.models import User
from settings.models import TypesAds


# Create your models here.

class Mytools(models.Model):
    title = models.CharField("Название", max_length=150)
    overview = models.CharField("Краткое описание", max_length=255)
    description = models.TextField("Подробное описание")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", blank=True, null=True)

    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = """инструмент"""
        verbose_name_plural = """инструменты"""
