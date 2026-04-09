from django.urls import path
from django.urls.conf import include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from . import views



router =  routers.DefaultRouter()
router.register('products',views.ProductViewSet, basename='products-detail')
router.register('collections',views.CollectionViewSet)
router.register('carts',views.CartViewset)
router.register('customers',views.CustomerViewSet)

products_router = routers.NestedDefaultRouter(router,'products', lookup = 'product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup = 'cart')
carts_router.register('items', views.ClassItemViewSet, basename= 'cart-items')


# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls