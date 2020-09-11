from django.db import models

# Create your models here.


class user_profile(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    phone_no = models.BigIntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_reference_id = models.CharField(max_length=100, blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    deleted_reference_id = models.CharField(max_length=100, blank=True, null=True)
    record_status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profile'

class commodity_main(models.Model):
    commodity_id = models.IntegerField(primary_key=True)
    commodity_name = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_reference_id = models.CharField(max_length=100, blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    deleted_reference_id = models.CharField(max_length=100, blank=True, null=True)
    record_status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commodity_main'


class commodities_buy_sell_main(models.Model):
    serial_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    commodity_id = models.IntegerField(blank=True, null=True)
    commodity_name = models.CharField(max_length=200, blank=True, null=True)
    buy_or_sell = models.CharField(max_length=2, blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    buy_sell_date = models.DateTimeField(blank=True, null=True)
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