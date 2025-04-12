from rest_framework.decorators import APIView
from .serializers import ProductionSerializer
from rest_framework.response import Response
from django.db.models import Avg


class ProductionView(APIView):
    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        serializer = ProductionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 400)

    def get(self, request):
        user = request.user
        serializer = ProductionSerializer(user.productions.all(), many=True)
        averages = user.productions.aggregate(
            moyenne_quantite=Avg('quantite'),
            moyenne_reste=Avg('reste')
        )
        moyenne_quantite = averages['moyenne_quantite']
        moyenne_reste = averages['moyenne_reste']
        next = moyenne_quantite - moyenne_reste
        return Response({
            "production": serializer.data,
            'next': next
        })
