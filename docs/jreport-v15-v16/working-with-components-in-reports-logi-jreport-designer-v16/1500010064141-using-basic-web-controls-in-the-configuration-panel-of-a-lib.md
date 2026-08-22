---
title: "Using Basic Web Controls in the Configuration Panel of a Library Component"
id: 1500010064141
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064141-Using-Basic-Web-Controls-in-the-Configuration-Panel-of-a-Library-Component
updated_at: 2022-09-27T00:57:42Z
---

# Using Basic Web Controls in the Configuration Panel of a Library Component

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064101-Using-Forms-in-a-Page-Report)

# Using Basic Web Controls in the Configuration Panel of a Library Component

You can use the following basic web controls which are used as variables in the [configuration panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Config) of a library component: Text Field, Checkbox, List and Drop-down List, so as to filter or sort the records in the table, chart or crosstab of the library component or change the properties of an object in the library component at runtime.

Below is a list of the sections covered in this topic:

* [Using Text Fields](#Field)
* [Using Checkboxes](#Box)
* [Using Lists/Drop-down Lists](#List)

## Using Text Fields

1. Open the configuration panel of the library component and do one of the following:
   * Select **Insert** > **Web Controls** > **Text Field**, then drag the text field to the required destination.
   * From the Components panel, drag ![Text Field button](https://devnet.logianalytics.com/hc/article_attachments/4404901309463/btn_insttxtfld.gif) to the required destination.
2. Right-click the text field and select **Web Options**  from the shortcut menu. The Web Options dialog displays.

   ![Web Options dialog for Text Field](https://devnet.logianalytics.com/hc/article_attachments/4404909151127/wboptn_txtfld.gif)
3. Select the type of the text field: Standard or Password.

   Standard means that the text field will be a normal text field. Password means that the text field will be a password box in which the typed characters will be displayed as asterisks.
4. Enter the name, value for the text field in the Name and Value text boxes.
5. In the Tool Tip text box, enter the tooltip you want to show for the text field. The tooltip will be displayed when dashboard end users hover the mouse over the text field in JDashboard.
6. Set the character width in the Display Width text box, and the maximum number of characters the user can enter in the Max Length text box.
7. Check the **Read Only** option if you would like to set this text field to be read-only.
8. Check the **Disabled** checkbox if you want to make the text field disabled.
9. Select **OK** insert the text field.
10. Specify the web action you want to apply to the text field: [Filter](#Filter), [Sort](#Sort) or [Change Property](#Property).

    **To apply the Filter web action:**

    1. Right-click the text field and select **Web Behaviors** > **Filter**  from the shortcut menu. The [Filter - Web Behavior](https://devnet.logianalytics.com/hc/en-us/articles/1500010066161-Filter-Web-Behavior-Dialog) dialog appears.

       ![Filter - Web Behavior dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901260567/fltrwbbhvr.gif)
    2. From the Apply Action To drop-down list, select the data component the records of which you want to filter.
    3. In the Filter On column, specify the field on which to filter the records. The field may be a column in the component, or be specified by the value of the text field.
    4. Specify the operator to compose the filter condition.
    5. In the Value column, specify the value of how to filter the field. The value may be input by yourself, or be the value of the text field. When you enter the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
    6. Select **OK** to accept the settings.

    Then at runtime, when dashboard end users specify a value for the text field and select OK in the configuration panel, the records in the specified data component will be filtered.

    **To apply the Sort web action:**

    1. Right-click the text field and select **Web Behaviors** > **Sort**  from the shortcut menu. The [Sort - Web Behavior](https://devnet.logianalytics.com/hc/en-us/articles/1500010067901-Sort-Web-Behavior-Dialog) dialog appears.

       ![Sort - Web Behavior dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901179799/sortwbbhvr.gif)
    2. From the Apply Action To drop-down list, select the data component the records of which you want to sort.
    3. In the Sort On column, specify the field on which to sort the records. The field may be a column in the component, or be specified by the value of the text field.
    4. Specify the sort value. The value may be Ascending or Descending, or be the value of the text field.
    5. If necessary, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) to add a new sort condition.

       To delete a sort condition, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif). To adjust the order of the sort conditions, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif).
    6. Select **OK** to accept the settings.

    Then at runtime, when dashboard end users specify a value for the text field and select OK in the configuration panel, the records in the specified data component will be sorted.

    **To apply the Change Property web action:**

    1. Right-click the text field and select **Web Behaviors** > **Change Property** from the shortcut menu. The [Change Property - Web Behavior](https://devnet.logianalytics.com/hc/en-us/articles/1500010029882-Change-Property-Web-Behavior-Dialog) dialog appears.

       ![Change Property - Web Behavior dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901291671/chgptywbbhvr.gif)
    2. From the Apply Action To drop-down list, select the object the properties of which you want to change.
    3. In the Properties column, specify the property you want to change. All the properties of the object you select from the Apply Action To drop-down list are listed here.
    4. In the Value column, specify the value of the property. The value may be input by yourself, or be specified by the value of the text field.
    5. If necessary, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) to add a new line to change a property.

       To delete a property line, select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif). To adjust the order of the properties, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif).
    6. Select **OK** to accept the settings.

    Then at runtime, when dashboard end users specify a value for the text field and select OK in the configuration panel, the properties of the specified object in the library component will be changed.

**Tip:** The Change Property web action can also be applied on the following objects in the library component body: fields and labels in tables/crosstabs, some chart elements such as legend, chart axis and so on, markers and areas in geographic maps, labels, parameter controls and the Submit button of parameter form controls.

## Using Checkboxes

1. Open the configuration panel of the library component and do one of the following:
   * Select **Insert** > **Web Controls** > **Checkbox**, then drag the checkbox to the required destination.
   * From the Components panel, drag ![Checkbox button](https://devnet.logianalytics.com/hc/article_attachments/4404901309975/btn_instchkbx.gif) to the required destination.
2. Right-click the checkbox and select **Web Options**from the shortcut menu. The Web Options dialog displays.

   ![Web Options dialo for Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4404901168663/wboptn_chekbx.gif)
3. Specify the name, value of the checkbox in the Name and Value fields.
4. In the Tool Tip field, enter the tooltip you want to show for the checkbox button. The tooltip will be displayed when dashboard end users hover the mouse over the checkbox in JDashboard.
5. Set Initially Checked to **true** if you want the checkbox to be selected by default.
6. Check the **Disabled** checkbox if you want to make the checkbox disabled.
7. Select **OK** to insert the checkbox.
8. Specify the [web action](#Action) you want to apply to the checkbox.

## Using Lists/Drop-down Lists

1. Open the configuration panel of the library component and do one of the following:
   * Select **Insert** > **Web Controls** > **List**/**Drop-down List** , then drag the list/drop-down list to the required destination.
   * From the Components panel, drag ![List button](https://devnet.logianalytics.com/hc/article_attachments/4404901310743/btn_instlist.gif)/![Drop-down List button](https://devnet.logianalytics.com/hc/article_attachments/4404909267223/btn_instdrpdnlst.gif) to the required destination.
2. Right-click the list/drop-down list and select **Web Options** from the shortcut menu. The Web Options dialog displays.

   ![Web Options dialog for List](https://devnet.logianalytics.com/hc/article_attachments/4404901169175/wboptn_list.gif)
3. Specify the item labels and the value of each item in the items box by inputting some strings as the labels and values respectively.

   If you want to use a DBField/formula field/parameter field to control the value, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) in the Value column to insert one with the Insert Fields dialog, and then select the format for the inserted field from the drop-down list in the Item Label column. Check the **All** radio button in the Insert Field dialog if you want to add an All value to the list/drop-down list. Then when All is selected as value of the list/drop-down list at runtime, all filter actions defined on the list/drop-down list will not take effect, and if you applied some other web action that needs value from the list/drop-down list, a Null value will be returned.
4. For a list web control, you can check the **Allow Multiple Selections** checkbox if you want to allow multiple items to be selected.
5. In the Selected field, specify the selected value for the list/drop-down list.
6. To use the runtime value as the selected value, check **Use Runtime Value**.
7. If you want to disable the list/drop-down list, check the **Disabled** option.
8. Select **OK** to insert the list/drop-down list.
9. Specify the [web action](#Action) you want to apply to the list/drop-down list.

**Note:** If you have specified a tooltip for a text field or checkbox, the tooltip will be displayed differently on different browsers:

* On Internet Explorer, the tip text will be automatically wrapped if its length exceeds the maximal tip width the browser allows. In addition, for Internet Explorer, you can manually add a new line by adding &#10 or &#13 ahead of the text when editing it in the Tool Tip text box.
* On Firefox, the tip text will be displayed in one line with the maximal tip width the browser allows, and the text that cannot be displayed within the width will be cut off and replaced by ellipsis.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064101-Using-Forms-in-a-Page-Report)
