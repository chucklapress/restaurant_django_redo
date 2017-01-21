from django.contrib import admin
from app.models import Menu, Employee, Order, Check, Menu_Item, DrinkOptions, OpenTicket

# Register your models here.
admin.site.register(Menu)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Check)
admin.site.register(Menu_Item)
admin.site.register(DrinkOptions)
admin.site.register(OpenTicket)
