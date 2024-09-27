from django.urls import path
from . import views
from .views import *

urlpatterns = [
    #getAllProducts
    path('getallproducts', views.getAllProducts, name='getallproducts'),
    #getProductUsingTheirid
    path('getproduct/<int:id>/',views.filterProduct,name='getProduct'),
    #addNewProduct
    path('addnewproduct',views.addNewProduct,name='addnewproduct'),
    #updateProduct
    path('updateproduct/<int:id>/',views.updateProduct,name='updateproduct'),
    #deleteProduct
    path('deleteproduct/<int:id>/',views.deleteProduct,name='deleteproduct')

]
