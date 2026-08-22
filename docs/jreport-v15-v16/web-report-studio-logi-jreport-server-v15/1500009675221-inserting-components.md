---
title: "Inserting Components"
id: 1500009675221
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components
updated_at: 2021-07-24T20:53:35Z
---

# Inserting Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675201-General-Operations-in-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components)

# Inserting Components

You can insert components into a web report via the Components panel on the left of the Web Report Studio window.

The following table lists the report areas that are valid targets for the various components：

|  | Report Layout Area | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Component | Page Header/Footer | Report Body | Tabular Cell | Table Cell |
| Chart | Y | Y | Y | N |
| Crosstab | Y | Y | Y | N |
| Table | Y | Y | Y | N |
| KPI component | Y | Y | Y | N |
|  |  |  |  |  |
| Label | Y | Y | Y | Y |
| Image | Y | Y | Y | N |
| Multimedia object | Y | Y | Y | N |
| Web control | Y | Y | Y | N |
|  |  |  |  |  |
| Group object | Y | Y | Y | Y |
| Detail object | Y | Y | Y | Y |
| Aggregation object | N | Y | N | Y |
| Formula | Y | Y | Y | Y |

Below is a list of the sections covered in this topic:

* [Inserting a Table](#Table)
* [Inserting a Crosstab](#Crosstab)
* [Inserting a Chart](#Chart)
* [Inserting a KPI Component](#KPI)
* [Inserting a Label](#Label)
* [Inserting an Image](#Image)
* [Inserting a Multimedia Object](#Multimedia)
* [Inserting a Web Control](#WebControl)
* [Inserting a Special Field](#Special)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Table

The procedure for inserting tables in a web report varies with the way with which you use to access Web Report Studio: [quick start way or standard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio#Way).

**To insert a table when Web Report Studio is in the quick start way**:

1. Drag ![](https://devnet.logianalytics.com/hc/article_attachments/4404926632471/btn_wbrpt_2tbl.gif) from the visualization toolbar or **Table** from the Components panel to the destination where you want to insert the table.
2. In the Select Data Source dialog, [select a business view and define the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009675381-Quick-Start-with-a-Table-Report#SelectData) as required.
3. Select **OK** to insert the table.

**To insert a table when Web Report Studio is in the standard way:**

When Web Report Studio is in the standard way, you can choose the table type as you want: [Group Above, Group Left, Group Left Above](#Group) or [Summary Table](#Summary).

* **Inserting a group table**
  1. Drag ![](https://devnet.logianalytics.com/hc/article_attachments/4404926632471/btn_wbrpt_2tbl.gif) from the visualization toolbar or **Table** from the Components panel to the destination where you want to insert the table. The [Insert Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009672241-Insert-Table) dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920389143/insrttbl_dsply.gif)
  2. Specify a title for the table in the Table Title text field, and if required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to set the font properties for the title.
  3. From the Data Source drop-down list, select the business view in the current catalog, on which the table will be built. If required, select the **Filter** button to [add some filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters) to the business view to narrow down data displayed in the table.
  4. Select a group type from the table type drop-down list: Group Above, Group Left, or Group Left Above.
  5. In the Details tab, add the required fields from the Resources box to be displayed in the table. Specify the display name of any added field in the Label column if necessary. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) to adjust the order of the fields.
  6. If you want to sort data in the table by values of specified fields, select the **Sort Fields By** button and set the sort manner in the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009647142-Custom-Sort) dialog.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920389399/cstmsrt.gif)

     1. Select a field as the sort by field from the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) to add it to the Sort By column.
     2. Select a sort order from the Sort column. Data in the table will then be sorted based on values of the specified sort by field in ascending or descending order.
     3. Repeat the above two steps to add more fields as the sort by fields if needed. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) to adjust the order of the sort by fields.
     4. Select **OK** to accept the sort criteria.
  7. In the Group tab, add the group objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) as the grouping criteria. Specify the sort manner of each group in the Sort column, which can be No Sort, Ascend, Descend, or Custom Sort. When Custom Sort is selected, you can select some fields in the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009647142-Custom-Sort) dialog, then the groups at the specified group level will be sorted by the values of the first record in each group on the related fields.
     Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) to adjust the order of the groups if needed.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920389783/insrttbl_grp.gif)
  8. To add summaries, go to the Summary tab. Select the group to which the summary will be applied, and add an aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) as the summary field. You can add several summaries to any group level. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) to adjust the order of the summary fields in the current group or move a summary field to another group if needed. For the Group Left table, you can use the Row and Column columns to control the position of the summary fields in the table.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920390039/insrttbl_sum.gif)
  9. Select **OK** to insert the table.
* **Inserting a summary table**  
   Summary tables are used for showing group and summary information so they can only contain group and aggregation fields. In a summary table, the groups on the left are higher than those on the right and calculation of the aggregation fields is always based on the innermost group no matter where they are positioned in the table.
  1. Drag ![](https://devnet.logianalytics.com/hc/article_attachments/4404926632471/btn_wbrpt_2tbl.gif) from the visualization toolbar or **Table** from the Components panel to the destination where you want to insert the table. The [Insert Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009672241-Insert-Table) dialog appears.
  2. Specify a title for the table in the Table Title text field, and if required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to set the font properties for the title.
  3. From the Data Source drop-down list, select the business view in the current catalog, on which the table will be built. If required, select the **Filter** button to [add some filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters) to the business view to narrow down data displayed in the table.
  4. Select Summary Table from the table type drop-down list.
  5. In the Columns tab, add the required fields from the Resources box to be displayed in the table. Only aggregation and group fields in the specified business view can be added to the table. For a group field you can specify the sorting manner of the group in the Sort column, which can be No Sort, Ascend, Descend, or Custom Sort. When Custom Sort is selected, you can select some fields in the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009647142-Custom-Sort) dialog, then the groups at the specified group level will be sorted by the values of the first record in each group on the related fields. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) to adjust the order of the fields if needed. The order of the group fields determines the group levels in the table: the topmost group field the highest group level and the lowest group field the innermost group level. All the aggregation fields are parallel and calculate based on the lowest group.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920390679/insrttbl_sumtable.gif)
  6. In the Summary screen, you can insert the aggregation fields selected in the Columns tab to the table header/footer and to the group headers/footers of existing groups. First select an aggregation field in the Resources box, then select the checkboxes representing the required locations.
     The aggregation field will be placed in the intersection of its summary column and the table/group header/footer row.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920390935/insrttbl_sum1.gif)
  7. Select **OK** to insert the table.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Crosstab

