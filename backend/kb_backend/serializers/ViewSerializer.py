from rest_framework import serializers
from ..models.View import View

class ViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = View
        fields = [
            "create_date"
        ]