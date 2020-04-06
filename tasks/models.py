from django.db import models
from logpage.models import Profile

# Create your models here.

class TypesAds(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name


class Tasks(models.Model):
    title = models.CharField("Название", max_length=150)
    overview = models.CharField("Краткое описание", max_length=255)
    description = models.TextField("Подробное описание")
    tasks_profile_fk = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True, null=True)
    tasks_types_ads_fk = models.ForeignKey(TypesAds, on_delete=models.CASCADE, verbose_name="Тип рекламы", blank=True, null=True)

    def __str__(self):
        return self.title


