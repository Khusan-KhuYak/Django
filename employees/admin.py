from django.contrib import admin
from .models import Employees

class EmployessAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'work_phone', 'managers', 'access_rights')
admin.site.register(Employees, EmployessAdmin)
