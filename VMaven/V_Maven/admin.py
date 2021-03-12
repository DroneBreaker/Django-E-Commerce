from django.contrib import admin
from .models import Category, Product

# Register your models here.
# admin.site.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity', 
        'in_stock', 'created', 'created_by', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #specify fiels that get populated
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)