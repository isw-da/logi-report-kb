---
title: "Manipulating Data Components"
id: 1500009669301
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669301-Manipulating-Data-Components
updated_at: 2021-07-24T20:55:17Z
---

# Manipulating Data Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669341-Synchronizing-Data-Components)

# Manipulating Data Components

You can manipulate data components, which refer to crosstabs, tables, charts, KPI components, and geographic maps, in dashboards as shown below.

**Applying a style to a data component**

Right-select in the component, then on the shortcut menu, select a style from the Apply Style submenu.

**Going through the data of tables, crosstabs and charts**

Going actions enable you to switch among data groups freely for viewing different records without having to create a new data component. They can be performed on table groups, crosstab column/row headers, and data labels on the chart category/series axis as well as the legend entry labels.

Choose the proper one to meet your needs from the following:

* **Go To**   
   Jumps to a different group by replacing the current.
* **Go to by Value**  
   Jumps to another group while applying the current value being selected on as a filter condition.
* **Go Down**  
   Goes from a group which is a higher level in a predefined hierarchy to the one-level-lower group while applying the current selected value as a filter condition.
* **Go Up**  
   Jumps from a group which is a lower level in a predefined hierarchy to the one-level-higher group.

**Note:** You can also directly select group objects to perform the go-down action, however, if the group objects are also defined with some links, you can go down to the next level with a single select only when the select priority of the go-down action is specified to be the highest at design time. Otherwise, you have to use the Go Down command on the objects' shortcut menu to perform the action.

For example demonstration of them, refer to [Going Through the Report Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data).

The go-to-by-value or go-down actions always happen along with the generation of a filter condition. The filters are displayed as "FieldName:Value" at the bottom of the library components, in a row one by one from left to right according to the time they are generated. When the row cannot hold all of the filters, two buttons are displayed at the two ends of the row for scrolling through the filters to the left and right. Each select on the button will show one hidden filter. To remove a filter condition, select **X** right to it.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926780695/dshbrd_mnplt_go.gif)

**Customizing the data format of values in tables, crosstabs and charts**

To customize the data format of the values of a field in a table or crosstab, right-click on any value of the field, then select a format from the Format submenu, or input a format in the text box at the bottom of the submenu and select **Enter** on the keyboard.

You can also customize the data format of the legend entry labels and data labels on the category and series axes if they are of Number or Date/Time type. To do this, right-click on the labels and select the required format from the Format submenu, or input a format in the text box at the bottom of the submenu and select **Enter** on the keyboard.

**Removing component level filters from a data component**

On the shortcut menu of data components, there is an option Remove Filters which is used to remove filter conditions generated via the configuration panel and via message delivery from the data components. These two kinds of filters are referred to as component-level filters.

In dashboards you can also use filter controls to do filtering, however filters created by filter controls are not under the control of the removing component level filter action, because they are regarded as dashboard-level filters.

**Manipulating a table**

