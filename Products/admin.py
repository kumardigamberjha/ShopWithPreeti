from django.contrib import admin
from .models import ProductModel, ProdBadge, Category, SubCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProdBadge)
admin.site.register(ProductModel)
