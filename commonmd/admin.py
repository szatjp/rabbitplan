from django.contrib import admin

from commonmd.models import ProCode

# Register your models here.


#admin.site.register(ProCode)

@admin.register(ProCode)
class ProCodeAdmin(admin.ModelAdmin):
    list_display = ('fstateid', 'fstatename', 'fnexttime')
    ordering = ['fstateid']