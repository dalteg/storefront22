from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Collection, OrderItem, Product
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer
from django.db.models import Count

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request':self.request}
    
    def  destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count()>0:
            return Response({'error':'product cannot  be  delete '
        'bacause it is  associated with order item.'},
        status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request,*self.args,**kwargs)
    



class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count()>0:
            return Response({'error':'Collection cannot be delete '
        'bacause it is  associated with one or more products.'},
        status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request,*self.args,**kwargs)

class  ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serelizer_class = ReviewSerializer

