# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# 第四个是 auth中用户权限有关的类。auth可以设置每个用户的权限。
from django.template.context_processors import csrf
from django.views.decorators.csrf  import csrf_exempt
from .forms import UserForm
from django.http import HttpResponse,HttpResponseRedirect
from models import AccountIncomeCodeTable,AccountIncomeTable,CardIncomeTable,NoticeIncomeCodeTable
from models import NoticeIncomeTable,ProductCodeTable,RetainedIncomeTable,SetBetweenNetworksTable
from models import EtcodeTable,PayeeusecodeTable,SettlementoperatorcodeTable,SettlementtypecodeTable,WriteofftypecodeTable
import time
from django.contrib import messages
import xlwt
import xlrd
import xlwt as ExcelWrite

################################ function ###################################

confirm = {0:'否',1:'是'}

def rtime():
    return time.time()*1000

def GetctCode():
    dicts= {}
    dbdatas = EtcodeTable.objects.all()
    for data in dbdatas:
        dicts[data.etcode] = data.etname
    return dicts

def GetProductCodeTable():
    dicts= {}
    dbdatas = ProductCodeTable.objects.all()
    for data in dbdatas:
        dicts[data.productcode] = data.productname
    return dicts


def GetAccountIncomeCodeTable():
    dicts= {}
    dbdatas = AccountIncomeCodeTable.objects.all()
    for data in dbdatas:
        dicts[data.accountcode] = data.accountname
    return dicts

def GetSettlementoperatorcodeTable():
    dicts= {}
    dbdatas = SettlementoperatorcodeTable.objects.all()
    for data in dbdatas:
        dicts[data.settlementoperatorcode] = data.settlementoperatorname
    return dicts

def GetSettlementtypecodeTable():
    dicts= {}
    dbdatas = SettlementtypecodeTable.objects.all()
    for data in dbdatas:
        dicts[data.settlementtypecode] = data.settlementtypename
    return dicts

def GetNoticeIncomeCodeTable():
    dicts= {}
    dbdatas = NoticeIncomeCodeTable.objects.all()
    for data in dbdatas:
        dicts[data.noticeincomecode] = data.noticeincomename
    return dicts

def GetWriteofftypecodeTable():
    dicts= {}
    dbdatas = WriteofftypecodeTable.objects.all()
    for data in dbdatas:
        dicts[data.writeofftypecode] = data.writeofftypename
    return dicts
################################ login ###################################
@csrf_exempt
def login_view(req):
    context = {}
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            #获取的表单数据与数据库进行比较
            user = authenticate(username = username,password = password)
            if user:
                #比较成功，跳转index
                auth.login(req,user)
                req.session['username'] = username
                return HttpResponseRedirect('/report')
            else:
                #比较失败，还在login
                context = {'uf':uf,'message':'登录失败，账号或密码错误！'}
                return render(req, 'login.html', context)
    else:
        uf = UserForm()
        context = {'uf':uf}
        return render(req, 'login.html', context)

#登出  
def logout_view(req):
    #清理cookie里保存username
    auth.logout(req)
    uf = UserForm()
    context = {'uf':uf,'message':'成功退出登录！'}
    return render(req, 'logoutf.html')

################################ report ###################################
@login_required(login_url='/nologin')  
@csrf_exempt
def report(req):
    #清理cookie里保存username
    dbdatas = AccountIncomeTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    ac = GetAccountIncomeCodeTable()

    for data in dbdatas:
        txt =[data.account_income_id,data.inputmonth,et[data.etcode],pc[str(data.productcode)],ac[data.accountcode],data.inputmoneycode,confirm[data.confirmcode]]
        datas.append(txt)

    
    #return render_to_response('index.html' , {'students':students , 'name':name,'datas':datas})
    username = req.session['username']

    return render(req, 'AccountIncome.html',{'username':username,'datas':datas,'et':et,'pc':pc,'ac':ac})


