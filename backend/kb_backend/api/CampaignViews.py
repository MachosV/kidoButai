from rest_framework.response import Response
from rest_framework.views import APIView
from kb_backend.serializers import CampaignSerializer,CampaignCreateSerializer, CampaignEditSerializer
from rest_framework import generics, status
from ..models import Campaign,CampaignLink
from rest_framework import pagination
from rest_framework import filters

class CustomPagination(pagination.CursorPagination):
    ordering = "-create_date"

class CampaignEndpoint(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()

    def get_serializer_class(self):
        if self.request.method=="PUT":
            return CampaignEditSerializer
        return super().get_serializer_class()

    def update(self, request, *args, **kwargs):
        serializer = CampaignEditSerializer(data=request.data)
        request.data["representationLink"] = Campaign.objects.get(id=kwargs["pk"]).representationLink
        if serializer.is_valid():
            CampaignLink.objects.filter(campaign=object).delete()
            for link in request.data["links"]:
                campaignLink = CampaignLink(link=link, campaign=object)
                campaignLink.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        return Campaign.objects.filter(owner=user)

class CampaignCreateEndpoint(generics.CreateAPIView):
    serializer_class = CampaignCreateSerializer
    #parser_classes = (parsers.JSONParser,)


    def create(self, request, *args, **kwargs):
        serializer = CampaignCreateSerializer(data=request.data)
        if serializer.is_valid():
            object = serializer.save()
            object.owner = request.user
            object.save()
            for link in request.data["links"]:
                campaignLink = CampaignLink(link=link, campaign=object)
                campaignLink.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CampaignListEndpoint(generics.ListAPIView):
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        user = self.request.user
        return Campaign.objects.filter(owner=user)



class CampaignUpdateEndpoint(APIView):
    def put(self,request, *args, **kwargs):
        campaignPK = kwargs.get('pk', None)
        campaignObject = Campaign.objects.get(pk=campaignPK, owner=request.user)
        serializer = CampaignEditSerializer(data=request.data)
        if serializer.is_valid():
            CampaignLink.objects.filter(campaign=campaignObject).delete()
            for link in request.data["links"]:
                campaignLink = CampaignLink(link=link, campaign=campaignObject)
                campaignLink.save()
            campaignObject.name = serializer.validated_data["name"]
            campaignObject.description = serializer.validated_data["description"]
            campaignObject.save()
        else:
            print(serializer._errors)
        return Response(serializer.data, status=status.HTTP_200_OK)