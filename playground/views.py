from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.
# request -> response
# request handler
# action



'''def say_hello(request):
    product = Product.objects.filter(pk=1).first()  # alternatively also 
    # pexists = Product.objects.filter(pk=1).exists()
alternatively use 
    try: # if  a product  is non existent you  can use the  try catch method or the  above
        product = Product.objects.get(pk=1) 
    except ObjectDoesNotExist:
        pass
    
    return render(request, 'hello.html', {'name' :'kagechi'})
'''

# filtering 
def say_hello(request):
    queryset = Product.objects.filter(unit_price__range=(20,30))
    return render(request, 'hello.html', {'name' :'kagechi', 'product':list(queryset)})
