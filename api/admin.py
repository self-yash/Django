from django.contrib import admin
from api.models import Order, OrderItem

# Register your models here.

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemAdmin
    ]

admin.site.register(Order,OrderAdmin)