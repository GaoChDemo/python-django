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
          for (var j = 0; j < 7; j++) {
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

  //弹出添加框
  function showPopup_Add() {
      var baseText = null;
      var popUp = document.getElementById("popupcontentAdd");
      popUp.style.top = "200px";
      popUp.style.right = "100px";
      if (baseText == null) baseText = popUp.innerHTML;
      popUp.innerHTML = baseText + "<div id=\"statusbar\"><button onclick=\"hidePopup(); \">Close window<button></div>";
      var sbar = document.getElementById("statusbar");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      popUp.style.visibility = "visible";
  }

  //隐藏添加框
  function hidePopup_Add() {
      var popUp = document.getElementById("popupcontentAdd");
      popUp.style.visibility = "hidden";
  }

  function showPopup_Modification() {
      var baseText = null;
      var popUpModification = document.getElementById("popupcontentModification");
      popUpModification.style.top = "200px";
      popUpModification.style.right = "100px";
      if (baseText == null) baseText = popUpModification.innerHTML;
      popUpModification.innerHTML = baseText + "<div id=\"statusbar1\"><button onclick=\"hidePopup(); \">Close window<button></div>";
      var sbar = document.getElementById("statusbar1");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      popUpModification.style.visibility = "visible";
  }

  //隐藏添加框
  function hidePopup_Modification() {
      var popUpModification = document.getElementById("popupcontentModification");
      popUpModification.style.visibility = "hidden";
  }
  

  function popupcontentDel() {
      var baseText = null;
      var popupcontentDel = document.getElementById("popupcontentDel");
      popupcontentDel.style.top = "200px";
      popupcontentDel.style.right = "100px";
      if (baseText == null) baseText = popupcontentDel.innerHTML;
      popupcontentDel.innerHTML = baseText + "<div id=\"statusbar1\"><button onclick=\"hidePopup(); \">Close window<button></div>";
      var sbar = document.getElementById("statusbar1");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      popupcontentDel.style.visibility = "visible";
  }

  function hide_del() {
      var show_del = document.getElementById("popupcontentDel");
      show_del.style.visibility = "hidden";
  }


