# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CurrencyData(models.Model):
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    currency_type = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    auto_increment_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'currency_data'

class CurrencyTypes(models.Model):
    currency_type = models.TextField(blank=True, null=True)
    type_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'currency_types'
