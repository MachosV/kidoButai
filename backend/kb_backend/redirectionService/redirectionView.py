from django.http import HttpResponse
from ..models import CampaignLink,Campaign
import random

def redirectionView(request,reprLink):
    try:
        campaignLinks = CampaignLink.objects.filter(campaign=Campaign.objects.get(representationLink=reprLink))
    except Exception as e:
        return HttpResponse("Not found")
    n = random.randint(0,len(campaignLinks)-1)
    html = '''
    <script>
    setTimeout(function(){window.location.href = "'''+campaignLinks[n].link+'''";}, 1500);
    </script>
    '''
    #html = '''<meta http-equiv="refresh" content="3;url={campaignLinks[n].link}" />'''
    return HttpResponse(html)