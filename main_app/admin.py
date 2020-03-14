from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from main_app.models import *


class AdminSlide(admin.ModelAdmin):
    fields = [
        'image',
        'model_image_tag',
        'title',
        'index',
        'description',
    ]

    def get_fields(self, request, obj=None):
        fields = list(super(AdminSlide, self).get_fields(request, obj))
        exclude_set = set()
        if not obj:
            exclude_set.add('model_image_tag')
        return [field for field in fields if field not in exclude_set]

    readonly_fields = ('model_image_tag',)
    list_display = ['image_tag', 'title', 'index']
    list_display_links = ['image_tag', 'title']
    ordering = ['-pk', ]
    search_fields = ['title', ]


class AdminBrand(admin.ModelAdmin):
    fields = [
        'name',
        'slug',
        'image',
        'model_image_tag',
        'description',
        'keywords',
        'meta_description',
    ]

    def get_fields(self, request, obj=None):
        fields = list(super(AdminBrand, self).get_fields(request, obj))
        exclude_set = set()
        if not obj:
            exclude_set.add('model_image_tag')
        return [field for field in fields if field not in exclude_set]

    readonly_fields = ('model_image_tag', )
    list_display = ['image_tag', 'name', 'slug']
    list_display_links = ['image_tag', 'name']
    ordering = ['-pk', ]
    search_fields = ['name', 'slug']


class AdminCategory(admin.ModelAdmin):
    ordering = ['-pk', ]
    search_fields = ['name', 'slug']


class AdminProduct(admin.ModelAdmin):
    fields = [
        'name',
        'image',
        'model_image_tag',
        'category',
        'brand',
        'model_brand_image_tag',
        'price',
        'discount_percent',
        'is_new',
        'status',
        'in_box',
        'in_pallet',
        'description',
        'keywords',
        'meta_description',
    ]

    def get_fields(self, request, obj=None):
        fields = list(super(AdminProduct, self).get_fields(request, obj))
        exclude_set = set()
        if not obj:
            exclude_set.add('model_image_tag')
            exclude_set.add('model_brand_image_tag')
        return [field for field in fields if field not in exclude_set]

    readonly_fields = ('model_image_tag', 'model_brand_image_tag', )
    list_display = ['image_tag', 'name', 'brand_image_tag', 'category', 'price']
    list_display_links = ['image_tag', 'name']
    list_filter = ['category', 'brand', 'is_new']
    search_fields = ['name', 'category__name', 'brand__name']
    ordering = ['-pk', ]


admin.site.register(Slide, AdminSlide)
admin.site.register(Brand, AdminBrand)
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(CommonPageDescription)
admin.site.register(ContactEmail)
admin.site.register(ContactPhone)
admin.site.register(ShopPartner)


@admin.register(UserEmail)
class UserEmailAdmin(ImportExportModelAdmin):
    search_fields = ['email', ]
