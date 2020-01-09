from main_app.models import Category, Brand, ContactPhone


def categories_processor(request):
    return {'menu_categories': Category.objects.all()}


def brands_processor(request):
    return {'menu_brands': Brand.objects.order_by('name')[:15]}


def contact_phones_processor(request):
    return {'menu_contact_phones': ContactPhone.objects.order_by('pk')[:2]}
