# Generated by Django 3.0.4 on 2020-04-18 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logpage', '0003_auto_20200418_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type_user',
            field=models.CharField(choices=[('adventiser', 'Рекламодатель'), ('playgrounds', 'Игровая площадка')], default='adventiser', max_length=100, verbose_name='Тип пользователя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
