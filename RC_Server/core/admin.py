from django.contrib import admin

# Register your models here.
from core.models import Seller, Product


class SellerAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Seller, SellerAdmin)
admin.site.register(Product)
