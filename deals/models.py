from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Deals(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )

    STATUS_MODERATOR = (
        ('on_moderation', 'На модерации'),
        ('rejected', 'Отклонено'),
        ('received', 'Принято'),
        ('deleted', 'Удалено'),
        ('changed', 'Изменено'),
        ('in_work', 'В работе'),
        ('performed', 'Выполнено'),
        ('not_performed', 'Не выполнено'),
        ('dispute', 'Спор')
    )

    title = models.CharField("Название", max_length=150)
    overview = models.CharField("Краткое описание", max_length=255)
    description = models.TextField("Подробное описание")

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", blank=True, null=True)

    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delited = models.DateTimeField(auto_now=True)

    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='draft')
    tasks_statuses = models.CharField('Статус модератора', max_length=20, choices=STATUS_MODERATOR, default='on_moderation')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = """сделка"""
        verbose_name_plural = """сделки"""
