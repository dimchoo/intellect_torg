from django.urls import path
from main_app.views import *

app_name = 'main_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sale/', SaleView.as_view(), name='sale'),
    path('delivery/', delivery_view, name='delivery'),
    path('contacts/', contacts_view, name='contacts'),
    path('price-list/', price_list_view, name='price_list'),
    path('products/product/<int:pk>/', ProductView.as_view(), name='product'),
    path('products/all/', AllProductsView.as_view(), name='all_products'),
    path('products/<slug>/', ProductsCategoryView.as_view(), name='products_category'),
    path('brands/all/', BrandsView.as_view(), name='all_brands'),
]
