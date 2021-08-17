from kb_backend.models.Campaign import Campaign
from django.db import models
import uuid
from django.contrib.auth.models import User

class View(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #link = models.CharField(max_length=512)
    create_date = models.DateTimeField(auto_now_add=True)
    campaign = models.ForeignKey(Campaign,on_delete=models.CASCADE)

