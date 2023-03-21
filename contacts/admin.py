from django.contrib import admin
from .models import Contacts
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'listing', 'phone')
    list_filter = ('listing', 'name')
    list_display_links = ('id', 'name', 'message', 'phone')


admin.site.register(Contacts, ContactAdmin)
