from django.contrib import admin

# Register your models here.
from awal_menyusui.models import Menyusui


class MenyusuiAdmin(admin.ModelAdmin):
    list_display = ('user', 'baby_name', 'ttl_baby', 'gender')


admin.site.register(Menyusui, MenyusuiAdmin)
