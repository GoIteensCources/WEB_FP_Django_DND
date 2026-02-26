from django.contrib import admin
from .models import Profile, Address


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    raw_id_fields = ('user', 'address')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'country', 'postal_code')
    list_filter = ('country',)
