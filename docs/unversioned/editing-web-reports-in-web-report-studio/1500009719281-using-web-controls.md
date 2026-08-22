---
title: "Using Web Controls"
id: 1500009719281
section: "Editing Web Reports in Web Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719281-Using-Web-Controls
updated_at: 2021-11-03T06:56:26Z
---

# Using Web Controls

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719141-Applying-Filters)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719101-Adding-Conditional-Formats-to-Data-Fields)

# Using Web Controls

Web controls are report components designed to be similar to the kinds of controls found on web pages. In Web Report Studio, these four types of web controls can be applied: parameter control, parameter form control, filter control, and navigation control.

Below is a list of the sections covered in this topic:

* [Using Parameter Control to Specify a Parameter to a Report](#Parameter)
* [Using Parameter Form Control to Run Reports](#Form)
* [Using Filter Control to Filter Report Data](#Filter)
* [Using Navigation Control to Undo/Redo Value Selection in Filter Controls](#Navigation)

## Using Parameter Control to Specify a Parameter to a Report

A parameter control is a web control that is bound with a parameter used by the current report. By specifying values to the parameter in a parameter control, you can pass the parameter values to Logi JReport and run the report with the specified values.

Cascading parameters cannot be used in parameter controls. If you want to do this, use parameter form controls instead.

**To insert a parameter control and use it to specify a parameter to a web report**:

1. Drag **Parameter Control** from the Components panel to the destination in the report. The [Insert Parameter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009690422-Insert-Parameter-Control) dialog appears.

   ![Insert Parameter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131378711/insrtprmctrl.gif)
2. Select the parameter you would like to add to the parameter control.
3. Select **OK** to insert the parameter control.
4. Switch Web Report Studio to View Mode to [specify the value for the parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009719221-Applying-Parameters). Once the value in the parameter control changes, the report will re-run with the new parameter value.

**Note:** If the specified parameter is no longer used in the report, the parameter control will become invalid.

## Using Parameter Form Control to Run Reports

A parameter form control is a web control that is bound with the parameters used by the current report or other reports. By specifying values to the parameters in a parameter form control, you can make the reports run with the specified parameter values.

**To insert a parameter form control and use it to run web reports:**

1. Drag **Parameter Form Control** from the Components panel to the destination in the report. The [Insert Parameter Form Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009690442-Insert-Parameter-Form-Control) dialog appears.

   ![Insert Parameter Form Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4412139488407/insrtprmfrmctrl.gif)
2. Specify the target reports to run using the parameter form control.
   * To run the current report, select **Current Report**, then specify the parameters used to run the report from the Select Parameters box.
   * To run other reports, select **Others**, then select the reports you want to run. If all the selected reports contain no parameters, you cannot finish the dialog.
3. Specify whether to include the Submit button in the parameter form control. If Submit is included, it is used to submit the parameter values you specified in the parameter form control. If Submit is not included, once you change the values of a parameter in the parameter form control, the new values will be applied automatically.
4. Select **OK**.
   The parameter form control is now inserted in the report, listing the selected parameters for the current report or all parameters used by the specified reports.
5. Switch Web Report Studio to View Mode to [specify values of the listed parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009719221-Applying-Parameters) in the parameter form control.  Select the **Submit** button to run the current report or the specified reports if the button is available. If there is no Submit button, the change of values in the parameter form control will trigger report re-running.

**Note:** If you save or publish a report containing a parameter form control to another directory, the reports that you bind the parameter form control with will not be saved or published along with the report.

## Using Filter Control to Filter Report Data

A filter control is used to filter one or more data components (tables, charts, crosstabs, banded object and KPIs) in a web report. For how a filter control works, see [Filtering scenarios and filter logic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712581-Filtering-the-Data-Components-in-a-Dashboard#Scenarios).

In web reports two types of filter controls are supported:

* **Text List** allows you to pick one or more random values from a list and is used with categorical or nominal variables. You can choose one or more values from anywhere in the list and there is no mean or median value calculation.
* **Drop-down List** functions basically the same as Text List. It differs from the Text List type by listing values by means of a drop-down list so that it takes less space in a report. In a drop-down list filter control, checkboxes are provided ahead of the values for easy selection of multiple values.

The filters created via filter controls are referred to as on-screen filters, the values of which can be [saved as the default ones](https://devnet.logianalytics.com/hc/en-us/articles/1500009719141-Applying-Filters#Default).

**To insert a filter control and use it to filter data in a web report:**

1. Drag **Filter Control** from the Components panel to the destination in the report. The [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009690402-Insert-Filter-Control) dialog appears.

   ![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4412139488663/insrtfltrctrl.gif)
2. Select a type from the Control Type drop-down list.
3. The Select Fields drop-down list lists all the group and detail objects in the business views used by the current report. Select the objects of the same data type to bind to the filter control, and then select outside of the drop-down list to close it. For Text List, the name of the first object you select in the list will be displayed as the name of the filter control.

   ![Select Fields](https://devnet.logianalytics.com/hc/article_attachments/4412131378967/wbrpt_edt_wbctrl_slctfld.gif)
4. By default, a text list filter control displays all values of the selected objects and a drop-down list displays 300 values at most. If you want to customize the value list, check **Customize Initial Values** and select **Fetch Data** to select the desired values in the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009690282-Fetch-Data) dialog. You can also type in the values manually in the value text box.

   ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4412131379223/wbrpt_edt_wbctrl_cstmz.gif)

   To enter a value, input it in one row, and then press the **Enter** key to start a new row. General text editing operations including copy, paste, cut, backspace, delete and so on are supported. You need to make sure of the accuracy of the formats and values. If the selected objects are of the Date/Time type, you can also select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif) to specify a date and time value from the calendar.
5. By default, all the on-screen filters that are applied to the same data components in a web report are linked. If you do not want the filter control to be affected by other on-screen filters, unselect **[Link to Other Filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009719141-Applying-Filters#Link)**.
6. From the Apply To drop-down list, specify which data components in the report the filter will be applied to.

   By default, Logi JReport applies the filter to all the data components created using the business views in which the selected objects are obtained. If you uncheck the data components which are based on the same business view as any selected objects, these objects will not be used in the filter and thus their values will not be listed in the filter control.
7. Select **OK** to insert the filter control. If the objects bound to the filter control have the same values, the values are distinctive in the filter control.
8. Switch Web Report Studio to View Mode to select the values with which you want to filter the report data. A filter condition based on the selected values is then applied to the specified data components in the report.

   For Text List, you can make use of the Ctrl or Shift key to select multiple values. If the values themselves have inter-relationship, after you make the selection, Logi JReport will deal with the rest values to put the related ones on the top and gray the ones that have no relationship with the selected values. The grayed values are still selectable.

   For Drop-down List, select the arrow button on the right to open the drop-down list, use the checkboxes ahead of the values to select or deselect them, and then select **OK** to apply the selected values. The <All> checkbox is used to select or deselect all the values.

After inserting filter controls in the report, you can also insert a navigation control for undoing/redoing the value selection in the filter controls. For details about the usage of navigation control, see [Using navigation control to undo/redo value selection in filter controls](#Navigation).

**Note:** If all the data components in a report that use a business view are deleted, the objects in the business view that have been bound to the filter controls in the report will be removed from the filter controls too.

### Managing a Filter Control

When right-clicking on a filter control, these options are available for managing the filter control.

![Filter Control options](https://devnet.logianalytics.com/hc/article_attachments/4412112487191/wbrpt_edt_wbctrl_fltrctrl.gif)

* **Edit**  
   Opens the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009715981-Edit-Filter-Control) dialog to edit the filter control settings.
* **Search**  
   Displays the search bar right above the value list which enables you to search values in the filter control. You can also select the button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif) on the title bar of the filter control to launch the search bar. For detailed usage about the search bar, refer to [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009690722-Select-Values) dialog.
* **Clear**  
   Cancels the selection of values in the filter control. You can also use the button ![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4412112487447/btn_clear.gif) on the title bar to cancel the selection. This operation can be undone/redone.
* **Sort**  
   Sorts the values in the filter control in the ascending or descending order. You can also use the button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112487703/btn_sort1.gif) on the title bar to sort the values.
* **Delete**  
   Removes the filter control from the report and the filter you created with the filter control will be removed from the report too. You can also use the button **X** on the title bar to delete the filter control.
* **Hide**  
   Hides the filter control.
* **Properties**  
   Opens the [Filter Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009689902-Filter-Control-Properties) dialog for modifying the properties of the filter control. The dialog provides an entry to editing the filter control. To do this, in the General tab, select ![Select Fields](https://devnet.logianalytics.com/hc/article_attachments/4412139488919/btn_chsr2.gif) beside the Filter On text box. Then in the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009715981-Edit-Filter-Control) dialog, change the settings in the same way as you take for [inserting the filter control](#InsertFilter).
* **Position**  
   Specifies the [position](https://devnet.logianalytics.com/hc/en-us/articles/1500009719201-Making-Simple-Modifications-to-Components#Position) of the filter control.

**Notes:**

* When there are more than 300 values in a filter control, Logi JReport will use Big Data Loading logic. In this case, the Shift Key for multiple selection will not work.
* If all the data components in a web report that use a business view are deleted, the fields in the business view that have been added in the filter controls in the report will be removed from the filter controls too.
* Sometimes, when the position of a filter control is changed due to layout change, the advanced search bar in the filter control may not follow the filter control but stay where it is.

## Using Navigation Control to Undo/Redo Value Selection in Filter Controls

A navigation control can be considered as an accessorial control for filter controls and used to deal with the value selection operations in all the filter controls in the same report.

To insert a navigation control into a report, drag **Navigation Control** from the Components panel to the destination in the report.

A navigation control is a combination of three buttons:

* **Back**  
   Goes back to the previous value selection status and refreshes the report data accordingly.
* **Clear**  
   Removes all the value selection histories and all the filter conditions based on the selections, and refreshes the report data accordingly.
* **Forward**  
   Goes forward to the next value selection status and refreshes the report data accordingly.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719141-Applying-Filters)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719101-Adding-Conditional-Formats-to-Data-Fields)