@login_required(login_url='/nologin')  
@csrf_exempt
def xlwt_report(req):
    #清理cookie里保存username
    dbdatas = AccountIncomeTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    ac = GetAccountIncomeCodeTable()

    workbook=xlwt.Workbook(encoding='utf-8')  
    booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)  

    datas.append(['出账单号','录入月份','城市','产品','出账类型','录入金额','是否已核实'])
    for data in dbdatas:
        if data.confirmcode == 1:
            txt =[data.account_income_id,data.inputmonth,et[data.etcode],pc[str(data.productcode)],ac[data.accountcode],data.inputmoneycode,confirm[data.confirmcode]]
            datas.append(txt)

    for i,row in enumerate(datas):  
        for j,col in enumerate(row):  
            booksheet.write(i,j,col)  

    workbook.save('report.xls') 
    return HttpResponseRedirect('/report')


 
# 数据库操作
@login_required(login_url='/nologin')  
@csrf_exempt
def testdb(request):
    test1 = AccountIncomeTable(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

    
def nologin(req):
    #return HttpResponseRedirect('/nologin')
    return render(req, 'nologin.html')

@login_required(login_url='/nologin')  
@csrf_exempt
def add_report(req):
    if req.method == 'POST':
        AccountNumber = req.POST.get('AccountNumber')
        inputMonth = req.POST.get('inputMonth')
        ctCode = req.POST.get('ctCode')
        productCode = req.POST.get('productCode')
        accountCode = req.POST.get('accountCode')
        iputMoneyCode = req.POST.get('inputMoneyCode')
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()

        test1 = AccountIncomeTable(account_income_id=AccountNumber,inputmonth=inputMonth,etcode=ctCode,productcode=productCode,accountcode=accountCode,inputmoneycode=iputMoneyCode,confirmcode=0)
        test1.save()
        return HttpResponseRedirect('/report')
    else:
        pass

@login_required(login_url='/nologin')  
@csrf_exempt
def h_report(req):
    if req.method == 'POST':
        hAccountNumber = req.POST.get('hAccountNumber')
       
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()

        AccountIncomeTable.objects.filter(account_income_id=hAccountNumber).update(confirmcode=1)
        return HttpResponseRedirect('/report')
    else:
        pass

@login_required(login_url='/nologin')  
@csrf_exempt
def del_report(req):
    if req.method == 'POST':
        dAccountNumber = req.POST.get('dAccountNumber')
        print dAccountNumber
        AccountIncomeTable.objects.filter(account_income_id=dAccountNumber).delete()
        #test1 = AccountIncomeTable(account_income_id=AccountNumber,inputmonth=inputMonth,etcode=ctCode,productcode=productCode,accountcode=accountCode,inputmoneycode=iputMoneyCode)
        #test1.save()
        #return HttpResponse("<p>数据添加成功！</p>")
        #messages.success(req,'Hello world.')
        return HttpResponseRedirect('/report')
    else:
        pass


@login_required(login_url='/nologin')  
@csrf_exempt
def mod_report(req):
    if req.method == 'POST':
        mAccountNumber = req.POST.get('mAccountNumber')
        minputMonth = req.POST.get('minputMonth')
        mctCode = req.POST.get('mctCode')
        mproductCode = req.POST.get('mproductCode')
        maccountCode = req.POST.get('maccountCode')
        miputMoneyCode = req.POST.get('minputMoneyCode')
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()
        AccountIncomeTable.objects.filter(account_income_id=mAccountNumber).update(inputmonth=minputMonth,etcode=mctCode,productcode=mproductCode,accountcode=maccountCode,inputmoneycode=miputMoneyCode)
        return HttpResponseRedirect('/report')
    else:
        pass


################################ card ###################################
@login_required(login_url='/nologin')  
@csrf_exempt
def card(req):
    #清理cookie里保存username
    dbdatas = CardIncomeTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    #print pc['110101']

    for data in dbdatas:
        txt =[data.card_income_id,data.inputdate,et[data.etcode],pc[str(data.productcode)],data.cardsalenumber,data.faceamount,data.totalamount,data.discounttotalamount,confirm[data.confirmcode]]
        datas.append(txt)

    
    #return render_to_response('index.html' , {'students':students , 'name':name,'datas':datas})
    username = req.session['username']

    return render(req, 'CardIncome.html',{'username':username,'datas':datas,'et':et,'pc':pc})

@login_required(login_url='/nologin')  
@csrf_exempt
def xlwt_card(req):
    #清理cookie里保存username
    dbdatas = CardIncomeTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    #print pc['110101']
    workbook=xlwt.Workbook(encoding='utf-8')  
    booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)  

    datas.append(['卡销售订单号','录入日期','城市','产品','卡销售数量','面值金额','卡总金额','折扣后总金额','是否已核实'])
    for data in dbdatas:
        if data.confirmcode == 1:
            txt =[data.card_income_id,data.inputdate,et[data.etcode],pc[str(data.productcode)],data.cardsalenumber,data.faceamount,data.totalamount,data.discounttotalamount,confirm[data.confirmcode]]
            datas.append(txt)

    for i,row in enumerate(datas):  
        for j,col in enumerate(row):  
            booksheet.write(i,j,col)  

    workbook.save('card.xls') 
    return HttpResponseRedirect('/card')


