from django.contrib import admin
from home.models import Setting

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Setting, SettingAdmin)