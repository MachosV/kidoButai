# Generated by Django 4.1.5 on 2023-01-20 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kb_backend', '0008_campaign_last_modified_date2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='last_modified_date2',
        ),
    ]
