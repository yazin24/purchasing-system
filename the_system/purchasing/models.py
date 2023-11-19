from django.db import models


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    
    items_suppliers = models.ManyToManyField('Item', related_name='suppliers_supplier')
    

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    unit_measurement = models.CharField(max_length=20)
    
    suppliers = models.ManyToManyField('Supplier', related_name='supplier_items')