from django.db import models

class Employees(models.Model):
    """
    Модель персонала
    """
    phone = models.CharField(max_length=20, blank=True)
    work_phone = models.CharField(max_length=10, blank=True)
    managers = models.CharField(max_length=30, blank=True)
    access_rights = models.CharField(max_length=30, blank=True)