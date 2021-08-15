# Generated by Django 3.2 on 2021-08-15 10:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kb_backend', '0005_campaign_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=512)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kb_backend.campaign')),
            ],
        ),
    ]