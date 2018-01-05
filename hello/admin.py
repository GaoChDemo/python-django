# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import AccountIncomeCodeTable,AccountIncomeTable,CardIncomeTable,NoticeIncomeCodeTable
from models import NoticeIncomeTable,ProductCodeTable,RetainedIncomeTable,SetBetweenNetworksTable
from models import EtcodeTable,PayeeusecodeTable,SettlementoperatorcodeTable,SettlementtypecodeTable,WriteofftypecodeTable
# Register your models here.
admin.site.register(AccountIncomeCodeTable)
admin.site.register(AccountIncomeTable)
admin.site.register(CardIncomeTable)
admin.site.register(NoticeIncomeCodeTable)
admin.site.register(NoticeIncomeTable)
admin.site.register(ProductCodeTable)
admin.site.register(RetainedIncomeTable)
admin.site.register(SetBetweenNetworksTable)
admin.site.register(EtcodeTable)
admin.site.register(PayeeusecodeTable)
admin.site.register(SettlementoperatorcodeTable)
admin.site.register(SettlementtypecodeTable)
admin.site.register(WriteofftypecodeTable)