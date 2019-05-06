from django.db import models

class Cargos(models.Model):
    """
    Модель грузов
    """
    type = models.CharField(max_length=30, blank=True)
    at = models.CharField(max_length=10, blank=True)
    volume = models.CharField(max_length=10, blank=True)