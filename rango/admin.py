from django.contrib import admin
from rango.models import Category, Page


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Category)
admin.site.register(Page, PageAdmin)
# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
