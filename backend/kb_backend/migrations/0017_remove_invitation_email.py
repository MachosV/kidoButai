# Generated by Django 4.1.5 on 2023-03-17 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kb_backend', '0016_invitation_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='email',
        ),
    ]
