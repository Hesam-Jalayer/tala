from django.db import models


class MilliGoldModel(models.Model):
    buy_price = models.CharField(max_length=100, null=True, blank=True)
    sell_price = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class TalaseModel(models.Model):
    buy_price = models.CharField(max_length=100, null=True, blank=True)
    sell_price = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class TlynModel(models.Model):
    buy_price = models.CharField(max_length=100, null=True, blank=True)
    sell_price = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)