1. Drag **Crosstab** from the Components panel or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920367639/btn_wbrpt_2crstb.gif) from the visualization toolbar to the destination where you want to insert the crosstab. The [Insert Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009672161-Insert-Crosstab) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920391319/insrtcrstb.gif)
2. Specify a title for the crosstab in the Crosstab Title text field, and if required, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to set the font properties for the title.
3. From the Data Source drop-down list, select the business view in the current catalog, on which the crosstab will be built. If required, select the **Filter** button to [add some filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters) to the business view to narrow down data displayed in the crosstab.
4. From the Resources box, select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379799/btn_addrow.gif) to add it to the Columns or Rows box as a group field. Then in the Label column, edit the display name of the group object if required. This will label the row/column when the crosstab is displayed. In the Sort column, specify the sorting manner for the group field.
5. Select an aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) or a numeric detail object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif) and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920380311/btn_addsum.gif) to add it to the Summaries box as an aggregate field. If a detail object is added, specify the aggregate function for it in the Aggregation column. In the Label column, edit the display name of the aggregate field, which will label the summaries.  If necessary, you can specify a comparison function for the aggregate field.

   **To specify a comparison function for an aggregate field:**

   1. Select the aggregate field in the Summaries box and select the **Comparison Function** button. The [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009671541-Comparison-Function) dialog appears.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404920391831/cmprsnfctn.gif)
   2. From the Function drop-down list, select the required function: Percentage, Permillage or Difference.
   3. Specify a position for the comparison function.
      * **Comparison Function Spans on Row Direction**  
         The comparison function will be placed into the column total cell of the crosstab.
      * **Comparison Function Spans on Column Direction**  
         The comparison function will be placed into the row total cell of the crosstab.
   4. Numbers that form the calculation of the comparison function are determined by the Break by and Refer to drop-down lists.

      Items in the Break by drop-down list vary with the position of the comparison function. It specifies the first parameter of the comparison function: the aggregate field or a subtotal.

      All available items are displayed in the Refer to drop-down list according to what you have selected from the Break by drop-down list. These items are outer group subtotals and the grand total. Select one as the other parameter of the comparison function.
   5. Select **OK** and you can see that a new field is added into the Summaries box. Set the display name for the field in the Label column as required.
