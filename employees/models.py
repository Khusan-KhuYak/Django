from django.db import models
from django.utils.translation import gettext as _

class Employees(models.Model):
    """
    Модель персонала
    """
    fio = models.CharField(_('ФИО'), max_length=30, blank=True)
    phone = models.CharField(_('Номер телефона '), max_length=20, blank=True)
    work_phone = models.CharField(_('Рабочий телефон '), max_length=10, blank=True)
    managers = models.CharField(_('Менеджеры '), max_length=30, blank=True)
    access_rights = models.CharField(_('Права доступа'), max_length=30, blank=True)

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"