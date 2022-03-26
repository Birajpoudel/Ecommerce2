from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(slider)
admin.site.register(Banner)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Subcategory)

class Product_Images(admin.TabularInline):
    model = Product_Image

class Additional_Informations(admin.TabularInline):
    model = Additional_Information

class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images, Additional_Informations)
    list_display = ('Product_name','Price','Categories','section')
    list_editable = ('Categories','section')


admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)
