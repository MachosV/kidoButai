from django.http import HttpResponse
from ..models import CampaignLink,Campaign
import random

def redirectionView(request,reprLink):
    campaignLinks = CampaignLink.objects.filter(campaign=Campaign.objects.get(representationLink=reprLink))
    n = random.randint(0,len(campaignLinks)-1)
    html = '''
    <script>
    setTimeout(function(){window.location.href = "'''+campaignLinks[n].link+'''";}, 1500);
    </script>
    '''
    #html = '''<meta http-equiv="refresh" content="3;url={link}" />'''
    return HttpResponse(html)