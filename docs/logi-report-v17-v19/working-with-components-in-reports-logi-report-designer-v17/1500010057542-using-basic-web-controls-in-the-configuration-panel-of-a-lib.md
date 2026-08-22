---
title: "Using Basic Web Controls in the Configuration Panel of a Library Component"
id: 1500010057542
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057542-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component
updated_at: 2021-07-23T19:14:52Z
---

# Using Basic Web Controls in the Configuration Panel of a Library Component

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057522-Using-Forms-in-a-Page-Report)

# Using Basic Web Controls in the Configuration Panel of a Library Component

This topic introduces how you can use the basic web controls in the configuration panel of a library component for specific purposes.

You can use the following basic web controls which are used as variables in the [configuration panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Config) of a library component: Text Field, Checkbox, List, and Drop-down List, so as to filter or sort the records in the table, chart or crosstab of the library component, or change the properties of an object in the library component at runtime.

This topic contains the following sections:

* [Using Text Fields](#Field)
* [Using Checkboxes](#Box)
* [Using Lists/Drop-down Lists](#List)

## Using Text Fields

1. Open the configuration panel of the library component and do one of the following:
   * Select **Insert** > **Web Controls** > **Text Field**, then drag the text field to the required destination.
   * From the **Components** panel, drag the **Text Field** icon ![Text Field icon](https://devnet.logianalytics.com/hc/article_attachments/4404848655511/icon_txtfld.gif) in the Web Controls category to the required destination.
2. Right-click the text field and select **Web Options** from the shortcut menu. Designer displays the [Web Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099161-Web-Options-Dialog-Box#Text).

   ![Web Options dialog box for Text Field](https://devnet.logianalytics.com/hc/article_attachments/4404848482199/wboptn_txtfld.gif)
3. Select the type of the text field: **Standard** or **Password**.

   Standard means that the text field is a normal text field. Password means that the text field is a password box in which the typed characters are displayed as asterisks.
4. Specify the name, value for the text field in the **Name** and **Value** text boxes.
5. In the **Tool Tip** text box, specify the tool tip you want to show for the text field. The tool tip displays when the dashboard users hover the mouse over the text field in JDashboard.
6. Set the character width in the **Display Width** text box, and the maximum number of characters the user can specify in the **Max Length** text box.
7. Select the **Read Only** option if you would like to set this text field to be read-only.
8. Select the **Disabled** checkbox if you want to make the text field disabled.
9. Select **OK** to finish defining the web options of the text field.
10. Specify the web action you want to apply to the text field: [Filter](#Filter), [Sort](#Sort), or [Change Property](#Property).

    **To apply the Filter web action:**

    1. Right-click the text field and select **Web Behaviors** > **Filter**  from the shortcut menu. Designer displays the [Filter - Web Behavior dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059062-Filter-Web-Behavior-Dialog-Box).

       ![Filter - Web Behavior dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848576023/fltrwbbhvr.gif)
    2. From the **Apply Action To** drop-down list, select the data component the records of which you want to filter.
    3. In the **Filter On** column, specify the field on which to filter the records. The field may be a column in the component, or be specified by the value of the text field.
    4. Specify the operator to compose the filter condition.
    5. In the **Value** column, specify the value of how to filter the field. The value may be specified by yourself, or be the value of the text field. When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".
    6. Select **OK** to accept the settings.

    Then at runtime, when the dashboard users specify a value for the text field and select OK in the configuration panel, JDashboard filters the records in the specified data component.

    **To apply the Sort web action:**

    1. Right-click the text field and select **Web Behaviors** > **Sort**  from the shortcut menu. Designer displays the [Sort - Web Behavior dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098841-Sort-Web-Behavior-Dialog-Box).

       ![Sort - Web Behavior dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856894231/sortwbbhvr.gif)
    2. From the **Apply Action To** drop-down list, select the data component the records of which you want to sort.
    3. In the **Sort On** column, specify the field by which to sort the records. The field may be a column in the component, or be specified by the value of the text field.
    4. Specify the sort value. The value may be **Ascending** or **Descending**, or be the value of the text field.
    5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more sort conditions and specify the sort-by fields and sort direction according to your requirements.

       To delete a sort condition, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the sort conditions, select a condition and select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button.
    6. Select **OK** to accept the settings.

    Then at runtime, when the dashboard users specify a value for the text field and select OK in the configuration panel, JDashboard sorts the records in the specified data component.

    **To apply the Change Property web action:**

    1. Right-click the text field and select **Web Behaviors** > **Change Property** from the shortcut menu. Designer displays the [Change Property - Web Behavior dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095681-Change-Property-Web-Behavior-Dialog-Box).

       ![Change Property - Web Behavior dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848630167/chgptywbbhvr.gif)
    2. From the **Apply Action To** drop-down list, select the object the properties of which you want to change.
    3. In the **Properties** column, specify the property you want to change. All the properties of the object you select from the Apply Action To drop-down list are available here.
    4. In the **Value** column, specify the value of the property. The value may be typed in by yourself, or be specified by the value of the text field.
    5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add more property conditions and specify the properties and values according to your requirements.

       To delete a property condition, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif); to adjust the order of the property conditions, select a condition and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif).
    6. Select **OK** to accept the settings.

    Then at runtime, when the dashboard users specify a value for the text field and select OK in the configuration panel, JDashboard changes the properties of the specified object in the library component.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You can also apply the Change Property web action to the following objects in the library component body: fields and labels in tables/crosstabs, some chart elements such as legend and chart axis, markers and areas in geographic maps, labels, parameter controls, and the Submit button of parameter form controls.

## Using Checkboxes

1. Open the configuration panel of the library component and do one of the following:
   * Select **Insert** > **Web Controls** > **Checkbox**, then drag the checkbox to the required destination.
   * From the **Components** panel, drag the **Checkbox** icon ![Check Box icon](https://devnet.logianalytics.com/hc/article_attachments/4404848657047/icon_chkbx.gif) in the Web Controls category to the required destination.
2. Right-click the checkbox and select **Web Options**from the shortcut menu. Designer displays the [Web Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099161-Web-Options-Dialog-Box#Checkbox).

   ![Web Options dialo for Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4404848482455/wboptn_chekbx.gif)
3. Specify the name, value of the checkbox in the **Name** and **Value** text boxes.
4. In the **Tool Tip** text box, type the tool tip you want to show for the checkbox button. The tool tip displays when the dashboard users hover the mouse over the checkbox in JDashboard.
5. Set **Initially Checked** to **true** if you want the checkbox to be selected by default.
6. Select the **Disabled** checkbox if you want to make the checkbox disabled.
7. Select **OK** to finish defining the web options of the checkbox.
8. Specify the [web action](#Action) you want to apply to the checkbox.

## Using Lists/Drop-down Lists

1. Open the configuration panel of the library component and do one of the following:
   * Select **Insert** > **Web Controls**> **List**/**Drop-down List** , then drag the list/drop-down list to the required destination.
   * From the **Components** panel, drag the **List**![List icon](https://devnet.logianalytics.com/hc/article_attachments/4404848657943/icon_list.gif)/**Drop-down List**![Drop-down List icon](https://devnet.logianalytics.com/hc/article_attachments/4404848658455/icon_drpdnlst.gif) icon in the Web Controls category to the required destination.
2. Right-click the list/drop-down list and select **Web Options** from the shortcut menu. Designer displays the [Web Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099161-Web-Options-Dialog-Box#List).

   ![Web Options dialog box for List](https://devnet.logianalytics.com/hc/article_attachments/4404848482967/wboptn_list.gif)
3. Specify the item labels and the value of each item in the items box by inputting some strings as the labels and values respectively.

   If you want to use a DBField, formula field, or parameter field to control the value, select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the **Value** column to insert one with the Insert Fields dialog box, and then select the format for the inserted field from the drop-down list in the **Item Label** column. Select the **All** radio button in the Insert Field dialog box if you want to add an "All" value to the list/drop-down list. Then when the dashboard users select "All" as value of the list/drop-down list at runtime, all filter actions defined on the list/drop-down list will not take effect, and if you applied some other web action that needs value from the list/drop-down list, JDashboard returns a "Null" value.
4. In the **Selected** field, specify the selected value for the list/drop-down list.
5. If you want to disable the list/drop-down list, select the **Disabled** option.
6. For a list web control, you can select the **Allow Multiple Selections** checkbox if you want to allow multiple items to be selected in the list, specify to display the list as Text, Button, Checkbox, or Radio Button, use the vertical or horizontal layout to display items in the list, and specify the width/height of each item and the vertical/horizontal gap between two adjacent items in the list.
7. Select **OK** to finish defining the web options of the list/drop-down list.
8. Specify the [web action](#Action) you want to apply to the list/drop-down list.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If you have specified a tool tip for a text field or checkbox, the tool tip displays differently on different browsers:

* On Internet Explorer, the tip text is automatically wrapped if its length exceeds the maximal tip width the browser allows. In addition, for Internet Explorer, you can manually add a new line by adding "&#10" or "&#13" ahead of the text when editing it in the Tool Tip text box.
* On Firefox, the tip text displays in one line with the maximal tip width the browser allows, and the text that it cannot display within the width is cut off and replaced by an ellipsis (...).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057522-Using-Forms-in-a-Page-Report)
