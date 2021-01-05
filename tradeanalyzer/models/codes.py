# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Codes(models.Model):
    last_update = models.CharField(max_length=8, blank=True, null=True)
    code = models.CharField(unique=True, max_length=200)
    full_code = models.CharField(max_length=200, blank=True, null=True)
    market_type = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codes'
        unique_together = (('id', 'code'),)
        app_label = 'tradeanalyzer'

