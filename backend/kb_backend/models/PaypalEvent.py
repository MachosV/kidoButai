from django.db import models

PaypalEventsChoices = (
        ('BILLING.SUBSCRIPTION.ACTIVATED', 'Subscription Activated'),
        ('BILLING.SUBSCRIPTION.CANCELLED', 'Subscription Canceled'),
        #('BILLING.SUBSCRIPTION.EXPIRED', 'Subscription Expired'),
        ('BILLING.SUBSCRIPTION.PAYMENT.FAILED','Subscription Payment Failed'),
        ('BILLING.SUBSCRIPTION.RE-ACTIVATED','Subscription Re-Activated')
    )

class PaypalEvent(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    event_type = models.CharField(max_length=50, choices=PaypalEventsChoices)

    def __str__(self):
        return f'{self.event_type} | {self.email}'