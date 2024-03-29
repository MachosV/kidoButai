# Generated by Django 4.1.5 on 2023-04-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb_backend', '0018_resetpasswordid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaypalEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('event_type', models.CharField(choices=[('BILLING.SUBSCRIPTION.ACTIVATED', 'Subscription Activated'), ('BILLING.SUBSCRIPTION.CANCELLED', 'Subscription Canceled'), ('BILLING.SUBSCRIPTION.EXPIRED', 'Subscription Expired'), ('BILLING.SUBSCRIPTION.PAYMENT.FAILED', 'Subscription Payment Failed'), ('BILLING.SUBSCRIPTION.RE-ACTIVATED', 'Subscription Re-Activated')], max_length=50)),
            ],
        ),
    ]