* **Filtering data in a table**  
   You can take the following ways to filter data in a table.
  + **Using shortcut menu**   
     Right-select on any value of a detail field by which you want to filter data, then you can see the Filter item which provides a submenu containing the following commands:
    - **Remove Filter**  
       This command is enabled when the field is ever applied a filter. Selecting this item will remove the filter from it.
    - **First N**  
       Filters the field to display only its first N values. You can select a number from the submenu or enter a positive integer into the text box on the submenu to specify the number.
    - **Last N**  
       Filters the field to display only its last N values. You can select a number from the submenu or enter a positive integer into the text box on the submenu to specify the number.
    - **Field values**  
       "Field values" is not the name for a command on the Filter submenu, but represents some items which are the values of the field you right-click on. Select a value and the field will be filtered to show only the specified value.
    - **More**  
       This command is enabled if the Filter submenu cannot list all values of the field. When it is enabled, selecting it brings up the [Select Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009670521-Select-Values) dialog. Select one value in the dialog and the field will be filtered to show only the selected value.
  + **Using filter button on table column header**You can use the filter button on any table column header to filter values in the column if the feature is enabled in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#ColumnHeader).
    By default, the feature is disabled so
    you need to configure the profile before you can use it.
    1. Go to the Profile > Customize Profile > Common tab.
    2. Check the option **Filter on Column Headers**.
    3. Check **Show Sort/Filter Status on Column Headers** if you want the filter buttons to be displayed on the table column headers after the columns are applied with filter conditions.
    4. Select **OK** to save the profile setting.
    5. Run a dashboard containing a table.
    6. Put the mouse pointer on any column header and you can find the filter button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926650135/btn_lblfltr.gif). Select the button a filter list which contains the same items as the [Filter submenu](#Menu) appears. Select the required item to filter the column. When a column is filtered its filter button will be highlighted. The summary column that contains multiple aggregation fields cannot be filtered using this way.
  + **Using labels**  
     With Logi JReport Designer, you can bind a label in a table with a field used in the table to enable filtering on the label by setting the label's Bind Column and Filterable properties. Then in JDashboard you can select the filter button beside the label to filter values of the bound field. This functions the same as via the [table column headers](#Header).

    When a label is bound with a field, if the Filter on Column Header feature is also enabled, the former has higher priority. For example, if you bind the label in column A header with the field in column B, when selecting the filter button on column A header, values in column B are filtered.
* **Sorting data in a group table**  
   You can take the following ways to sort data in a group table. When you sort data in a group table by a detail field and then by another detail field, data in the table will be sorted by the later sort condition first and then by the former sort condition.
  + **Using shortcut menu**  
     Right-select on any value in the table, then on the shortcut menu select **Ascend** or **Descend** from the Sort submenu. If a detail/summary field value is selected on, the sorting will affect the order of detail/summary records in the table; if it is a group field value, the order of groups in the group level represented by the group field will be rearranged. To remove the sort condition, select **No Sort**.
  + **Using the sort button on table column header**You can use the sort button on any table column header to sort values in the column if the feature is enabled in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#ColumnHeader). By default the feature is enabled.
    1. On the Profile > Customize Profile > Common tab, make sure the option Sort on Column Headers is checked.
    2. Check **Show Sort/Filter Status on Column Headers** if you want the sort button to be displayed with the current sort status on the table column headers after the columns are applied with sort orders.
    3. Select **OK** to save the profile setting.
    4. Run a dashboard containing a table.
    5. Put the mouse pointer on any column header and you can find the sort button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920372247/btn_lblsort.gif).
    6. To sort data in the column ascending, select the upward triangle; to sort the values descending, select the downward triangle. When a sort order is applied on a column, the corresponding triangle on its sort button will be highlighted. You can select the highlighted triangle to remove the sort order.

       A summary column that contains multiple summary fields cannot be sorted using this way. Moreover a group header in a web report table created in Web Report Studio is always merged as a table cell. If a summary column contains only one aggregation field which is in a merged group header, you cannot use this way to sort it either.
  + **Using labels**  
     With Logi JReport Designer, you can bind a label in a table with a field used in the table to enable sorting on the label by setting the label's Bind Column and Sortable properties. Then in JDashboard you can select the sort button beside the label to sort values of the bound field. This functions the same as via the [table column headers](#Header).

    When a label is bound with a field, if the Sort on Column Header feature is also enabled, the former has higher priority. For example, if you bind the label in column A header with the field in column B, when selecting the sort button on column A header, values in column B are sorted.
* **Sorting data in a summary table**  
   You can use the [same methods on group tables](#Group) to sort the group and aggregation fields in summary tables. However for summary tables, you can define whether to use major sort or minor sort via the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#Sort) (Profile > Customize Server Preferences > General > Use Major Sort as Default). By default, major sort is applied which is to sort data in a summary table by the last sort condition only, that is to say the later sort condition always replaces the former one. When minor sort is used, sort of a lower group is always based on the sort result of all its higher level groups.

  For example, a summary table contains group fields G1, G2 and G3 (G1 the highest group level and G3 the lowest) and the aggregation fields A1 and A2. When minor sort is applied, after sorting group G1 column ascending, if you apply a sort on group G2 column descending, the table will be sorted based on group G1 ascending first and then group G2 descending, then you further sort group G3 descending and the sort result is G1 ascending, G2 descending and G3 descending. Based on this sort result, you apply the ascending order on the aggregation field A1, and the table is now sorted based on G1 ascending, G2 descending and A1 ascending. Sort order on G3 is removed, this is because all aggregation fields calculate data based on the lowest group in a summary table and they are considered as one group, so on the lowest group and the aggregation fields only one sort order can take effect. Therefore based on the former sort result, if you apply a sort order on G3 again the sort on A1 will be removed.

**Manipulating a chart**

You can perform the following operations on a chart, including the KPI chart in a KPI component.

* **Swapping chart groups**  
   You can switch data between the category and series axes, or between the category and value axes of a chart if there is no field on the series axes.
  To do this, right-click in the chart, then on the shortcut menu, select **Swap Chart Groups**.
* **Sorting category/series labels**  
   You can sort the labels on the category or series axes of a chart in either descending or ascending alphabetical order. To do this, right-click in the chart, then on the shortcut menu, select the required order from the Sort Category or Sort Series submenu.
* **Changing the chart type**  
   Right-select in the chart, then on the shortcut menu, locate **Chart Type**. From the drop-down menu, select the desired chart type and its subtype.
* **Zooming in chart values**  
   For a bar, bench, line, area or stock chart, you can select the values you are interested in to have them zoomed in. To do this, drag the mouse from the start value to the end value you want to select, then release the mouse. The selected values will be zoomed in. If you want to return to the initial status, just select the return button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926638615/btn_wbrpt_return.gif) on the upper right corner of the chart paper.
