from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models import Sum
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
    
class Seed(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(unique= True, max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def __str__(self):
        return f"{self.name}"
    
    def total_sale_stock(self):
        sales_stock = Sale.objects.filter(item=self).aggregate(
            total_stock=Sum('quantity_kg')
        )['total_stock']
        return sales_stock or 0

    def total_purchase_stock(self):
        purchase_stock = Purchase.objects.filter(item=self).aggregate(
            total_stock=Sum('total_kg')
        )['total_stock']
        return purchase_stock or 0

    def total_sales_amount(self):
        # Calculate the total sales amount for this seed
        total_sales = Sale.objects.filter(item=self).aggregate(
            total_amount=Sum('amount')
        )['total_amount']
        return total_sales or 0

    def total_purchase_amount(self):
        # Calculate the total purchase amount for this seed
        total_purchases = Purchase.objects.filter(item=self).aggregate(
            total_amount=Sum('amount')
        )['total_amount']
        return total_purchases or 0
    

class Purchase(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Seed, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=False,null=True)
    quantity_mn = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=0)
    packing = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=0)
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=0) # remove this field
    total_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_40kg = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    loss = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    loss_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    left_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vehicle = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return f"{self.user} - {self.item} - {self.date}"
    

class Sale(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Seed, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=False,null=True)
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=0)
    quantity_mn = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    commission = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vehicle = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.item} - {self.date}"