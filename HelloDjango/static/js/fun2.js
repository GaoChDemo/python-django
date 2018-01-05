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
  $(function() {
      window.onscroll = function() {
          oper_div.scrollMouse();
      };
  });

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
  var baseText = null;
  function showPopup() {
      var popUp = document.getElementById("popupcontent");
      popUp.style.top = "200px";
      popUp.style.right = "100px";
      if (baseText == null) baseText = popUp.innerHTML;
      popUp.innerHTML = baseText + "<div id=\"statusbar\"><button onclick=\"hidePopup(); \">Close window<button></div>";
      var sbar = document.getElementById("statusbar");
      sbar.style.marginTop = (parseInt(1000) - 40) + "px";
      popUp.style.visibility = "visible";
  }

  //隐藏添加框
  function hidePopup() {
      var popUp = document.getElementById("popupcontent");
      popUp.style.visibility = "hidden";
  }
    
  function del(){       
      if(window.confirm("确实要删除吗？")){  
          
          //删除后处罚
      }
      else{  
          return;  
      }  
  }  