@login_required(login_url='/nologin')  
@csrf_exempt  
def add_card(req):
    if req.method == 'POST':
        CardNumber = req.POST.get('CardNumber')
        inputDate = req.POST.get('inputDate')
        ctCode = req.POST.get('ctCode')
        productCode = req.POST.get('productCode')
        cardSaleNumber = req.POST.get('cardSaleNumber')
        faceAmount = req.POST.get('faceAmount')
        totalAmount = req.POST.get('totalAmount')
        discountTotalAmount = req.POST.get('discountTotalAmount')
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()
        test1 = CardIncomeTable(card_income_id=CardNumber,inputdate=inputDate,etcode=ctCode,productcode=productCode,cardsalenumber=cardSaleNumber,faceamount=faceAmount,totalamount=totalAmount,discounttotalamount=discountTotalAmount,confirmcode=0)
        test1.save()
        return HttpResponseRedirect('/card')
    else:
        pass


@login_required(login_url='/nologin')  
@csrf_exempt
def h_card(req):
    if req.method == 'POST':
        hCardNumber = req.POST.get('hCardNumber')
       
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()

        CardIncomeTable.objects.filter(card_income_id=hCardNumber).update(confirmcode=1)
        return HttpResponseRedirect('/card')
    else:
        pass

@login_required(login_url='/nologin')  
@csrf_exempt  
def del_card(req):
    if req.method == 'POST':
        dCardNumber = req.POST.get('dCardNumber')
        CardIncomeTable.objects.filter(card_income_id=dCardNumber).delete()
        #test1 = AccountIncomeTable(account_income_id=AccountNumber,inputmonth=inputMonth,etcode=ctCode,productcode=productCode,accountcode=accountCode,inputmoneycode=iputMoneyCode)
        #test1.save()
        #return HttpResponse("<p>数据添加成功！</p>")
        #messages.success(req,'Hello world.')
        return HttpResponseRedirect('/card')
    else:
        pass


@login_required(login_url='/nologin')  
@csrf_exempt
def mod_card(req):
    if req.method == 'POST':
        mCardNumber = req.POST.get('mCardNumber')
        minputDate = req.POST.get('minputDate')
        mctCode = req.POST.get('mctCode')
        mproductCode = req.POST.get('mproductCode')
        mcardSaleNumber = req.POST.get('mcardSaleNumber')
        mfaceAmount = req.POST.get('mfaceAmount')
        mtotalAmount = req.POST.get('mtotalAmount')
        mdiscountTotalAmount = req.POST.get('mdiscountTotalAmount')
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()
        CardIncomeTable.objects.filter(card_income_id=mCardNumber).update(inputdate=minputDate,etcode=mctCode,productcode=mproductCode,cardsalenumber=mcardSaleNumber,faceamount=mfaceAmount,totalamount=mtotalAmount,discounttotalamount=mdiscountTotalAmount)
        return HttpResponseRedirect('/card')
    else:
        pass


################################ setbet ###################################
@login_required(login_url='/nologin')  
@csrf_exempt
def setbet(req):
    #清理cookie里保存username
    dbdatas = SetBetweenNetworksTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    sc = GetSettlementoperatorcodeTable()
    stc = GetSettlementtypecodeTable()
    #print pc['110101']

    for data in dbdatas:
        txt =[data.set_between_networks_id,data.settlementmonth,et[data.etcode],pc[str(data.productcode)],sc[data.settlementoperatorcode],stc[data.settlementtypecode],data.settlementamount,confirm[data.confirmcode]]
        datas.append(txt)

    
    #return render_to_response('index.html' , {'students':students , 'name':name,'datas':datas})
    username = req.session['username']

    return render(req, 'Setbetweennetworks.html',{'username':username,'datas':datas,'et':et,'pc':pc,'sc':sc,'stc':stc})

