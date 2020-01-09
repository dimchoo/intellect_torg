from django.urls import path
from main_app.views import HomeView, ProductView

app_name = 'main_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/product/<int:pk>/', ProductView.as_view(), name='product')
]
