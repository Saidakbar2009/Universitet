from django.contrib import admin
from .models import *
from django.contrib.auth.models import *
# Register your models here.
@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    list_display = ['ism', 'jins', 'daraja', 'yosh', 'fan']
    search_fields = ['ism']

@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_display = ['nom', 'aktiv']
    search_fields = ['nom']
    list_filter = ['aktiv']

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ['nom', 'yonalish', 'asosiy']
    list_filter = ['asosiy']
    search_fields = ['nom']
# admin.site.register(Yonalish)
# admin.site.register(Fan)
# admin.site.register(Ustoz)