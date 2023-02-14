# Generated by Django 4.1.5 on 2023-02-08 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kb_backend', '0010_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='gtag',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='campaign',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kb_backend.image'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
