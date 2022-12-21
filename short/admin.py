from django.contrib import admin
from .models import *
class ALLurlAdmin(admin.ModelAdmin):
    list_display = ['user','websitename','url','shorted']
admin.site.register(ALLurl , ALLurlAdmin)
