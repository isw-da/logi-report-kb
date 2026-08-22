---
title: "Applying Filters in Web Report"
id: 5741470839191
section: "Web Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741470839191-Applying-Filters-in-Web-Report
updated_at: 2022-10-31T17:18:34Z
---

# Applying Filters in Web Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741476511127-Going-Through-Web-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741484852887-Using-Web-Controls-in-Web-Report)

# Applying Filters in Web Report

You can apply filters to business views and data components such as tables, crosstabs, charts, banded objects, and KPIs in a web report to narrow down the data in the web report. This topic describes how you can apply filters in web reports.

This topic contains the following sections:

* [Applying Filters to Datasets for Data Components](#BV)
* [Filtering the Data Components in a Report](#Component)
  + [Using the Filter Dialog](#Dialog)
  + [Using the Filter Panel](#Panel)
  + [Using the Shortcut Menu](#Menu)
  + [Using Column Headers](#Header)
  + [Using Labels](#Label)
* [Managing On-Screen Filters](#OnScreen)
  + [Saving and Using Default On-Screen Filter Values](#Default)
  + [Link Relationship Between On-Screen Filters](#Link)

## Applying Filters to Datasets for Data Components

When creating a web report, you can apply filters to the datasets of data components to narrow down the data scope of the data components. Filters for datasets are defined into two categories in Logi Report: predefined filters and user defined filters. As the name suggests, predefined filters are defined in advance when you create or edit the related business views in Designer, and user defined filters are created on the datasets when you use them.

You can define dataset filters on the component level in Web Report Studio. Each time you create a data component, you can apply a filter to the dataset it uses without affecting other data components based on the same dataset.

**To apply a filter to the dataset that a data component uses:**

1. Do any of the following to open the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985329714327-Edit-Dataset-Filter-Dialog-Box-Properties):
   * Navigate to **Menu** > **Edit** > **Edit Dataset Filter**.
   * Select the **Dataset Filter** button ![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905616155543/btn_wbrpt_qryfltr.gif) on the toolbar.
   * Right-click a data component and select **Edit Dataset Filter** from the shortcut menu.
   * For a table, chart, crosstab, or banded object, while creating or editing it with the report wizard, select **Filter** next to the **Data Source** drop-down list.
2. If you accessed the dialog box from the menu or toolbar, select a data component from the **Apply To** drop-down list to filter the dataset it uses.
3. Specify the filter you want to apply to the dataset.

   Server lists all the predefined filters of the business view that the specified data component uses, in the **Filter** drop-down list. Choose the one you want to apply. If you want to further edit the filter, select it and then redefine the filter. Server saves the edited filter as a user defined filter to the dataset.

   If you prefer to define a filter on your own, select **User Defined** from the **Filter** drop-down list, then define the filter according to your requirements.

   The dialog box has the basic and advanced modes for you to define a filter using either [simple expressions](#Simple) or [complex expressions.](#Complex)

   * **To define a filter using simple expressions:**
     1. Make sure the dialog box is in the basic mode.

        ![Edit Dataset Filter dialog box - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/9905575240087/edtdtstfltr_basic.gif)
     2. Select the field you want to filter from the field drop-down list.
     3. From the operator drop-down list, select the operator with which you want to compose the filter expression.
     4. Type the values of the field in the value text box, or select one or more values from the drop-down list.

        When you see **More...** at the end of the value list, you can select it to open the [Select Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741446661015-Select-Values-Dialog-Box-Properties), which lists more values, and then select the values you want.

        When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\". To specify an empty string as the value for a field of String type, simply leave the text box blank (value length=0).

        You can also select the parameter button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/9905575308823/btn_dshbrd_prm.gif) and then select a parameter to specify the value dynamically. When the available parameters cannot meet your requirement, you can [create a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/5741476426263-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-#Param) to use in the filter.
     5. If you want to add another condition line, from the logic operator drop-down list,
        + To add a condition line of the AND relationship with the current line, select **And**, then define the expression.
        + To add a condition line of the OR relationship with the current line, select **Or**, then define the expression.

        You can repeat this to add more condition lines. To delete a condition line, select the delete button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905575282199/btn_pgrpt_no.gif) on its left.
   * **To define a filter using complex expressions:**
     1. Select **Advanced** to switch to the advanced mode.

        ![Edit Dataset Filter dialog box - Advanced mode](https://devnet.logianalytics.com/hc/article_attachments/9905575342359/edtdtstfltr_adv.gif)
     2. Select **Add Condition** to add a condition line.
     3. From the field drop-down list, select the field you want to filter.
     4. From the operator drop-down list, select the operator with which you want to compose the filter expression.
     5. Type the values of the field in the value text box, or select one or more values from the drop-down list.

        When you see **More...** at the end of the value list, you can select it to open the [Select Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741446661015-Select-Values-Dialog-Box-Properties), which lists more values, and then select the values you want.

        When you type multiple values manually, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
        To specify an empty string as the value for a field of String type, simply leave the text box blank (value length=0).

        You can also select the button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/9905575308823/btn_dshbrd_prm.gif) and then select a parameter from the drop-down list to specify the value dynamically. When the available parameters cannot meet your requirement, you can [create a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/5741476426263-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-#Param) to use in the filter.
     6. To add another condition line, select **Add Condition** and define the expression.
     7. Select the logic button until you get the required logic to specify the relationship between the two filter expressions. The logic can be AND, OR, AND NOT, or OR NOT.
     8. You can repeat the preceding steps to add more condition lines.
     9. To group some conditions, select them and then select **Group**. Server adds the selected conditions in one group, and they work as one line of filter expression. It is the equivalent of adding parenthesis in a logic expression.
     10. You can further group conditions and groups together.
     11. To take any condition or group in a group out, select it, and then select **Ungroup**.
     12. To adjust the priority of a condition line or a group, select it and then select **Up** or **Down**.
     13. To delete a condition line or a group, select it, and then select **Delete**.

   **Tip:** When the dialog box is in the basic mode, and you select a predefined filter from the **Filter** drop-down list which is a complex one, Server switches the dialog box to the advanced mode automatically.
4. Select **OK** to apply the filter. If you opened the Edit Dataset Filter dialog box from the report wizard, Server applies the specified filter to the dataset after you finish the wizard.

   If the filter conditions use parameters, Server lists the parameters in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/5741490884759-Applying-Parameters-to-Web-Report). You can then specify the parameter values in the panel to dynamically define the filter conditions.

## Filtering the Data Components in a Report

To filter the data components in a web report, you can take any of the following ways: use the Filter dialog box, use the Filter panel, or [use filter controls](https://devnet.logianalytics.com/hc/en-us/articles/5741484852887-Using-Web-Controls-in-Web-Report#Filter). For tables, you can also filter them via shortcut menu, column headers, or labels, and for banded objects, via shortcut menu and labels.

### Using the Filter Dialog

When using the Filter dialog box to filter report data, you can only apply the filter to a specific data component in the current web report.

1. Navigate to **Menu** > **Edit** > **Filter**, or select the **Filter** button ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/9905578238359/btn_filter.gif) on the toolbar. Server displays the [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449994391-Filter-Dialog-Box-Properties).

   ![Filter dialog - Basic mode](https://devnet.logianalytics.com/hc/article_attachments/9905654923287/fltr_basic.gif)
2. From the **Apply To** drop-down list, select the data component in the report which you want to apply the filter to.

   **Tip:** For web reports that you created in Logi Report Designer, the default selected data component and available data components in the **Apply To** drop-down list are determined by the **Default for Filter** and **Invisible for Filter Dialogs** properties of the components.
3. Define the filter using either [simple expressions](#Simple) or [complex expressions](#Complex).
4. Select **OK** to apply the filter. If the filter conditions use parameters, Server lists the parameters in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/5741490884759-Applying-Parameters-to-Web-Report), and you can specify the parameter values in the panel to dynamically define the filter conditions.

The Filter dialog box provides an entry to all the filters that the current web report uses. You can select **Inspector** to view more filter information in the [Filter Inspector dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741429092119-Filter-Inspector-Dialog-Box-Properties).

### Using the Filter Panel

You can use the Filter panel on the left of Web Report Studio to filter data components in the current report, and create in the panel as many filters as you want which resemble [filter controls](https://devnet.logianalytics.com/hc/en-us/articles/5741484852887-Using-Web-Controls-in-Web-Report#Filter).

The filters that you created via the Filter panel are referred to as on-screen filters, the values of which you can [save as the default ones](#Default).

**To use the Filter panel:**

1. Select the add button + on the title bar of the panel. Server displays the [Select Field dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741436598295-Select-Field-Dialog-Box-Properties).

   ![Select Field dialog - Filter](https://devnet.logianalytics.com/hc/article_attachments/9905633669015/slctfld.gif)
2. The **Select Fields** box lists all the group and detail objects in the business views that the current report uses. Select the objects of the same data type based on which you want to create the filter.
3. From the **Apply To** drop-down list, select the data components in the report to apply the filter to.

   By default, Server applies the filter to all the data components created using the business view that contains the selected objects. If you select the data components which are not based on the same business view as any selected objects, Server does not add those objects with their values in the filter when it adds the filter in the Filter panel.
4. Select **OK**. Server adds a filter box in the Filter panel. If the objects bound to the filter box have the same values, the values are distinctive in the filter box.
5. Select the values with which you want to filter the report data. Server applies a filter condition based on the selected values to the specified data components in the report.

   You can make use of the Ctrl or Shift key to select multiple values. If the values themselves have inter-relationship, after you make the selection, Server deals with the rest values to put the related ones on the top and gray the ones that have no relationship with the selected values. The grayed values are still selectable.

The following section describes more about the Filter panel:

![Filter Panel](https://devnet.logianalytics.com/hc/article_attachments/9905655004695/wbrpt_edt_fltr_fltrpnl1.gif)

You can use the buttons on the bottom of the Filter panel to deal with the value selection in the panel.

* **Back**  
  Select to go back to the previous value selection status and refresh the report data accordingly.
* **Clear**  
  Select to remove all the value selection histories and all the filter conditions based on the selections and refresh the report data accordingly.
* **Forward**  
  Select to go forward to the next value selection status and refresh the report data accordingly.

For each filter in the panel, you can manage it with the buttons on its title bar or the shortcut menu:

![Filter Panel options](https://devnet.logianalytics.com/hc/article_attachments/9905655037463/wbrpt_edt_fltr_fltrpnl2.gif)

* **Search**![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)  
   Select to open the search bar right above the value list for searching the values you want. For more information, see the [Select Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741446661015-Select-Values-Dialog-Box-Properties).
* **Clear**![Clear button](https://devnet.logianalytics.com/hc/article_attachments/9905617258903/btn_clear.gif)  
   Select to cancel the selection of values in the current filter box.
* **Clear All**  
   Select to cancel the selection of all values in the Filter panel.
* **Sort**![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905629589015/btn_sort1.gif)  
   Select to sort the values in the ascending or descending order.
* **Delete**![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)  
   Select to remove the filter from the Filter panel and remove the corresponding filter conditions from the report too.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* Server removes the values in the filter box when you remove the data components that use the same business view as the involved objects of these values.
* When there are more than 300 values for an object, Server uses Big Data Loading logic. In this case, the Shift Key for multiple selection does not work.
* You cannot see the filter conditions created via the Filter panel when you open web reports in Logi Report Designer.
* If you delete all the data components in a report that use a business view, Server removes the objects in the business view from the Filter panel too.

### Using the Shortcut Menu

For tables and banded objects, you can use the filter-related commands on the shortcut menu to filter the data. To do this, right-click any value of a detail field by which you want to filter data, to show the shortcut menu. You will see the **Filter** submenu with these commands:

![Filter Submenu](https://devnet.logianalytics.com/hc/article_attachments/9905655062039/wbrpt_edt_fltr_menu.gif)

* **Remove Filter**  
  Server enables this command after you have applied filter on the field. You can select the command to remove the filter from the field.
* **First N**  
  It filters the field to display only its first N values. You can select a number from the submenu or type a positive integer into the text box on the submenu to specify the number.
* **Last N**  
  It filters the field to display only its last N values. You can select a number from the submenu or type a positive integer into the text box on the submenu to specify the number.
* **Select Values**   
  Select this item and Server displays the [Select Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741446661015-Select-Values-Dialog-Box-Properties) for you to select the values to filter the field with.

### Using Column Headers

You can use the filter button on any table column header to filter values in the column. Before doing this, you need to enable the feature in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties#ColumnHeader) first.

1. Choose according to your user account:
   * Anyone can configure for themselves: navigate to the **My Profile** > **Customize Profile** page, then select **Customize Profile**. Server displays the [Customize Profile dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties). Select **Enable Customize Properties**.
   * Administrators can configure for all users: navigate to the **Administration** > **Server Profile** > **Customize Profile** page. Then, select **New Profile** if you want to create a new profile or select **Edit** to update an existing profile (later you need to make sure you select this profile as the default profile). Server displays a profile dialog box. Select **Common**.
2. Select **Filter on Column Headers**.
3. Select **Show Sort/Filter Status on Column Headers** if you want the filter buttons to display on the table column headers after you apply filter conditions to the columns. Select **OK** to save the profile setting.
4. Run a web report that contains a table in Web Report Studio.
5. Hover over any column header and you can see the filter button ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/9905655086359/btn_lblfltr.gif).

   ![Filter Button on Column Header](https://devnet.logianalytics.com/hc/article_attachments/9905655111959/wbrpt_edt_fltr_header1.gif)
6. Select the filter button ![Filter button](https://devnet.logianalytics.com/hc/article_attachments/9905655086359/btn_lblfltr.gif). Server displays a filter list which contains the same items as the [Filter submenu](#Menu).
7. Select the required item to filter the column. Server highlights the filter button in the column.

   ![Highlighted Filter Button](https://devnet.logianalytics.com/hc/article_attachments/9905633821335/wbrpt_edt_fltr_header2.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)You cannot filter a summary column that contains multiple aggregation objects, via its column header.

### Using Labels

With Logi Report Designer, you can bind a label in a table/banded object with a field in the table/banded object, to enable filtering on the label, by setting the label's **Bind Column** and **Filterable** properties. Then, when running the table/banded object in Web Report Studio, you can select the filter button beside the label to filter values of the bound field. This functions the same as via the [table column headers](#Header).

When a label is bound with a field, if you have also enabled the **Filter on Column Header** feature in the server profile, the former has higher priority. For example, if you bind the label in the column A header with the field in column B, when you select the filter button on the column A header, Server filters the values in column B.

**Tip:** After filtering the data in a table or banded object by either shortcut menu, column header, or label, you may notice the corresponding filter expression in the Filter dialog box.

## Managing On-Screen Filters

Filters that you created via the [Filter panel](#Panel) and [filter controls](https://devnet.logianalytics.com/hc/en-us/articles/5741484852887-Using-Web-Controls-in-Web-Report#Filter) in a web report are called on-screen filters. You can save values for them as the default values.

### Saving and Using Default On-Screen Filter Values

When you have enabled the [Use Default On-screen Filter Values](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#OnScreenFilter) feature for web reports in the server profile, you can save the values that you specified to the on-screen filters as the default values for a web report and for yourself. Then the next time when you run the web report, Server applies the saved values to the on-screen filters by default. The default on-screen filter values work on a user-report basis.

* To save values that you specified for the on-screen filters in a report as the default values, navigate to **Menu** > **Edit** > **On-screen Filter Values**, and then select **Save as Default**.
* To clear the default values that you have saved for the on-screen filters in a report, navigate to **Menu** > **Edit** > **On-screen Filter Values**, and then select **Clear Default**.
* To replace the values that you specified for the on-screen filters in a report with the saved default values, navigate to **Menu** > **Edit** > **On-screen Filter Values**, and then select **Restore to Default**.
* To generate the report data by applying all filters to the database, navigate to **Menu** > **Edit** > **On-screen Filter Values**, and then select **Push Down**.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

  + Generally, for small data, setting Push Down as "false" can reduce the number of database accesses; for large data, setting Push Down as "true" can improve the performance by pushing down the execution to the database.
  + On-Screen Filter Push-Down has higher priority than Business View Prefetch (See the **Prefetch** property in Business View Properties in the *Logi Report Designer Guide*) and Dataset Reuse.
  + On-Screen Filter Push-Down cannot work in reports that have used one of the following data resources: [In-Memory Cube](https://devnet.logianalytics.com/hc/en-us/articles/5741437977495-Managing-In-Memory-Cubes), [Cached Report Data](https://devnet.logianalytics.com/hc/en-us/articles/5741453292183-Managing-Cached-Report-Data), and Query Result Set.

### Link Relationship Between On-Screen Filters

By default, all the on-screen filters that you applied to the same data components in a web report are interlinked. The link relationship is reflected on the filter values dynamically: selecting a value in one on-screen filter will result in that values which do not belong to the selected value, contain the selected value, or relate to the selected value are grayed in all the other linked on-screen filters for distinguishing. For example, there is a filter control based on the field Country and another on City, and they both apply to the same table. When you select USA in the Country filter control, the values in the City filter control change as follows: if the filter control has a scroll bar, Server displays the cities belonging to USA in the upper area of the filter control, and put the other cities in the lower area and grays them out; if it has no scroll bar, all the values remain their positions, and Server grays out the values not belonging to USA. In both cases all the values are still selectable.

When using a filter control, you can determine whether to make the filter control apply the link relationship via the **Link to Other Filters** option.

See an example showing the logic of other linked on-screen filters:

When:

* Filter1 applies to DC1, DC2, and DC3.
* Filter2 applies to DC1.
* Filter3 applies To DC2.
* Filter4 applies to DC2 and DC3.

The result:

* For Filter1, other linked filters are Filter2, Filter3, and Filter4.
* For Filter2, other linked filter is Filter1.
* For Filter3, other linked filters are Filter1 and Filter4.
* For Filter4, other linked filters are Filter1 and Filter3

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741476511127-Going-Through-Web-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741484852887-Using-Web-Controls-in-Web-Report)
