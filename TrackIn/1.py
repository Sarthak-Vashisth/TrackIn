# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CommoditiesBuySellMain(models.Model):
    serial_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    commodity_id = models.IntegerField(blank=True, null=True)
    commodity_name = models.CharField(max_length=200, blank=True, null=True)
    buy_or_sell = models.CharField(max_length=2, blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    buy_sell_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_reference_id = models.CharField(max_length=100, blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    deleted_reference_id = models.CharField(max_length=100, blank=True, null=True)
    record_status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commodities_buy_sell_main'
