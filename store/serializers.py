from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        field = ['id','title']


class  ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields  = ['id', 'title','unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name='calculated_tax')
    

    def calculated_tax(tax, product:Product):
        return product.unit_price * Decimal(1.1)