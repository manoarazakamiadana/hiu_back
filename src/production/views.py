from rest_framework.decorators import APIView
from .serializers import ProductionSerializer
from rest_framework.response import Response


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
        data = serializer.data

        total_quantite = 0
        total_vendu = 0
        for d in data:
            d["stock"] = d["quantite"] - d["vendue"]
            total_quantite += d["quantite"]
            total_vendu += d["vendue"]

        n = len(data)

        efficacite_production = (total_vendu/total_quantite)*100

        reste = total_quantite-total_vendu

        next = (total_quantite/n) - (reste/n)

        return Response({
            "production": data,
            "efficacite_production": efficacite_production,
            "stock_actuel": reste,
            'next': next
        })
