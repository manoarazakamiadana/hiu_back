from .models import Production
from rest_framework import serializers


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = ["id", "quantite", "date", "nom", "user", "vendue"]
