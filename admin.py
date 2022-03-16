from django.contrib import admin
from . models import *
from . models import Contactus

from import_export.admin import ImportExportModelAdmin


class BrandAdmin(ImportExportModelAdmin):
    pass

    
admin.site.register(Contactus, BrandAdmin)


# Register your models here.

# @admin.register(Contactus)
# class Contactus(admin.ModelAdmin):
#     list_display = ['name','email', 'phone', 'message']
#     search_fields = ('name','email', 'phone','message')
# admin.site.register(Contactus)