---
title: "Using Customized Controls in a Table"
id: 1500009584281
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584281-Using-Customized-Controls-in-a-Table
updated_at: 2021-07-24T05:55:57Z
---

# Using Customized Controls in a Table

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584301-Managing-Cells-Columns-and-Rows-in-a-Table)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563302-Crosstabs)

# Using Customized Controls in a Table

For tables in page reports, you can apply customized controls to perform web actions such as sorting and filtering by binding the Customized Control web action on objects in the tables.

A customized control is a user defined web action dialog. The report designer first defines a customized control to be triggered from an object in a page report table, then at runtime end users can trigger the customized control which is shown as a dialog to perform the specified web actions.

In Logi JReport Designer the report designer can store the properties of a customized control into a file with the extension .wctrl to the customized control library which is the Customized Control folder under the installation root. Logi JReport Server saves customized controls in DBMS.

Customized controls do not take part in the report layout and are not exported in the report results.

Below is a list of the sections covered in this topic:

> * [Defining a Customized Control](#Define)
> * [Managing Customized Controls](#Manage)
> * [Sample of Customized Control Contents](#Sample)

## Defining a Customized Control

1. Right-click an object as a trigger in a page report table, for example a column header label, and select **Display Type** from the shortcut menu.
2. In the Web Behaviors box of the Display Type dialog, choose an [event](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label#Event) from the Events column, then select in the Actions column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box to display the Web Action List dialog.

   ![Web Action list dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889313687/wbactnlst.gif)
3. Select **Customized Control** to create a customized control, or select **Customized Control from Lib** to reference a customized control file from the library, and then select **OK**.
   * When Customized Control is selected, the [Customized Control – Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009586181-Customized-Control-Web-Action-Builder-Dialog) dialog is displayed.

     ![Customized Control - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889372695/cstmzdctrlactn.gif)

     1. In the Size box, specify the width and height of the customized control in the browser window at runtime. To make the customized control automatically sized according to its contents, check **Auto**.
     2. In the Position box, specify the position of the customized control in the browser window at runtime:
        + **In the center of the browser window**  
           The customized control is placed in the center of the browser window at runtime.
        + **According to mouse position**  
           The customized control is placed where the mouse is selected. The option is useful when the event is concerned with mouse action.
        + **Relative to the trigger component**  
           The position of the customized control is placed where the trigger object is.
        + **Absolute**  
           If checked, you can further specify the absolute X and Y positions of the customized control in pixels.
     3. In the Contents text box, input HTML fragment with JavaScript code. Select [here](#Sample) for a sample.
     4. To save the customized control properties into a file to the customized control library, select **Save As**. Then in the New Customized Control File dialog, provide the file name and select **OK**.
     5. Select **OK** to create the customized control.
   * When Customized Control from Lib is selected, the Manage Customized Controls dialog is displayed, where all the customized control files in the customized control library are listed. Select the one you want and select **OK**.
4. Select **OK** in the Display Type dialog to finish defining the customized control.

At runtime when the specified event occurs on the trigger object in the table, a dialog based on the customized control definition will be displayed. End users can use it to perform the defined web actions.

## Managing Customized Controls

With the [Manage Customized Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009587761-Manage-Customized-Controls-Dialog) dialog you can manage the customized control files saved in the customized control library as follows (to open the dialog, select **Report** > **Manage Customized Controls**).

![Manage Customized Controls dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893867927/mngcstmzdctrl.gif)

* **Creating a new customized control file**  
   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif), provide a name to the new file in the New Customized Control File dialog, then [define the customized control properties](#Define) in the Customized Control – Web Action Builder dialog.
* **Editing a customized control file**  
   Right-click the file and select **Edit** from the shortcut menu, then in the Customized Control – Web Action Builder dialog, [modify the customized control properties](#Define).
* **Renaming a customized control file**  
   Right-click the file and select **Rename** from the shortcut menu. Input a new name and then select outside of the name area to accept the change.
* **Creating a copy of a customized control file**  
   Right-click the file and select **Duplicate** from the shortcut menu. A copy will be created and listed in the manager. You can then change the name of the copy file and the properties of the customized control.
* **Removing a****customized control file**  
   Select the file and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif), or right-click the file and select **Delete** from the shortcut menu.
* **Sorting the customized control files**  
   By default the customized control files are listed in the ascending order according to their names. To change the sort order, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893868183/btn_sortcc1.gif). However the descending order will not be remembered after you exit the dialog. The next time you access the dialog it is always the ascending order.

## Sample of Customized Control Contents

When editing the contents of a customized control, the HTML fragment should be plain text that is children DOM element of HTML Body. You can use web action APIs in the HTML fragment. For details, refer to the index.html file in the `<server_install_root>\public_html\webos\doc` folder.

For example, suppose the contents of a customized control is defined like this:

|  |
| --- |
| `<style>  #plugin {  background-color: gray;  }    #plugin td {  background-color: white;  }`  `.item--available {  }`  `.item--unavailable{  color: #CCCCCC;  }`  `</style>  <table id="plugin" cellspacing="1px" style="margin:0px;width:100%;height:300px;border:1px solid silver;background-color:;">  <tr style="height:30px;"><td>  <table style="text-align:center;width:100%;background-color:;">  <tr>  <td><button id="btnSortA" onclick="this.doSort('Ascending')">Ascending</button></td>  <td style="border-left:1px solid gray;"><button id="btnSortD" onclick="this.doSort('Descending')">Descending</button></td>  </tr>  </table>  </td></tr>  <tr style="height:25px;"><td style="background-color:#cccccc;padding:3px;">  <input id="searchbox" style="width:85%;margin-right:3px;" type="text" onkeyup="this.search(e)"/>  <div style="width:10px;height:19px;float:right;cursor:pointer;"  onclick="this.clearSearch()">x</div>  </td></tr>  <tr style="height:150px;"><td>  <div id="fc-values" onclick="this.selectValue(e)" style="width:100%;height:150px;overflow:auto;"></div>  </td></tr>  <tr style="height:30px;">  <td style="background-color:#cccccc;"><button onclick="this.doFilter()">Apply</button><button onclick="this.clear()">Clear</button></td>  </tr>  </table>`  `<script type="text/javascript">`  `var comp; // data container  var field; // db field  var filter;`  `var _onGetDataContainer = function(msg){  var result = msg.result;  if(result.err == 0){  comp = result.obj.comp;  if(!comp) return;  comp.getAssocDBField(context.dsid, _onGetDBField);  }else{  System.err.println(result.msg);  throw new Error(result.msg);  }  }.$bind(this);`  `var _onGetDBField = function(msg){  var result = msg.result;  if(result.err == 0){  field = result.obj.field;  // TODO enable sort ?  Report.getFilterCtrl(field, comp, _onGetFilterCtrl);  }else{  System.err.println(result.msg);  throw new Error(result.msg);  }  }.$bind(this);`  `var _onGetFilterCtrl = function(msg){  var result = msg.result;  if(result.err == 0){  filter = result.obj.ctrl;  if(!filter) return;  // TODO enable filter ?  _renderValues.call(this, filter);  }else{  System.err.println(result.msg);  throw new Error(result.msg);  }  }.$bind(this);`  `var _canSort = function(){  var b = !!comp && !!field;  return b ? comp.isSortable() : false;  };`  `var _canFilter = function(){  var b = !!comp && !!field && !!filter  return b ? comp.isFilterable() : false;  };`  `var _renderValues = function(filter, values){  var td = document.getElementById("fc-values"),  i, len, val, item, buf, showAll;`  `showAll = !values;  values = values || filter.getAllValues();  td.innerHTML = "";  var isAll = filter.isAllSelected();  for(i=showAll ? -1:0, len=values.length; i<len; i++){  val = i < 0 ? {disp:"All", real:"__ALL__", selected:isAll, available:true} :  values[i];  item = document.createElement("LI");  item.className = val.available ? "item--available" : "item--unavailable";  buf = ["<input type='checkbox' id='fc-index-",i,"' "];  buf.push("value=\"", val.real, "\"");  if(val.selected){  buf.push("checked");  }  buf.push("/>", val.disp);  item.innerHTML = buf.join("");  td.appendChild(item);   }  };`  `this.doSort = function(type){  if(!_canSort()) return;  comp.sort(field, type);  };`  `this.selectValue = function(e){  e = e || window.event;  var ele = e.srcElement||e.target, key, checked;  if(ele.tagName != "INPUT") return;  key = ele.value;  checked = ele.checked;  if("__ALL__" === key){  filter.selectAll(checked);  _renderValues.call(this, filter);  }else{  filter.select(key, checked);   // The element for 'All' should be updated checked status  ele = document.getElementById("fc-index--1");  if(filter.isAllSelected()){  ele.checked = true;  }else{  ele.checked = false;  }  }  };`  `this.doFilter = function(){  if(!_canFilter()) return;  filter.applyFilter();  this.hide();  };`  `this.clear = function(){  if(!filter) return;  filter.clearSelects();  _renderValues.call(this, filter);  };`  `this.search = function(e){  if(!filter) return;  e = e || window.event;  var ele = e.srcElement||e.target, value = ele.value, values;  if(value){  values = filter.search(value);  }  _renderValues.call(this, filter, values);  };   this.clearSearch = function(){  document.getElementById("searchbox").value="";  if(!filter) return;   _renderValues.call(this, filter);  };`  `Report.getDataContainerBy(context.dsid, _onGetDataContainer);`  `</script>` |

At runtime the customized control dialog looks like as follows:

|  |  |  |
| --- | --- | --- |
| |  |  | | --- | --- | | Ascending | Descending | |
| x |
|  |
| ApplyClear |

**Related topics:**

> * [Publishing Additional Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources#Additional) for how to publish customized control files to Logi JReport Server.
> * [Downloading Customized Controls from Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009592621-Downloading-Resources-from-Logi-JReport-Server#CC)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584301-Managing-Cells-Columns-and-Rows-in-a-Table)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563302-Crosstabs)
