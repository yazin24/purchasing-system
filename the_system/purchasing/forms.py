from django import forms
from .models import Supplier, Item


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'supplier_address', 'contact_person', 'contact_number']
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_amount', 'unit_mesaurement']