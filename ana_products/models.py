from django.db import models
import os
from django.db.models import Q
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.

LABEL_CHOICES = (
    ('موجود', 'موجود'),
    ('ناموجود', 'ناموجود'),
)


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    if instance.id is not None:
        final_name = f"{instance.id}-{instance.title}{ext}"
    else:
        myvar = Product.objects.all()
        myvar = len(list(myvar))
        if myvar == 0:
            final_name = f"1-{instance.title}{ext}"
        else:
            max_last_product_id = Product.objects.latest('id').id
            final_name = f"{max_last_product_id + 1}-{instance.title}{ext}"

    return f'products_img/{final_name}'


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(default=None)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def get_absolute_url(self):
        return f"/category-{self.slug}"

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name='subcategory')

    def __str__(self):
        return self.title


# this class is a model manager for product model(because we instaciated only in product model)
class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_product_by_title(self, my_title):
        qs = self.get_queryset().filter(title=my_title)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField(default=None)
    discount_price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name='products')
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True, related_name='products')
    label = models.CharField(choices=LABEL_CHOICES, default='M', max_length=8)
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=True)

    objects = ProductsManager()

    def get_absolute_url(self):
        return f"/product/{self.title.replace(' ', '-')}"

    def __str__(self):
        return self.title


def cat_subcat_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(cat_subcat_pre_save_receiver, sender=Category)
pre_save.connect(cat_subcat_pre_save_receiver, sender=SubCategory)


# for product detail gallery carousel
class Images(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name='images')
    mini_image = models.ImageField(upload_to='products_img/', blank=True)


class Comment(models.Model):
    writer_name = models.CharField(max_length=80)
    body = models.TextField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.writer_name


class Answer(models.Model):
    writer_name = models.CharField(max_length=80)
    body = models.TextField(max_length=150)
    reply_to = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='answers')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.writer_name

