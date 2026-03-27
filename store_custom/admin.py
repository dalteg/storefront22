from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem



class TagInline(GenericTabularInline):
    autocomplete_fields =['tag']
    model = TaggedItem


class  CustomProductAdnin(ProductAdmin):
    inlines =[TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdnin)