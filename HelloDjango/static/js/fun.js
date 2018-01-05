  // 左边导航栏跟着页面滑动
  var oper_div = {};
  oper_div.scrollMouse = function() {
      this._id = "#divId";
      this._top = 0; //距离上边框距离
      this._scrollTop = (document.documentElement.scrollTop || document.body.scrollTop) + this._top;
      $(this._id).stop();
      if (this._scrollTop > 200) {
          document.getElementById("divId").className = "homebar";
      } 
      else {
          $(this._id).removeClass("divId");
      };
  };
  

function hideMand() {
  var table, tr, td, i;
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");

      // 循环表格每一行，查找匹配项
      for (i = 0; i < tr.length; i++) {
          for (var j = 0; j < 10; j++) {
            td = tr[i].getElementsByTagName("td")[j];
            if (td) {
                if (td.innerHTML == "是") {
                     tr[i].style.color = "red";
                } 
                
            }
          }
       }
}



  //搜索
  function myFunction() {
      // 声明变量
      var input, filter, table, tr, td, i;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");

      // 循环表格每一行，查找匹配项
      for (i = 0; i < tr.length; i++) {
          for (var j = 0; j < 10; j++) {
            td = tr[i].getElementsByTagName("td")[j];
            if (td) {
                if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                    break;
                } 
                else {
                  tr[i].style.display = "none";
                }
            }
          }
       }
    }
