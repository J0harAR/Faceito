# Generated by Django 4.1.1 on 2022-11-18 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_remove_usuario_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
    ]
