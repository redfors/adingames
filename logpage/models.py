from django.db import models
from django.contrib.auth.models import User
from settings.models import Playgrounds, Advertiser


# Create your models here.

class Profile(models.Model):
    STATUS_CHOICES = (
        ('adventiser', 'Рекламодатель'),
        ('playgrounds', 'Игровая площадка'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    type_user = models.CharField("Тип пользователя", max_length=100, choices=STATUS_CHOICES, default='adventiser')
    telephone = models.BigIntegerField("телефон", blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    playground_id = models.ForeignKey(Playgrounds, on_delete=models.CASCADE, verbose_name="Игровая площадка", blank=True, null=True)
    advertiser_id = models.ForeignKey(Advertiser, on_delete=models.CASCADE, verbose_name="Рекламодатель", blank=True,
                                      null=True)
    # Advertiser.objects.get()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = """пользовательские данные"""
        verbose_name_plural = """пользовательские данные"""
