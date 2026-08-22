---
title: "Applying Filters"
id: 1500009719141
section: "Editing Web Reports in Web Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719141-Applying-Filters
updated_at: 2021-11-03T06:56:28Z
---

# Applying Filters

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692802-Going-Through-the-Report-Data)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719281-Using-Web-Controls)

# Applying Filters

You can apply filters to business views and data components such as tables, crosstabs, charts, banded objects and KPIs of a web report so as to narrow down the data displayed in the web report.

Below is a list of the sections covered in this topic:

* [Applying Filters to Business Views](#BV)
* [Filtering the Data Components in a Report](#Report)

+ [Using the Filter Dialog](#Dialog)
+ [Using the Filter Panel](#Panel)
+ [Using the Shortcut Menu](#Menu)
+ [Using Column Headers](#Header)
+ [Using Labels](#Label)

* [Managing On-Screen Filters](#OnScreen)

+ [Saving and Using Default On-Screen Filter Values](#Default)
+ [Link Relationship Between On-Screen Filters](#Link2)

## Applying Filters to Business Views

When creating a web report, you can apply filters to the specified business view to narrow down the data scope of the data component using the business view. Filters for business views are defined into two categories in Web Report Studio: predefined filters and user-defined filters. As the name suggests, predefined filters are defined in advance when creating or editing the business views in Logi JReport Designer, and user-defined filters are created on business views while they are used.

Business view filters are defined on the component level in Web Report Studio, which means each time you create a component, you can apply a filter to the business view the component uses and it will not affect other components based on the same business view.

### Applying a Filter to the Business View for a Data Component

**To apply a filter to the business view used by a data component:**

1. Do any of the following to open the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009716841-Query-Filter) dialog:
   * Select **Menu** > **Edit** > **Query Filter**.
   * Select the **Query Filter** button ![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412112483479/btn_wbrpt_qryfltr.gif) on the toolbar.
   * Right-click a data component and select **Query Filter** from the shortcut menu.
   * For a table, chart, crosstab or banded object, while creating or editing it with the report wizard, select the **Filter** button next to the Data Source drop-down list.
2. If the dialog is accessed from the menu or toolbar, you need to specify a data component from the Apply To drop-down list to apply the filter to the business view the data component uses.
3. You can choose to apply a predefined filter of the specified business view from the Query Filter drop-down list. If you prefer to define a filter on your own, select **User-Defined** from the drop-down list, and then define the filter according to your requirements. You can also edit a predefined filter if required and save it as a user-defined filter to the business view.
4. The dialog has the basic and advanced modes for you to define a filter using either [simple expressions](#Simple) or  [complex expressions.](#Complex)
   * **To define a filter using simple expressions:**
     1. Make sure the dialog is in the basic mode.

        ![Query Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4412131397783/qryfltr_basic.gif)
     2. Select the field on which the filter will be based from the field drop-down list.
     3. From the operator drop-down list, set the operator with which to compose the filter expression.
     4. Type the values of how to filter the field in the value text box, or select one or more values from the drop-down list. When you type in the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

        You can also select the button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4412139509783/btn_dshbrd_prm.gif) and then select a parameter from the drop-down list to specify the value dynamically and when the available parameters cannot meet your requirement, you can [create a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-#Param) to use in the filter.
     5. If you want to add another condition line, from the logic operator drop-down list,
        + To add a condition line of the AND relationship with the current line, select **AND**, then define the expression as required.
        + To add a condition line of the OR relationship with the current line, select **OR**, then define the expression as required.

        Repeat this to add more condition lines if required. To delete a condition line, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112514327/btn_pgrpt_no.gif) on its left.
   * **To define a filter using complex expressions:**
     1. Switch the dialog to the advanced mode.

        ![Query Filter dialog - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/4412131398679/qryfltr_adv.gif)
     2. Select the **Add Condition** button to add a condition line.
     3. From the field drop-down list, select the field on which the filter will be based.
     4. From the operator drop-down list, set the operator with which to compose the filter expression.
     5. Type the values of how to filter the field in the value text box, or select one or more values from the drop-down list. When you type in the value manually, if multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

        You can also select the button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4412139509783/btn_dshbrd_prm.gif) and then select a parameter from the drop-down list to specify the value dynamically and when the available parameters cannot meet your requirement, you can [create a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-#Param) to use in the filter.
     6. To add another condition line, select the **Add Condition** button and define the expression as required. Then select the logic button until you get the required logic to specify the relationship between the two filter expressions. The logic can be AND, OR, AND NOT, or OR NOT.
     7. Repeat the above steps to add more condition lines if necessary.

        To group some conditions, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.** It is the equivalent of adding parenthesis in a logic expression.

        To adjust the priority of a condition line or a group, select it and select the **Up** or **Down** button.

        To delete a condition line or a group, select it and select the **Delete** button.

   **Tip:** When the dialog is in the basic mode and you select a predefined filter from the Query Filter drop-down list which is a complex one, it will be switched to the advanced mode automatically.
5. After you finish the report wizard, the specified filter is applied to the business view. If parameters are used in the filter conditions, they are listed in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009719221-Applying-Parameters) and you can specify the parameter values in the panel to dynamically define the filter conditions.

## Filtering the Data Components in a Report

To filter the data components in a web report, you can take any of the following ways: using the Filter dialog, using the Filter panel or [using filter controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009719281-Using-Web-Controls#Filter). For tables, you can also filter them via shortcut menu, column headers or labels, and for banded objects, via shortcut menu and labels.

### Using the Filter Dialog

When using the Filter dialog to filter report data, you can only make the filter applied to a specific data component in the current web report.

1. Select **Menu** > **Edit** > **Filter**, or the **Filter** button ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/4412139484823/btn_filter.gif) on the toolbar. The [Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009689882-Filter) dialog appears.

   ![Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/4412131398935/fltr_basic.gif)
2. From the Apply To drop-down list, select the data component in the report to which you want to apply the filter.

   **Tip:** For web reports created in Logi JReport Designer, the default selected data component and available data components in the Apply To drop-down list are determined by the Default for Filter and Invisible for Filter Dialogs properties of the components.
3. Define the filter using either [simple expressions](#Simple) or [complex expressions](#Complex).
4. When done, select **OK** to apply the filter. If parameters are used in the filter conditions, they are listed in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009719221-Applying-Parameters) and you can specify the parameter values in the panel to dynamically define the filter conditions.

The Filter dialog provides an entry to all the filters used in the current web report. You can select the Inspector button to view the detailed filter information in the [Filter Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500009716161-Filter-Inspector) dialog.

### Using the Filter Panel

The Filter panel on the left of Web Report Studio is used to filter data components in the current report. You can create in the panel as many filters as you want which resemble [filter controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009719281-Using-Web-Controls#Filter).

The filters created via the Filter panel are referred to as on-screen filters, the values of which can be [saved as the default ones](#Default).

**To use the Filter panel:**

1. Select + on the title bar of the panel. The [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009716961-Select-Field) dialog appears.

   ![Select Field dialog - Filter](https://devnet.logianalytics.com/hc/article_attachments/4412131399191/slctfld.gif)
2. The Select Fields box lists all the group and detail objects in the business views used by the current report. Select the objects of the same data type based on which to create the filter.
3. From the Apply To drop-down list, specify which data components in the report the filter will be applied to.

   By default, Logi JReport applies the filter to all the data components created using the business views in which the selected objects are contained. If you uncheck the data components which are based on the same business view as any selected objects, these objects will not be used in the filter and thus their values will not be listed when the filter is added in the Filter panel.
4. Select **OK**. A filter box is then added in the Filter panel. If the objects bound to the filter box have the same values, the values are distinctive in the filter box.
5. Select the values with which you want to filter the report data. A filter condition based on the selected values is then applied to the specified data components in the report.

   You can make use of the Ctrl or Shift key to select multiple values. If the values themselves have inter-relationship, after you make the selection, Logi JReport will deal with the rest values to put the related ones on the top and gray the ones that have no relationship with the selected values. The grayed values are still selectable.

The following shows more about working with the Filter panel:

![Filter Panel](https://devnet.logianalytics.com/hc/article_attachments/4412139510167/wbrpt_edt_fltr_fltrpnl1.gif)

You can use the buttons on the bottom of the Filter panel to deal with the value selection in the panel.

* **Back**  
   Goes back to the previous value selection status and refreshes the report data accordingly.
* **Clear**  
   Removes all the value selection histories and all the filter conditions based on the selections, and refreshes the report data accordingly.
* **Forward**  
   Goes forward to the next value selection status and refreshes the report data accordingly.

For each filter in the panel, you can manage it with the buttons on its title bar or the shortcut menu as follows:

![Filter Panel options](https://devnet.logianalytics.com/hc/article_attachments/4412131399447/wbrpt_edt_fltr_fltrpnl2.gif)

* **Search**![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)  
   Displays the search bar right above the value list for searching the desired values. For detailed usage about the search bar, refer to [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009690722-Select-Values) dialog.
* **Clear**![Clear button](https://devnet.logianalytics.com/hc/article_attachments/4412112487447/btn_clear.gif)  
   Cancels the selection of values in the current filter box.
* **Clear All**  
   Cancels the selection of all values in the Filter panel.
* **Sort**![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112487703/btn_sort1.gif)  
   Sorts the values in the ascending or descending order.
* **Delete**![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)  
   Removes the filter from the Filter panel and the corresponding filter conditions will be removed from the report too.

**Notes:**

* Values in a filter box will be removed when the data components that use the same business view as the involved objects of these values are removed.
* When there are more than 300 values for an object, Logi JReport will use Big Data Loading logic. In this case, the Shift Key for multiple selection will not work.
* The filter conditions created via the Filter panel cannot be seen when web reports are opened in Logi JReport Designer.
* If all the data components in a report that use a business view are deleted, the objects in the business view that have been added in the Filter panel in the report will be removed from the Filter panel too.

### Using the Shortcut Menu

For tables and banded objects, you can use the filter-related commands on the shortcut menu to filter the data. To do this, point to any value of a detail field by which you want to filter data, then right-click to show the shortcut menu. You will see the Filter item which provides a submenu containing the following commands:

![Filter Submenu](https://devnet.logianalytics.com/hc/article_attachments/4412112514583/wbrpt_edt_fltr_menu.gif)

* **Remove Filter**  
   This command is enabled after you have applied filtering on the field. You can select it to remove the filter ever defined on it.
* **First N**  
   Filters the field to display only its first N values. You can select a number from the submenu or enter a positive integer into the text box on the submenu to specify the number.
* **Last N**  
   Filters the field to display only its last N values. You can select a number from the submenu or enter a positive integer into the text box on the submenu to specify the number.
* **Select Values**   
  Brings up the [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009690722-Select-Values) dialog to select the values to filter the field with.

### Using Column Headers

You can use the filter button on any table column header to filter values in the column if the feature is enabled in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#ColumnHeader). By default, the feature is disabled so
you need to configure the profile before you can use it.

1. In the Common tab of the My Profile > Customize Profile page or Administration > Server Profile > Customize Profile page, check the option **Filter on Column Headers**, then check **Show Sort/Filter Status on Column Headers** if you want the filter buttons to be displayed on the table column headers after the columns are applied with filter conditions. Select **OK** to save the profile setting.
2. Run a web report containing a table in Web Report Studio.
3. Put the mouse pointer on any column header and you can find the filter button ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/4412139510423/btn_lblfltr.gif).

   ![Filter Button on Column Header](https://devnet.logianalytics.com/hc/article_attachments/4412112514839/wbrpt_edt_fltr_header1.gif)
4. Select the button and a filter list which contains the same items as the [Filter submenu](#Menu) appears.
5. Select the required item to filter the column. When a column is filtered its filter button will be highlighted.

   ![Highlighted Filter Button](https://devnet.logianalytics.com/hc/article_attachments/4412112515351/wbrpt_edt_fltr_header2.gif)

**Note:** The summary column that contains multiple aggregation objects cannot be filtered via its column header.

### Using Labels

With Logi JReport Designer, you can bind a label in a table/banded object with a field used in the table/banded object to enable filtering on the label by setting the label's Bind Column and Filterable properties. Then when running the table/banded object in Web Report Studio you can select the filter button beside the label to filter values of the bound field. This functions the same as via the [table column headers](#Header).

When a label is bound with a field, if the Filter on Column Header feature is also enabled, the former has higher priority. For example, if you bind the label in column A header with the field in column B, when selecting the filter button on column A header, values in column B are filtered.

**Tips:**

* After filtering the data in a table or banded object by either shortcut menu, column header or label, you may notice that the corresponding filter expression displays in the Filter dialog if you open this dialog.
* Using Logi JReport Designer, you can specify the default selected component and available components in the Apply to drop-down list of the Filter dialog via the Default for Filter and Invisible for Filter Dialogs properties of the components.

## Managing On-Screen Filters

Filters created via the [Filter panel](#Panel) and [filter controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009719281-Using-Web-Controls#Filter) in a web report are called on-screen filters. Logi JReport allows you to save values for them as the default values.

### Saving and Using Default On-Screen Filter Values

When the [Use Default On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#OnScreenFilter) feature is enabled for web reports in the server profile, each end user can save the values specified to the on-screen filters as the default values for the report and for him. Then the next time when the user runs the report, the saved values will be applied to the on-screen filters by default. The default on-screen filter values work on a user-report basis.

* To save values specified to the on-screen filters in a report as the default values, select **Menu** >  **Edit** > **On-screen Filter Values** and then select **Save as Default**.
* To clear the default values that have been saved to the on-screen filters in a report, select **Menu** > **Edit** > **On-screen Filter Values** and then select **Clear Default**.
* To replace the values specified in the on-screen filters in a report with the saved default values, select **Menu** >  **Edit** > **On-screen Filter Values** and then select **Restore to Default**.

### Link Relationship Between On-Screen Filters

By default, all the on-screen filters applied to the same data components in a web report are interlinked. The link relationship is reflected on the filter values dynamically: selecting a value in one on-screen filter will result in that values which do not belong to the selected value, contain the selected value or relate to the selected value are grayed in all the other linked on-screen filters for distinguishing. For example, there is a filter control based on the field Country and another on City and they both are applied to the same table. When you select USA in the Country filter control, the values in the City filter control will change as follows: if the filter control has scrollbar, the cities belong to USA are displayed in the upper area of the filter control, and the other cities are put in the lower area and grayed out; if it has no scrollbar, all the values remain their positions and the values not belonging to USA are grayed out. In both cases all the values are still selectable.

When using a filter control, you can determine whether or not to make the filter control apply the link relationship via the Link to Other Filters option.

Below is an example showing the logic of other linked on-screen filters:

When:

* Filter1 is applied to DC1, DC2, and DC3.
* Filter2 is applied to DC1.
* Filter3 is applied To DC2.
* Filter4 is applied to DC2 and DC3.

The result:

* For Filter1, other linked filters are Filter2, Filter3, and Filter4.
* For Filter2, other linked filter is Filter1.
* For Filter3, other linked filters are Filter1 and Filter4.
* For Filter4, other linked filters are Filter1 and Filter3

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692802-Going-Through-the-Report-Data)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719281-Using-Web-Controls)
