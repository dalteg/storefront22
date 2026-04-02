from decimal import Decimal
from store.models import Cart, Product, Collection, Review
from rest_framework import serializers

class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only = True)
    class Meta:
        model = Collection
        fields = ['id','title','products_count']



class  ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields  = ['id', 'title','description','slug', 'inventory','unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name='calculated_tax')
    

    def calculated_tax(tax, product:Product):
        return product.unit_price * Decimal(1.1)
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','name','description']
    
    def create(self, validated_data):
        product_id =  self.context['product_id']
        return Review.objects.create(Product_id = product_id, **validated_data)


class CartSerializer(serializers.ModelSerializer):
    id  =  serializers.UUIDField(read_only = True)
    class Meta:
        model = Cart
        fields = ['id', 'items']