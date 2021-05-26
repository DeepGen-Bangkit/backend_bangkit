from django.contrib import admin

# Register your models here.
from kehamilan.models import Kehamilan


class KehamilanAdmin(admin.ModelAdmin):
    list_display = ('user','ttl', 'hpht', 'hpl')


admin.site.register(Kehamilan, KehamilanAdmin)