* **Configuring real time chart settings**   
   For a real time chart, you can further configure it when inserted in a dashboard. To do this:
  1. Right-select the chart and select **Real-time Settings** from the shortcut menu. The [Real-time Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009646242-Real-Time-Settings) dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920583447/rltmset.gif)
  2. Specify the time interval at which the chart will get data and refresh itself automatically in the Refresh Interval text field.
  3. Specify the most recent N records to be kept for the real time data on the chart in the Show Most Recent text field.
  4. Select the **Incremental Fetch** button to add the fields you want to use as the unique key of the real time chart in the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009646322-Unique-Key) dialog.

     Once a unique key is defined, each time when the real time chart automatically updates itself, duplicated data records will be filtered out based on the unique key. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, no more records of this product ID in USA will be added to the real time chart because they have the same unique key value even though the data may have changed. To use this effectively you want to use a unique key value that changes with time such as a datetime field.
  5. Check the **Use Scrollable Bar** checkbox if you want to use a scrollbar to control the visible value range on the X axis of the chart, then specify how many data items will be selected on the scrollbar and displayed on the axis by default, the percentage the scrollbar occupies the whole size of the chart, and whether to show the thumbnail chart in the scrollbar.
  6. Select **OK** to accept the settings and close the dialog.
* **Stopping or resuming a real time chart from refreshing**  
   For a real time chart, you can stop or resume it from automatically refreshing by right-clicking it and selecting the Pause Refresh or Resume command from the shortcut menu.
* **Showing/Hiding the chart legend or legend label**  
  Right-select the chart and select the corresponding show/hide option from the shortcut menu to show or hide the legend or legend label. However, the legend will always be displayed at the export and print result.

  This operation is not supported on KPI charts since they do not have legend.

**Manipulating a crosstab**

* **Sorting column/row header**   
   To sort a column/row header, right-click on the header, then on the shortcut menu, select **Ascend** or **Descend** from the Sort submenu. To remove the sort condition, select **No Sort**.
* **Switching crosstab fields**  
   A convenient way to change the fields in a crosstab is by using the Switch command. To do this, right-click a row/column/summary and select **Switch Row**/**Switch**  **Column**/**Switch Summary** from the shortcut menu. The fields available for the row/column/summary are listed in the submenu with the current used field checked. Select the field you want to use to replace the current one.
* **Adjusting the width of crosstab fields according to the contents**  
   When the contents in the field of a crosstab need more space to completely display, you can adjust the width of the field according to its contents. To achieve it, right-click the field and select **Autofit** from the shortcut menu.

**Manipulating geographic map group markers/areas**

* **Going up/down on geographic map group markers/areas**
  + For the group level that is higher than some other group levels in a geographic map component, point to its group marker/area, right-click it and select **Go Down** from the shortcut menu to jump one group level down.
  + For the group level that is lower than some other group levels in a geographic map component, point to its group marker/area, right-click it and select **Go Up** from the shortcut menu to jump one group level up.
* **Showing/Hiding geographic map group markers/areas**  
   By default, all visible group markers/areas are shown. To hide them, right-click the geographic map (not the group markers/areas) and select **Hide Markers/Areas** from the shortcut menu. If you want to show them again, right-click the geographic map and select **Show Markers/Areas** from the shortcut menu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669341-Synchronizing-Data-Components)
