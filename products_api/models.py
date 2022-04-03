from django.core.validators import FileExtensionValidator
from django.db import models
import os
from time import gmtime, strftime

from profiles_api.models import UserProfile


def upload_to_category(instance, filename):
    file_extension = os.path.splitext(filename)[1]
    str_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return 'category/{category}/{filename}+{str_time}{ext}' \
        .format(
            category=instance.name,
            filename=instance.name,
            str_time=str_time,
            ext=file_extension)


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='upload_to_category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


def upload_to_product(instance, filename):
#
    file_extension = os.path.splitext(filename)[1]
    str_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    return 'products/{product_name}/{filename}+{str_time}{ext}'\
        .format(
                product_name=instance.name,
                filename=instance.name,
                str_time=str_time,
                ext=file_extension)


class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image1 = models.FileField(null=True, blank=True, upload_to=upload_to_product, validators=[FileExtensionValidator(['png', 'jpg', 'svg', 'jpeg'])])
    image2 = models.FileField(null=True, blank=True, upload_to=upload_to_product, validators=[FileExtensionValidator(['png', 'jpg', 'svg', 'jpeg'])])
    image3 = models.FileField(null=True, blank=True, upload_to=upload_to_product, validators=[FileExtensionValidator(['png', 'jpg', 'svg', 'jpeg'])])
    price = models.IntegerField()
    stock = models.IntegerField(blank=True, null=True,)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # print("Available : ", available)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

