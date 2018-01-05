# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class AccountIncomeCodeTable(models.Model):
    accountcode = models.IntegerField(db_column='accountCode', primary_key=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=125)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Account_income_Code_table'


class AccountIncomeTable(models.Model):
    inputmonth = models.CharField(db_column='inputMonth', max_length=125, blank=True, null=True)  # Field name made lowercase.
    etcode = models.IntegerField(db_column='etCode', blank=True, null=True)  # Field name made lowercase.
    productcode = models.ForeignKey('ProductCodeTable', models.DO_NOTHING, db_column='productCode', blank=True, null=True)  # Field name made lowercase.
    accountcode = models.ForeignKey(AccountIncomeCodeTable, models.DO_NOTHING, db_column='accountCode', blank=True, null=True)  # Field name made lowercase.
    inputmoneycode = models.IntegerField(db_column='inputMoneyCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Account_income_table'


class CardIncomeTable(models.Model):
    inputdate = models.CharField(db_column='inputDate', max_length=125, blank=True, null=True)  # Field name made lowercase.
    etcode = models.IntegerField(db_column='etCode', blank=True, null=True)  # Field name made lowercase.
    productcode = models.ForeignKey('ProductCodeTable', models.DO_NOTHING, db_column='productCode', blank=True, null=True)  # Field name made lowercase.
    cardsalenumber = models.IntegerField(db_column='cardSaleNumber', blank=True, null=True)  # Field name made lowercase.
    faceamount = models.IntegerField(db_column='faceAmount', blank=True, null=True)  # Field name made lowercase.
    totalamount = models.IntegerField(db_column='totalAmount', blank=True, null=True)  # Field name made lowercase.
    discounttotalamount = models.IntegerField(db_column='discountTotalAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Card_income_table'


class NoticeIncomeCodeTable(models.Model):
    noticeincomecode = models.IntegerField(db_column='NoticeIncomeCode', primary_key=True)  # Field name made lowercase.
    noticeincomename = models.CharField(db_column='NoticeIncomeName', max_length=125)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notice_income_Code_table'


class NoticeIncomeTable(models.Model):
    bussinesscollectiondate = models.CharField(db_column='bussinessCollectionDate', max_length=125, blank=True, null=True)  # Field name made lowercase.
    etcode = models.IntegerField(db_column='etCode', blank=True, null=True)  # Field name made lowercase.
    productcode = models.ForeignKey('ProductCodeTable', models.DO_NOTHING, db_column='productCode', blank=True, null=True)  # Field name made lowercase.
    noticeincomecode = models.ForeignKey(NoticeIncomeCodeTable, models.DO_NOTHING, db_column='NoticeIncomeCode', blank=True, null=True)  # Field name made lowercase.
    bussinessincomeamount = models.IntegerField(db_column='bussinessIncomeAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notice_income_table'


class ProductCodeTable(models.Model):
    productcode = models.IntegerField(db_column='productCode', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=125)  # Field name made lowercase.
    whetheruser = models.CharField(db_column='whetherUser', max_length=125, blank=True, null=True)  # Field name made lowercase.
    whetheraccount = models.CharField(db_column='whetherAccount', max_length=125, blank=True, null=True)  # Field name made lowercase.
    whethercard = models.CharField(db_column='whetherCard', max_length=125, blank=True, null=True)  # Field name made lowercase.
    whethersettlement = models.CharField(db_column='whetherSettlement', max_length=125, blank=True, null=True)  # Field name made lowercase.
    whetherretained = models.CharField(db_column='whetherRetained', max_length=125, blank=True, null=True)  # Field name made lowercase.
    whethernotice = models.CharField(db_column='whetherNotice', max_length=125, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product_Code_Table'


class RetainedIncomeTable(models.Model):
    writeoffdate = models.CharField(db_column='writeOffDate', max_length=125, blank=True, null=True)  # Field name made lowercase.
    etcode = models.IntegerField(db_column='etCode', blank=True, null=True)  # Field name made lowercase.
    productcode = models.ForeignKey(ProductCodeTable, models.DO_NOTHING, db_column='productCode', blank=True, null=True)  # Field name made lowercase.
    writeofftypecode = models.ForeignKey('WriteofftypecodeTable', models.DO_NOTHING, db_column='writeOffTypeCode', blank=True, null=True)  # Field name made lowercase.
    writeoffamount = models.IntegerField(db_column='writeOffAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Retained_income_table'


class SetBetweenNetworksTable(models.Model):
    settlementmonth = models.CharField(db_column='settlementMonth', max_length=125, blank=True, null=True)  # Field name made lowercase.
    etcode = models.IntegerField(db_column='etCode', blank=True, null=True)  # Field name made lowercase.
    productcode = models.ForeignKey(ProductCodeTable, models.DO_NOTHING, db_column='productCode', blank=True, null=True)  # Field name made lowercase.
    settlementoperatorcode = models.ForeignKey('SettlementoperatorcodeTable', models.DO_NOTHING, db_column='settlementOperatorCode', blank=True, null=True)  # Field name made lowercase.
    settlementtypecode = models.ForeignKey('SettlementtypecodeTable', models.DO_NOTHING, db_column='settlementTypeCode', blank=True, null=True)  # Field name made lowercase.
    settlementamount = models.IntegerField(db_column='settlementAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Set_between_networks_table'


class EtcodeTable(models.Model):
    etcode = models.IntegerField(db_column='etCode', primary_key=True)  # Field name made lowercase.
    etname = models.CharField(db_column='etName', max_length=125)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etCode_table'


class PayeeusecodeTable(models.Model):
    payeeusecode = models.IntegerField(db_column='payeeUseCode', primary_key=True)  # Field name made lowercase.
    payeeusename = models.CharField(db_column='payeeUseName', max_length=125)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payeeUseCode_table'


class SettlementoperatorcodeTable(models.Model):
    settlementoperatorcode = models.IntegerField(db_column='settlementOperatorCode', primary_key=True)  # Field name made lowercase.
    settlementoperatorname = models.CharField(db_column='settlementOperatorName', max_length=125)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'settlementOperatorCode_table'


class SettlementtypecodeTable(models.Model):
    settlementtypecode = models.IntegerField(db_column='settlementTypeCode', primary_key=True)  # Field name made lowercase.
    settlementtypename = models.CharField(db_column='settlementTypeName', max_length=125)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'settlementTypeCode_table'


class WriteofftypecodeTable(models.Model):
    writeofftypecode = models.IntegerField(db_column='writeOffTypeCode', primary_key=True)  # Field name made lowercase.
    writeofftypename = models.CharField(db_column='writeOffTypeName', max_length=125)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'writeOffTypeCode_table'


