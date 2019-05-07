from django.contrib import admin
from .models import Cargostatus

class CargostatsAdmin(admin.ModelAdmin):
    list_display = ('number', 'status', 'who_maked', 'data_time', 'delta', 'customer_rate', 'rate_carriage')
admin.site.register(Cargostatus, CargostatsAdmin)
