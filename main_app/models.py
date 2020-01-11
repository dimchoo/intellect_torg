from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Slide(models.Model):
    image = models.ImageField(verbose_name='Изображение слайда', upload_to='slides')
    title = models.CharField(verbose_name='Заголовок слайда', max_length=64)
    index = models.SmallIntegerField(verbose_name='Индекс')
    description = models.CharField(verbose_name='Описание слайда', max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Карусель'


class Brand(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32, unique=True)
    slug = models.SlugField(verbose_name='Строка в браузере', max_length=32, unique=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='brands')
    description = RichTextUploadingField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32, unique=True)
    slug = models.SlugField(verbose_name='Строка в браузере', max_length=32, unique=True)
    description = RichTextUploadingField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=80, unique=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='products')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='Бренд', on_delete=models.CASCADE)
    _TYPE_CHOICES = (
        ('Base', 'Base'),
        ('New', 'New'),
        ('Sale', 'Sale'),
    )
    type = models.CharField(verbose_name='Тип', max_length=4, choices=_TYPE_CHOICES, default='Base')
    old_price = models.DecimalField(verbose_name='Старая цена', max_digits=6, decimal_places=2, blank=True, null=True)
    new_price = models.DecimalField(verbose_name='Новая цена', max_digits=6, decimal_places=2, default=0)
    _STATUS_CHOICES = (
        ('В наличии', 'В наличии'),
        ('Ожидается', 'Ожидается'),
        ('Нет в наличии', 'Нет в наличии'),
    )
    status = models.CharField(verbose_name='Статус', max_length=14, choices=_STATUS_CHOICES, default='В наличии')
    in_box = models.CharField(verbose_name='В коробке', max_length=32)
    in_pallet = models.CharField(verbose_name='В паллете', max_length=32)
    description = RichTextUploadingField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class CommonPageDescription(models.Model):
    _PAGE_CHOICES = (
        ('Главная', 'Главная'),
        ('Каталог', 'Каталог'),
        ('Бренды', 'Бренды'),
        ('Распродажа', 'Распродажа'),
        ('Доставка', 'Доставка'),
        ('Контакты', 'Контакты'),
    )
    page_name = models.CharField(
        verbose_name='Название страницы',
        max_length=14,
        choices=_PAGE_CHOICES,
        default='Главная'
    )
    description = RichTextUploadingField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return 'Описание страницы "{}"'.format(self.page_name)

    class Meta:
        verbose_name = 'Описание страницы'
        verbose_name_plural = 'Описания основных страниц'


class ContactEmail(models.Model):
    email = models.CharField(verbose_name='Email', max_length=128)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Контактные почтовые адреса (Email)'


class ContactPhone(models.Model):
    phone = models.CharField(verbose_name='Номер вида +71234567890', max_length=12)
    readable_phone = models.CharField(verbose_name='Этот же номер вида +7(123) 456-78-90', max_length=20)

    def __str__(self):
        return self.readable_phone

    class Meta:
        verbose_name = 'Контактный номер телефона'
        verbose_name_plural = 'Контактные номера телефонов'


class UserEmail(models.Model):
    email = models.EmailField(verbose_name='Email', max_length=180)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка на рассылку'
        verbose_name_plural = 'Подписки на рассылку'
