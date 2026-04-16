from django.contrib import admin

# Register your models here.

from .models import Supplier
admin.site.register(Supplier)

from .models import WaterBottle
admin.site.register(WaterBottle)


