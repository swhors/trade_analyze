# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from mysite import settings

class Prices(models.Model):
    last_update = models.CharField(max_length=8, blank=True, null=True)
    price_date = models.DateField(blank=False, null=False)
    code = models.CharField(max_length=200, blank=False, null=False)
    price_open = models.IntegerField(blank=True, null=True)
    price_close = models.IntegerField(blank=True, null=True)
    price_high = models.IntegerField(blank=True, null=True)
    price_low = models.IntegerField(blank=True, null=True)
    price_adj_close = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    __debug = False

    class Meta:
        managed = False
        db_table = 'prices'
        app_label = 'tradeanalyzer'

    def checkAndSave(self):
        row = Prices.objects.filter(code=self.code, price_date=self.price_date)
        if self.__debug == True:
            print(__name__, 'checkAndSave', len(row), row)
        if len(row) == 0:
            models.Model.save(self)
        else:
            if self.__debug == True:
                print(__name__, 'row exists', row)
    def deleteItem(self, code, price_date):
        Prices.objects.filter(code=code, price_date=price_date).delete()

def priceMapper(code, date,open,high,low,close,volume):
    prices = Prices(price_date = date,\
                    code = code,\
                    price_open = open,\
                    price_high = high,\
                    price_close = close,\
                    price_low = low,\
                    volume = volume )
    prices.save()
    return prices

