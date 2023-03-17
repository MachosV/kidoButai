from kb_backend.redirectionService.redirectionView import redirectionView
from django.contrib.auth import login
from django.urls import path

from .api import CampaignViews
from .api import AuthViews
from .api import ImageUploader
from .api import IPNListener
from .api import UserViews

urlpatterns = [
    path('IPNListener',IPNListener.IPNListener,name="IPNListener"),
    path('user/create',UserViews.UserCreateEndpoint.as_view(),name="UserCreate"),
    path('images',ImageUploader.ImageUploader.as_view(),name="ImageUploader"),
    path('campaign', CampaignViews.CampaignListEndpoint.as_view() , name='CampaignListEndpoint'),
    path('campaign/create', CampaignViews.CampaignCreateEndpoint.as_view() , name='CampaignCreateEndpoint'),
    path('campaign/<pk>', CampaignViews.CampaignEndpoint.as_view() , name='CampaignRUDEndpoint'),
    path('campaign/<pk>/update', CampaignViews.CampaignUpdateEndpoint.as_view() , name='CampaignUEndpoint'),
    path('auth/changePassword',AuthViews.ChangePassword.as_view(), name='ChangePassword'),
    path('auth/checkAuth',AuthViews.CheckAuth.as_view(), name='CheckAuthView'),
    path('auth',AuthViews.AuthView.as_view(), name='AuthenticationView'),
]