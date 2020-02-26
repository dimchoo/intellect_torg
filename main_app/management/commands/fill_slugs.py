from django.core.management import BaseCommand
from django.template.defaultfilters import slugify

from main_app.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = Product.objects.all()
        for product in products:
            product.slug = slugify(product.name)
            product.save()

        print('Done!')
