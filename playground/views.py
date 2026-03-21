from itertools import product

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order



def say_hello(request):
    result = Product.objects.aggregate(Count('id'))
    return render(request, 'hello.html', {'result': result})