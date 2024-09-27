from django.db import models


class Shop(models.Model):
    shopid = models.AutoField(primary_key=True,editable=False)
    shopname= models.CharField(max_length=300)
    def __str__(self):
        return self.shopname

class Gst(models.Model):
    gstid= models.AutoField(primary_key=True,editable=False)
    gstpercentage=models.CharField(max_length=300)
    def __str__(self):
        return self.gstpercentage

class Product(models.Model):
    productid = models.AutoField(primary_key=True, editable=False)
    productcode = models.CharField(max_length=300)
    productname = models.CharField(max_length=250)
    quantity = models.IntegerField()
    stockcount = models.IntegerField()
    purchasingdate=models.DateField()
    purchasingprice = models.DecimalField(max_digits=10, decimal_places=2)
    gst=models.ForeignKey(Gst,on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE) 
    def __str__(self):
        return self.productname

    

