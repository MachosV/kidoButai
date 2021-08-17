from kb_backend.api.AuthViews import AuthView
from kb_backend.redirectionService.redirectionView import redirectionView
from django.contrib.auth import login
from django.urls import path

from .api import CampaignViews
from .api import AuthViews
from .api import ViewViews

urlpatterns = [
    path('campaign', CampaignViews.CampaignListEndpoint.as_view() , name='CampaignListEndpoint'),
    path('campaign/create', CampaignViews.CampaignCreateEndpoint.as_view() , name='CampaignCreateEndpoint'),
    path('campaign/<pk>', CampaignViews.CampaignEndpoint.as_view() , name='CampaignRUDEndpoint'), #can retrieve and delete
    path('campaign/<pk>/update', CampaignViews.CampaignUpdateEndpoint.as_view() , name='CampaignUEndpoint'), #can update
    path('stats/<pk>',ViewViews.ViewListEndpoint.as_view(),name="ViewList"),
    path('stats/<pk>/daily',ViewViews.ViewListDailyEndpoint.as_view(),name="ViewListDaily"),
    path('auth',AuthViews.AuthView.as_view(), name='AuthenticationView'),
    path('example',AuthViews.ExampleView.as_view(), name='ExampleAuthView'),
]