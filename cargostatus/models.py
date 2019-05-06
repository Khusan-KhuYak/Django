from django.db import models

class Cargostatus(models.Model):
    """
    Модели статуса грузов
    """
    status = models.CharField(max_length=30, blank=True)
    who_maked = models.CharField(max_length=20, blank=True)
    data_time = models.DateTimeField(auto_now=True)
    delta = models.CharField(max_length=30, blank=True)
    customer_rate = models.CharField(max_length=30, blank=True)
    rate_carriage = models.CharField(max_length=30, blank=True)