@login_required(login_url='/nologin')  
@csrf_exempt
def xlwt_setbet(req):
    #清理cookie里保存username
    dbdatas = SetBetweenNetworksTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    sc = GetSettlementoperatorcodeTable()
    stc = GetSettlementtypecodeTable()
    #print pc['110101']
    workbook=xlwt.Workbook(encoding='utf-8')  
    booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)  

    datas.append(['网间结算订单号','结算月份','城市','产品','结算运营商','结算类型','结算金额','是否已核实'])
    for data in dbdatas:
        if data.confirmcode == 1:
            txt =[data.set_between_networks_id,data.settlementmonth,et[data.etcode],pc[str(data.productcode)],sc[data.settlementoperatorcode],stc[data.settlementtypecode],data.settlementamount,confirm[data.confirmcode]]
            datas.append(txt)

    for i,row in enumerate(datas):  
        for j,col in enumerate(row):  
            booksheet.write(i,j,col)  

    workbook.save('setbet.xls') 
    return HttpResponseRedirect('/setbet')


@login_required(login_url='/nologin')  
@csrf_exempt
def add_setbet(req):
    if req.method == 'POST':
        SettlementNumber = req.POST.get('SettlementNumber')
        settlementMonth = req.POST.get('settlementMonth')
        ctCode = req.POST.get('ctCode')
        productCode = req.POST.get('productCode')
        settlementOperatorCode = req.POST.get('settlementOperatorCode')
        settlementTypeCode = req.POST.get('settlementTypeCode')
        settlementAmount = req.POST.get('settlementAmount')
     
        test1 = SetBetweenNetworksTable(set_between_networks_id=SettlementNumber,settlementmonth=settlementMonth,etcode=ctCode,productcode=productCode,settlementoperatorcode=settlementOperatorCode,settlementtypecode=settlementTypeCode,settlementamount=settlementAmount,confirmcode=0)
        test1.save()
        return HttpResponseRedirect('/setbet')
    else:
        pass


@login_required(login_url='/nologin')  
@csrf_exempt
def h_setbet(req):
    if req.method == 'POST':
        hSettlementNumber = req.POST.get('hSettlementNumber')
       
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()

        SetBetweenNetworksTable.objects.filter(set_between_networks_id=hSettlementNumber).update(confirmcode=1)
        return HttpResponseRedirect('/setbet')
    else:
        pass


@login_required(login_url='/nologin')  
@csrf_exempt
def del_setbet(req):
    if req.method == 'POST':
        dSettlementNumber = req.POST.get('dSettlementNumber')
        SetBetweenNetworksTable.objects.filter(set_between_networks_id=dSettlementNumber).delete()
        
        messages.success(req,'Hello world.')
        return HttpResponseRedirect('/setbet')
    else:
        pass


@login_required(login_url='/nologin')  
@csrf_exempt
def mod_setbet(req):
    if req.method == 'POST':
        mSettlementNumber = req.POST.get('mSettlementNumber')
        msettlementMonth = req.POST.get('msettlementMonth')
        mctCode = req.POST.get('mctCode')
        mproductCode = req.POST.get('mproductCode')
        msettlementOperatorCode = req.POST.get('msettlementOperatorCode')
        msettlementTypeCode = req.POST.get('msettlementTypeCode')
        msettlementAmount = req.POST.get('msettlementAmount')

        SetBetweenNetworksTable.objects.filter(set_between_networks_id=mSettlementNumber).update(settlementmonth=msettlementMonth,etcode=mctCode,productcode=mproductCode,settlementoperatorcode=msettlementOperatorCode,settlementtypecode=msettlementTypeCode,settlementamount=msettlementAmount)
        return HttpResponseRedirect('/setbet')
    else:
        pass

