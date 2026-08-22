---
title: "Convert to Chart"
id: 1500009671581
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009671581-Convert-to-Chart
updated_at: 2021-07-24T20:54:36Z
---

# Convert to Chart

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009671561-Conditional-Formatting)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009671601-Convert-to-Crosstab)

# Convert to Chart

The Convert to Chart dialog appears when you focus on a table, crosstab, or chart and then select a chart type on the visualization toolbar but the data fields in the current component are not enough for the target chart type. It helps you to convert a data component to the chart type, and varies with different chart types:
[common chart types](#Common), [organization chart](#Org) and [heat map](#Map).

**OK**

Converts to the specified chart type and closes the dialog.

**Cancel**

Cancels the conversion and closes the dialog.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920501783/btn_help.gif)

Displays the help document about this feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926700311/btn_close.gif)

Ignores the setting and closes this dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## For Common Chart Types

[See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926640919/cnvtcht.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif)

Specifies the font properties of the chart title.

* **Font**  
   Lists all the available font faces that can be selected to apply to the title.
* **Font Style**   
   Specifies the font style of the title. It can be one of the following: plain, bold, italic, and bold italic.
* **Size**  
   Specifies the font size of the title.
* **Align**  
   Specifies the position of the title to be left, right, center or justify.
* **Font Color**  
   Specifies the font color of the title.
* **Background Color**  
   Specifies the background color of the title.
* **OK**  
   Applies the changes.
* **Cancel**  
   Cancels the changes.

**Data Source**

Specifies the business view in the current catalog on which the chart will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009672441-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Resources**

Displays the resources that can be added to the chart.

**Show All Fields/Show Used Fields**

Specifies to show all the business view elements or only the ones used in the current data component in the Resources box. Not available when you select another business view to convert to chart with.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

* **Predefined Order**  
   Sorts the view elements in the order defined in the Business View Editor on Logi JReport Designer.
* **Resource Types**  
   Sorts the view elements by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
   Sorts the view elements in alphabetical order. Elements that are not in any category will be sorted first, then the categories, and the elements in each category will also be sorted alphabetically.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)

Launches the quick search toolbar to search for view elements. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)

Adds the selected resource to be displayed in the chart.

**Value box**

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects.

* **Primary Axis**  
   Adds a chart type to the primary axis.
* **Secondary Axis**  
   Adds a chart type to the secondary axis. Active only when the option Secondary Axis is checked.
* **X-Axis**  
   Lists the value you want to show on the X axis of the bubble chart.
* **Y-Axis**  
   Lists the value you want to show on the Y axis of the bubble chart.
* **Size**   
   Lists the value you want to show as the bubble size.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920392343/btn_wbrpt_adcmbtyp.gif)

Adds a combo chart to the Primary Axis or Secondary Axis.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif)

Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009647202-Edit-Additional-Value) dialog to edit the selected additional value.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)

Moves the selected view element one level up.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)

Moves the selected view element one level down.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif)

Adds a new pair of Y Axis and Radius for the bubble chart.

**Secondary Axis**

Specifies whether to show the secondary axis in the chart.

**Category box**

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) that will be displayed on the category axis of the chart.

For a real time chart, if no object is specified on the category axis, Use System Refresh Time will be automatically displayed in the Category text box, namely, the time at which the chart refreshes itself will be used as the category value.

**Series box**

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) that will be displayed on the series axis of the chart. Not available to real time chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920392855/btn_wbrpt_topn.gif)

Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009647162-Category-Options) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009647762-Series-Options) dialog to define the sort order of the category or series values and specify the number of the category or series values that will be displayed in the chart.

**Motion Bar for Playable Chart**

Lists the group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif)you want to use as the motion field. A motion field can only be of Integer, Date or Time data type. Available to single bar, bench and bubble chart types only.

* **Special Function**  
   Available only when the motion field is of Date data type. Select it to define the special function.
  + **Field**  
     Displays on which field the special function will be applied.
  + **Function**  
     Specifies the special function to the field.
  + **OK**  
     Accepts the special function settings and leaves the dialog.
  + **Cancel**  
     Cancels the special function settings and leaves the dialog.

**Real Time**

Specifies to run the chart in real time mode, which means it will be updated automatically by using real time data. Available to single bar, bench, line, and area chart types only.

* **Use System Time for Category**  
   Specifies to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
   Specifies the time interval at which the chart will get data and refresh itself automatically.
* **Show Most Recent N Points**  
   Specifies the number of records that will be kept for the real time data on the chart.
* **Incremental Fetch**  
   Opens the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009672641-Unique-Key) dialog to configure a unique key for the real time chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)

Removes the selected resource.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## For Organization Chart

[See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920553751/cnvtcht_org.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the chart title.

**Data Source**

Specifies the business view in the current catalog on which the chart will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009672441-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Resources**

Displays the resources that can be added to the chart.

**Show All Fields/Show Used Fields**

Specifies to show all the business view elements or only the ones used in the current data component in the Resources box. Not available when you select another business view to convert to chart with.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)

Sorts the view elements in the specified [order](#Sort) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)

Launches the quick search toolbar to search for view elements. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).

**Value box**

* **Primary Axis**  
   Select Org from the chart type drop-down menu.
* **Node**  
   Adds a field from the Resources box which identifies the entity by selecting both the field and Node and then selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif).
* **Parent**  
   Adds a field from the Resources box which shows the "reporting to" relationship among the entity members, that is, which child node field member reports to or belongs to which child node field member, by selecting both the field and Parent and then selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif).
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected child node or parent field.

**Properties**

The properties box presents a node model of the org chart. Data fields, labels and images can be inserted into the node as the information about the entity in the org chart, by using ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif). By default all added objects are placed at the left top of the node, you need to adjust their positions and sizes in the node. You can also resize the node if required.

To remove an object from the node, select it and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## For Heat Map

[See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926731159/cnvtcht_htmp.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif)

Specifies the [font properties](#Title) of the chart title.

**Data Source**

Displays the business view that has been used in the chart.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009672441-Query-Filter) dialog to specify the filter you want to apply to the selected business view.

**Resources**

Displays the resources that can be added to the chart.

**Show All Fields/Show Used Fields**

Specifies to show all the business view elements or only the ones used in the current data component in the Resources box. Not available when you select another business view to convert to chart with.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)

Sorts the view elements in the specified [order](#Sort) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)

Launches the quick search toolbar to search for view elements. For the usage of the toolbar select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource#Search).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)

Adds the selected field into the Area or Property box.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920418583/btn_rmvitem.gif)

Removes the selected field from the Area or Property box.

**Chart type drop-down list**

Displays Heat Map as the selected chart type.

**Area**

Lists the fields used to group the data to different areas. There should be at least one group. When there are multiple groups, their levels are defined by their positions from top down. The group at the top is of the highest level and the bottom the lowest.

* **Color by**  
   Specifies whether to color by a group. 0-n groups can be used as the color-by fields.
* **Label by**  
   Specifies whether to show the group name in the innermost rectangle.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)  
   Moves the selected group field one level up.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)  
   Moves the selected group field one level down.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920392855/btn_wbrpt_topn.gif)  
   Opens the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009672121-Group-Options) dialog to define the sort order of the group values and specify the number of the group values that will be displayed in the chart.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)  
   Removes the selected group field.

**Property**

Lists the summary fields used as size-by/color-by or displayed in the innermost rectangle.

* **Size by**  
   Specifies to size by one summary or none.
* **Color by**  
   Specifies to color by one summary or none.
* **Label by**  
   Specifies whether to show a summary in the innermost rectangle.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009671561-Conditional-Formatting)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009671601-Convert-to-Crosstab)
