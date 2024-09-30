from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializer import ProductSerializer,PurchaseProductSerializer
from .models import Product,Purchaseproduct
from rest_framework.decorators import api_view, permission_classes


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

#delete a product
@api_view(['DELETE'])
def deleteProduct(request,id):
    try:
        product = Product.objects.get(productid=id)
        product.delete()
        return Response({'message':'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({'error':'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
#purchase a product
@api_view(['POST'])
def purcahseProduct(request):
    product_id = request.data.get('productid')
    quantity_to_pruchase = request.data.get('quantity')

    try:
        product = Product.objects.get(productid=product_id)
        if product.quantity >= quantity_to_pruchase:
            purchase_record = Purchaseproduct.objects.create(
                productid=product,
                quantity=quantity_to_pruchase
            )
            product.quantity -= quantity_to_pruchase
            product.save()
            serializer = PurchaseProductSerializer(purchase_record)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Not enough stock available"}, status=status.HTTP_400_BAD_REQUEST) 
        
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
#




