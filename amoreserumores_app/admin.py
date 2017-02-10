from django.contrib import admin
from .models import Catalog, CatalogCategory, Product, ProductAttribute, ProductDetail
# Register your models here.

@admin.register(Catalog, CatalogCategory, Product, ProductAttribute, ProductDetail)
class DefaultAdmin(admin.ModelAdmin):
    pass