from django.contrib import admin

from .models import Device, Product, Status

admin.site.register(Device)
admin.site.register(Product)
admin.site.register(Status)