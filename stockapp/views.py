from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializer import ProductSerializer
from .models import Product
from twilio.rest import Client
from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes
import random
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
from io import BytesIO
from django.contrib.staticfiles import finders
import os
from datetime import datetime
from django.utils import timezone
from django.core.files.storage import default_storage as storage
from django.core.mail import EmailMessage


#get all products
@api_view(['GET'])
def getAllProducts(request):
    allproducts = Product.objects.all()
    serializer = ProductSerializer(allproducts,many=True)
    return Response(serializer.data)

#get products using their id
@api_view(['GET'])
def filterProduct(request,id):
    try:
        product = get_object_or_404(Product,productid=id)
        serializer= ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": str(e)},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#post a product 
@api_view(['POST'])
def addNewProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.save()
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update a product
@api_view(['PUT'])
def updateProduct(request,id):
    try:
        product = Product.objects.get(productid=id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        updated_product = serializer.save()
        updated_product_serializer = ProductSerializer(updated_product)
        return Response(updated_product_serializer.data, status=status.HTTP_200_OK) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteProduct(request,id):
    try:
        product = Product.objects.get(productid=id)
        product.delete()
        return Response({'message':'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({'error':'Product not found'}, status=status.HTTP_404_NOT_FOUND)




