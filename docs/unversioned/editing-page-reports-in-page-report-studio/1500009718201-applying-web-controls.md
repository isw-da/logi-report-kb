---
title: "Applying Web Controls"
id: 1500009718201
section: "Editing Page Reports in Page Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls
updated_at: 2021-11-03T06:56:46Z
---

# Applying Web Controls

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691522-Adding-Report-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691642-Manipulating-Data-Components)

# Applying Web Controls

Web controls are report components designed to be similar to the kinds of controls found on web pages. In Page Report Studio, these four types of web controls can be applied: parameter control, parameter form control, filter control, and navigation control. However for page report created in Logi JReport Designer, you can add web controls to them only when the corresponding catalog contains business views.

A [Logi JReport Live license for Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009691022-Logi-JReport-licenses#ServerLive) is required in order to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

Below is a list of the sections covered in this topic:

* [Using Parameter Control to Specify a Parameter to a Report](#Parameter)
* [Using Parameter Form Control to Run Reports](#ParamForm)
* [Using Filter Control to Filter Report Data](#Filter)
* [Using Navigation Control to Undo/Redo Value Selection in Filter Controls](#Navigation)

## Using Parameter Control to Specify a Parameter to a Report

A parameter control is a web control that is bound with a parameter used by the current report. By specifying values to the parameter in a parameter control, you can pass the parameter values to Logi JReport and run the report with the specified values.

Cascading parameters cannot be used in parameter controls. If you want to do this, use parameter form controls instead.

**To insert a parameter control and use it to specify a parameter to a report**:

1. Do either of the following:
   * Select **Menu** > **Insert** > **Parameter Control**, then point to the destination where you want to add the parameter control and select the mouse button.
   * Drag **Parameter Control** from the Toolbox panel to the destination in the report.

   The [Insert Parameter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009687602-Insert-Parameter-Control) dialog appears.

   ![Insert Parameter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131418647/insrtprmctrl.gif)
2. Select the parameter you would like to add to the parameter control, then select **OK**.
3. A parameter control will be added into the report. Specify the value for the parameter. [You may specify the value in one of these ways.](https://devnet.logianalytics.com/hc/en-us/articles/1500009687182-Enter-Parameter-Values)
4. Once the value in the parameter control changes, the report will re-run with the new parameter value.

**Note:** If the specified parameter is no longer used in the report, the parameter control will become invalid.

## Using Parameter Form Control to Run Reports

A parameter form control is a web control that is bound with the parameters used by the current report or other reports. By specifying values to the parameters in a parameter form control, you can make the reports run with the specified parameter values.

**To insert a parameter form control and use it to run report:**

1. Do either of the following:
   * Select **Menu** > **Insert** > **Parameter Form Control**, then point to the destination where you want to add the parameter form control and select the mouse button.
   * Drag **Parameter Form Control** from the Toolbox panel to the destination in the report.

   The [Insert Parameter Form Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009687622-Insert-Parameter-Form-Control) dialog appears.

   ![Insert Parameter Form Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131418903/insrtprmfrmctrl.gif)
2. Specify the target reports to run using the parameter form control.
   * To run the current report, select **Current Report**, then specify the parameters used to run the report from the Select Parameters box.
   * To run other reports, select **Others**, then select the reports you want to run. If all the selected reports contain no parameters, you cannot finish the dialog.
3. Specify whether to include the Submit button in the parameter form control. If Submit is included, it is used to submit the parameter values you specified in the parameter form control. If Submit is not included, once you change the values of a parameter in the parameter form control, the new values will be applied automatically.
4. Select **OK** in the dialog to save the changes.

   The parameter form control is now inserted in the report. It lists the selected parameters for the current report or lists all parameters used by the specified reports.
5. In the parameter form control, specify values of the listed parameters. [You may specify the values in these ways.](https://devnet.logianalytics.com/hc/en-us/articles/1500009687182-Enter-Parameter-Values)
6. Select the **Submit** button to run the current report or the specified reports if the button is available. If there is no Submit button, the change of values in the parameter form control will trigger report re-running.

**Note:** If you save or publish a report containing a parameter form control to another directory, the reports that you bind the parameter form control with will not be saved or published along with the report.

## Using Filter Control to Filter Report Data

A filter control is used to filter one or more data components in a report, which refer to tables, banded objects, charts, and crosstabs. For how a filter control works, see [Filtering Scenarios](https://devnet.logianalytics.com/hc/en-us/articles/1500009712581-Filtering-the-Data-Components-in-a-Dashboard#Scenarios).

The filters created via filter controls are also referred to as on-screen filters.

**To insert a filter control and use it to filter report data:**

1. Do either of the following:
   * Drag **Filter Control** from the Toolbox panel to the destination in the report.
   * Select **Menu** > **Insert** > **Filter Control**, then point to the destination where you want to add the filter control and select the mouse button.

   The [Insert Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009687562-Insert-Filter-Control) dialog appears.

   ![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131419159/insrtfltrctrl.gif)
2. The Select Fields drop-down list lists all the group and detail objects in the business views used by the current report. Select the objects of the same data type based on which to create the filter control, and then select outside of the drop-down list to close it. The name of the first selected object will be displayed as the name of the filter control.

   ![Insert Filter Control dialog - Select Fields](https://devnet.logianalytics.com/hc/article_attachments/4412112540055/pgrpt_edit_wbctrl_slctfld.gif)
3. All values of the selected objects are used in the filter control by default. If you want to customize the value list, check **Customize Initial Values** and then select **Fetch Data** to select the desired values in the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009687502-Fetch-Data) dialog. You can also type in the values manually in the text box below.

   To enter a value, input it in one row, and then press the Enter key to start a new row. General text editing operations including copy, paste, cut, backspace, delete and so on are supported. You need to make sure of the accuracy of the formats and values.

   ![Insert Filter Control dialog - Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4412131419415/pgrpt_edit_wbctrl_cstmz.gif)
4. By default, all filter controls that are applied to the same data components are linked. Selecting a value in one filter control, for example, USA, will result in that all the other linked filter controls respond to gray the values that do not belong to USA or that do not contain USA or that are not related to USA like London. If you do not want the filter control to be affected by other on-screen filters, unselect [**Link to Other Filters**](#Link).
5. From the Apply To drop-down list, specify which data components in the report the filter will be applied to.

   By default, Logi JReport applies the filter to all the data components created using the business views in which the selected objects are obtained. If you uncheck the data components which are based on the same business view as any selected objects, these objects will not be used in the filter and thus their values will not be listed in the filter control.
6. Select **OK** to insert the filter control. If the objects bound to the filter control have the same values, the values are distinctive in the filter control.
7. Select the values with which you want to filter the report data. A filter condition based on the selected values is then applied to the specified data components in the report.

   You can make use of the Ctrl or Shift key to select multiple values. If the values themselves have inter-relationship, after you make the selection, Logi JReport will deal with the rest values to put the related ones on the top and gray the ones that have no relationship with the selected values. The grayed values are still selectable.

After inserting filter controls in the report, you can also insert a [navigation control](#Navigation) for undoing/redoing the value selection in the filter controls.

**Note:** If all the data components in a report that use a business view or are deleted, the objects in the business view that have been bound to the filter controls in the report will be removed from the filter controls too.

### Managing a Filter Control

When you right-click on the title bar of a filter control, these options are available for managing the filter control.

![Filter Control Options](https://devnet.logianalytics.com/hc/article_attachments/4412131419671/pgrpt_edit_wbctrl_fltrctrl.gif)

* **Properties**  
   Opens the [Filter Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009713081-Filter-Control-Properties) dialog for modifying the properties of the filter control. The dialog provides an entry to editing the filter control. To do this, in the General tab, select ![Select Fields](https://devnet.logianalytics.com/hc/article_attachments/4412139488919/btn_chsr2.gif) beside the Filter On text box. Then in the [Edit Filter Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009712981-Edit-Filter-Control) dialog, change the settings of the filter control.
* **Search**  
   Displays the search bar which enables you to search values in the filter control. You can also select the button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif) on the title bar of the filter control to launch the search bar.

  ![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4412139498519/btn_srchtlbr.gif)

  The following are details about the usage of the search bar:

  + **Text box**   
     Type in the text you want to search for and the matched text will be highlighted among the field values.
  + **X**  
     Closes the search bar. You can also select outside of the search bar to achieve this.
  + ![Advanced Options](https://devnet.logianalytics.com/hc/article_attachments/4412112501655/btn_srchtlbr_adv.gif)  
     Lists the advanced options.
    - **Highlight All**   
       Specifies whether to highlight all matched text.
    - **Match Case**   
       Specifies whether to search for text that meets the case of the typed text.
    - **Match Whole Word**   
       Specifies whether to search for text that matches a whole word and ignore partial word matches.
  + ![Previous button](https://devnet.logianalytics.com/hc/article_attachments/4412139498775/btn_srchtlbr_prv.gif)  
     When Highlight All is selected, you can use this button to go to the previous matched text.
  + ![Next button](https://devnet.logianalytics.com/hc/article_attachments/4412139499031/btn_srchtlbr_nxt.gif)  
     When Highlight All is selected, you can use this button to go to the next matched text.
* **Clear**  
   Cancels the selection of values in the filter control. You can also use the button ![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4412112487447/btn_clear.gif) on the title bar to cancel the selection. This operation can be undone/redone.
* **Sort**  
   Sorts the values in the filter control in the ascending or descending order.
* **Delete**  
   Removes the filter control from the report and the filter you created with the filter control will be removed from the report too. You can also use the close button on the title bar to remove the filter control.
* **Hide**  
   Hides the filter control.

### Saving and Using Default Values in Filter Controls

When the [Use Default On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#OnScreenFilter) feature is enabled for page reports, each end user can save the values specified to the filter controls in a page report as the default values for the report and for him. Next time when the user runs the report, the saved values will be applied to the filter controls by default. The default values in filter controls work on a user-report basis.

* To save values specified to the filter controls in a report as the default values, select **Menu** >  **Report**  > **On-screen Filter Values** and then select **Save as Default**.
* To clear the default values that have been saved to the filter controls in a report, select **Menu** >  **Report**  > **On-screen Filter Values** and then select **Clear Default**.
* To replace the values specified in the filter controls in a report with the saved default values, select **Menu** > **Report**  > **On-screen Filter Values** and then select **Restore to Default**.

### Link Relationship Between Filter Controls

By default, all the filter controls applied to the same data components in a report are interlinked. The link relationship is reflected on the filter values dynamically: selecting a value in one on-screen filter will result in that values which do not belong to the selected value, contain the selected value or relate to the selected value are grayed in all the other linked filter controls for distinguishing. For example, there is a filter control based on the field Country and another on City and they both are applied to the same table. When you select USA in the Country filter control, the values in the City filter control will change as follows if the control has scrollbar: the cities belong to USA are displayed in the upper area of the filter control, and the other cities are put in the lower area and grayed out. If the City filter control has no scrollbar, all the values remain their positions and the values not belonging to USA are grayed out. In both cases all the values are still selectable.

When using a filter control, you can determine whether or not to make the filter control apply the link relationship via the Link to Other Filters option.

Below is an example showing the logic of other linked filters:

When

* Filter1 is applied to DC1, DC2, and DC3.
* Filter2 is applied to DC1.
* Filter3 is applied To DC2.
* Filter4 is applied to DC2 and DC3.

The result:

* For Filter1, other linked filters are Filter2, Filter3, and Filter4.
* For Filter2, other linked filter is Filter1.
* For Filter3, other linked filters are Filter1 and Filter4.
* For Filter4, other linked filters are Filter1 and Filter3

## Using Navigation Control to Undo/Redo Value Selection in Filter Controls

A navigation control can be considered as an accessorial control for filter controls and is used to deal with the value selection operations in all the filter controls in the same report.

To insert a navigation control into a report, do either of the following:

* Select **Menu** > **Insert** > **Navigation Control**, then point to the destination where you want to add the navigation control and select the mouse button.
* Drag **Navigation Control** from the Toolbox panel to the destination in the report.

A navigation control is a combination of three buttons:

* **Back**  
   Goes back to the previous value selection status and refreshes the report data accordingly.
* **Clear**  
   Removes all the value selection histories and all the filter conditions based on the selections, and refreshes the report data accordingly.
* **Forward**  
   Goes forward to the next value selection status and refreshes the report data accordingly.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691522-Adding-Report-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691642-Manipulating-Data-Components)
