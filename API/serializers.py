from .models import Clothes
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"

