from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main_app.models import Slide, Product, Brand


class HomeView(ListView):
    model = Product
    template_name = 'main_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['slides'] = Slide.objects.all().order_by('index')
        context['new_products_slice'] = Product.objects.filter(type='New').order_by('-pk')[:8]
        context['sale_products_slice'] = Product.objects.filter(type='Sale').order_by('-pk')[:8]
        context['popular_brands_slice'] = Brand.objects.order_by('?')[:12]
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'main_app/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['similar_products'] = Product.objects.filter(
            category=self.object.category
        ).order_by('?').exclude(pk=self.object.pk)[:4]
        return context
