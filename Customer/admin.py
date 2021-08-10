from django.contrib import admin

from .models import Cart
admin.site.register(Cart)

from .models import Customer
admin.site.register(Customer)