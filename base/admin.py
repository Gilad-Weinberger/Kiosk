from django.contrib import admin
from .models import Order, RabbiOrderBurgers, RabbiOrderHotdogs

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'food', 'pay')
    list_filter = ('food', 'pay')
    search_fields = ('name', 'food', 'pay')

admin.site.register(Order, OrderAdmin)
admin.site.register(RabbiOrderBurgers)
admin.site.register(RabbiOrderHotdogs)