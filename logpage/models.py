from django.db import models
from django.conf import settings


# Create your models here.

class Profile(models.Model):
    STATUS_CHOICES = (
        ('adventiser', 'Рекламодатель'),
        ('playground', 'Игровая площадка'),
    )
    user = models.CharField(max_length=100)
    type_user = models.CharField("Тип пользователя", max_length=100, choices=STATUS_CHOICES, default='adventiser')
    telephone = models.BigIntegerField("телефон", blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = """пользовательские данные"""
        verbose_name_plural = u"""пользовательские данные"""
