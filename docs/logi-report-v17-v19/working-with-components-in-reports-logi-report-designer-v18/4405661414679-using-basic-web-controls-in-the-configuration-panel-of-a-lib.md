---
title: "Using Basic Web Controls in the Configuration Panel of a Library Component"
id: 4405661414679
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661414679-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component
updated_at: 2022-01-27T20:34:37Z
---

# Using Basic Web Controls in the Configuration Panel of a Library Component

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661413527-Using-Forms-in-a-Page-Report)

# Using Basic Web Controls in the Configuration Panel of a Library Component

This topic introduces how you can use the basic web controls in the configuration panel of a library component for specific purposes.

You can use the following basic web controls as variables in the [configuration panel](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#Config) of a library component: Text Field, Checkbox, List, and Drop-down List, so as to filter or sort the tables, charts, or crosstabs in the library component, or change properties of the objects in the library component at runtime.

This topic contains the following sections:

* [Using Text Fields](#Field)
* [Using Checkboxes](#Box)
* [Using Lists/Drop-down Lists](#List)

## Using Text Fields

1. Open the configuration panel of the library component.
2. Do either of the following:
   * From the **Components** panel, drag the **Text Field** icon ![Text Field icon](https://devnet.logianalytics.com/hc/article_attachments/4420394874775/icon_txtfld.gif) in the **Web Controls** category to the required destination.
   * Navigate to **Home**/**Insert** > **Web Controls** > **Text Field**, then drag the text field to the desired position.
3. Right-click the text field and select **Web Options** from the shortcut menu. Designer displays the [Web Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661746199-Web-Options-Dialog-Box#Text).

   ![Web Options dialog box for Text Field](https://devnet.logianalytics.com/hc/article_attachments/4420394715159/wboptn_txtfld.gif)
4. Select **Standard** to use the text field as a normal text field, or **Password** to use the text field as a password box in which the typed characters display as asterisks.
5. Specify the name, value for the text field in the **Name** and **Value** text boxes.
6. In the **Tool Tip** text box, specify the tool tip you want to show for the text field. The tool tip displays when the dashboard users hover the mouse over the text field in JDashboard.
7. Set the character width in the **Display Width** text box, and the maximum number of characters the user can specify in the **Max Length** text box.
8. Select **Read Only** if you would like to set this text field to be read-only.
9. Select **Disabled** if you want to disable the text field at runtime.
10. Select **OK** to finish defining the web options of the text field.
11. Specify the web action you want to apply to the text field: [Filter](#Filter), [Sort](#Sort), or [Change Property](#Property).

    **To apply the Filter web action**

    1. Right-click the text field and navigate to **Web Behaviors** > **Filter** on the shortcut menu. Designer displays the [Filter - Web Behavior dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661555863-Filter-Web-Behavior-Dialog-Box).

       ![Filter - Web Behavior dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402481815/fltrwbbhvr.gif)
    2. From the **Apply Action To** drop-down list, select a data component in the library component the data of which you want to filter.
    3. In the **Filter On** column, specify the field on which to filter data. You can filter on a field included in the business view the specified data component uses, or use a web control that you add in the configuration panel of the library component to get the field name from the web control at runtime.
    4. In the **Operator** column, select the operator to compose the filter condition.
    5. In the **Value** column, specify the value of how to filter the field. You can select **<Input...>** and type the value in the text box, or select a web control to get the value at runtime.

       When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
    6. Select **OK** to accept the settings.

    Then at runtime, when the dashboard users specify a value for the text field and select OK in the configuration panel, JDashboard filters the specified data component based on the condition.

    **To apply the Sort web action**

    1. Right-click the text field and navigate to **Web Behaviors** > **Sort** on the shortcut menu. Designer displays the [Sort - Web Behavior dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661723543-Sort-Web-Behavior-Dialog-Box).

       ![Sort - Web Behavior dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420394728087/sortwbbhvr.gif)
    2. From the **Apply Action To** drop-down list, select a data component in the library component the data of which you want to sort, or a group of a table in the library component to sort the groups in the group level.
    3. In the **Sort On** column, specify the field on which to sort data. If you select to sort a data component, you can sort on a field the data component contains, or use a web control that you add in the configuration panel of the library component to get the field name from the web control at runtime; if you select a table group, you can only use a web control to get the field name.
    4. In the **Sort Value** column, specify the order to perform the sort: Ascending, Descending, or select a web control to obtain the sort order at runtime.
    5. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif) to add more condition lines and specify the sort conditions. To delete a sort condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif).
    6. Adjust the order of the sort conditions using **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif). The order determines the sort priority of the conditions at runtime.
    7. Select **OK** to accept the settings.

    Then at runtime, when the dashboard users specify a value for the text field and select OK in the configuration panel, JDashboard sorts the specified data component or table group based on the conditions.

    **To apply the Change Property web action**

    1. Right-click the text field and navigate to **Web Behaviors** > **Change Property** on the shortcut menu. Designer displays the [Change Property - Web Behavior dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664432407-Change-Property-Web-Behavior-Dialog-Box).

       ![Change Property - Web Behavior dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420410843287/chgptywbbhvr.gif)
    2. From the **Apply Action To** drop-down list, select an object in the library component the properties of which you want to change.
    3. In the **Properties** column, select the property of the object you want to change.
    4. In the **Value** column, specify the value of the property. You can select **<Input...>** and type the value in the text box, or select a web control that you add in the configuration panel of the library component to get the value at runtime.
    5. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif) to add more condition lines and specify the property conditions. To delete a property condition, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif) to adjust the order of the condition lines.
    6. Select **OK** to accept the settings.

    Then at runtime, when the dashboard users specify a value for the text field and select OK in the configuration panel, JDashboard changes properties of the specified object in the library component.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg)

* When you select a web control in the condition to define a web action, JDashboard should be able to retrieve a valid value from the web control at runtime in order to compose a valid condition; otherwise, nothing happens when the action is triggered.
* You can also apply the Change Property web action to the following objects in the library component body: fields and labels in tables/crosstabs, some chart elements such as legend and chart axis, markers and areas in geographic maps, labels, parameter controls, and the Submit button of parameter form controls.

## Using Checkboxes

1. Open the configuration panel of the library component.
2. Do either of the following:
   * From the **Components** panel, drag the **Checkbox** icon ![Checkbox icon](https://devnet.logianalytics.com/hc/article_attachments/4420410862999/icon_chkbx.gif) in the **Web Controls** category to the required destination.
   * Navigate to **Home**/**Insert** > **Web Controls** > **Checkbox**, then drag the checkbox to the desired position.
3. Right-click the checkbox and select **Web Options** from the shortcut menu. Designer displays the [Web Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661746199-Web-Options-Dialog-Box#Checkbox).

   ![Web Options dialo for Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4420394715671/wboptn_chekbx.gif)
4. Specify the name, value of the checkbox in the **Name** and **Value** text boxes.
5. In the **Tool Tip** text box, type the tool tip you want to show for the checkbox. The tool tip displays when the dashboard users hover the mouse over the checkbox in JDashboard.
6. Set **Initially Checked** to **true** if you want the checkbox to be selected by default.
7. Select **Disabled** if you want to disable the checkbox at runtime.
8. Select **OK** to finish defining the web options of the checkbox.
9. Specify the [web action](#Action) you want to apply to the checkbox.

## Using Lists/Drop-down Lists

1. Open the configuration panel of the library component.
2. Do either of the following:
   * From the **Components** panel, drag the **List**![List icon](https://devnet.logianalytics.com/hc/article_attachments/4420394876183/icon_list.gif)/**Drop-down List**![Drop-down List icon](https://devnet.logianalytics.com/hc/article_attachments/4420410863895/icon_drpdnlst.gif) icon in the **Web Controls** category to the required destination.
   * Navigate to **Home**/**Insert** > **Web Controls** > **List**/**Drop-down List**, then drag the list/drop-down list to the desired position.
3. Right-click the list/drop-down list and select **Web Options** from the shortcut menu. Designer displays the [Web Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661746199-Web-Options-Dialog-Box#List).

   ![Web Options dialog box for List](https://devnet.logianalytics.com/hc/article_attachments/4420410653463/wboptn_list.gif)
4. Specify the item labels and the value of each item in the item box by inputting some strings as the labels and values respectively.

   If you want to use a DBField, formula field, or parameter field to control the value, select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420410588951/btn_ellipsis1.gif) in the **Value** column to insert one using the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661626647-Insert-Fields-Dialog-Box), and then select the format for the inserted field from the drop-down list in the **Item Label** column. Select **All** in the Insert Field dialog box if you want to add an "All" value to the list/drop-down list. Then when the dashboard users select "All" as value of the list/drop-down list at runtime, all filter actions defined on the list/drop-down list will not take effect, and if you apply some other web action that needs value from the list/drop-down list, JDashboard returns a "Null" value.
5. In the **Selected** field, specify the selected value for the list/drop-down list.
6. Select **Disabled** if you want to disable the list/drop-down list at runtime.
7. For a list web control, you can also specify the following settings: select **Allow Multiple Selections** if you want to allow multiple items to be selected in the list, specify to display the list as Text, Button, Checkbox, or Radio Button, use the vertical or horizontal layout to display items in the list, and specify the width/height of each item and the vertical/horizontal gap between two adjacent items in the list.
8. Select **OK** to finish defining the web options of the list/drop-down list.
9. Specify the [web action](#Action) you want to apply to the list/drop-down list.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) If you have specified a tool tip for a text field or checkbox, the tool tip displays differently on different browsers.

* On Internet Explorer, the tip text is automatically wrapped if its length exceeds the maximal tip width the browser allows. In addition, for Internet Explorer, you can manually add a new line by adding "&#10" or "&#13" ahead of the text when editing it in the Tool Tip text box.
* On Firefox, the tip text displays in one line with the maximal tip width the browser allows, and the text that it cannot display within the width is cut off and replaced by an ellipsis (...).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661415703-Using-Basic-Web-Controls-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661413527-Using-Forms-in-a-Page-Report)
