from rest_framework import serializers
from ..models.ImageModel import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'upload_date']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['image'] = instance.image.url
        return response