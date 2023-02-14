from django.db import models
import uuid
from django.contrib.auth.models import User
from .ImageModel import Image

class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=32, blank=False)
    description = models.CharField(max_length=250, blank=False)
    representationLink = models.CharField(max_length=64, blank=False, unique=True)
    owner = models.ForeignKey(User, unique=False, on_delete=models.CASCADE,default=1)
    gtag = models.CharField(max_length=16,blank=False, default="")
    image = models.OneToOneField(Image, on_delete=models.CASCADE, blank=True, null=True)
    options = models.CharField(max_length=800, default="")

class CampaignLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.CharField(max_length=512)
    campaign = models.ForeignKey(Campaign,on_delete=models.CASCADE, related_name='links')