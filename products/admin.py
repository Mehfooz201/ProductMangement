from django.contrib import admin
from .models import Product, Category


admin.site.register(Category)


# Register your models here
@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'is_published', 'created_at']
    list_display_links = ['id', 'name']
    list_filter = ['price']
    # list_editable = ['is_published']
    search_fields = ['name', 'price']
