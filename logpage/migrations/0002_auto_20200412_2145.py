# Generated by Django 3.0.4 on 2020-04-12 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='advertiser_id',
            new_name='advertiser',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='playground_id',
            new_name='playground',
        ),
    ]