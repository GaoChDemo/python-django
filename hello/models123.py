# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class AccountIncomeCodeTable(models.Model):
    accountcode = models.CharField(max_length=125,default='root')  # Field name made lowercase.
    accountname = models.CharField(max_length=125,default='root')  # Field name made lowercase.