from django import forms
from .models import Supplier, Item


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'address', 'contact_person', 'contact_number']
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'amount', 'unit_measurement']