################################ retained ###################################
@login_required(login_url='/nologin')  
@csrf_exempt
def retained(req):
    #清理cookie里保存username
    dbdatas = RetainedIncomeTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    wc = GetWriteofftypecodeTable()
    #print pc['110101']

    for data in dbdatas:
        txt =[data.retained_income_id,data.writeoffdate,data.etcode,data.productcode,data.writeofftypecode,data.writeoffamount,confirm[data.confirmcode]]
        datas.append(txt)

    
    #return render_to_response('index.html' , {'students':students , 'name':name,'datas':datas})
    username = req.session['username']
    return render(req, 'Retainedincome.html',{'username':username,'datas':datas,'et':et,'pc':pc,'wc':wc})

@login_required(login_url='/nologin')  
@csrf_exempt
def xlwt_retained(req):
    #清理cookie里保存username
    dbdatas = RetainedIncomeTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    wc = GetWriteofftypecodeTable()
    #print pc['110101']
    workbook=xlwt.Workbook(encoding='utf-8')  
    booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)  

    datas.append(['预存转收入订单号','销账日期','城市','产品','销账类型','销帐金额','是否已核实'])
    for data in dbdatas:
        if data.confirmcode == 1:
            txt =[data.retained_income_id,data.writeoffdate,data.etcode,data.productcode,data.writeofftypecode,data.writeoffamount,confirm[data.confirmcode]]
            datas.append(txt)

    for i,row in enumerate(datas):  
        for j,col in enumerate(row):  
            booksheet.write(i,j,col)  

    workbook.save('retained.xls') 
    return HttpResponseRedirect('/retained')


@login_required(login_url='/nologin')  
@csrf_exempt
def add_retained(req):
    if req.method == 'POST':
        RatainedNumber = req.POST.get('RatainedNumber')
        writeOffDate = req.POST.get('writeOffDate')
        ctCode = req.POST.get('ctCode')
        productCode = req.POST.get('productCode')
        writeOffTypeCode = req.POST.get('writeOffTypeCode')
        writeOffAmount = req.POST.get('writeOffAmount')
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()
        test1 = RetainedIncomeTable(retained_income_id=RatainedNumber,writeoffdate=writeOffDate,etcode=ctCode,productcode=productCode,writeofftypecode=writeOffTypeCode,writeoffamount=writeOffAmount,confirmcode=0)
        test1.save()
        return HttpResponseRedirect('/retained')
    else:
        pass

@login_required(login_url='/nologin')  
@csrf_exempt 
def h_retained(req):
    if req.method == 'POST':
        hRatainedNumber = req.POST.get('hRatainedNumber')
       
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()

        RetainedIncomeTable.objects.filter(retained_income_id=hRatainedNumber).update(confirmcode=1)
        return HttpResponseRedirect('/retained')
    else:
        pass


@login_required(login_url='/nologin')  
@csrf_exempt
def del_retained(req):
    if req.method == 'POST':
        dRatainedNumber = req.POST.get('dRatainedNumber')
        RetainedIncomeTable.objects.filter(retained_income_id=dRatainedNumber).delete()
        #test1 = AccountIncomeTable(account_income_id=AccountNumber,inputmonth=inputMonth,etcode=ctCode,productcode=productCode,accountcode=accountCode,inputmoneycode=iputMoneyCode)
        #test1.save()
        #return HttpResponse("<p>数据添加成功！</p>")
        return HttpResponseRedirect('/retained')
    else:
        pass


@login_required(login_url='/nologin')  
@csrf_exempt
def mod_retained(req):
    if req.method == 'POST':
        mRatainedNumber = req.POST.get('mRatainedNumber')
        mwriteOffDate = req.POST.get('mwriteOffDate')
        mctCode = req.POST.get('mctCode')
        mproductCode = req.POST.get('mproductCode')
        mwriteOffTypeCode = req.POST.get('mwriteOffTypeCode')
        mwriteOffAmount = req.POST.get('mwriteOffAmount')
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()
        RetainedIncomeTable.objects.filter(retained_income_id=mRatainedNumber).update(writeoffdate=mwriteOffDate,etcode=mctCode,productcode=mproductCode,writeofftypecode=mwriteOffTypeCode,writeoffamount=mwriteOffAmount)
        return HttpResponseRedirect('/retained')
    else:
        pass



