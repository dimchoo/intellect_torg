from django.db import models


class File(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32, unique=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-pk']
