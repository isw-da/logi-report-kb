---
title: "Using Customized Controls in Tables"
id: 1500009606462
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606462-Using-Customized-Controls-in-Tables
updated_at: 2021-07-24T16:05:12Z
---

# Using Customized Controls in Tables

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606202-Crosstabs)

# Using Customized Controls in Tables

Customized control is a user defined web action dialog for performing sorting and filtering operations. It works only in page report tables that are created using query resources. You can define the size, position, and [contents](#Sample) of a customized control, make it triggered from an object in a page report table, publish the report to Logi Report Server, then at runtime end users can trigger the customized control which is shown as a dialog to perform the specified web actions.

In Logi Report Designer the report designer can store the definition of a customized control into a file with the extension .wctrl to the customized control library which is the Customized Control folder under the installation root. Logi Report Server saves customized controls in DBMS.

Customized controls do not take part in the report layout and are not exported in the report result.

This topic includes the following sections:

* [Defining a Customized Control](#Define)
* [Managing Customized Controls](#Manage)
* [Sample of Customized Control Contents](#Sample)

## Defining a Customized Control

1. Right-click a column header label or group-by field as the trigger in a page report table, and select **Display Type** from the shortcut menu.
2. In the Web Behaviors box of the Display Type dialog, choose an [event](https://devnet.logianalytics.com/hc/en-us/articles/1500009629441-Using-Basic-Web-Controls-in-a-Report#Event) from the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) that appears in the text box to display the Web Action List dialog.

   ![Web Action List](https://devnet.logianalytics.com/hc/article_attachments/4404904233623/wbactnlst.gif)
3. Select **Customized Control** to create a customized control, or select **Customized Control from Lib** to reference a customized control file from the library, and then select **OK**.
   * When Customized Control is selected, the [Customized Control – Web Action Builder](https://devnet.logianalytics.com/hc/en-us/articles/1500009630321-Customized-Control-Web-Action-Builder-Dialog) dialog is displayed.

     ![Customized Control - Web Action Builder](https://devnet.logianalytics.com/hc/article_attachments/4404904362519/cstmzdctrlactn.gif)

     1. In the Size box, specify the width and height of the customized control in the browser window at runtime. To make the customized control automatically sized according to its contents, select **Auto**.
     2. In the Position box, specify the position of the customized control in the browser window at runtime:
        + **In the center of the browser window**  
           The customized control is placed in the center of the browser window at runtime.
        + **According to mouse position**  
           The customized control is placed where the mouse is selected. The option is useful when the event is concerned with mouse action.
        + **Relative to the trigger component**  
           The position of the customized control is placed where the trigger object is.
        + **Absolute**  
           If the option is selected, you can further specify the absolute X and Y positions of the customized control in pixels.
     3. In the Contents text box, type HTML fragment with JavaScript code. [Go here](#Sample) for a sample.
     4. To save the customized control definition into a file to the customized control library, select **Save As**. Then in the New Customized Control File dialog, provide the file name and select **OK**.
     5. Select **OK** to create the customized control.
   * When Customized Control from Lib is selected, the Manage Customized Controls dialog is displayed, where all the customized control files in the customized control library are listed. Select the one you want and select **OK**. The selected customized control file should be published to Logi Report Server together with the report in order for the customized control to take effect. [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009636101-Publishing-and-Downloading-Resources#Additional) for details about how to publish customized control files.
4. Select **OK** in the Display Type dialog to finish defining the customized control.

At runtime when the specified event occurs on the trigger object in the table, a dialog based on the customized control definition will be displayed. End users can use it to perform the defined web actions.

## Managing Customized Controls

With the [Manage Customized Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009632401-Manage-Customized-Controls-Dialog) dialog you can manage the customized control files saved in the customized control library as follows (to open the dialog, select **Report** > **Manage Customized Controls**).

![Manage Customized Controls](https://devnet.logianalytics.com/hc/article_attachments/4404904255767/mngcstmzdctrl.gif)

* **Creating a new customized control file**  
  Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif), provide a name to the new file in the New Customized Control File dialog, then [define the customized control](#Builder) in the Customized Control – Web Action Builder dialog.
* **Editing a customized control file**  
  Right-click the file and select **Edit** from the shortcut menu, then in the Customized Control – Web Action Builder dialog, [modify the customized control definition](#Builder).
* **Renaming a customized control file**  
  Right-click the file and select **Rename** from the shortcut menu. Type a new name and then select outside of the name area to accept the change.
* **Creating a copy of a customized control file**  
  Right-click the file and select **Duplicate** from the shortcut menu. A copy will be created and listed in the manager. You can then change the name of the copy file and the definition of the customized control.
* **Removing a****customized control file**  
   Select the file and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif), or right-click the file and select **Delete** from the shortcut menu.
* **Sorting the customized control files**  
   By default the customized control files are listed in the ascending order according to their names. To change the sort order, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404904256279/btn_sortcc1.gif). However the descending order will not be remembered after you exit the dialog. The next time you access the dialog it is always the ascending order.

## Sample of Customized Control Contents

The contents of customized control is HTML fragment and should be plain text that is children DOM element of HTML Body. You can use web action APIs in the HTML fragment. For details about the APIs, access RptComponent.js in the `<server_install_root>\public_html\webos\jsvm\src\com\jinfonet\api` folder.

For example, suppose the contents of a customized control is defined like this:

```
<style>  
#plugin {  
background-color: gray;  
}   
  
#plugin td {  
background-color: white;  
}  
  
.item--available {  
}  
  
.item--unavailable{  
color: #CCCCCC;  
}  
</style>  
  
<table id="plugin" cellspacing="1px" style="margin:0px;width:100%;height:300px;border:1px solid silver;background-color:;">  
<tr style="height:30px;"><td>  
<table style="text-align:center;width:100%;background-color:;">  
<tr>  
<td><button id="btnSortA" onselect="this.doSort('Ascending')">Ascending</button></td>  
<td style="border-left:1px solid gray;"><button id="btnSortD" onselect="this.doSort('Descending')">Descending</button></td>  
</tr>  
</table>  
</td></tr>  
<tr style="height:25px;"><td style="background-color:#cccccc;padding:3px;">  
<input id="searchbox" style="width:85%;margin-right:3px;" type="text" onkeyup="this.search(e)"/>  
<div style="width:10px;height:19px;float:right;cursor:pointer;"  
onselect="this.clearSearch()">x</div>  
</td></tr>  
<tr style="height:150px;"><td>  
<div id="fc-values" onselect="this.selectValue(e)" style="width:100%;height:150px;overflow:auto;"></div>  
</td></tr>  
<tr style="height:30px;">  
<td style="background-color:#cccccc;"><button onselect="this.doFilter()">Apply</button><button onselect="this.clear()">Clear</button></td>  
</tr>  
</table>  
  
<script type="text/javascript">  
  
var comp; // Data container  
 
var field; // DBField  
var filter;  
  
var _onGetDataContainer = function(msg){  
var result = msg.result;  
 
if(result.err == 0){  
comp = result.obj.comp;  
if(!comp) return;  
comp.getAssocDBField(context.dsid, _onGetDBField);  
}else{  
System.err.println(result.msg);  
throw new Error(result.msg);  
 
}  
}.$bind(this);  
  
var _onGetDBField = function(msg){  
var result = msg.result;  
if(result.err == 0){  
field = result.obj.field;  
 
// To enable sort  
Report.getFilterCtrl(field, comp, _onGetFilterCtrl);  
}else{  
System.err.println(result.msg);  
throw new Error(result.msg);  
}  
}.$bind(this);  
  
var _onGetFilterCtrl = function(msg){  
var result = msg.result;  
if(result.err == 0){  
filter = result.obj.ctrl;  
if(!filter) return;  
// To enable filter  
_renderValues.call(this, filter);  
}else{  
System.err.println(result.msg);  
throw new Error(result.msg);  
}  
}.$bind(this);  
  
var _canSort = function(){  
var b = !!comp && !!field;  
return b ? comp.isSortable() : false;  
};  
  
var _canFilter = function(){  
var b = !!comp && !!field && !!filter  
return b ? comp.isFilterable() : false;  
};  
  
var _renderValues = function(filter, values){  
var td = document.getElementById("fc-values"),  
 
i, len, val, item, buf, showAll;  
  
showAll = !values;  
values = values || filter.getAllValues();  
td.innerHTML = "";  
var isAll = filter.isAllSelected();  
for(i=showAll ? -1:0, len=values.length; i<len; i++){  
val = i < 0 ? {disp:"All", real:"__ALL__", selected:isAll, available:true} :  
values[i];  
item = document.createElement("LI");  
item.className = val.available ? "item--available" : "item--unavailable";  
buf = ["<input type='check box' id='fc-index-",i,"' "];  
buf.push("value=\"", val.real, "\"");  
if(val.selected){  
buf.push("checked");  
}  
buf.push("/>", val.disp);  
item.innerHTML = buf.join("");  
td.appendChild(item);   
}  
};  
  
this.doSort = function(type){  
if(!_canSort()) return;  
comp.sort(field, type);  
};  
  
this.selectValue = function(e){  
e = e || window.event;  
var ele = e.srcElement||e.target, key, checked;  
if(ele.tagName != "INPUT") return;  
key = ele.value;  
checked = ele.checked;  
if("__ALL__" === key){  
filter.selectAll(checked);  
 _renderValues.call(this, filter);  
}else{  
filter.select(key, checked);  
  
// The element for "All" should be updated checked status.  
ele = document.getElementById("fc-index--1");  
if(filter.isAllSelected()){  
ele.checked = true;  
}else{  
ele.checked = false;  
 
}  
}  
};  
  
this.doFilter = function(){  
if(!_canFilter()) return;  
filter.applyFilter();  
this.hide();  
};  
  
this.clear = function(){  
if(!filter) return;  
filter.clearSelects();  
 _renderValues.call(this, filter);  
};  
  
			
this.search = function(e){  
if(!filter) return;  
e = e || window.event;  
var ele = e.srcElement||e.target, value = ele.value, values;  
if(value){  
values = filter.search(value);  
}  
 _renderValues.call(this, filter, values);  
};  
  
this.clearSearch = function(){  
document.getElementById("searchbox").value="";  
if(!filter) return;   
_renderValues.call(this, filter);  
};  
  
Report.getDataContainerBy(context.dsid, _onGetDataContainer);  
  
</script>
```

Suppose that the trigger object is a group-by field Region, at runtime the customized control dialog looks like as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4404916831127/cmpnt_table_cc.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606202-Crosstabs)
