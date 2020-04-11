from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Contractors(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )

    title = models.CharField("Название", max_length=150)
    overview = models.CharField("Краткое описание", max_length=255)
    description = models.TextField("Подробное описание")

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", blank=True, null=True)

    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delited = models.DateTimeField(auto_now=True)

    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = """контрагент"""
        verbose_name_plural = """контрагенты"""
