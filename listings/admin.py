from django.contrib import admin
from .models import Listings

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','realtor','price','bedrooms')
    list_display_links=('id','title')
    list_per_page =25
    list_editable=('is_published',)
    list_filter=('realtor',)
    search_fields=('title','zipcode','address','city','state')

# Register your models here.
admin.site.register(Listings,ListingsAdmin)
