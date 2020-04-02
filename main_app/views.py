from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from main_app.models import *
from main_app.forms import EmailForm


class HomeView(ListView):
    model = Product
    template_name = 'main_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['slides'] = Slide.objects.all().order_by('index')
        context['new_products_slice'] = Product.objects.filter(is_new=True).order_by('-pk')[:8]
        context['sale_products_slice'] = Product.objects.filter(discount_percent__gt=0).order_by('-pk')[:8]
        context['popular_brands_slice'] = Brand.objects.order_by('?')[:12]
        context['page_descriptions'] = CommonPageDescription.objects.filter(page_name='Главная')

        keywords_obj = CommonPageDescription.objects.filter(
            page_name='Главная',
            keywords__isnull=False
        ).first()
        if keywords_obj:
            context['meta_keywords'] = keywords_obj.keywords
        else:
            context['meta_keywords'] = None

        desc_obj = CommonPageDescription.objects.filter(
            page_name='Главная',
            meta_description__isnull=False
        ).first()
        if desc_obj:
            context['meta_description'] = desc_obj.meta_description
        else:
            context['meta_description'] = None

        return context


class ProductView(DetailView):
    model = Product
    template_name = 'main_app/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['similar_products'] = Product.objects.filter(
            category=self.object.category
        ).order_by('?').exclude(slug=self.object.slug)[:4]
        return context


class AllProductsView(ListView):
    model = Product
    paginate_by = 4
    context_object_name = 'all_products_list'
    template_name = 'main_app/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_descriptions'] = CommonPageDescription.objects.filter(page_name='Каталог')

        keywords_obj = CommonPageDescription.objects.filter(
            page_name='Каталог',
            keywords__isnull=False
        ).first()
        if keywords_obj:
            context['meta_keywords'] = keywords_obj.keywords
        else:
            context['meta_keywords'] = None

        desc_obj = CommonPageDescription.objects.filter(
            page_name='Каталог',
            meta_description__isnull=False
        ).first()
        if desc_obj:
            context['meta_description'] = desc_obj.meta_description
        else:
            context['meta_description'] = None

        return context


class ProductsCategoryView(ListView):
    model = Product
    paginate_by = 4
    template_name = 'main_app/products_category.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_title'] = Category.objects.filter(slug=self.kwargs['slug']).first().name
        context['page_description'] = Category.objects.filter(slug=self.kwargs['slug']).first().description

        keywords_obj = Category.objects.filter(
            slug=self.kwargs['slug'],
            keywords__isnull=False
        ).first()
        if keywords_obj:
            context['meta_keywords'] = keywords_obj.keywords
        else:
            context['meta_keywords'] = None

        desc_obj = Category.objects.filter(
            slug=self.kwargs['slug'],
            meta_description__isnull=False
        ).first()
        if desc_obj:
            context['meta_description'] = desc_obj.meta_description
        else:
            context['meta_description'] = None

        return context


class BrandsView(ListView):
    model = Brand
    paginate_by = 6
    template_name = 'main_app/brands.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_descriptions'] = CommonPageDescription.objects.filter(page_name='Бренды')

        keywords_obj = CommonPageDescription.objects.filter(
            page_name='Бренды',
            keywords__isnull=False
        ).first()
        if keywords_obj:
            context['meta_keywords'] = keywords_obj.keywords
        else:
            context['meta_keywords'] = None

        desc_obj = CommonPageDescription.objects.filter(
            page_name='Бренды',
            meta_description__isnull=False
        ).first()
        if desc_obj:
            context['meta_description'] = desc_obj.meta_description
        else:
            context['meta_description'] = None

        return context


class BrandProductsView(ListView):
    model = Product
    paginate_by = 4
    template_name = 'main_app/brand_products.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(brand__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_title'] = Brand.objects.filter(slug=self.kwargs['slug']).first().name
        context['page_description'] = Brand.objects.filter(slug=self.kwargs['slug']).first().description

        keywords_obj = Brand.objects.filter(
            slug=self.kwargs['slug'],
            keywords__isnull=False
        ).first()
        if keywords_obj:
            context['meta_keywords'] = keywords_obj.keywords
        else:
            context['meta_keywords'] = None

        desc_obj = Brand.objects.filter(
            slug=self.kwargs['slug'],
            meta_description__isnull=False
        ).first()
        if desc_obj:
            context['meta_description'] = desc_obj.meta_description
        else:
            context['meta_description'] = None

        return context


