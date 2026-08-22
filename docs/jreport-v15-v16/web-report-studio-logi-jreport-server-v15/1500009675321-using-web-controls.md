---
title: "Using Web Controls"
id: 1500009675321
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675321-Using-Web-Controls
updated_at: 2021-07-24T20:53:34Z
---

# Using Web Controls

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675181-Adding-Conditional-Formats-to-Fields)

# Using Web Controls

Web controls are report components designed to be similar to the kinds of controls found on web pages. In Web Report Studio, these four types of web controls can be applied: parameter control, parameter form control, filter control, and navigation control.

This topic describes each of the web controls and how to use them.

Below is a list of the sections covered in this topic:

* [Using Parameter Control to Specify a Parameter to a Report](#Parameter)
* [Using Parameter Form Control to Run Reports](#Form)
* [Using Filter Control to Filter Report Data](#Filter)
* [Using Navigation Control to Undo/Redo Value Selection in Filter Controls](#Navigation)

## Using Parameter Control to Specify a Parameter to a Report

A parameter control is a web control that is bound with a parameter used by the current report. By specifying values to the parameter in a parameter control, you can pass the parameter values to Logi JReport and run the report with the specified values.

Cascading parameters cannot be used in parameter controls. If you want to do this, use parameter form controls instead.

**To insert a parameter control and use it to specify a parameter to a report**:

1. Drag **Parameter Control** from the Components panel to the destination in the report. The [Insert Parameter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009672221-Insert-Parameter-Control) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920368151/insrtprmctrl.gif)
2. Select the parameter you would like to add to the parameter control, then select **OK**.
3. A parameter control will be added into the report.

   You can then switch Web Report Studio to View Mode to specify the value for the parameter. [You may specify the value in one of these ways.](https://devnet.logianalytics.com/hc/en-us/articles/1500009647742-Report-Parameters) Once the value in the parameter control changes, the report will re-run with the new parameter value.

**Note:** If the specified parameter is no longer used in the report, the parameter control will become invalid.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Using Parameter Form Control to Run Reports

A parameter form control is a web control that is bound with the parameters used by the current report or other reports. By specifying values to the parameters in a parameter form control, you can make the reports run with the specified parameter values.

**To insert a parameter form control and use it to run reports:**

1. Drag **Parameter Form Control** from the Components panel to the destination in the report. The [Insert Parameter Form Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009647622-Insert-Parameter-Form-Control) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926632727/insrtprmfrmctrl.gif)
2. Specify the target reports to run using the parameter form control.
   * To run the current report, select **Current Report**, then specify the parameters used to run the report from the Select Parameters box.
   * To run other reports, select **Others**, then select the reports you want to run. If all the selected reports contain no parameters, you cannot finish the dialog.
3. Specify whether to include the Submit button in the parameter form control. If Submit is included, it is used to submit the parameter values you specified in the parameter form control. If Submit is not included, once you change the values of a parameter in the parameter form control, the new values will be applied automatically.
4. Select **OK** in the dialog to save the changes.
   The parameter form control is now inserted in the report, listing the selected parameters for the current report or all parameters used by the specified reports.

   You can then switch Web Report Studio to View Mode to specify values of the listed parameters in the parameter form control. [You may specify the values in these ways.](https://devnet.logianalytics.com/hc/en-us/articles/1500009647742-Report-Parameters) Select the **Submit** button to run the current report or the specified reports if the button is available. If there is no Submit button, the change of values in the parameter form control will trigger report re-running.

**Note:** If you save or publish a report containing a parameter form control to another directory, the reports that you bind the parameter form control with will not be saved or published along with the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Using Filter Control to Filter Report Data

A filter control is used to filter one or more data components in a report, which refer to tables, charts, and crosstabs. For how a filter control works, see [Filtering scenarios](https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data#Scenarios).

The filters created via filter controls are referred to as on-screen filters, the values of which can be [saved as the default ones](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters#Default).

**To insert a filter control and use it to filter report data:**

1. Drag **Filter Control** from the Components panel to the destination in the report.
2. The [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009672181-Insert-Filter-Control) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926633239/insrtfltrctrl.gif)
3. From the Select Fields drop-down list, select the fields of the same data type to bind to the filter control, and then select outside of the drop-down list to close it. The name of the first displayed field you select in the list will be displayed as the name of the filter control.

   To filter components created from the same business view, select a field in the business view.

   To filter components created from different business views, find a common field these business views contain, then select the field in each of the business views.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926633495/wbrpt_edt_wbctrl_slctfld.gif)
4. All values of the selected fields are used in the filter control by default. If you want to customize the value list, check **Customize Initial Values** and then select **Fetch Data** to select the desired values in the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009672101-Fetch-Data) dialog. You can also type in the values manually in the text box below.

   To enter a value, input it in one row, and then press the Enter key to start a new row. General text editing operations including copy, paste, cut, backspace, delete and so on are supported. You need to make sure of the accuracy of the formats and values.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920368919/wbrpt_edt_wbctrl_cstmz.gif)
5. If you do not want the filter control to be affected by other on-screen filters, unselect **[Link to Other Filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters#Link)**.
6. The Apply To drop-down list provides the components involving the selected fields. Select the components which you want to filter.
7. Select **OK**. The filter control is inserted in the report.

   You can then switch Web Report Studio to View Mode to select one or more values in the filter control to apply.

After inserting filter controls in the report, you can also insert a navigation control for undoing/redoing the value selection in the filter controls. For details about the usage of navigation control, see [Using navigation control to undo/redo value selection in filter controls](#Navigation).

### Managing a Filter Control

When right-clicking on a filter control, these options are available for managing the filter control.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920369175/wbrpt_edt_wbctrl_fltrctrl.gif)

* **Edit**  
   Opens the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009647242-Edit-Filter-Control) dialog to edit the filter control settings.
* **Search**  
   Displays the quick search toolbar right above the value list which enables you to search values in the filter control. You can also select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif) on the title bar of the filter control to launch the quick search toolbar. For detailed usage about the quick search toolbar, refer to [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009672541-Select-Values) dialog.
* **Clear**  
   Cancels the selection of values in the filter control. You can also use the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920369559/btn_clear.gif) on the title bar to cancel the selection. This operation can be undone/redone.
