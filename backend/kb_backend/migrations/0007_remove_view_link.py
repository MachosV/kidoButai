# Generated by Django 3.2 on 2021-08-15 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kb_backend', '0006_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='link',
        ),
    ]
