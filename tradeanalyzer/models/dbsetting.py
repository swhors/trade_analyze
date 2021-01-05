# -*- coding: utf-8 -*-
from __future__ import division
from django.db import models

##############################################################################
#
# Begin of Config Class
#
class DbSetting(models.Model):
    dbserver   = models.CharField(max_length=100)
    dbport     = models.IntegerField(default=3060)
    dbuser     = models.CharField(max_length=100)
    dbpassword = models.CharField(max_length=100)
    dbname     = models.CharField(max_length=100)

    def __str__(self):
        return 'DbSetting'
