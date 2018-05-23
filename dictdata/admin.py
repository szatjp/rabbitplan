# coding:utf-8

from django.contrib import admin

from dictdata.models import JaWord

# Register your models here.


@admin.register(JaWord)
class JaWordAdmin(admin.ModelAdmin):
    list_display = ('fwordno', 'fword', 'fpronunciation', 'fdate')
    ordering = ['fwordno']