from django.contrib import admin
from .models import Cargos

class CargosAdmin(admin.ModelAdmin):
    list_display = ('number', 'type', 'at', 'volume')
admin.site.register(Cargos, CargosAdmin)