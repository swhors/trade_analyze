# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class CrawlLog(models.Model):
    end_date = models.DateTimeField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    fail = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    etc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crawl_log'
        app_label = 'tradeanalyzer'