6. Add more group/aggregate fields to the crosstab. If you want to remove any field, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif). To adjust the order of the fields, select a field and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif).
7. Select **OK** to insert the crosstab.

**Tip:** When you create a crosstab with wizard, by default there will be no labels generated for its columns, rows and summaries (the Label columns in the Columns, Rows and Summaries boxes of the wizard are blank by default). You can make Logi JReport automatically provide the labels which by default are the display names of the added objects by setting the [profile options](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#Crosstab) Add Labels for Crosstab Rows and Columns and Add Labels for Crosstab Summaries. You can also customize the profile option Display Crosstab Summaries Vertically to make the summaries in crosstabs displayed horizontally in Web Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Chart

Normally, a chart displays values in a static way and you cannot change the values on it once it is created. However, Logi JReport provides you with options to make the chart interactive and dynamic. For example, if your data source uses data that changes quickly over time such as stock market values, you can create a real time chart, so that the chart will update itself based on a defined interval by using the real time data from the data source. You can make a chart move at runtime based on the value changes of a motion field by creating a motion chart. In a motion chart, the chart is playable. You can start or stop the chart to play the dynamic trend of the motion field, control the moving speed of the chart, and if you create a bubble motion chart, you can even use a trail control to make the chart move showing a bubble or line trail.

In Web Report Studio, when you create a chart, you can choose to make it a [common chart](#Common), an [organization chart](#Org), a [heat map](#Heatmap), a [real time chart](#RealTime), or a [motion chart](#Motion).

**To create a common chart:**

1. Drag **Chart** from the Components panel or a chart icon from the visualization toolbar to the destination where you want to insert the chart. The [Insert Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009647562-Insert-Chart) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926645527/insrtcht.gif)
2. Specify a title for the chart in the Chart Title text field, and if required select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to set the font properties for the title.
3. From the Data Source drop-down list, select the business view in the current catalog, on which the chart will be built. If required, select the **Filter** button to [add some filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters) to the business view to narrow down data displayed in the chart.
4. To create a single chart, in the Primary Axis box, select the required chart type from the chart type drop-down list.

   To create a combo chart, select**![](https://devnet.logianalytics.com/hc/article_attachments/4404920392343/btn_wbrpt_adcmbtyp.gif)** above the Primary Axis box and an additional chart type will be added. You can replace the additional chart type by selecting the required one from the chart type drop-down list. Repeat this to add more chart types. Check the **Secondary Axis** checkbox if you want to have the secondary axis (Y2) and define the chart types on the axis as required. To delete a type, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif).
5. In the Primary Axis or Secondary Axis box, select a chart type and add an aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) or an additional value ![](https://devnet.logianalytics.com/hc/article_attachments/4404920392599/btn_wbrpt_adtnl.gif) as the data of the type. You can add more than one data field to a chart type. Each added chart type shall have at least one data field.

   If you select a bubble chart type, you need to specify the fields to be shown on the bubble X axis, Y axis and the value you want to show as the bubble size in the value box. Note that when you specify a value for the bubble X axis, this value will be displayed on the category axis instead of the one specified in the Bubble box. However, the value defined in the Bubble box will also be included in data calculation.

   **To add an additional value to a chart type:**

   1. Select the chart type in the value box.
   2. In the Resources box, expand the **Additional Values** node, then select **Constant Value**/**Average Value**.
   3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) beside the value box. The Edit Additional Value dialog appears.
   4. In the Name text box, specify the display name for the constant/average value.
   5. Input the constant value with numeric type in the Value text box, or select a field based on which the average value will be calculated from the Based On drop-down list.
   6. Select **OK**, and the defined constant/average value will be added to the chart type.

      To modify a constant/average value, select the value in the value box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif). In the Edit Additional Value dialog, edit the value as required.
6. Select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) in the Resources box and add it to the category or series box, the data of which will be displayed on the corresponding axis. The names of the two boxes for the axes vary with different chart types, for example, the actual names are X-Axis and Clustering for a clustered bar chart.
7. If you want to define some sort order and Select N condition on the category or series field, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920392855/btn_wbrpt_topn.gif) above the category or series box, then define the order and condition in the Category/Series Options dialog.

   **To define a sort order and Select N condition on the category/series field:**

   1. In the Category Order box of the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009647162-Category-Options) dialog/Series Order box of the [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009647762-Series-Options) dialog, specify in which order values of the category/series field will be sorted.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404926645911/ctgryoptn.gif)
   2. In the Category/Series Selection box, specify the Select condition to All, Top N or Bottom N. If All is selected, all category/series values will be shown in the chart; if Top N or Bottom N is selected, the text field next to it will be enabled and you can specify an integer here, which means that the first or last N category/series values will be shown in the chart**.**
   3. Check the **Based On** checkbox and specify values for the two drop-down lists that follow according to your requirement.

      If Based On is unchecked, the order of the first or last N category/series values will be based on what you specify in the Category/Series Order box of the dialog; if you check it, the order will be based on values of the summary field and the sort direction you specify in the drop-down lists next to Based On.
   4. If you have selected Top N or Bottom N from the Select drop-down list, you can check the **Remaining Categories**/**Series In** checkbox and then type a character string in the text field, so that the category/series values beyond the first or last N range will be merged into the group with the name as that character string.
   5. If you are specifying the Order/Select N condition for the category field, you can also check **Overall Series** to calculate the top or bottom N category values based on the series values.
   6. If necessary, you can input a number M in the Skip First text field, then the first M category/series values will be skipped and the Select N condition will begin with M+1. The skipped values will be merged into the Remaining Categories/Series group.
   7. Select **OK** to accept the settings.
8. Select **OK** to insert the chart.

**To create an organization chart:**

Organization chart, also referred to as org chart, is a one-root-node-tree-structure diagram showing the ownership or reporting to relations among the nodes which are mapped to a specific entity.

1. Repeat the above [steps 1 to 4](#Common) for creating a common chart.
2. In the Primary Axis box, select the **Org** chart type.
3. Select **Node** in the value box, next select a field from the Resources box, and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) to add the field for defining the entity.
4. Select **Parent** in the value box, next select a field from the Resources box, and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) to add the field for defining the ownership or reporting to relations among the entity members. For example, if the child node field is Employee ID, the parent field can be the one about IDs showing which employ ID reports to which employ ID. Note that the parent field should use different one from the child node field.
5. The properties panel displays a node model in the org chart. You can add objects including data objects, labels, and images from the Resources box into the node by using the ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) button and then adjust their positions and sizes in the node and the size of the node if required. Those added objects will be displayed in each node as the information about the entity members.
6. Select **OK** to insert the chart.

