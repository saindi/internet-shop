from django.contrib import admin
from catalog.models import ProductModel, CategoryModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = "slug", "name", "category_id", "amount", "available"
    list_editable = "amount", "available"
    list_filter = "category_id", "amount", "price"
    prepopulated_fields = {
        "slug": ["name"],
    }


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = "slug", "name", "description"
    prepopulated_fields = {
        "slug": ["name"],
    }