* **Sort**  
   Sorts the values in the filter control in the ascending or descending order. You can also use the button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404920370327/btn_sort1.gif) on the title bar to sort the values.
* **Delete**  
  Removes the filter control from the report and the filter you created with the filter control will be removed from the report too. You can also use the button **X** on the title bar to delete the filter control.
* **Hide**  
   Hides the filter control.
* **Properties**  
  Opens the [Filter Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009647342-Filter-Control-Properties) dialog for modifying the properties of the filter control. The dialog provides an entry to editing the filter control. To do this, in the General tab, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920370839/btn_chsr2.gif) beside the Filter On text box. Then in the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009647242-Edit-Filter-Control) dialog, change the settings in the same way as you take for [inserting the filter control](#InsertFilter).
* **Position**  
   Specifies the [position](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components#Position) of the filter control.

**Notes:**

* When there are more than 300 values in a filter control, Logi JReport will use Big Data Loading logic. In this case, the Shift Key for multiple selection will not work.
* Sometimes, when the position of a filter control is changed due to layout change, the advanced search toolbar in the filter control may not follow the filter control but stay where it is.
* When viewing reports on a mobile browser, to specify multiple values in a filter control, long-press on a value until you see the OK and Cancel buttons appear at the bottom of the filter control which means that the filter control enters the mode for multiple selection. The value you long-press on will be selected. Then select other values and select the **OK** button to apply them. Only when you exit the multiple-selection mode of one filter control can you activate that of another filter control.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675181-Adding-Conditional-Formats-to-Fields)
