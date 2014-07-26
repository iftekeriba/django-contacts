from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'nid', 'email')
    search_fields = ['first_name', 'last_name', 'nid']


admin.site.register(Contact, ContactAdmin)