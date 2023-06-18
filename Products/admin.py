from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'price', 'quantity')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"cat_slug": ("name",)}

class InfoUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_old')
    list_display_links = ('id', )

admin.site.register(Product, ProductAdmin)
admin.site.register(UserDetail, InfoUserAdmin)
admin.site.register(Category, CategoryAdmin)
