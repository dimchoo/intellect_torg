from django.urls import path
from main_app.views import *

app_name = 'main_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('sale/', SaleView.as_view(), name='sale'),
    path('delivery/', delivery_view, name='delivery'),
    path('contacts/', contacts_view, name='contacts'),
    path('price-list/', price_list_view, name='price_list'),

    path('products/all/', AllProductsView.as_view(), name='all_products'),
    path('products/search/', search_view, name='search'),
    path('products/category/<str:slug>/', ProductsCategoryView.as_view(), name='products_category'),
    path('products/product/<str:slug>/', ProductView.as_view(), name='product'),

    path('brands/all/', BrandsView.as_view(), name='all_brands'),
    path('brands/products/<str:slug>/', BrandProductsView.as_view(), name='brand_products'),
    path('successful-subscription/', successful_subscription_view, name='successful_subscription'),
    path('for-subscribe/', UserEmailCreateView.as_view(), name='for_subscribe'),
]