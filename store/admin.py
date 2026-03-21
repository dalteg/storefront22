from django.contrib import admin
from. import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10
    
    @admin.display(ordering ='inventory')
    def inventory_status(self, Product):
        if Product.inventory <10:
            return 'Low'
        return 'OK'

# Register your models here.
admin.site.register(models.Collection)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name','last_name']
    list_per_page = 10
    