# Generated by Django 4.1.5 on 2023-01-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb_backend', '0007_remove_view_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='last_modified_date2',
            field=models.DateTimeField(auto_now=True),
        ),
    ]