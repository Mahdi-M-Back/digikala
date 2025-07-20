from django.contrib import admin
from .models import ShippingAddress, Order,OrderIthem


admin.site.register(ShippingAddress)
#admin.site.register(Order)
admin.site.register(OrderIthem)

class OrderItemInLine(admin.TabularInline):
    model = OrderIthem
    extra = 0

@admin.register(Order)
class OrederAdmin(admin.ModelAdmin):
    readonly_fields = ['date_ordered' , 'last_update']
    inlines = [OrderItemInLine]