from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main_app.models import Slide, Product, Brand, CommonPageDescription, ContactPhone, ContactEmail


class HomeView(ListView):
    model = Product
    template_name = 'main_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['slides'] = Slide.objects.all().order_by('index')
        context['new_products_slice'] = Product.objects.filter(type='New').order_by('-pk')[:8]
        context['sale_products_slice'] = Product.objects.filter(type='Sale').order_by('-pk')[:8]
        context['popular_brands_slice'] = Brand.objects.order_by('?')[:12]
        context['page_descriptions'] = CommonPageDescription.objects.filter(page_name='Главная')
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


class AllProductsView(ListView):
    model = Product
    paginate_by = 4
    context_object_name = 'all_products_list'
    template_name = 'main_app/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_descriptions'] = CommonPageDescription.objects.filter(page_name='Каталог')
        return context


class ProductsCategoryView(ListView):
    model = Product
    paginate_by = 4
    template_name = 'main_app/products_category.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_title'] = Product.objects.filter(
            category__slug=self.kwargs['slug']
        ).first().category.name
        context['page_description'] = Product.objects.filter(
            category__slug=self.kwargs['slug']
        ).first().category.description
        return context


class SaleView(ListView):
    model = Product
    paginate_by = 4
    template_name = 'main_app/sale.html'

    def get_queryset(self):
        return Product.objects.filter(type='Sale').order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_descriptions'] = CommonPageDescription.objects.filter(page_name='Распродажа')
        return context


def contacts_view(request):
    page_descriptions = CommonPageDescription.objects.filter(page_name='Контакты')
    contacts_phones = ContactPhone.objects.all()
    contacts_emails = ContactEmail.objects.all()

    context = {
        'page_descriptions': page_descriptions,
        'contacts_phones': contacts_phones,
        'contacts_emails': contacts_emails,
    }

    return render(request, 'main_app/contacts.html', context)


def delivery_view(request):
    page_descriptions = CommonPageDescription.objects.filter(page_name='Доставка')

    return render(request, 'main_app/delivery.html', {'page_descriptions': page_descriptions})


def price_list_view(request):
    price_list_emails = ContactEmail.objects.all()

    return render(request, 'main_app/price-list.html', {'price_list_emails': price_list_emails})


class BrandsView(ListView):
    model = Brand
    paginate_by = 6
    template_name = 'main_app/brands.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_descriptions'] = CommonPageDescription.objects.filter(page_name='Бренды')
        return context

