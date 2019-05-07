from django.db import models
from django.utils.translation import gettext as _

class Cargostatus(models.Model):
    """
    Модели статуса грузов
    """
    number = models.CharField(_('Номер груза'), max_length=20, blank=True)
    status = models.CharField(_('Статус '), max_length=30, blank=True)
    who_maked = models.CharField(_('Кто поставил '), max_length=20, blank=True)
    data_time = models.DateTimeField(_('Дата и время '), auto_now=True)
    delta = models.CharField(_('Дельта '), max_length=30, blank=True)
    customer_rate = models.CharField(_('Ставка клиента '), max_length=30, blank=True)
    rate_carriage = models.CharField(_('Ставка заказчика '), max_length=30, blank=True)

    class Meta:
        verbose_name = "Груз"
        verbose_name_plural = "Статус грузов"