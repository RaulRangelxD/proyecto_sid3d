# Generated by Django 5.0.6 on 2024-06-13 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.IntegerField(default=False, verbose_name='Perfil'),
        ),
    ]
