# Generated by Django 3.0.4 on 2020-04-12 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cards',
            old_name='user_id',
            new_name='user',
        ),
    ]
