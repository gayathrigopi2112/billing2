from rest_framework import serializers
from .models import Product,Gst,Shop

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'




    

    