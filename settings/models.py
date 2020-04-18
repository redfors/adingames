from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TypesAds(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = """тип рекламы"""
        verbose_name_plural = """типы рекламы"""

class CategoryAds(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = """кактегория рекламы"""
        verbose_name_plural = """категории рекламы"""


class FormatAds(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = """формат рекламы"""
        verbose_name_plural = """форматы рекламы"""


class Playgrounds(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )

    STATUS_MODERATOR = (
        ('on_moderation', 'На модерации'),
        ('rejected', 'Отклонено'),
        ('received', 'Принято'),
        ('deleted', 'Удалено'),
        ('changed', 'Изменено')
    )

    name = models.CharField("Название", max_length=150)
    overview = models.CharField("Краткое описание", max_length=255)
    description = models.TextField("Подробное описание")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", blank=True, null=True)
    types_ads_id = models.ForeignKey(TypesAds, on_delete=models.CASCADE, verbose_name="Тип рекламы", blank=True,
                                     null=True)
    # playground_id = models.ForeignKey()

    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delited = models.DateTimeField(auto_now=True)

    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='draft')
    tasks_statuses = models.CharField('Статус модератора', max_length=20, choices=STATUS_MODERATOR,
                                      default='on_moderation')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = """площадка"""
        verbose_name_plural = """площадки"""


class Advertiser(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = """рекламодатель"""
        verbose_name_plural = """рекламодатели"""