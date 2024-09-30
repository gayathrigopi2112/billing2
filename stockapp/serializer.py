from rest_framework import serializers
from .models import Product,Gst,Shop,Purchaseproduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'

class PurchaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchaseproduct
        fields ='__all__'

