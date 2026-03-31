from decimal import Decimal
from store.models import Product, Collection, Review
from rest_framework import serializers

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        field = ['id','title','products_count']

    products_count = serializers.IntegerField(read_only = True)


class  ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields  = ['id', 'title','description','slug', 'inventory','unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name='calculated_tax')
    

    def calculated_tax(tax, product:Product):
        return product.unit_price * Decimal(1.1)
    

class ReviewSerializer(serializers.ModelSerializer):
    class meta:
        model = Review
        fields = ['id','data','name','description','product']
