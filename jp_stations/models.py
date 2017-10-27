from django.db import models

from . import managers


STATUS_IN_OPERATION = 0
STATUS_BEFORE_OPERATION = 1
STATUS_ABOLITION = 2
STATUSES = (
    (STATUS_IN_OPERATION, '運行中'),
    (STATUS_BEFORE_OPERATION, '運行前'),
    (STATUS_ABOLITION, '運行廃止'),
)


class Company(models.Model):
    objects = managers.CompanyManager()
    name = models.CharField(
        max_length=50,
        verbose_name='会社名',
    )
    status = models.IntegerField(
        choices=STATUSES,
        verbose_name='営業状態',
    )

    def __str__(self):
        return self.name


class Line(models.Model):
    objects = managers.LineManager()
    name = models.CharField(
        max_length=50,
        verbose_name='路線名',
    )
    status = models.IntegerField(
        choices=STATUSES,
        verbose_name='営業状態',
    )
    company = models.ForeignKey(
        Company,
        verbose_name='鉄道会社',
    )

    def __str__(self):
        return f'{self.name}線'


class Station(models.Model):
    objects = managers.StationManager()
    name = models.CharField(
        max_length=50,
        verbose_name='駅名',
    )
    postal_code = models.CharField(
        max_length=8,
        verbose_name='郵便番号',
    )
    address = models.CharField(
        max_length=50,
        verbose_name='住所',
    )
    latitude = models.FloatField(
        verbose_name='緯度',
    )
    longitude = models.FloatField(
        verbose_name='経度',
    )
    status = models.IntegerField(
        choices=STATUSES,
        verbose_name='営業状態',
    )
    lines = models.ManyToManyField(
        Line,
        verbose_name='路線',
    )

    def __str__(self):
        return f'{self.name}駅'
