---
title: "Defining Web Behaviors of Objects in a Report"
id: 9898540480023
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report
updated_at: 2022-11-02T08:18:23Z
---

# Defining Web Behaviors of Objects in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735555544087-Changing-the-Display-Type-of-Objects-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735586301207-Setting-Up-Data-Container-Links-in-a-Report)

# Defining Web Behaviors of Objects in a Report

A web behavior contains a trigger event and a web action to be triggered when the event occurs on a specific object at runtime. By adding web behaviors to objects in your report, you can customize the objects to make them respond to interactive events, and execute corresponding web actions such as Sort and Filter. For example, you can associate a web action with an object's Click event, then at runtime, when users run the report and select the object, Server performs the specified operation. This topic describes the events you can use to trigger web actions and how you can specify the web behaviors of different objects in your report.

Generally, you can add web behaviors to basic web controls, labels, data fields, and special fields in a report. In a library component, you can also define web behaviors on chart elements and geographic map markers and areas.

This topic contains the following sections:

* [Trigger Events of Web Actions](#Event)
* [Specifying Web Behaviors of a Web Control/Label/Field](#WebControl)
  + [Applying the Parameter Web Action](#Parameter)
  + [Applying the Filter Web Action](#Filter)
  + [Applying the Sort Web Action](#Sort)
  + [Applying the Property Web Action](#Property)
  + [Applying the Go Down Web Action](#GoDown)
  + [Applying the Go Up Web Action](#GoUp)
  + [Applying the Go To Web Action](#GoTo)
  + [Applying the Send Message Web Action](#SendMessage)
* [Specifying Web Behaviors of a Chart](#Chart)
* [Specifying Web Behaviors of a Geographic Map](#GeoMap)

## Trigger Events of Web Actions

You can use the following events to trigger web actions.

| Event | Description |
| --- | --- |
| Blur | Fires when the object loses the input focus. |
| Data Change | Fires when the content of the object or selection changes. |
| Click | Fires when users select the left mouse button on the object. |
| onContextMenu | Fires when users select the right mouse button on the object, opening the shortcut menu. |
| Double\_Click | Fires when users double-click the object. |
| Focus | Fires when the object receives focus. |
| Key Down | Fires when users press a key. |
| Key Press | Fires when users press an alphanumeric key. |
| Key Up | Fires when users release a key. |
| Mouse Down | Fires when users select the object with either mouse button. |
| Mouse Move | Fires whens users move the mouse over the object. |
| Mouse Out | Fires when users move the mouse pointer outside the boundaries of the object. |
| Mouse Over | Fires when users move the mouse pointer into the object. |
| Mouse Up | Fires when users release a mouse button while the mouse is over the object. |
| Resize | Fires when the size of the object is about to change. |
| Scroll | Fires when users reposition the scroll box in the scroll bar on the object. |
| Select | Fires when the current selection changes. |

## Specifying Web Behaviors of a Web Control/Label/Field

You can specify the web behaviors of a basic web control while [defining its web options](https://devnet.logianalytics.com/hc/en-us/articles/5735527852183-Using-Basic-Web-Controls-in-a-Report), or of a label, data field, or special field while [changing its display type](https://devnet.logianalytics.com/hc/en-us/articles/5735555544087-Changing-the-Display-Type-of-Objects-in-a-Report), using the [Display Type dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513570199-Display-Type-Dialog-Box). However, for the basic web controls in the configuration panel of a library component, you need to use a different method to specify their web behaviors. See [Using Basic Web Controls in Library Component Configuration Panel](https://devnet.logianalytics.com/hc/en-us/articles/5735512656535-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component#Action).

**To specify the web behaviors of an object using the Display Type dialog box**

1. In the **Web Behaviors** panel of the Display Type dialog box, choose an event from the **Events** column, then select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif).

   ![Display Type dialog box - Text Field](https://devnet.logianalytics.com/hc/article_attachments/9898515531927/dsplytp_txtfld.gif)
2. In the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735531755159-Web-Action-List-Dialog-Box), select the required action and select **OK**. Designer displays different web actions in the dialog box according to the report type.

   ![Web Action List dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898477209367/wbactnlst.gif)

   * When you select one of the following web actions: [Parameter](#Parameter), [Filter](#Filter), [Sort](#Sort), [Property](#Property), [Go Down](#GoDown), [Go Up](#GoUp), [Go To](#GoTo), [Send Message](SendMessage), or [Customized Control](https://devnet.logianalytics.com/hc/en-us/articles/5735499153175-Using-Customized-Controls-in-Tables), Designer displays the corresponding web action builder dialog box for you to build the action.
   * When you select [Customized Control from Lib](https://devnet.logianalytics.com/hc/en-us/articles/5735499153175-Using-Customized-Controls-in-Tables), Designer displays the [Manage Customized Controls dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566696983-Manage-Customized-Controls-Dialog-Box), which shows all the customized control files in the customized control library. Select the one you want and select **OK**.
   * When you select a user-defined action which requires no parameter, for example, user\_showTOC, Designer applies the action to the web control and closes the Web Action List dialog box. You can use this type of web actions in query-based page reports only.
   * When you select a user-defined action which needs parameters, for example, user\_zoomTo, Designer displays the Parameters dialog box, which lists the parameters the web action requires. You can use this type of web actions in query-based page reports only. The following shows a sample dialog box.

     ![Parameters dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898523726359/rpt_wbbhv_prm.gif)

     + Specify the parameter values in the **Value** column.
     + For parameters that refer to instance name, you can type the mapping name of the instance, or the display name plus the prefix "&" as the parameter value.
     + For more information about the parameter values, see [Appendix 3: Parameters of User-Defined Web Actions](https://devnet.logianalytics.com/hc/en-us/articles/5735520289815-Appendix-3-Parameters-of-User-Defined-Web-Actions).

   You can also define your own web actions by adding API functions into the file **API.js** located at `<designer_install_root>\lib\html\javascript\dhtml` and the same name file located at `<server_install_root>\public_html\dhtmljsp\js`.
3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) in the Display Type dialog box and repeat the preceding steps to add more web behaviors to the object. To delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
4. Adjust the order of the web behaviors by selecting a web behavior and selecting **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif). Then, when an event that has been bound with more than one web action happens at runtime on the object, Server triggers the upper action first.

The following describes how to define a specific web action.

### Applying the Parameter Web Action

You can use the Parameter web action to run a specified report, especially one with parameters using the predefined parameter values when the designated event occurs on the trigger object at runtime.

**To define the Parameter web action**

1. In the Web Action List dialog box, select **\*Parameter** and select **OK**. Designer displays the [Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524319767-Parameter-Web-Action-Builder-Dialog-Box).

   ![Parameter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898461147415/prmwbactnbld.gif)
2. Specify the handler which receives the parameters of the web action. The handler may be the default one in the current server, or in another server specified by **Customized Path**.
3. From the **Get Input From** drop-down list, specify where to get the input, which may be a [form](https://devnet.logianalytics.com/hc/en-us/articles/5735564508951-Using-Forms-in-a-Page-Report) (available to page report only), a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Form) in the report, or "Other in report".
4. In the **Apply Action To** section, specify how to apply the action.
   * If you want to apply the action to run a report, select **Report** and select **Browse** to specify the report in the current catalog that you want to run when the event occurs on the trigger object at runtime; or select **Web Control** and select a web control in the current report to retrieve the report name at runtime. Then from the **Target Frame** drop-down list, select the window or frame to open the report.
   * Select **Refresh Current Report** if you want to refresh the current report when the event occurs on the trigger object at runtime.
5. In the parameter box, specify the parameters and the values with which to run or refresh the current report.
   * When you select Report and specify a report, if the report contains parameters, Designer loads the parameters automatically into the parameter box. Edit the value for each parameter.
   * When you select Web Control or Refresh Current Report, Designer lists all the parameters used by the current report in the parameter box if it contains parameters. Edit the value for each parameter.
   * You can also use web controls in the current report to retrieve the name and value of a parameter from the values of the web controls at runtime.
6. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add more parameter lines to specify other parameter values. If you specify a parameter value more than once, the last setting takes effect.
7. To delete a parameter, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the order of the parameter lines.
8. Select **OK** to accept the parameter values.

### Applying the Filter Web Action

You can use the Filter web action to filter a specified data component in a page report, or several data components at a time in a web report/library component based on predefined filter conditions when the designated event occurs on the trigger object at runtime.

**To define the Filter web action in a page report**

1. In the Web Action List dialog box, select **\*Filter** and select **OK**. Designer displays the [Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735500770711-Filter-Web-Action-Builder-Dialog-Box#Page).

   ![Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898464341783/fltrwbactnbld-pg.gif)
2. From the **Get Input From** drop-down list, specify where to get the input, which can be a [form](https://devnet.logianalytics.com/hc/en-us/articles/5735564508951-Using-Forms-in-a-Page-Report), a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Form) in the current page report, or "Other in report".
3. From the **Apply Action To** drop-down list, select a data component in the page report the data of which you want to filter.
4. In the **Filter On** column, specify the field on which to filter data. You can filter on a DBField in the query that the specified data component uses or a formula related to the query, or select a web control in the page report to retrieve the field name at runtime.
5. In the **Operator** column, specify the operator to compose the filter condition.
6. In the **Value** column, specify the value of how to filter the field. You can select **<Input...>** from the drop-down list and type the value in the text box, or select a web control to retrieve it at runtime.

   When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
7. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add more condition lines and specify the filter conditions. To delete a filter condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the order of the condition lines.
8. In the **More** column, specify the relationship between the filter conditions: "And" or "Or".
9. Select **OK** to accept the filter conditions.

**To define the Filter web action in a web report/library component**

1. In the Web Action List dialog box, select **\*Filter** and select **OK**. Designer displays the [Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735500770711-Filter-Web-Action-Builder-Dialog-Box#Web).

   ![Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898464348311/fltrwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current web report/library component the data of which you want to filter.
3. From the **Get Input From** drop-down list, specify where to get the input, which can be a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Form) in the web report/library component, or "Other in report".
4. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a filter condition line.
5. In the **Filter On** column, specify the field on which to filter data. You can filter on a field contained in the business view the specified data component uses, or select a web control in the web report/library component to retrieve the field name at runtime.
6. In the **Operator** column, specify the operator to compose the filter condition.
7. In the **Value** column, specify the value of how to filter the field. You can select **<Input...>** from the drop-down list and type the value in the text box, or select a web control to retrieve it at runtime. When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
8. Add more condition lines and specify the filter conditions. To delete a filter condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the order of the condition lines.
9. In the **More** column, specify the relationship between the filter conditions: "And" or "Or".
10. Select other data components in the Apply Action To box and take the preceding steps to specify the filter conditions on them.
11. Select **OK** to accept the filter conditions.

### Applying the Sort Web Action

You can use the Sort web action to sort a specified data component or group in a page report, or several data components and groups at a time in a web report/library component based on predefined sort conditions when the designated event occurs on the trigger object at runtime.

**To define the Sort web action in a page report**

1. In the Web Action List dialog box, select **\*Sort** and select **OK**. Designer displays the [Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544459671-Sort-Web-Action-Builder-Dialog-Box#Page).

   ![Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898477861655/sortwbactnbld-pg.gif)
2. From the **Get Input From** drop-down list, specify where to get the input, which can be a [form](https://devnet.logianalytics.com/hc/en-us/articles/5735564508951-Using-Forms-in-a-Page-Report), a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Form) in the current page report, or "Other in report".
3. From the **Apply Action To** drop-down list, select a data component in the current page report tab or a group of a table/banded object in the page report tab, the data of which you want to sort.
4. In the **Sort On** column,
   * If you select to sort a data component, you can sort on a field of the data component, or select a web control in the page report tab to retrieve the field name at runtime.
   * If you select to sort a group, leave the cell in the column blank or select a web control to retrieve the field name at runtime.
5. In the **Sort Value** column, specify the order to perform the sort: Ascending, Descending, or select a web control to get the sort order at runtime.
6. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add more condition lines and specify the sort conditions. To delete a sort condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
7. Adjust the order of the sort conditions using **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif). The order determines the sort priority of the conditions at runtime.
8. Select **OK** to accept the sort conditions.

**To define the Sort web action in a web report/library component**

1. In the Web Action List dialog box, select **\*Sort** and select **OK**. Designer displays the [Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544459671-Sort-Web-Action-Builder-Dialog-Box#Web).

   ![Sort - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898477868567/sortwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the web report/library component or a group of a table/banded object in the web report/library component, the data of which you want to sort.
3. From the **Get Input From** drop-down list, specify where to get the input, which can be a [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Form) in the current page report, or "Other in report".
4. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a sort condition.
5. In the **Sort On** column,
   * If you select to sort a data component, you can sort on a field of the data component, or select a web control in the web report/library component to retrieve the field name at runtime.
   * If you select to sort a group, leave the cell in the column blank or select a web control to retrieve the field name at runtime.
6. In the **Sort Value** column, specify the order to perform the sort: Ascending, Descending, or select a web control to get the sort order at runtime.
7. Add more condition lines and specify the sort conditions. To delete a sort condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
8. Adjust the order of the sort conditions using **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif). The order determines the sort priority of the conditions at runtime.
9. Select other data components and groups in the Apply Action To box and take the preceding steps to specify the sort conditions on them.
10. Select **OK** to accept the sort conditions.

### Applying the Property Web Action

You can use the Property web action to change properties of the specified report objects when the designated event occurs on the trigger object at runtime. However, you can apply this web action in web reports and library components only.

**To define the Property web action**

1. In the Web Action List dialog box, select **\*Property** and select **OK**. Designer displays the [Change Property - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508185111-Change-Property-Web-Action-Builder-Dialog-Box).

   ![Change Property - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898533153431/chgptywbactnbld.gif)
2. In the **Apply Action To** box, select an object in the current web report/library component the properties of which you want to change.
3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a property condition line.
4. In the **Properties** column, select the property of the object you want to change.
5. In the **Value** column, type the value of the property. You can also select a web control in the web report/library component to retrieve the value at runtime.
6. Add more condition lines and specify the property conditions. To delete a property condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the order of the condition lines.
7. Select other objects in the Apply Action To box and take the preceding steps to specify their property values.
8. Select **OK** to accept the property values.

### Applying the Go Down Web Action

You can use the Go Down web action to drill data of the specified data components to lower-level groups according to the predefined [hierarchies](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business views the data components use when the designated event occurs on the trigger object at runtime. However, you can apply this web action in web reports and library components only.

The Go Down web action works on the groups of tables and banded objects, the column and row fields of crosstabs, the category and series fields of charts, and the current layer of geographic maps.

**To define the Go Down web action**

1. In the Web Action List dialog box, select **\*Go Down** and select **OK**. Designer displays the [Go Down - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735543300759-Go-Down-Web-Action-Builder-Dialog-Box).

   ![Go Down - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898479420311/godwnwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current web report/library component whose data you want to drill through.
3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a condition line. You can add one condition only.
4. In the **Go Down On** column, select the group in the specified data component, on which to perform the go-down action. For a geographic map, it is "Current Layer" and you cannot change it.
5. In the **Use Hierarchy** column, select the hierarchy based on which to perform the go-down action.
   You can also select a web control in the web report/library component to retrieve a hierarchy name at runtime. For a geographic map, the "Built-in" hierarchy is used and you cannot change it.
6. In the **By Value** column, type a value of the specified group field to go down to the lower level with the filter condition "SpecifiedGroupField=TheValue". You can also use a web control to retrieve a value at runtime.
7. Select other data components in the Apply Action To box and take the preceding steps to define the go-down conditions for them.
8. Select **OK** to accept the conditions.

### Applying the Go Up Web Action

You can use the Go Up web action to drill data of the specified data components to upper-level groups according to the predefined [hierarchies](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog#Hierarchy) in the business views the data components use when the designated event occurs on the trigger object at runtime. However, you can apply this web action in web reports and library components only.

The Go Up web action works on the groups of tables and banded objects, the column and row fields of crosstabs, the category and series fields of charts, and the current layer of geographic maps.

**To define the Go Up web action**

1. In the Web Action List dialog box, select **\*Go Up** and select **OK**. Designer displays the [Go Up - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523517079-Go-Up-Web-Action-Builder-Dialog-Box).

   ![Go Up - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898479411991/goupwbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current web report/library component whose data you want to drill through.
3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a condition line. You can add one condition only.
4. In the **Go Up On** column, select a group in the specified data component, on which to perform the go-up action. For a geographic map, it is "Current Layer" and you cannot change it.
5. In the **Use Hierarchy** column, select the hierarchy based on which to perform the go-up action, or select a web control in the web report/library component to retrieve a hierarchy name at runtime. For a geographic map, the "Built-in" hierarchy is used and you cannot change it.
6. Select other data components in the Apply Action To box and take the preceding steps to define the go-up conditions for them.
7. Select **OK** to accept the conditions.

### Applying the Go To Web Action

You can use the Go To web action enables you to change the data fields in the specified data components when the designated event occurs on the trigger object at runtime. However, you can apply this web action in web reports and library components only.

The Go To web action works on the groups of tables, the column/row fields and aggregations of crosstabs, and the category and series fields of charts.

**To define the Go To web action**

1. In the Web Action List dialog box, select **\*Go To** and select **OK**. Designer displays the [Go To - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566447127-Go-To-Web-Action-Builder-Dialog-Box).

   ![Go To - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898462324119/gotowbactnbld.gif)
2. In the **Apply Action To** box, select a data component in the current web report/library component whose data field you want to change.
3. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a condition line. You can add one condition only.
4. In the **Go To On** column, select a group for a table or chart, or a column/row field or aggregation for a crosstab, on which to perform the go-to action.
5. In the **To Column** column, select another group object in the business view the web report/library component uses to change the "Go To On" field to, or select a web control in the web report/library component to retrieve a group name at runtime.
6. To apply the go-to action by filtering the "Go To On" field at the same time, select **By Value**, then select **<Input...>** from the drop-down list and type the value by which to filter the field in the text box or select a web control to retrieve the value at runtime. Skip this step if you select to perform the action on a crosstab aggregation.
7. Select other data components in the Apply Action To box and take the preceding steps to define the go-to conditions for them.
8. Select **OK** to accept the conditions.

### Applying the Send Message Web Action

You can use the Send Message web action to send out a message when the designated event occurs on the trigger object at runtime, to ask the message receivers to perform the specified operation in the message. However, you can apply this web action in library components only. See [Delivering Messages Between Library Components](https://devnet.logianalytics.com/hc/en-us/articles/5735576827671-Delivering-Messages-Between-Library-Components) for more information about the message mechanism of Logi Report.

**To define the Send Message web action**

1. In the Web Action List dialog box, select **\*SendMessage** and select **OK**. Designer displays the [Send Message - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524850583-Send-Message-Web-Action-Builder-Dialog-Box).

   ![Send Message - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898477882903/sndmsgwbactnbld.gif)
2. [Define the message](https://devnet.logianalytics.com/hc/en-us/articles/5735576827671-Delivering-Messages-Between-Library-Components#Message) you want to send out from the object.
3. Select **OK** to accept the settings.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When you select a web control in a condition to define a web action, Server should be able to retrieve a valid value from the web control at runtime in order to compose a valid condition; otherwise, nothing happens when the designated event occurs on the trigger object.

## Specifying Web Behaviors of a Chart

When you [format some elements of a chart](https://devnet.logianalytics.com/hc/en-us/articles/5735520553751-Formatting-Chart-Elements) in a library component, including the data markers, legend, and category (X) axis, Designer displays an additional Behaviors tab in the chart format dialog box for you to add web behaviors to the elements. For example, when formatting the chart legend, you see the Format Legend dialog box like this:

![Format Legend dialog box - Behavior](https://devnet.logianalytics.com/hc/article_attachments/9898480614551/fmtlgnd_bhvr.gif)

**To add web behaviors to a chart element**

1. In the **Behaviors** tab of the chart format dialog box, select a [trigger event](#Event) from the drop-down list in the **Events** column.
2. Select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif).
3. In the Web Action List dialog box, bind a web action that you want to trigger at runtime when the specified event occurs on the element. The web actions you can bind include [Filter](#Filter), [Sort](#Sort), [Parameter](#Parameter), [Property](#Parameter), and [Send Message](#SendMessage).
4. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add and define more web behaviors on the element. To delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
5. You can select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the order of the behaviors. At runtime, when an event that is bound with more than one web action happens, Server triggers the upper action first.

## Specifying Web Behaviors of a Geographic Map

When [creating geographic map](https://devnet.logianalytics.com/hc/en-us/articles/5735512449175-Inserting-Geographic-Maps-in-a-Report#Web) in a library component, you can bind web behaviors to the markers and areas of each group in the geographic map.

1. In the Display screen of the Create Geographic Map dialog box, select a group in the **Drill Path** box, then select **Web Behaviors**. Designer displays the [Web Behaviors dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544817687-Web-Behaviors-Dialog-Box).

   ![Add Web Behaviors to Geographic Map](https://devnet.logianalytics.com/hc/article_attachments/9898539869591/rpt_wbbhv_map.gif)
2. In the **Marker** tab, select a [trigger event](#Event) from the drop-down list in the **Events** column.
3. Select in the **Actions** column and select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif).
4. In the Web Action List dialog box, bind a web action that you want to trigger at runtime when the specified event occurs on the markers. The web actions you can bind include [Parameter](#Parameter), [Filter](#Filter), [Sort](#Sort), [Change Property](#Property), and [Send Message](SendMessage).
5. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add and define more web behaviors on the markers. To delete a web behavior, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
6. You can select a web behavior and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the order of the behaviors. At runtime, when an event that is bound with more than one web action happens, Server triggers the upper action first.
7. Switch to the **Area** tab to bind web behaviors to the areas of the group in the same way, if you enable areas for the geographic map.
8. Select **OK** to finish defining web behaviors of the markers and areas for the specified group and return to the map wizard.
9. Select other groups of the geographic map in the Drill Path box to specify web behaviors of their markers and areas.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735555544087-Changing-the-Display-Type-of-Objects-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735586301207-Setting-Up-Data-Container-Links-in-a-Report)
