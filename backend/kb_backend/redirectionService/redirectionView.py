from django.http import HttpResponse
from ..models import CampaignLink,Campaign
import random
import html
import string

def redirectionView(request,reprLink):
    try:
        campaign = Campaign.objects.get(representationLink=reprLink)
        campaignLinks = CampaignLink.objects.filter(campaign=campaign)
    except Exception as e:
        return HttpResponse("Not found")
    n = random.randint(0,len(campaignLinks)-1)
    gtag = html.escape(campaign.gtag)
    redirectLink = html.escape(campaignLinks[n].link)

    with open("kb_backend/redirectionService/redirectionPage.html", 'r') as f:
            template = f.read()
    template = string.Template(template)
    html = template.substitute(redirectLink=redirectLink, gtag=gtag)
    # html = '''
    # <script>
    # setTimeout(function(){window.location.href = "'''+campaignLinks[n].link+'''";}, 1500);
    # </script>
    # '''
    #html = '''<meta http-equiv="refresh" content="3;url={campaignLinks[n].link}" />'''
    return HttpResponse(html)