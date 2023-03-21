from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','is_mvp','email','phone')
    list_editable=('is_mvp',)
    list_display_links=('id','name')
    list_per_page=25
    search_fields=('name',)

# Register your models here.
admin.site.register(Realtor,RealtorAdmin)