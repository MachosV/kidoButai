from django.contrib.auth import login
from django.urls import path

from .redirectionService import redirectionView

urlpatterns = [
    path('<reprLink>', redirectionView.redirectionView , name='redirectionView'),
]