class SaleView(ListView):
    model = Product
    paginate_by = 4
    template_name = 'main_app/sale.html'

    def get_queryset(self):
        return Product.objects.filter(discount_percent__gt=0).order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_descriptions'] = CommonPageDescription.objects.filter(page_name='Распродажа')

        keywords_obj = CommonPageDescription.objects.filter(
            page_name='Распродажа',
            keywords__isnull=False
        ).first()
        if keywords_obj:
            context['meta_keywords'] = keywords_obj.keywords
        else:
            context['meta_keywords'] = None

        desc_obj = CommonPageDescription.objects.filter(
            page_name='Распродажа',
            meta_description__isnull=False
        ).first()
        if desc_obj:
            context['meta_description'] = desc_obj.meta_description
        else:
            context['meta_description'] = None

        return context


class NewView(ListView):
    model = Product
    paginate_by = 4
    template_name = 'main_app/new_products.html'

    def get_queryset(self):
        return Product.objects.filter(is_new=True).order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['page_descriptions'] = CommonPageDescription.objects.filter(page_name='Новинки')

        keywords_obj = CommonPageDescription.objects.filter(
            page_name='Новинки',
            keywords__isnull=False
        ).first()
        if keywords_obj:
            context['meta_keywords'] = keywords_obj.keywords
        else:
            context['meta_keywords'] = None

        desc_obj = CommonPageDescription.objects.filter(
            page_name='Новинки',
            meta_description__isnull=False
        ).first()
        if desc_obj:
            context['meta_description'] = desc_obj.meta_description
        else:
            context['meta_description'] = None

        return context


def contacts_view(request):
    page_descriptions = CommonPageDescription.objects.filter(page_name='Контакты')
    contacts_phones = ContactPhone.objects.all()
    contacts_emails = ContactEmail.objects.all()

    keywords_obj = CommonPageDescription.objects.filter(
        page_name='Контакты',
        keywords__isnull=False
    ).first()
    if keywords_obj:
        meta_keywords = keywords_obj.keywords
    else:
        meta_keywords = None

    desc_obj = CommonPageDescription.objects.filter(
        page_name='Контакты',
        meta_description__isnull=False
    ).first()
    if desc_obj:
        meta_description = desc_obj.meta_description
    else:
        meta_description = None

    context = {
        'page_descriptions': page_descriptions,
        'contacts_phones': contacts_phones,
        'contacts_emails': contacts_emails,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description,
    }

    return render(request, 'main_app/contacts.html', context)


def delivery_view(request):
    page_descriptions = CommonPageDescription.objects.filter(page_name='Доставка')

    keywords_obj = CommonPageDescription.objects.filter(
        page_name='Доставка',
        keywords__isnull=False
    ).first()
    if keywords_obj:
        meta_keywords = keywords_obj.keywords
    else:
        meta_keywords = None

    desc_obj = CommonPageDescription.objects.filter(
        page_name='Доставка',
        meta_description__isnull=False
    ).first()
    if desc_obj:
        meta_description = desc_obj.meta_description
    else:
        meta_description = None

    context = {
        'page_descriptions': page_descriptions,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description,
    }

    return render(request, 'main_app/delivery.html', context)


def price_list_view(request):
    price_list_emails = ContactEmail.objects.all()

    return render(request, 'main_app/price-list.html', {'price_list_emails': price_list_emails})


def search_view(request):
    products_list = Product.objects.none()
    query = request.GET.get('q')
    if query:
        products_list = Product.objects.filter(
            Q(name__icontains=query) |
            Q(brand__name__icontains=query)
        ).distinct()

    paginator = Paginator(products_list, 4)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products
    }
    return render(request, "main_app/search.html", context)


def successful_subscription_view(request):
    return render(request, 'main_app/successful_subscription.html')


class UserEmailCreateView(CreateView):
    model = UserEmail

    def post(self, request, *args, **kwargs):
        bound_form = EmailForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('main_app:successful_subscription')
