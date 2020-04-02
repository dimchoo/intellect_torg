from main_app.models import Category, Brand, ContactPhone, ShopPartner
from main_app.forms import EmailForm

from datetime import datetime as dt


def categories_processor(request):
    return {'menu_categories': Category.objects.all()}


def brands_processor(request):
    return {'menu_brands': Brand.objects.order_by('name')[:15]}


def contact_phones_processor(request):
    return {'menu_contact_phones': ContactPhone.objects.order_by('pk')[:2]}


def subscribe_form_processor(request):
    return {'subscribe_form': EmailForm()}


def shop_partners_processor(request):
    return {'shop_partners': ShopPartner.objects.all()[:7]}


def year_processor(request):
    return {'year_now': dt.now().year}