**To create a heat map:**

Heat map is composed of rectangles marked by colors and sizes. The rectangles are grouped by group fields. Each rectangle represents a value of a group field or a combination of values of multiple group fields.

1. Repeat the above [steps 1 to 4](#Common) for creating a common chart.
2. In the Primary Axis box, select the **Heat Map** chart type.
3. Add the fields used to group the data into the Area box one by one. Use ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) and ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) to adjust the order of the groups. To remove a group field, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif).
4. If you want to define some sort order and Select N condition on a group field, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920392855/btn_wbrpt_topn.gif) above the Area box. In the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009672121-Group-Options) dialog, specify the order and condition [in the same way you do to the category/series field](#SlctN).
5. Add proper summaries into the Property box.

   The summary properties should match the groups. For example, if the groups level is A > B > C, the static summaries grouped by C can be inserted into the Property box, but the static summaries grouped by A, B or other fields cannot.

   If no group is specified in the Area box, you can insert any static summary, and its group-by field will be inserted into the Area box automatically.
6. From both Area and Property boxes, specify the fields to do color by and size by, and select the fields to display in the innermost rectangle in the heat map.

**To create a real time chart:**

Real time chart is supported on single bar, bench, line, and area chart types.

1. Repeat the above [steps 1 to 4](#Common) for creating a common chart.
2. In the Primary Axis box, select a chart type of bar, bench, line, or area, then add the detail objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif) or group objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif)of numeric type as the data of the type.
3. Check the **Real Time** checkbox.
4. By default, Use System Time for Category is checked and you can see the text Use System Refresh Time is displayed in the category box, which means the time at which the chart refreshes itself will be used as the category value. You can uncheck the Use System Time for Category option and add another group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) to be displayed on the category axis. If you want to define some sort order and Select N condition on the category field you specify, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920392855/btn_wbrpt_topn.gif) above the category box, then [define the order and condition](#SlctN) in the Category Options dialog.
5. Specify the time interval at which the chart will get data and refresh itself automatically in the Refresh Interval text field.
6. Specify the most recent N records to be kept for the real time data on the chart in the Show Most Recent text field.
7. Select the **Incremental Fetch** button to add the fields you want to use as the unique key of the real time chart in the Unique Key dialog.

   Once a unique key is defined, each time when the real time chart automatically updates itself, duplicated data records will be filtered out based on the unique key. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, no more records of this product ID in USA will be added to the real time chart because they have the same unique key value.
8. Select **OK** to insert the chart.

**To create a motion chart:**

Motion chart is supported on single chart of bar, bench and bubble types.

1. Repeat the above [steps 1 to 4](#Common)  for creating a common chart.
2. In the Primary Axis box, select a chart type of bar, bench or bubble, then add the required aggregation objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) or additional values ![](https://devnet.logianalytics.com/hc/article_attachments/4404920392599/btn_wbrpt_adtnl.gif)as the data of the type.

   If you select a bubble chart type, you need to specify the fields to be shown on the bubble X axis, Y axis and the value you want to show as the bubble radius in the value box. Note that when you specify a value for the bubble X axis, this value will be displayed on the category axis instead of the one specified in the Bubble box. However, the value defined in the Bubble box will also be included in data calculation.
3. Select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) in the Resources box and add it to the category or series box, the data of which will be displayed on the corresponding axis.
4. If you want to define some [sort order and Select N condition](#SlctN) on the category or series field you specify, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920392855/btn_wbrpt_topn.gif) above the category or series box, then define the order and condition in the Category/Series Options dialog.
5. Check **Motion Bar for Playable Chart**, add a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif)of Integer, Date or Time type as the motion field. When the element is of the Date data type, you can define some special function for it by selecting the Special Function button.
6. Select **OK** to insert the chart.

When a motion chart is created, you can use the motion control section to make the chart move. Select the play button and the chart will show its dynamic trend based on the value change of the motion field which is bound in the motion bar. To stop it, select the button again. You can also control its moving speed by dragging the slider between Slow and Fast on the speed control. For a bubble chart, you can control whether the chart will be moving in bubble or line trail.

**See also**:

* "Creating a Real Time Chart" in the *Logi JReport Designer User's Guide* for real time chart example.
* "Creating a Motion Chart" in the *Logi JReport Designer User's Guide* for motion chart example.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a KPI Component

1. Drag **KPI** from the Components panel or drag ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/4404920393239/btn_kpi.gif) from the visualization toolbar to the destination where you want to insert the KPI component.
2. In the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009672481-Select-Data-Source#KPI) dialog, select a data source and then a business view in the current catalog to bind with the KPI component. Select **OK**.

   ![Select Data Source for KPI Component dialog](https://devnet.logianalytics.com/hc/article_attachments/4404926646295/slctdtsrc-kpi.gif)
3. A blank KPI component is inserted in the report. You can now define the KPI component by adding objects into it.

   ![Blank KPI template](https://devnet.logianalytics.com/hc/article_attachments/4404926646551/wbrpt_edt_insrt_kpi.gif)
4. Drag an aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) or a formula from the Resources panel as the KPI value. The name label of the object is added in the KPI component at the same time. Edit the label text if needed.
5. Insert a KPI chart to demonstrate data about the KPI value.
   1. Right-select in the blank area of the KPI component and then select **Insert KPI Chart** from the shortcut menu. The [Insert Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009647562-Insert-Chart#KPI) dialog appears.
   2. Specify a title for the chart in the Chart Title text field, and if required select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to set the font properties for the title.
   3. The Data Source drop-down list shows the business view bound with the KPI component. It cannot be changed.
   4. Select the type for the KPI chart. Only the following chart types are supported for a KPI chart: Bar, Bench, Line, Area, Pie, and Bullet.
   5. Define the KPI chart [in the same way you would do for a normal chart](#Chart).
   6. Select **OK**. A chart is now inserted into the KPI component.
6. Add more aggregation, formulas, [labels](#Label) or [images](#Image) into the KPI component if required.
7. [Resize](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components#Resize) the KPI component and the objects in it and [adjust the position](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components#Move) of the objects by dragging to improve the layout.

See also "KPI Components" in the *Logi JReport Designer User's Guide* for a KPI example.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Label

1. Drag **Label** from the Components panel to the destination.
2. Double-select the label, when the text box becomes editable input the desired text.
3. Select outside of the label to apply the change.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting an Image

1. Drag **Image** from the Components panel to the destination where you want to insert the image. The [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009647582-Insert-Image) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920393495/insrtimg.gif)
2. Specify the image you want to insert.
   * To use an image in the local file system, select **Local File**, then select **Browse** to find the image.
   * To use an image on a website, select **Web URL**, then input the image URL or paste the URL in the Image URL text field.
   * To use an image in the image library of Web Report Studio, select **Library**, then select the image in the My Images box.
3. Select **OK** to insert the image.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Multimedia Object

1. Drag **Multimedia Object** from the Components panel to the destination where you want to insert the multimedia object. The [Insert Multimedia](https://devnet.logianalytics.com/hc/en-us/articles/1500009647602-Insert-Multimedia) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920394007/insrtmultmda.gif)
2. Choose from the three multimedia object types: Flash, Real Media file, or Windows Media File.
3. In the File Name/URL text field, specify the full path of the multimedia object you want to insert or use the Browse button to find it if it is on your local disk. Or you can provide a URL for loading it from a website.
4. The Plug-in page text field provides a default URL from which to download the player to play the inserted multimedia object on a web page.
5. In the Properties box, specify the properties for the multimedia object as required.
6. Select **OK** to insert the multimedia object.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Web Control

You can insert the following web controls into a web report: parameter control, parameter form control, filter control, and navigation control. For details, see [Using Web Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009675321-Using-Web-Controls).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Inserting a Special Field

To insert a special field into a web report, just drag the special field from the Components panel to the destination in the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675201-General-Operations-in-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components)
