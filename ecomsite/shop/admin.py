from django.contrib import admin
from .models import Product, Order

# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Shopping online"
admin.site.register(Product)
admin.site.register(Order)
