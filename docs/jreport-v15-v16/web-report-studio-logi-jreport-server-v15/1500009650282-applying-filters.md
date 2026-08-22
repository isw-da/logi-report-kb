---
title: "Applying Filters"
id: 1500009650282
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters
updated_at: 2021-07-24T20:53:36Z
---

# Applying Filters

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675321-Using-Web-Controls)

# Applying Filters

You can apply filters to business views and data components such as tables, crosstabs and charts of a web report so as to narrow down the data displayed in the web report.

Below is a list of the sections covered in this topic:

* [Applying Filters to Business Views](#BV)
* [Filtering the Data Components in a Report](#Report)
* [Managing On-Screen Filters](#OnScreen)

## Applying Filters to Business Views

When creating a web report, you can choose to apply filters to the specified business view to narrow down the data scope of the data component using the business view. Filters for business views are defined into two categories in Web Report Studio: predefined filters and user-defined filters. As the name suggests, predefined filters are defined in advance when creating or editing the business views in Logi JReport Designer, and user-defined filters are created on business views while they are used.

Business view filters are defined on the component level in Web Report Studio, which means each time you create a component, you can apply a filter to the business view the component uses and it will not affect other components based on the same business view.

Filters can be applied to a business view in the report wizard.

1. In the report wizard, select the **Filter** button next to the Data Source drop-down list. The [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009672441-Query-Filter) dialog appears.
2. The dialog has the basic and advanced modes for you to define a filter using either [simple expressions](#Simple) or  [complex expressions.](#Complex)

   When it is in the advanced mode, you can also choose to apply a predefined filter of the specified business view from the Query Filter drop-down list. If you prefer to define a filter on your own, select **User-Defined** from the drop-down list, and then define the filter according to your requirements. You can also edit a predefined filter if required and save it as a user-defined filter to the business view.

   * **To define a filter using simple expressions:**
     1. Make sure the dialog is in the basic mode.

        ![](https://devnet.logianalytics.com/hc/article_attachments/4404920397847/qryfltr_basic.gif)
     2. Select the field on which the filter will be based from the field drop-down list.
     3. From the operator drop-down list, set the operator with which to compose the filter expression.
     4. Type the values of how to filter the field in the value text box, or select one or more values from the drop-down list. You can also select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398103/btn_dshbrd_prm.gif) and then select a parameter from the drop-down list to specify the value dynamically and when the available parameters cannot meet your requirement, you can create a [local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-#Param) to use in the filter.
     5. If you want to add another condition line, from the logic operator drop-down list,
        + To add a condition line of the AND relationship with the current line, select **AND**, then define the expression as required.
        + To add a condition line of the OR relationship with the current line, select **OR**, then define the expression as required.

        Repeat this to add more filter expressions if required. To delete a condition line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398359/btn_pgrpt_no.gif) on its left.
   * **To define a filter using complex expressions:**
     1. Switch the dialog to the advanced mode.

        ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398615/qryfltr_adv.gif)
     2. Select the **Add Condition** button to add a condition line.
     3. From the field drop-down list, select the field on which the filter will be based.
     4. From the operator drop-down list, set the operator with which to compose the filter expression.
     5. Type the values of how to filter the field in the value text box, or select one or more values from the drop-down list. You can also select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398103/btn_dshbrd_prm.gif) and then select a parameter from the drop-down list or [create a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-#Param) to specify the value dynamically.
     6. To add another condition line, select the **Add Condition** button and define the expression as required. Then select the logic button until you get the required logic to specify the relationship between the two filter expressions. The logic can be AND, OR, AND NOT, or OR NOT.
     7. Repeat the above steps to add more filter expressions if necessary.

        To group some conditions, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.** It is the equivalent of adding parenthesis in a logic expression.

        To adjust the priority of a condition line or a group, select it and select the **Up** or **Down** button.

        To delete a condition line or a group, select it and select the **Delete** button.
3. After you finish the report wizard, the specified filter is applied to the business view. If parameters are used in the filter conditions, they are listed in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009650342-Applying-Parameters#Panel) and you can specify the parameter values in the panel to dynamically define the filter conditions.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Filtering the Data Components in a Report

To filter the data components in a web report, you can take any of the following ways: [using the Filter](#Dialog) dialog, [using filter controls](#Control), [using the Filter panel](#Panel). For tables you can also filter them via [shortcut menu](#Menu), [column headers](#Header) or [labels](#Label).

### Using the Filter Dialog

When using the Filter dialog to filter report data, you can only make the filter applied to a specific data component in the current web report.

**To filter report data using the Filter dialog:**

1. Select **Menu** > **Edit** > **Filter**, or the **Filter** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920359831/btn_filter.gif) on the toolbar. The [Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009671821-Filter) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398871/fltr_basic.gif)
2. From the Apply to drop-down list, select the component in the web report to which you want to apply the filter.

   **Tip:** For web reports created in Logi JReport Designer, the default selected component and available components in the Apply to drop-down list are determined by the Default for Filter and Invisible for Filter Dialogs properties of the components in the web reports.
3. Define the filter using either [simple expressions](#Simple) or [complex expressions](#Complex).
4. When done, select **OK** to apply the filter. If parameters are used in the filter conditions, they are listed in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009650342-Applying-Parameters#Panel) and you can specify the parameter values in the panel to dynamically define the filter conditions.

The Filter dialog provides an entry to all the filters used in the current web report. You can select the Inspector button to view the detailed filter information in the [Filter Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500009647362-Filter-Inspector) dialog.

### Using Filter Control

You can use the Filter web control to filter one or more data components that use the same data source in a web report. A filter control can do filtering based on one field or multiple fields of the same data type. For details, see [Using filter control to filter report data](https://devnet.logianalytics.com/hc/en-us/articles/1500009675321-Using-Web-Controls#Filter).

### Using the Filter Panel

The Filter panel on the left of Web Report Studio is used to filter data components in the current report that use the same business view.

**To use the Filter panel:**

1. Select + on the title bar of the panel to add group and detail objects from the business views used in the current report. Each added group/detail object and its values are housed in a separate box.
2. Select the values with which you want to filter the report data. You can make use of the Ctrl or Shift key to do multiple selection.

   A filter condition based on the selected values is then applied to all the data components in the report that use the same business view, regardless whether the data components contain the fields holding those values.

The value selection applies a filter condition and the logic is as follows:

* **For one value selection:**

  *Selected\_Field=Selected\_Value*

  For example, *Country=USA*
* **For multiple selection:**

  *(Selected\_Field1=Selected\_Value1 or Selected\_Field1=Selected\_Value2) and (Selected\_Field2=Selected\_Value3 or Selected\_Field2=Selected\_Value4)...*

  For example, *(Country=USA or Country=China) and (Year=2008 or Year=2009)*

The following shows more about working with the Filter panel:

![](https://devnet.logianalytics.com/hc/article_attachments/4404926649495/wbrpt_edt_fltr_fltrpnl1.gif)

You can use the buttons on the bottom of the Filter panel to deal with the value selection in the panel.

* **Back**  
   Goes back to the previous value selection status and refreshes the report data accordingly.
* **Clear**  
   Removes all the value selection histories and all the filter conditions based on the selections, and refreshes the report data accordingly.
* **Forward**  
   Goes forward to the next value selection status and refreshes the report data accordingly.

After right-clicking in the box for a group/detail object in the Filter panel, these options are available for managing the object.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920399127/wbrpt_edt_fltr_fltrpnl2.gif)

* **Search**  
   Displays the quick search toolbar right above the value list which enables you to search values in the group/detail object. You can also use the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif) on the group/detail name title bar to launch the quick search toolbar. For detailed usage about the quick search toolbar, refer to [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009672541-Select-Values) dialog.
* **Clear**  
   Cancels the selection of values in the group/detail object. You can also use the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920369559/btn_clear.gif) on the group/detail name title bar to achieve this.
* **Clear All**  
   Cancels the selection of all values in all the group and detail objects.
* **Sort**  
   Sorts the values in the group/detail object in the ascending or descending order. You can also use the button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404920370327/btn_sort1.gif) on the group/detail name title bar to sort the values.
* **Delete**  
   Removes the group/detail object from the Filter panel and the filter you created with the object will be removed from the report too. You can also select **X** on the group/detail name title bar to remove it.

**Notes:**

* When there are more than 300 values for an object, Logi JReport will use Big Data Loading logic. In this case, the Shift Key for multiple selection will not work.
* The filters created via the Filter panel cannot be seen when web reports are opened in Logi JReport Designer.

### Using Shortcut Menu

For tables in web reports you can use the filter-related commands on the shortcut menu to filter the data. To do this, point to any value of a detail field by which you want to filter data, then right-click to show the shortcut menu. You will see the Filter item which provides a submenu containing the following commands:

![](https://devnet.logianalytics.com/hc/article_attachments/4404926649879/wbrpt_edt_fltr_menu.gif)

* **Remove Filter**  
   This command is enabled after you have applied filtering on the field. You can select it to remove the filter ever defined on it.
* **First N**  
   Filters the field to display only its first N values. You can select a number from the submenu or enter a positive integer into the text box on the submenu to specify the number.
* **Last N**  
   Filters the field to display only its last N values. You can select a number from the submenu or enter a positive integer into the text box on the submenu to specify the number.
* **Field values**  
   "Field values" is not the name for a command on the Filter submenu, but represents some items which are the values of the field you right-click on. Select a value and the field will be filtered to show only the specified value.
* **More**  
   This command is enabled if the Filter submenu cannot list all values of the field. When it is enabled, selecting it brings up the [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009672541-Select-Values) dialog. Select one value in the dialog and the field will be filtered to show only the selected value.

### Using Table Column Headers

You can use the filter button on any table column header to filter values in the column if the feature is enabled in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#ColumnHeader). By default, the feature is disabled so
you need to configure the profile before you can use it.

1. Go to the Profile > Customize Profile > Common tab.
2. Check the option **Filter on Column Headers**.
3. Check **Show Sort/Filter Status on Column Headers** if you want the filter buttons to be displayed on the table column headers after the columns are applied with filter conditions.
4. Select **OK** to save the profile setting.
5. Run a web report containing a table in Web Report Studio.
6. Put the mouse pointer on any column header and you can find the filter button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926650135/btn_lblfltr.gif).
   Select the button a filter list which contains the same items as the [Filter submenu](#Menu) appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926650391/wbrpt_edt_fltr_header.gif)
7. Select the required item to filter the column. When a column is filtered its filter button will be highlighted. The summary column that contains multiple aggregation fields cannot be filtered using this way.

### Using Labels

With Logi JReport Designer, you can bind a label in a table with a field used in the table to enable filtering on the label by setting the label's Bind Column and Filterable properties. Then when running the table in Web Report Studio you can select the filter button beside the label to filter values of the bound field. This functions the same as via the [table column headers](#Header).

When a label is bound with a field, if the Filter on Column Header feature is also enabled, the former has higher priority. For example, if you bind the label in column A header with the field in column B, when selecting the filter button on column A header, values in column B are filtered.

**Tips:**

* After filtering the data in a table by either shortcut menu, column header or label, you may notice that the corresponding filter expression displays in the Filter dialog if you open this dialog.
* Using Logi JReport Designer, you can specify the default selected component and available components in the Apply to drop-down list of the Filter dialog via the Default for Filter and Invisible for Filter Dialogs properties of the components.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Managing On-Screen Filters

Filters created via the [Filter panel](#Panel) and [filter controls](#Control) in a web report are called on-screen filters. Logi JReport allows you to save values for them as the default values.

### Saving and Using Default on-Screen Filter Values

When the [Use Default On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#OnScreenFilter) feature is enabled for web reports in the server profile, each end user can save the values specified to the on-screen filters as the default values for the report and for him. Then the next time when the user runs the report, the saved values will be applied to the on-screen filters by default. The default on-screen filter values work on a user-report basis.

* To save values specified to the on-screen filters in a report as the default values, on the Menu drop-down list, go to **Edit** > **On-screen Filter Values** and then select **Save as Default**.
* To clear the default values that have been saved to the on-screen filters in a report, on the Menu drop-down list, go to **Edit** > **On-screen Filter Values** and then select **Clear Default**.
* To replace the values specified in the on-screen filters in a report with the saved default values, on the Menu drop-down list, go to **Edit** > **On-screen Filter Values** and then select **Restore to Default**.

### Link Relationship Between On-Screen Filters

By default, all the on-screen filters applied to the same data components in a report are interlinked. The link relationship is reflected on the filter values dynamically: selecting a value in one on-screen filter will result in that values which do not belong to the selected value, contain the selected value or relate to the selected value are grayed in all the other linked on-screen filters for distinguishing. For example, there is a filter control based on the field Country and another on City and they both are applied to the same table. When you select USA in the Country filter control, the values in the City filter control will change as follows if the control has scrollbar: the cities belong to USA are displayed in the upper area of the filter control, and the other cities are put in the lower area and grayed out. If the City filter control has no scrollbar, all the values remain their positions and the values not belonging to USA are grayed out. In both cases all the values are still selectable.

When using a filter control, you can determine whether or not to make the filter control apply the link relationship via the Link to Other Filters option.

Below is an example showing the logic of other linked on-screen filters:

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675321-Using-Web-Controls)
