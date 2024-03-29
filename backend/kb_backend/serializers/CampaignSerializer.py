from django.db import IntegrityError
from rest_framework import  serializers
from ..models.Campaign import Campaign, CampaignLink

class CampaignLinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CampaignLink
        fields = "__all__"

class CampaignLinkEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = CampaignLink
        fields = ["link"]

class CampaignSerializer(serializers.ModelSerializer):
    
    links = CampaignLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = "__all__"



class CampaignLinkCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = CampaignLink
            fields = [
                "id",
                "link"
            ]

class CampaignCreateSerializer(serializers.ModelSerializer):
    
    links = CampaignLinkCreateSerializer(read_only=True,many=True)
    
    class Meta:
        model = Campaign
        fields = "__all__"
        #exclude = ['owner']

    #def perform_create(self,serializer):
     #   serializer.save(owner=self.request.user)

    #def create(self, validated_data):
     #   try:
      #      instance = Campaign.objects.create(**validated_data)
       # except IntegrityError:
        #    print(IntegrityError)
         #   raise serializers.ValidationError("Foreign key constraint failure")
        #return instance

class CampaignEditSerializer(serializers.ModelSerializer):
    links = CampaignLinkCreateSerializer(read_only=True,many=True)
    class Meta:
        model = Campaign
        fields = [
            "name",
            "description",
            "links"
        ]
        read_only_fields = ['representationLink',"owner"]