# Generated by Django 2.2.7 on 2020-02-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='meta_description',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Мета-описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Мета-описание'),
        ),
        migrations.AddField(
            model_name='commonpagedescription',
            name='meta_description',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Мета-описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Мета-описание'),
        ),
    ]