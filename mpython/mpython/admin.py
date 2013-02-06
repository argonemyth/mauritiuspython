# We will register django-easy-maps's AddressAdmin here
from django.contrib import admin
from easy_maps.models import Address
from easy_maps.admin import AddressAdmin

admin.site.register(Address, AddressAdmin)
