from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    STATUS_MODERATOR = (
        ('on_moderation', 'На модерации'),
        ('rejected', 'Отклонено'),
        ('received', 'Принято'),
        ('deleted', 'Удалено'),
        ('changed', 'Изменено')
    )

    title = models.CharField("Название", max_length=150)
    overview = models.CharField("Краткое описание", max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", blank=True, null=True)

    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delited = models.DateTimeField(auto_now=True)

    tasks_statuses = models.CharField('Статус модератора', max_length=20, choices=STATUS_MODERATOR,
                                      default='on_moderation')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = """аккаунт"""
        verbose_name_plural = """аккаунты"""
