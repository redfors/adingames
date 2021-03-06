# Generated by Django 3.0.4 on 2020-04-17 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('overview', models.CharField(max_length=255, verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Подробное описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('delited', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовано')], default='draft', max_length=10, verbose_name='Статус')),
                ('tasks_statuses', models.CharField(choices=[('on_moderation', 'На модерации'), ('rejected', 'Отклонено'), ('received', 'Принято'), ('deleted', 'Удалено'), ('changed', 'Изменено'), ('in_work', 'В работе'), ('performed', 'Выполнено'), ('not_performed', 'Не выполнено'), ('dispute', 'Спор')], default='on_moderation', max_length=20, verbose_name='Статус модератора')),
                ('types_ads', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.TypesAds', verbose_name='Тип рекламы')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'задание',
                'verbose_name_plural': 'задания',
            },
        ),
    ]