################################ notice ###################################
@login_required(login_url='/nologin')  
@csrf_exempt
def notice(req):
    #清理cookie里保存username
    dbdatas = NoticeIncomeTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    nc = GetNoticeIncomeCodeTable()
    #print pc['110101']

    for data in dbdatas:
            txt =[data.notice_income_id,data.bussinesscollectiondate,et[data.etcode],pc[str(data.productcode)],nc[data.noticeincomecode],data.bussinessincomeamount,confirm[data.confirmcode]]
            datas.append(txt)

    
    #return render_to_response('index.html' , {'students':students , 'name':name,'datas':datas})
    username = req.session['username']

    return render(req, 'Noticeincome.html',{'username':username,'datas':datas,'et':et,'pc':pc,'nc':nc})

@login_required(login_url='/nologin')  
@csrf_exempt
def xlwt_notice(req):
    #清理cookie里保存username
    dbdatas = NoticeIncomeTable.objects.all()
    datas = []
    et = GetctCode()
    pc = GetProductCodeTable()
    nc = GetNoticeIncomeCodeTable()
    #print pc['110101']
    workbook=xlwt.Workbook(encoding='utf-8')  
    booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)  

    datas.append(['通知单订单号','营业收款日期','城市','产品','通知单收入类型','营业收入金额','是否已核实'])
    for data in dbdatas:
        if data.confirmcode == 1:
            txt =[data.notice_income_id,data.bussinesscollectiondate,et[data.etcode],pc[str(data.productcode)],nc[data.noticeincomecode],data.bussinessincomeamount,confirm[data.confirmcode]]
            datas.append(txt)

    for i,row in enumerate(datas):  
        for j,col in enumerate(row):  
            booksheet.write(i,j,col)  

    workbook.save('notice.xls') 
    return HttpResponseRedirect('/notice')


@login_required(login_url='/nologin')  
@csrf_exempt 
def add_notice(req):
    if req.method == 'POST':
        NoticeNumber = req.POST.get('NoticeNumber')
        businessCollectionData = req.POST.get('businessCollectionData')
        ctCode = req.POST.get('ctCode')
        productCode = req.POST.get('productCode')
        notificationIncomeCode = req.POST.get('notificationIncomeCode')
        businessIncomeAmount = req.POST.get('businessIncomeAmount')

        test1 = NoticeIncomeTable(notice_income_id=NoticeNumber,bussinesscollectiondate=businessCollectionData,etcode=ctCode,productcode=productCode,noticeincomecode=notificationIncomeCode,bussinessincomeamount=businessIncomeAmount,confirmcode=0)
        test1.save()
        return HttpResponseRedirect('/notice')
    else:
        pass

@login_required(login_url='/nologin')  
@csrf_exempt
def h_notice(req):
    if req.method == 'POST':
        hNoticeNumber = req.POST.get('hNoticeNumber')
       
        #test1 = AccountIncomeTable(inputmonth=inputMonth,inputmoneycode=iputMoneyCode)
        #test1.save()

        NoticeIncomeTable.objects.filter(notice_income_id=hNoticeNumber).update(confirmcode=1)
        return HttpResponseRedirect('/notice')
    else:
        pass



@login_required(login_url='/nologin')  
@csrf_exempt
def del_notice(req):
    if req.method == 'POST':
        dNoticeNumber = req.POST.get('dNoticeNumber')
        NoticeIncomeTable.objects.filter(notice_income_id=dNoticeNumber).delete()
        return HttpResponseRedirect('/notice')
    else:
        pass

@login_required(login_url='/nologin')  
@csrf_exempt
def mod_notice(req):
    if req.method == 'POST':
        mNoticeNumber = req.POST.get('mNoticeNumber')
        mbusinessCollectionData = req.POST.get('mbusinessCollectionData')
        mctCode = req.POST.get('mctCode')
        mproductCode = req.POST.get('mproductCode')
        mnotificationIncomeCode = req.POST.get('mnotificationIncomeCode')
        mbusinessIncomeAmount = req.POST.get('mbusinessIncomeAmount')
        
        NoticeIncomeTable.objects.filter(notice_income_id=mNoticeNumber).update(bussinesscollectiondate=mbusinessCollectionData,etcode=mctCode,productcode=mproductCode,noticeincomecode=mnotificationIncomeCode,bussinessincomeamount=mbusinessIncomeAmount)
        return HttpResponseRedirect('/notice')
    else:
        pass