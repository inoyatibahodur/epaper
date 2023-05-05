from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer

class ProductView(APIView):
    def get(self, request):
        productes = Product.objects.all()        
        serializer = ProductSerializer(productes, many=True)
        return Response({"productes": serializer.data})

    def post(self, request):
        product = request.data.get('productes')        
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(product_saved.title)})

