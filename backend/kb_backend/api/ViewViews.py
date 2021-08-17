from django.db.models.aggregates import Count
from kb_backend.models.Campaign import Campaign
from kb_backend.serializers.ViewSerializer import ViewSerializer
from ..models import View
from rest_framework import generics, serializers
import datetime as dt
from datetime import datetime


class StatSerializer(serializers.Serializer):
    create_date = serializers.CharField(max_length=12)
    count = serializers.IntegerField()


class ViewListEndpoint(generics.ListAPIView):
    serializer_class = StatSerializer
    queryset = View.objects.all()

    def get_queryset(self):
        user = self.request.user
        campaign = Campaign.objects.get(id=self.kwargs["pk"], owner=user)
        startDate = self.request.GET.get('startDate', '')
        startDate = datetime.strptime(startDate,"%d/%m/%Y")
        print(startDate + dt.timedelta(days=7))

        qs = View.objects.filter(campaign=campaign,create_date__gte=startDate, create_date__lte=startDate + dt.timedelta(days=7)).extra({'create_date':"date(create_date)"}).\
        values('create_date').\
        annotate(count=Count('create_date'))
        
        return qs