//************************** account ************************************************
  //弹出添加框
  function showPopup_Adda() {
      var baseText = null;
      var popUp = document.getElementById("popupcontentAdd");
      popUp.style.top = "200px";
      popUp.style.right = "100px";
      if (baseText == null) baseText = popUp.innerHTML;
      popUp.innerHTML = baseText + "<div id=\"statusbar\"></div>";
      var sbar = document.getElementById("statusbar");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      var myDate = new Date();
      newtime = myDate.getTime();
      document.getElementById("AccountNumber").value = newtime;
      popUp.style.visibility = "visible";

  }

  //隐藏添加框
  function hidePopup_Add() {
      var popUp = document.getElementById("popupcontentAdd");
      popUp.style.visibility = "hidden";
  }

  function showPopup_Modificationa(obj) {
      var con = obj.parentNode.parentNode.children[6].innerText;
      if(con == "是"){
        alert("已核实信息无法修改!");
        return false;
      }
      var baseText = null;
      var popUpModification = document.getElementById("popupcontentModification");
      popUpModification.style.top = "200px";
      popUpModification.style.right = "100px";
      if (baseText == null) baseText = popUpModification.innerHTML;
      popUpModification.innerHTML = baseText + "<div id=\"statusbar1\"></div>";
      var sbar = document.getElementById("statusbar1");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("mAccountNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("minputMonth").value = obj.parentNode.parentNode.children[1].innerText;
      var select = document.getElementById('mctCode');
      var valu = obj.parentNode.parentNode.children[2].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('mproductCode');
      var valu = obj.parentNode.parentNode.children[3].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('maccountCode');
      var valu = obj.parentNode.parentNode.children[4].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      document.getElementById("minputMoneyCode").value = obj.parentNode.parentNode.children[5].innerText;
      popUpModification.style.visibility = "visible";
  }


function popupcontentCa(obj) {
      var con = obj.parentNode.parentNode.children[6].innerText;
      if(con == "是"){
        alert("已核实信息无法再次核实!");
        return false;
      }
      var baseText = null;
      var popupcontentH = document.getElementById("popupcontentH");
      popupcontentH.style.top = "200px";
      popupcontentH.style.right = "100px";
      if (baseText == null) baseText = popupcontentH.innerHTML;
      popupcontentH.innerHTML = baseText + "<div id=\"statusbar3\"></div>";
      var sbar = document.getElementById("statusbar3");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("hAccountNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("hinputMonth").value = obj.parentNode.parentNode.children[1].innerText;
      document.getElementById("hctCode").value = obj.parentNode.parentNode.children[2].innerText;
      document.getElementById("hproductCode").value = obj.parentNode.parentNode.children[3].innerText;
      document.getElementById("haccountCode").value = obj.parentNode.parentNode.children[4].innerText;
      document.getElementById("hinputMoneyCode").value = obj.parentNode.parentNode.children[5].innerText;
      popupcontentH.style.visibility = "visible";
}


function hidePopupC() {
   var popupcontentH = document.getElementById("popupcontentH");
   popupcontentH.style.visibility = "hidden";
}

//隐藏添加框
function hidePopup_Modification() {
      var popUpModification = document.getElementById("popupcontentModification");
      popUpModification.style.visibility = "hidden";
}

    
function popupcontentDela(obj) {
      var con = obj.parentNode.parentNode.children[6].innerText;
      if(con == "是"){
        alert("已核实信息无法删除!");
        return false;
      }
      var baseText = null;
      var popupcontentDel = document.getElementById("popupcontentDel");
      popupcontentDel.style.top = "200px";
      popupcontentDel.style.right = "100px";
      if (baseText == null) baseText = popupcontentDel.innerHTML;
      popupcontentDel.innerHTML = baseText + "<div id=\"statusbar2\"></div>";
      var sbar = document.getElementById("statusbar2");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("dAccountNumber").value = obj.parentNode.parentNode.children[0].innerText;
      popupcontentDel.style.visibility = "visible";
}

function hide_del() {
      var show_del = document.getElementById("popupcontentDel");
      show_del.style.visibility = "hidden";
}

function delok()
{
      alert("删除成功！");
}

function xlwtok()
{
      alert("导出成功！");
}

function hok()
{
      alert("核实成功！");
}

function IsNum(num){
  var reNum=/^\d*$/;
  return(reNum.test(num));
}

function addoka()
{
    var str = document.getElementById("inputMoneyCode").value;
    var strda = document.getElementById("inputMonth").value;
    if(strda == "")
    {
      alert("日期不能为空!");
      return false;
    }

    if(str == "")
    {
      alert("金额不能为空!");
      return false;
    }
    else if(!IsNum(str))
    {
      alert("金额格式不正确!");
      return false;
    }
    else
    {
      alert("添加成功!");
    }
}

function modoka()
{
    var str = document.getElementById("minputMoneyCode").value;
    var strda = document.getElementById("minputMonth").value;
    if(strda == "")
    {
      alert("日期不能为空!");
      return false;
    }
    if(str == "")
    {
      alert("金额不能为空!");
      return false;
    }
    else if(!IsNum(str))
    {
      alert("金额格式不正确!");
      return false;
    }
    else
    {
      alert("修改成功!");
    }
}
//*****************************  card  ********************************
function showPopup_Addc() {
      var baseText = null;
      var popUp = document.getElementById("popupcontentAdd");
      popUp.style.top = "200px";
      popUp.style.right = "100px";
      if (baseText == null) baseText = popUp.innerHTML;
      popUp.innerHTML = baseText + "<div id=\"statusbar\"></div>";
      var sbar = document.getElementById("statusbar");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      var myDate = new Date();
      newtime = myDate.getTime();
      document.getElementById("CardNumber").value = newtime;
      popUp.style.visibility = "visible";

  }

  function showPopup_Modificationc(obj) {
      var con = obj.parentNode.parentNode.children[8].innerText;
      if(con == "是"){
        alert("已核实信息无法修改!");
        return false;
      }
      var baseText = null;
      var popUpModification = document.getElementById("popupcontentModification");
      popUpModification.style.top = "200px";
      popUpModification.style.right = "100px";
      if (baseText == null) baseText = popUpModification.innerHTML;
      popUpModification.innerHTML = baseText + "<div id=\"statusbar1\"></div>";
      var sbar = document.getElementById("statusbar1");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("mCardNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("minputDate").value = obj.parentNode.parentNode.children[1].innerText;
      var select = document.getElementById('mctCode');
      var valu = obj.parentNode.parentNode.children[2].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('mproductCode');
      var valu = obj.parentNode.parentNode.children[3].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      document.getElementById("mcardSaleNumber").value = obj.parentNode.parentNode.children[4].innerText;
      document.getElementById("mfaceAmount").value = obj.parentNode.parentNode.children[5].innerText;
      document.getElementById("mtotalAmount").value = obj.parentNode.parentNode.children[6].innerText;
      document.getElementById("mdiscountTotalAmount").value = obj.parentNode.parentNode.children[7].innerText;
      popUpModification.style.visibility = "visible";
  }

function popupcontentCc(obj) {
      var con = obj.parentNode.parentNode.children[8].innerText;
      if(con == "是"){
        alert("已核实信息无法再次核实!");
        return false;
      }
      var baseText = null;
      var popupcontentH = document.getElementById("popupcontentH");
      popupcontentH.style.top = "200px";
      popupcontentH.style.right = "100px";
      if (baseText == null) baseText = popupcontentH.innerHTML;
      popupcontentH.innerHTML = baseText + "<div id=\"statusbar3\"></div>";
      var sbar = document.getElementById("statusbar3");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("hCardNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("hinputDate").value = obj.parentNode.parentNode.children[1].innerText;
      document.getElementById("hctCode").value = obj.parentNode.parentNode.children[2].innerText;
      document.getElementById("hproductCode").value = obj.parentNode.parentNode.children[3].innerText;
      document.getElementById("hcardSaleNumber").value = obj.parentNode.parentNode.children[4].innerText;
      document.getElementById("hfaceAmount").value = obj.parentNode.parentNode.children[5].innerText;
      document.getElementById("htotalAmount").value = obj.parentNode.parentNode.children[6].innerText;
      document.getElementById("hdiscountTotalAmount").value = obj.parentNode.parentNode.children[7].innerText;
      popupcontentH.style.visibility = "visible";
}
    
 function popupcontentDelc(obj) {
      var con = obj.parentNode.parentNode.children[8].innerText;
      if(con == "是"){
        alert("已核实信息无法删除!");
        return false;
      }
      var baseText = null;
      var popupcontentDel = document.getElementById("popupcontentDel");
      popupcontentDel.style.top = "200px";
      popupcontentDel.style.right = "100px";
      if (baseText == null) baseText = popupcontentDel.innerHTML;
      popupcontentDel.innerHTML = baseText + "<div id=\"statusbar2\"></div>";
      var sbar = document.getElementById("statusbar2");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("dCardNumber").value = obj.parentNode.parentNode.children[0].innerText;
      popupcontentDel.style.visibility = "visible";
  }

function IsNum(num){
  var reNum=/^\d*$/;
  return(reNum.test(num));
}

function addokc()
{
    var str = document.getElementById("inputDate").value;
    var str1 = document.getElementById("cardSaleNumber").value;
    var str2 = document.getElementById("faceAmount").value;
    var str3 = document.getElementById("totalAmount").value;
    var str4 = document.getElementById("discountTotalAmount").value;
    if(str == "")
    {
      alert("日期不能为空!");
      return false;
    }

    if(str1 == "")
    {
      alert("卡销售数量不能为空!");
      return false;
    }
    else if(!IsNum(str1))
    {
      alert("卡销售数量格式不正确!");
      return false;
    }
    
    if(str2 == "")
    {
      alert("面值金额不能为空!");
      return false;
    }
    else if(!IsNum(str2))
    {
      alert("面值金额格式不正确!");
      return false;
    }

    if(str3 == "")
    {
      alert("卡总金额不能为空!");
      return false;
    }
    else if(!IsNum(str3))
    {
      alert("卡总金额格式不正确!");
      return false;
    }

    if(str4 == "")
    {
      alert("折扣后总金额不能为空!");
      return false;
    }
    else if(!IsNum(str4))
    {
      alert("折扣后总金额不正确!");
      return false;
    }
    else
    {
      alert("添加成功!");
    }
}

function modokc()
{
  var str = document.getElementById("minputDate").value;
    var str1 = document.getElementById("mcardSaleNumber").value;
    var str2 = document.getElementById("mfaceAmount").value;
    var str3 = document.getElementById("mtotalAmount").value;
    var str4 = document.getElementById("mdiscountTotalAmount").value;
    if(str == "")
    {
      alert("日期不能为空!");
      return false;
    }

    if(str1 == "")
    {
      alert("卡销售数量不能为空!");
      return false;
    }
    else if(!IsNum(str1))
    {
      alert("卡销售数量格式不正确!");
      return false;
    }
    
    if(str2 == "")
    {
      alert("面值金额不能为空!");
      return false;
    }
    else if(!IsNum(str2))
    {
      alert("面值金额格式不正确!");
      return false;
    }

    if(str3 == "")
    {
      alert("卡总金额不能为空!");
      return false;
    }
    else if(!IsNum(str3))
    {
      alert("卡总金额格式不正确!");
      return false;
    }

    if(str4 == "")
    {
      alert("折扣后总金额不能为空!");
      return false;
    }
    else if(!IsNum(str4))
    {
      alert("折扣后总金额不正确!");
      return false;
    }
    else
    {
      alert("修改成功!");
    }
}

//*****************************  网间  ********************************
function showPopup_Addw() {
      var baseText = null;
      var popUp = document.getElementById("popupcontentAdd");
      popUp.style.top = "200px";
      popUp.style.right = "100px";
      if (baseText == null) baseText = popUp.innerHTML;
      popUp.innerHTML = baseText + "<div id=\"statusbar\"></div>";
      var sbar = document.getElementById("statusbar");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      var myDate = new Date();
      newtime = myDate.getTime();
      document.getElementById("SettlementNumber").value = newtime;
      popUp.style.visibility = "visible";
  }

  function showPopup_Modificationw(obj) {
      var con = obj.parentNode.parentNode.children[7].innerText;
      if(con == "是"){
        alert("已核实信息无法修改!");
        return false;
      }
      var baseText = null;
      var popUpModification = document.getElementById("popupcontentModification");
      popUpModification.style.top = "200px";
      popUpModification.style.right = "100px";
      if (baseText == null) baseText = popUpModification.innerHTML;
      popUpModification.innerHTML = baseText + "<div id=\"statusbar1\"></div>";
      var sbar = document.getElementById("statusbar1");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("mSettlementNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("msettlementMonth").value = obj.parentNode.parentNode.children[1].innerText;
      var select = document.getElementById('mctCode');
      var valu = obj.parentNode.parentNode.children[2].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('mproductCode');
      var valu = obj.parentNode.parentNode.children[3].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('msettlementOperatorCode');
      var valu = obj.parentNode.parentNode.children[4].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('msettlementTypeCode');
      var valu = obj.parentNode.parentNode.children[5].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      document.getElementById("msettlementAmount").value = obj.parentNode.parentNode.children[6].innerText;
      popUpModification.style.visibility = "visible";
  }

function popupcontentCw(obj) {
      var con = obj.parentNode.parentNode.children[7].innerText;
      if(con == "是"){
        alert("已核实信息无法再次核实!");
        return false;
      }
      var baseText = null;
      var popupcontentH = document.getElementById("popupcontentH");
      popupcontentH.style.top = "200px";
      popupcontentH.style.right = "100px";
      if (baseText == null) baseText = popupcontentH.innerHTML;
      popupcontentH.innerHTML = baseText + "<div id=\"statusbar3\"></div>";
      var sbar = document.getElementById("statusbar3");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("hSettlementNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("hsettlementMonth").value = obj.parentNode.parentNode.children[1].innerText;
      document.getElementById("hctCode").value = obj.parentNode.parentNode.children[2].innerText;
      document.getElementById("hproductCode").value = obj.parentNode.parentNode.children[3].innerText;
      document.getElementById("hsettlementOperatorCode").value = obj.parentNode.parentNode.children[4].innerText;
      document.getElementById("hsettlementTypeCode").value = obj.parentNode.parentNode.children[5].innerText;
      document.getElementById("hsettlementAmount").value = obj.parentNode.parentNode.children[6].innerText;
      popupcontentH.style.visibility = "visible";
}
    
 function popupcontentDelw(obj) {
      var con = obj.parentNode.parentNode.children[7].innerText;
      if(con == "是"){
        alert("已核实信息无法删除!");
        return false;
      }
      var baseText = null;
      var popupcontentDel = document.getElementById("popupcontentDel");
      popupcontentDel.style.top = "200px";
      popupcontentDel.style.right = "100px";
      if (baseText == null) baseText = popupcontentDel.innerHTML;
      popupcontentDel.innerHTML = baseText + "<div id=\"statusbar2\"></div>";
      var sbar = document.getElementById("statusbar2");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("dSettlementNumber").value = obj.parentNode.parentNode.children[0].innerText;
      popupcontentDel.style.visibility = "visible";
  }

function IsNum(num){
  var reNum=/^\d*$/;
  return(reNum.test(num));
}

function addokw()
{
    var str = document.getElementById("settlementAmount").value;
    var strda = document.getElementById("settlementMonth").value;
    if(strda == "")
    {
      alert("日期不能为空!");
      return false;
    }

    if(str == "")
    {
      alert("卡总金额不能为空!");
      return false;
    }
    else if(!IsNum(str))
    {
      alert("卡总金额格式不正确!");
      return false;
    }
    else
    {
      alert("添加成功!");
    }
}

function modokw()
{
    var str = document.getElementById("msettlementAmount").value;
    var strda = document.getElementById("msettlementMonth").value;
    if(strda == "")
    {
      alert("日期不能为空!");
      return false;
    }

    if(str == "")
    {
      alert("卡总金额不能为空!");
      return false;
    }
    else if(!IsNum(str))
    {
      alert("卡总金额格式不正确!");
      return false;
    }
    else
    {
      alert("修改成功!");
    }
}





//*****************************  预存  ********************************
function showPopup_Addy() {
      var baseText = null;
      var popUp = document.getElementById("popupcontentAdd");
      popUp.style.top = "200px";
      popUp.style.right = "100px";
      if (baseText == null) baseText = popUp.innerHTML;
      popUp.innerHTML = baseText + "<div id=\"statusbar\"></div>";
      var sbar = document.getElementById("statusbar");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      var myDate = new Date();
      newtime = myDate.getTime();
      document.getElementById("RatainedNumber").value = newtime;
      popUp.style.visibility = "visible";

  }

  function showPopup_Modificationy(obj) {
      var con = obj.parentNode.parentNode.children[6].innerText;
      if(con == "是"){
        alert("已核实信息无法修改!");
        return false;
      }
      var baseText = null;
      var popUpModification = document.getElementById("popupcontentModification");
      popUpModification.style.top = "200px";
      popUpModification.style.right = "100px";
      if (baseText == null) baseText = popUpModification.innerHTML;
      popUpModification.innerHTML = baseText + "<div id=\"statusbar1\"></div>";
      var sbar = document.getElementById("statusbar1");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("mRatainedNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("mwriteOffDate").value = obj.parentNode.parentNode.children[1].innerText;
      var select = document.getElementById('mctCode');
      var valu = obj.parentNode.parentNode.children[2].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('mproductCode');
      var valu = obj.parentNode.parentNode.children[3].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('mwriteOffTypeCode');
      var valu = obj.parentNode.parentNode.children[4].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      document.getElementById("mwriteOffAmount").value = obj.parentNode.parentNode.children[5].innerText;
      popUpModification.style.visibility = "visible";
  }

function popupcontentCy(obj) {
      var con = obj.parentNode.parentNode.children[6].innerText;
      if(con == "是"){
        alert("已核实信息无法再次核实!");
        return false;
      }
      var baseText = null;
      var popupcontentH = document.getElementById("popupcontentH");
      popupcontentH.style.top = "200px";
      popupcontentH.style.right = "100px";
      if (baseText == null) baseText = popupcontentH.innerHTML;
      popupcontentH.innerHTML = baseText + "<div id=\"statusbar3\"></div>";
      var sbar = document.getElementById("statusbar3");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("hRatainedNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("hwriteOffDate").value = obj.parentNode.parentNode.children[1].innerText;
      document.getElementById("hctCode").value = obj.parentNode.parentNode.children[2].innerText;
      document.getElementById("hproductCode").value = obj.parentNode.parentNode.children[3].innerText;
      document.getElementById("hwriteOffTypeCode").value = obj.parentNode.parentNode.children[4].innerText;
      document.getElementById("hwriteOffAmount").value = obj.parentNode.parentNode.children[5].innerText;
      popupcontentH.style.visibility = "visible";
}

 function popupcontentDely(obj) {
      var con = obj.parentNode.parentNode.children[6].innerText;
      if(con == "是"){
        alert("已核实信息无法删除!");
        return false;
      }
      var baseText = null;
      var popupcontentDel = document.getElementById("popupcontentDel");
      popupcontentDel.style.top = "200px";
      popupcontentDel.style.right = "100px";
      if (baseText == null) baseText = popupcontentDel.innerHTML;
      popupcontentDel.innerHTML = baseText + "<div id=\"statusbar2\"></div>";
      var sbar = document.getElementById("statusbar2");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("dRatainedNumber").value = obj.parentNode.parentNode.children[0].innerText;
      popupcontentDel.style.visibility = "visible";
  }

function IsNum(num){
  var reNum=/^\d*$/;
  return(reNum.test(num));
}

function addoky()
{
    var str = document.getElementById("writeOffAmount").value;
    var strda = document.getElementById("writeOffDate").value;
    if(strda == "")
    {
      alert("日期不能为空!");
      return false;
    }

    if(str == "")
    {
      alert("销帐金额不能为空!");
      return false;
    }
    else if(!IsNum(str))
    {
      alert("销帐金额格式不正确!");
      return false;
    }
    else
    {
      alert("添加成功!");
    }
}

function modoky()
{
    var str = document.getElementById("mwriteOffAmount").value;
    var strda = document.getElementById("mwriteOffDate").value;
    if(strda == "")
    {
      alert("日期不能为空!");
      return false;
    }

    if(str == "")
    {
      alert("销帐金额不能为空!");
      return false;
    }
    else if(!IsNum(str))
    {
      alert("销帐金额格式不正确!");
      return false;
    }
    else
    {
      alert("修改成功!");
    }
}





//*****************************  通知  ********************************
function showPopup_Addt() {
      var baseText = null;
      var popUp = document.getElementById("popupcontentAdd");
      popUp.style.top = "200px";
      popUp.style.right = "100px";
      if (baseText == null) baseText = popUp.innerHTML;
      popUp.innerHTML = baseText + "<div id=\"statusbar\"></div>";
      var sbar = document.getElementById("statusbar");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      var myDate = new Date();
      newtime = myDate.getTime();
      document.getElementById("NoticeNumber").value = newtime;
      popUp.style.visibility = "visible";

  }

  function showPopup_Modificationt(obj) {
      var con = obj.parentNode.parentNode.children[6].innerText;
      if(con == "是"){
        alert("已核实信息无法修改!");
        return false;
      }
      var baseText = null;
      var popUpModification = document.getElementById("popupcontentModification");
      popUpModification.style.top = "200px";
      popUpModification.style.right = "100px";
      if (baseText == null) baseText = popUpModification.innerHTML;
      popUpModification.innerHTML = baseText + "<div id=\"statusbar1\"></div>";
      var sbar = document.getElementById("statusbar1");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("mNoticeNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("mbusinessCollectionData").value = obj.parentNode.parentNode.children[1].innerText;
      var select = document.getElementById('mctCode');
      var valu = obj.parentNode.parentNode.children[2].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('mproductCode');
      var valu = obj.parentNode.parentNode.children[3].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      var select = document.getElementById('mnotificationIncomeCode');
      var valu = obj.parentNode.parentNode.children[4].innerText;
       for (var i = 0, count = select.options.length; i < count; i++) {
             if (select.options[i].text == valu) {
                   select.selectedIndex = i;
                   break;
            }
      }
      document.getElementById("mbusinessIncomeAmount").value = obj.parentNode.parentNode.children[5].innerText;
      popUpModification.style.visibility = "visible";
  }


  function popupcontentCt(obj) {
      var con = obj.parentNode.parentNode.children[6].innerText;
      if(con == "是"){
        alert("已核实信息无法再次核实!");
        return false;
      }
      var baseText = null;
      var popupcontentH = document.getElementById("popupcontentH");
      popupcontentH.style.top = "200px";
      popupcontentH.style.right = "100px";
      if (baseText == null) baseText = popupcontentH.innerHTML;
      popupcontentH.innerHTML = baseText + "<div id=\"statusbar3\"></div>";
      var sbar = document.getElementById("statusbar3");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("hNoticeNumber").value = obj.parentNode.parentNode.children[0].innerText;
      document.getElementById("hbusinessCollectionData").value = obj.parentNode.parentNode.children[1].innerText;
      document.getElementById("hctCode").value = obj.parentNode.parentNode.children[2].innerText;
      document.getElementById("hproductCode").value = obj.parentNode.parentNode.children[3].innerText;
      document.getElementById("hnotificationIncomeCode").value = obj.parentNode.parentNode.children[4].innerText;
      document.getElementById("hbusinessIncomeAmount").value = obj.parentNode.parentNode.children[5].innerText;
      popupcontentH.style.visibility = "visible";
}
    
 function popupcontentDelt(obj) {
      var con = obj.parentNode.parentNode.children[6].innerText;
      if(con == "是"){
        alert("已核实信息无法删除!");
        return false;
      }
      var baseText = null;
      var popupcontentDel = document.getElementById("popupcontentDel");
      popupcontentDel.style.top = "200px";
      popupcontentDel.style.right = "100px";
      if (baseText == null) baseText = popupcontentDel.innerHTML;
      popupcontentDel.innerHTML = baseText + "<div id=\"statusbar2\"></div>";
      var sbar = document.getElementById("statusbar2");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      document.getElementById("dNoticeNumber").value = obj.parentNode.parentNode.children[0].innerText;
      popupcontentDel.style.visibility = "visible";
  }

function IsNum(num){
  var reNum=/^\d*$/;
  return(reNum.test(num));
}

function addokt()
{
    var str = document.getElementById("businessIncomeAmount").value;
    var strda = document.getElementById("businessCollectionData").value;
    if(strda == "")
    {
      alert("日期不能为空!");
      return false;
    }

    if(str == "")
    {
      alert("营业收入金额不能为空!");
      return false;
    }
    else if(!IsNum(str))
    {
      alert("营业收入金额格式不正确!");
      return false;
    }
    else
    {
      alert("添加成功!");
    }
}

function modokt()
{
  var str = document.getElementById("mbusinessIncomeAmount").value;
  var strda = document.getElementById("mbusinessCollectionData").value;
    if(strda == "")
    {
      alert("日期不能为空!");
      return false;
    }
    if(str == "")
    {
      alert("营业收入金额不能为空!");
      return false;
    }
    else if(!IsNum(str))
    {
      alert("营业收入金额格式不正确!");
      return false;
    }
    else
    {
      alert("修改成功!");
    }
}