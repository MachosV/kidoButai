from django.db import models

class ResetPasswordId(models.Model):
    username = models.CharField(max_length=255)
    link = models.CharField(max_length=255, unique=True)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username+" "+self.link
    