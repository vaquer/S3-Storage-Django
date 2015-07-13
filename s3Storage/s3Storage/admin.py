from __future__ import absolute_import
from django.contrib import admin
from .models import TestModel


class TestModelAdmin(admin.ModelAdmin):
    '''
        Admin View for TestModel
    '''
    list_display = ('name', 'pic',)
    list_filter = ('name',)
    search_fields = ['name']

admin.site.register(TestModel, TestModelAdmin)
