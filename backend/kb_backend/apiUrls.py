from kb_backend.api.AuthViews import AuthView
from kb_backend.redirectionService.redirectionView import redirectionView
from django.contrib.auth import login
from django.urls import path

from .api import CampaignViews
from .api import AuthViews
from .api import ViewViews
from .api import ImageUploader

urlpatterns = [
    path('images',ImageUploader.ImageUploader.as_view(),name="ImageUploader"),
    path('campaign', CampaignViews.CampaignListEndpoint.as_view() , name='CampaignListEndpoint'),
    path('campaign/create', CampaignViews.CampaignCreateEndpoint.as_view() , name='CampaignCreateEndpoint'),
    path('campaign/<pk>', CampaignViews.CampaignEndpoint.as_view() , name='CampaignRUDEndpoint'),
    path('campaign/<pk>/update', CampaignViews.CampaignUpdateEndpoint.as_view() , name='CampaignUEndpoint'),
    path('stats/<pk>/weekly',ViewViews.ViewListWeeklyEndpoint.as_view(),name="ViewListWeekly"),
    path('stats/<pk>/daily',ViewViews.ViewListDailyEndpoint.as_view(),name="ViewListDaily"),
    path('auth',AuthViews.AuthView.as_view(), name='AuthenticationView'),
    path('checkAuth',AuthViews.CheckAuth.as_view(), name='CheckAuthView'),
]