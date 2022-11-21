from product.models import Product
from rest_framework.serializers import ModelSerializer

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        field = '__all__'


        