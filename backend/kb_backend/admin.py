from kb_backend.models import View
from django.contrib import admin
from .models import Campaign
from .models import CampaignLink
from .models import Image
from .models import Invitation
# Register your models here.

admin.site.register(Campaign)
admin.site.register(View)
admin.site.register(CampaignLink)
admin.site.register(Image)
admin.site.register(Invitation)