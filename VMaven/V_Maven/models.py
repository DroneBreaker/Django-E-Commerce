from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.manager import ManagerDescriptor
from django.urls import reverse


# Create your models here.
# class Customer(models.Model):
#     first_name = models.CharField(max_length=90)
#     last_name = models.CharField(max_length=90)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     address = models.CharField(max_length=50)

#     def __str__(self):
#         return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('V_Maven:category_list', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField(upload_to='images/', blank=False)
    discount_price = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    slug = models.SlugField()
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('V_Maven:product_detail', args=[self.slug])


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    products = models.ManyToManyField(OrderItem)
    start_date = models.DateField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)