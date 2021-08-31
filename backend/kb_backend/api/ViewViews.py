from django.db.models.aggregates import Count
from kb_backend.models.Campaign import Campaign
from ..models import View
from rest_framework import generics, serializers
import datetime as dt
from datetime import datetime
from django.db.models.functions import Trunc
from django.db.models.functions import ExtractHour

class StatSerializerWeekly(serializers.Serializer):
    create_date = serializers.CharField(max_length=12)
    count = serializers.IntegerField()

class StatSerializerHourly(serializers.Serializer):
    hour = serializers.IntegerField()
    count = serializers.IntegerField()


class ViewListWeeklyEndpoint(generics.ListAPIView):
    serializer_class = StatSerializerWeekly
    queryset = View.objects.all()
    pagination_class = None


    def get_queryset(self):
        user = self.request.user
        campaign = Campaign.objects.get(id=self.kwargs["pk"], owner=user)
        startDate = self.request.GET.get('startDate', '')
        startDate = datetime.strptime(startDate,"%d/%m/%Y")

        qs = View.objects.filter(campaign=campaign,create_date__gte=startDate, create_date__lte=startDate + dt.timedelta(days=7)).extra({'create_date':"date(create_date)"}).\
        values('create_date').\
        annotate(count=Count('create_date'))
        
        return qs


class ViewListDailyEndpoint(generics.ListAPIView):
    serializer_class = StatSerializerHourly
    queryset = View.objects.all()
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        campaign = Campaign.objects.get(id=self.kwargs["pk"], owner=user)
        startDate = self.request.GET.get('startDate', '')
        startDate = datetime.strptime(startDate,"%d/%m/%Y")

        print(startDate.year, startDate.month, startDate.day)

        qs = View.objects.filter(campaign=campaign,create_date__day=startDate.day,create_date__month=startDate.month,create_date__year=startDate.year)\
        .annotate(hour=ExtractHour("create_date"))\
        .values('hour').annotate(count=Count('id'))
        
        print(qs.query)
        print(qs)

        return qs