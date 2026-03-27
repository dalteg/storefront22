from django.shortcuts import render
from django.db import connection
from store.models import OrderItem, Product, Order, Product, Customer, Collection


def say_hello(request):
    cursot = connection.cursor()
    cursor
    queryset = Product.objects.raw('SELECT * FROM store_product')
    return render(request, 'hello.html', {'name': 'Mugendi', 'result':list(queryset)})