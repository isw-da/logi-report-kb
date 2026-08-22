---
title: "Using Advanced Web Controls"
id: 1500009629421
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629421-Using-Advanced-Web-Controls
updated_at: 2021-07-24T16:05:10Z
---

# Using Advanced Web Controls

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606642-Using-Forms-in-a-Page-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606262-Images)

# Using Advanced Web Controls

Advanced web controls refer to Expand/Collapse Group, Parameter Control, Parameter Form Control, Filter Control, and Navigation Control. They are defined with specific web actions and are used for specific purposes.

The advanced web controls can be inserted into the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports#Relationship).

This topic includes the following sections:

* [Expanding/Collapsing the Group Records in Banded Objects](#Expand)
* [Using Parameter Controls to Specify Parameters to Reports](#Param)
* [Using Parameter Form Controls to Run Reports](#Form)
* [Using Filter Controls to Filter Report Data](#Filter)
* [Using Navigation Controls to Undo/Redo Value Selection in Filter Controls](#Navigate)

## Expanding/Collapsing the Group Records in Banded Objects

The Expand/Collapse Group web control can be used in the group header panels of banded objects in page reports, so that end users in Page Report Studio can use the web control to expand/collapse records in the groups of the banded objects. Note that, this feature works only in [continuous page mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages#Mode).

**To insert to a Expand/Collapse Group web control in a banded object:**

1. Make sure to clear the **Page Layout** command on the View menu.
2. Select the group header panel, then select **Insert** > **Web Control** > **Expand/Collapse Group**.
3. Select on the group header panel, and the web control will be inserted there.

After publishing the report to Logi Report Server and run it in Page Report Studio, end users will be able to use the web control which appears like a plus or minus sign to expand or collapse a group (that is, to show or hide the details of that group). Furthermore, you can use two properties of a group panel to set the expanding/collapsing state of all groups in the corresponding group level. That is, the Expand Detail Data property controls whether or not to expand the groups, and the Shrink Footer property controls whether or not to hide the group footer panel when collapsing the group.

## Using Parameter Controls to Specify Parameters to Reports

A parameter control is a web control that is bound with a parameter used by the current report. By specifying values to the parameter in a parameter control at runtime, end users can pass the parameter values to Logi Report and run the report with the specified values.

Parameter controls do not support inserting cascading parameters. If you want to do this, use [parameter form controls](#Form) instead.

**To insert a parameter control into a report**:

1. Do one of the following:
   * Drag ![Parameter Control](https://devnet.logianalytics.com/hc/article_attachments/4404916784791/btn_paramcntrl.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Parameter****Control**, then select the mouse button in the destination.

   The [Insert Parameter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009608842-Insert-Parameter-Control-Dialog) dialog appears.

   ![Insert Parameter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904266135/instprmtrctrl.gif)
2. In the dialog, specify the parameter you want to add to the parameter control from the Select a Parameter box, which lists all the parameters except cascading parameters used in the current report. For a report created using business views, you can also use [a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param).
3. Select **OK** to insert the parameter control.

## Using Parameter Form Controls to Run Reports

A parameter form control is a web control that is bound with the parameters used by the current report or other reports. By specifying values to the parameters in a parameter form control at runtime, end users can run the reports with the specified parameter values.

**To insert a parameter form control into a report:**

1. Do one of the following:
   * Drag ![Parameter Form Control button](https://devnet.logianalytics.com/hc/article_attachments/4404904265367/btn_paramfrmcntrl.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Parameter Form Control**, then select the mouse button in the destination.

   The [Insert Parameter Form Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009632241-Insert-Parameter-Form-Control-Dialog) dialog appears.

   ![Insert Parameter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904265879/instprmtrfrmctrl.gif)
2. Specify the target reports to run using the parameter form control.
   * To run the current report, select **Current Report**, then specify the parameters used to run the report from the Select Parameters box. For a report created using business views, you can also use [local parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param) to run it.
   * To run other reports, select **Others**, then select the reports you want to run. If all the selected reports contain no parameters, you cannot finish the dialog.
3. Specify whether to include the Submit button in the parameter form control. If Submit is included, it is used to submit the parameter values end users specify in the parameter form control. If Submit is not included, once end users change the value of a parameter in the parameter form control, the new value will be applied automatically.
4. Select **OK** to insert the parameter form control.

**Note:** If you save a report containing a parameter form to another directory or publish it to local directory or to Logi Report Server, the reports that you selected in the parameter form in order to run will not be saved or published along with the report. You need to ensure that all the reports are published to the same folder on Logi Report Server.

## Using Filter Controls to Filter Report Data

Filter controls are used to filter one or more data components in a report based on the fields in the data resources the data components are created from. After inserting filter controls, you can also insert a [navigation control](#Navigate) for undoing/redoing the value selection in the filter controls. The filter created via filter control is also referred to as on-screen filter.

**Filter control types**

Logi Report Designer supports four types of filter controls:

* **Text List** allows you to pick one or more random values from a list and is used with categorical or nominal variables. You can choose one or more values from anywhere in the list and there is no mean or median value calculation.
* **Drop-down List** functions basically the same as Text List. It differs from the Text List type by listing values by means of a drop-down list so that it takes less space in a report. In a drop-down list filter control, checkboxes are provided ahead of the values for easy selection of multiple values. This type is supported in web reports and library components.
* **Single Value Slider** allows you to select one single value from a list and suitable for displaying a few values like quarters. This type is supported in library components.
* **Range Slider** allows you to pick multiple sequential values from a list and is used for interval variables such as dates, times, quantity and currency variables where the slider represents the scale from lowest to highest values and the middle represents the median value. This type is supported in library components.

**Filtering scenarios and filter logic**

Filtering based on one field is a common usage. Bind a field to a filter control, and then based on the field to filter the data components created from the same data resource as the field. Another special usage is to filter data components created using different data resources. In this case you need to choose a common field all the data resources contain and select the common field from all the data resources to bind them to the filter control. The name of the fields do not need to be the same but the data returned needs to be similar.

After you select values in one or more filter controls in a report, a filter condition based on the selected values of the specified fields will be applied to the designated data components in the report, with each field affecting only the data components based on the same data resource as the field. The value selection logic is as follows:

* When one value of one field is selected, the filter condition is *Field1=SelectedValue1*, for example, *Country=USA*. The filter condition will be applied to the data components that are created using the same data resource as the field.
* When multiple values of multiple fields in one data resource are selected, the filter condition uses AND logic between the fields: *(Field1=SelectedValue1 or Field1=SelectedValue2) and (Field2=SelectedValue3 or Field2=SelectedValue4)...*, for example, *(Country=USA or Country=China) and (Year=2017 or Year=2018)*. The filter condition will be applied to the data components that are created using the data resource.
* When multiple values of multiple fields in different data resources are selected, the filter condition uses OR logic between the fields: *(Field1=SelectedValue1 or Field1=SelectedValue2) or (Field2=SelectedValue3 or Field2=SelectedValue4)...*, for example, *(Country=USA or Country=China) or (Year=2017 or Year=2018)*. The filter condition will be applied to all the data components that are created using these data resource.

**To insert a filter control in a report:**

1. Do any of the following:
   * Drag ![Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404904266647/btn_instfltrcntrl.gif) from the Components panel to the destination.
   * Select **Insert** > **Web Controls** > **Filter Control**, then select the mouse button in the destination.

   The [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009632161-Insert-Filter-Control-Dialog) dialog appears.

   ![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916785303/instfltrctrl.gif)
2. The Control Type drop-down list lists the [filter control types](#Type) that can be used in the current report. Select the type you need.
3. From the Select Fields drop-down list, select the fields of the same data type to bind to the filter control, then select outside of the drop-down list to close it.

   ![Select Fileds for Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404904421783/cmpnt_wbcntrl_advc_fltr1.gif)

   For a text list filter control, after the filter control is created the name of the first displayed field you select in the field list will be used as the name of the filter control.
4. By default all values of the selected fields are used in the filter control except for the drop-down list filter control which can display 300 values at most. If you want to customize the value list, select **Customize Initial Values**  and customize the values as you want.
   * **To customize the values for a text list, drop-down list or single value slider**:  
      select **Fetch Data** to select values from the database in the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009631741-Fetch-Data-Dialog) dialog. You can also type the values manually in the value text box.

     ![Customize Values for Text List/Single Value Slider](https://devnet.logianalytics.com/hc/article_attachments/4404904266903/cmpnt_wbcntrl_advc_fltr2.gif)

     To add a value, type it in one row, and then press the **Enter** key to start a new row. General text editing operations including Copy, Paste, Cut, Backspace, Delete, and so on are supported. You need to make sure of the accuracy of the formats and values. If the selected fields are of the Date/Time type, you can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404904203031/btn_clndr.gif) to specify a date and time value from the calendar.
   * **To customize the values for a range slider:**  
      Select the start value of the slider from the From drop-down list and the end value from the To drop-down list. If the selected fields are of the Date/Time type, you can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404904203031/btn_clndr.gif) to specify a date and time value from the calendar.

     ![Customize Values for Range Value Slider](https://devnet.logianalytics.com/hc/article_attachments/4404916785559/cmpnt_wbcntrl_advc_fltr3.gif)
5. By default, all filter controls that are applied to the same data components are linked. Selecting a value in one filter control, for example, USA, will result in that all the other linked filter controls respond to gray the values that do not belong to or contain USA or that are not related to USA like London. If you do not want the filter control to be affected by other filter controls, unselect **Link to Other Filters**. For the case of one filter control using a business view and another using a query, if the business view contains the query definition, the two filter controls are also linked.
6. If you are creating a slider and the fields selected to bind to the slider are of the Date/Time type, the Special Function drop-down list is available. You can apply a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables#Function) to the fields.
7. From the Apply To drop-down list, specify which data components the filter will be applied to.

   By default, Logi Report applies the filter to all the data components created using the data resources in which the selected fields are obtained. If you do not select the data components which are based on the same data resource as any selected fields, these fields will not be used in the filter and thus their values will not be listed in the filter control.
8. Select **OK** to insert the filter control.

   At runtime, end users can select one or more values from the text list or drop-down list filter control, a value from the single value slider, or a value range on the range slider to filter the specified data components. If the fields bound to the filter control have the same values, the values are distinctive in the filter control.

For the filter controls inserted into a report, you can further edit them if you want. To edit a filter control, right-click the filter control and select **Edit Filter Control** from the shortcut menu. In the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009630681-Edit-Filter-Control-Dialog) dialog, edit the filter control settings.

**Note:** If all the data components in a report created on the same data resource are deleted, the fields in the data resource that have been added in the filter controls in the report will be removed from the filter controls too.

## Using Navigation Controls to Undo/Redo Value Selection in Filter Controls

A navigation control can be considered as an accessorial control for filter controls and is used to deal with the value selection operations in all the filter controls in the same report.

To insert a navigation control into a report, do either of the following:

* Drag ![Navigation Control button](https://devnet.logianalytics.com/hc/article_attachments/4404904422039/btn_instnvgtncmtrl.gif) from the Components panel to the destination.
* Select **Insert** > **Web Controls** > **Filter Control**, then point to the destination where you want to add the navigation control and select the mouse button.

A navigation control is a combination of three buttons:

* **Back**  
   Goes back to the previous value selection status and refreshes the report data accordingly.
* **Clear**  
   Removes all the value selection histories and all the filter conditions based on the selections, and refreshes the report data accordingly.
* **Forward**  
   Goes forward to the next value selection status and refreshes the report data accordingly.

By default, these three buttons are displayed as normal buttons, however, you can change their button type to be image button. To do this:

1. Select the target button, right-click it and select **Button Type** > **Image Button** from the shortcut menu.
2. In the Image Button dialog, select **Browse** to specify the path or type the URL of the image source in the text box.

   ![Image Button dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904268695/imgbtn.gif)
3. Select **OK** to confirm.

If you want to get back the normal button type, you just need to right-click the target image button, and select **Normal Button** from the Button Type submenu.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606642-Using-Forms-in-a-Page-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606262-Images)
