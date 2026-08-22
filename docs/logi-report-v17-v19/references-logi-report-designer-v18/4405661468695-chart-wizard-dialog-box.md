---
title: "Chart Wizard Dialog Box"
id: 4405661468695
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661468695-Chart-Wizard-Dialog-Box
updated_at: 2022-03-28T06:55:04Z
---

# Chart Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664433559-Chart-Iterator-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661466135-Choose-Data-Dialog-Box)

# Chart Wizard Dialog Box

You can use the Chart Wizard dialog box to [create a page report tab with a chart in it](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#Page), [create a library component with a chart in it,](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#LC) or [edit an existing chart](https://devnet.logianalytics.com/hc/en-us/articles/4405664389143-Modifying-Charts#Edit) in a report. This topic describes the options in the dialog box.

Designer displays different options in the Chart Wizard dialog box according to the type of the data resource used for the chart: [business view](#BV) or [query resource](#Query).

## Chart Wizard Dialog Box - Business View Based

When you use the Chart Wizard dialog box for creating or editing a chart using a business view, you see the following screens in the dialog box (Designer displays the Filter screen only when you use the dialog box for creating a chart):

* [Data Screen](#BVData)
* [Type Screen](#BVType)
* [Display Screen](#BVDisplay)
* [Filter Screen](#BVFilter)
* [Layout Screen](#BVLayout)
* [Style Screen](#BVStyle)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the chart. You can select from all the predefined business views in the current catalog and Designer automatically creates a dataset based on the business view you select.

![Chart Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4420542176023/chtwzd_dt_bv.gif)

**Inherit from the Parent**

Designer displays and enables this option only when you use the dialog box for editing a chart that is inside any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel. Select it if you want the chart to inherit the business view that its parent banded object uses.

### Type Screen

Use this screen to specify the [chart type](https://devnet.logianalytics.com/hc/en-us/articles/4405664391703-Chart-Types). When using business view as the data resource, you can only create a 2-D chart.

![Chart Wizard - Type](https://devnet.logianalytics.com/hc/article_attachments/4420556218007/chtwzd_type_bv.gif)

**Single chart**

Select to create a single chart.

* **Chart Type**  
  This box lists all the chart types that you can use to create a single chart. Select the type you want.
* **Subtype**  
  This box lists all the subtypes of the selected chart type. Select the subtype for the chart. You can point to a subtype icon to get its name.

**Combo chart**

Select to create more than one type using the primary or secondary axis. The types should be featured as a combination chart.

* **Chart Type**  
  This box lists all the chart types that you can use in a combo chart. Select the type you want.
* **Subtype**  
  This box lists all the subtypes of the selected chart type. Select the subtype for the combo chart. You can point to a subtype icon to get its name.
* **Chart Type Groups**  
  This box lists the chart types that you select to use in the combo chart.
  + **Primary Axis**
    - **<Add Combo Type>**  
      Select to add a chart type to the primary axis.
  + **Secondary Axis**
    - **<Add Combo Type>**  
      Select to add a chart type to the secondary axis.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**  
  Select to delete the specified chart type from the Chart Type Groups box.

### Display Screen

Use this screen to specify the data to display in the chart. Designer displays different options in the screen according to the type of the chart: [common chart types](#BVCommon), [organization chart](#BVOrg), or [heat map](#BVHeatMap).

#### For Common Chart Types

![Chart Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4420556218263/chtwzd_dsply_bv.gif)

**Title**

Specify the title of the chart.

**Resources**

This box lists the resources in and related to the specified business view, which you can use for the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the chart.

**Category**/**Series**

This box lists the field that you add to display on the category/series axis of the chart. For a gauge chart, you can select Advanced to show or hide the Category and Series boxes.

For a real time chart, if you do not specify the category field, Designer displays the text "Use System Refresh Time" in the Category box by default, meaning, Designer uses the time at which the chart refreshes itself as the category value. Designer disables the Series box in this case.

* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664591383-User-Defined-Group-Dialog-Box) to define how to group information.
* **Order/Select N**   
  Select to open the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661493527-Category-Options-Dialog-Box) or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661699223-Series-Options-Dialog-Box) to specify the sort order of the category or series values and define the number of the category or series values to show in the chart.

**Show Values**

This box lists the values that you add to show in the chart.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420556150039/btn_edit.gif)**Edit button**  
  Select to open the [Edit Additional Value dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664454935-Edit-Additional-Value-Dialog-Box) to edit an additional value. Designer enables this button only when you select a constant value or an average value in the Show Values box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif)**Move Up button**  
  Select to move the specified value higher in the display order.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified value lower in the display order.
* **Bubble chart options**  
  Designer displays the following options for a bubble chart.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif)**Add button**  
    Select to add a new pair of Y-Axis and Size for the bubble chart.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**  
    Select to delete the specified value or axis from the bubble chart.
  + **X-Axis**  
    This node lists the value that you add to show on the X axis of the bubble chart. By default, Designer applies the field that you add to the category axis of the chart as the value. You can add another value to display instead.
  + **Y-Axis**  
    This node lists the value that you add to show on the Y axis of the bubble chart.
  + **Size**  
    This node lists the value that you add to show as the bubble size.

**Motion Bar for Playable Chart**

Designer enables this option only for single bar, bench, or bubble chart in a web report or library component. Select it and then add a field as the motion field to make the chart a motion chart. A motion field can only be of the Integer, Date, or Time data type.

* **Special Function**  
  Designer enables this button when the motion field is of the Date data type. Select it to open the [Special Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661724823-Special-Function-Dialog-Box) to define special function to the motion field.

**Real Time**

Designer enables this option only for single bar, bench, line, or area chart in a web report or library component. Select it to run the chart in real time mode.

* **Use System Time for Category**  
  Select to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
  Specify the time interval at which the chart gets data and refreshes itself automatically.
* **Show Most Recent N Points**  
  Specify the number of points to keep for the real time data in the chart.
* **Incremental Fetch**  
  Select to open the [Unique Key dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661742743-Unique-Key-Dialog-Box) to configure a unique key for the real time chart.

#### For Organization Chart

![Chart Wizard - Org Display](https://devnet.logianalytics.com/hc/article_attachments/4420550949783/chtwzd_dsply_org_bv.gif)

**Node**

Specify the field the values of which to display as the nodes in the org chart.

**Parent**

Specify the field which shows the "reporting to" relationship among the node field values.

**Resources**

This box lists the resources in and related to the specified business view, which you can add to display in each node in the org chart. You can also add images and labels to the nodes.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to display in the org chart.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the org chart.

**Properties**

This box presents a node model for specifying the information that you want to display in each node in the org chart.

#### For Heat Map

![Chart Wizard - Heat Map Display](https://devnet.logianalytics.com/hc/article_attachments/4420556218519/chtwzd_dsply_htmp_bv.gif)

**Resources**

This box lists the resources in and related to the specified business view, which you can use for the heat map.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to display in the heat map.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the heat map.

**Area**

This box lists the groups that you add for the heat map. There should be at least one group.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif)**Move Up button**  
  Select to move the specified group to a higher group level.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified group to a lower group level.
* **Color By**  
  Select to use the group to determine the fill color of the rectangles.
* **Label By**  
  Select to show the values of the group in the innermost rectangles.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664591383-User-Defined-Group-Dialog-Box) to define how to group information.
* **Order/Select N**  
  Select to open the [Group Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661615767-Group-Options-Dialog-Box) to specify the sort order of the group values and define the number of the group values to display in the heat map.

**Property**

This box lists the aggregations that you add to calculate data in the heat map based on the lowest group.

* **Size By**  
  Select to use the aggregation to determine the size of the rectangles.
* **Color By**  
  Select to use the aggregation to determine the fill color of the rectangles.
* **Label By**  
  Select to show the values of the aggregation in the innermost rectangles.

### Filter Screen

Designer displays the Filter screen only when you use the dialog box for creating a chart. You can use this screen to narrow down the data to display in the chart.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661510295-Edit-Filter-Dialog-Box).

![Chart Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420556218903/chtwzd_fltr_bv.gif)

### Layout Screen

Use this screen to specify the layout of the chart elements. Designer does not display some options for certain chart types. For more information about the options, [select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664387479-Inserting-Charts-in-a-Report#Layout).

![Chart Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4420556219159/chtwzd_layout.gif)

### Style Screen

Use this screen to specify the style of the chart.

![Chart Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4420542176407/chtwzd_sty.gif)

**Style**

This box lists the styles that you can apply to the chart. Select the style for the chart.

* **<Custom>**  
  This style contains no information. Designer uses it to support reports that was built with previous versions which did not bind any style, or when Designer cannot find the bound style in the style list.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the chart.

**Inherit Style**

Designer displays this option only when you use the dialog box for editing a chart and the chart is inside a banded object. Select it if you want the chart to inherit the style of its parent.

**Page Setup**

Designer displays this button only when you use the dialog box for creating a chart in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664543511-Page-Setup-Dialog-Box) to specify page properties for the report tab.

## Chart Wizard Dialog Box - Query Based

When you use the Chart Wizard dialog box for creating or editing a chart using a query resource, you see the following screens in the dialog box (Designer displays the Filter screen only when you use the dialog box for creating a chart):

* [Data Screen](#Data)
* [Type Screen](#Type)
* [Display Screen](#Display)
* [Filter Screen](#Filter)
* [Layout Screen](#Layout)
* [Style Screen](#Style)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the chart.

![Chart Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4420542176663/chtwzd_dt.gif)

**Data resource box**

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the chart.

**More Options**/**Less Options**

Select to show or hide the options for specifying a dataset for the chart.

* **New Dataset**  
  Select to create a dataset based on a data resource in the current catalog. If you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661685015-Query-Editor-Dialog-Box). You can also select the first item under a resource node to add or create a data resource of the type in the catalog and use it to create the dataset.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select **Edit** to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box), or select **<New Dataset...>** to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661656087-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option only when you use the dialog box for editing a chart and the parent object containing the chart already applies a dataset. Select it if you want the chart to inherit the dataset from its parent.

### Type Screen

Use this screen to specify the [chart type](https://devnet.logianalytics.com/hc/en-us/articles/4405664391703-Chart-Types).

![Chart Wizard - Type](https://devnet.logianalytics.com/hc/article_attachments/4420550950551/chtwzd_type.gif)

**Single chart**

Select to create a single chart.

* **Chart Type**  
  This box lists all the chart types that you can use to create a single chart. Select the type you want.
* **Subtype**  
  This box lists all the subtypes of the selected chart type. Select the subtype for the chart. You can point to a subtype icon to get its name.

**Combo chart**

Select to create more than one type using the primary or secondary axis. The types should be featured as a combination chart.

* **Chart Type**  
  This box lists all the chart types that you can use in a combo chart. Select the type you want.
* **Subtype**  
  This box lists all the subtypes of the selected chart type. Select the subtype for the combo chart. You can point to a subtype icon to get its name.
* **Chart Type Groups**  
  This box lists the chart types that you select to use in the combo chart.
  + **Primary Axis**
    - **<Add Combo Type>**  
      Select to add a chart type to the primary axis.
  + **Secondary Axis**
    - **<Add Combo Type>**  
      Select to add a chart type to the secondary axis.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**  
  Select to delete the specified chart type from the Chart Type Groups box.

### Display Screen

Use this screen to specify the data to display in the chart. Designer displays different options in the screen according to the type of the chart: [common chart types](#Common), [organization chart](#Org), or [heat map](#HeatMap).

#### For Common Chart Types

![Chart Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4420542177431/chtwzd_dsply.gif)

**Resources**

This box lists the data fields in and related to the specified query resource, which you can use for the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the chart.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4420542098711/btn_replace.gif)**Replace button**

Select to replace the specified field in the chart with the selected field in the Resources box. Designer displays this button only when you use the dialog box for modifying a chart.

**Category**/**Series**

This box lists the field that you add to display on the category/series axis of the chart. For a gauge chart, you can select Advanced to show or hide the Category and Series boxes.

For a real time chart, if you do not specify the category field, Designer displays the text "Use System Refresh Time" in the Category box, meaning, Designer uses the time at which the chart refreshes itself as the category value. Designer disables the Series box in this case.

* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664591383-User-Defined-Group-Dialog-Box) to define how to group information.
* **Special Function**  
  Select to open the [Special Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661724823-Special-Function-Dialog-Box) to define special function to the field.
* **Order/Select N**   
  Select to open the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661493527-Category-Options-Dialog-Box) or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661699223-Series-Options-Dialog-Box) to specify the sort order of the category or series values and define the number of the category or series values to show in the chart.

**Show Values**

This box lists the values that you add to show in the chart. For a back-to-back bench chart, you can only add one value.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420556150039/btn_edit.gif)**Edit button**  
  Select to open the [Edit Additional Value dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664454935-Edit-Additional-Value-Dialog-Box) to edit an additional value. Designer enables this button only when you select a constant value or an average value in the Show Values box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif)**Move Up button**  
  Select to move the specified value higher in the display order.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified value lower in the display order.
* **Bubble chart options**  
  Designer displays the following options for a bubble chart.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif)**Add button**  
    Select to add a new pair of Y Axis and Radius for the bubble chart.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**  
    Select to delete the specified value or axis from the bubble chart.
  + **X Axis**  
    This node lists the value that you add to show on the X axis of the bubble chart. By default, Designer applies the field that you add to the category axis of the chart as the value. You can add another value to display instead.
  + **Y Axis**  
    This node lists the value that you add to show on the Y axis of the bubble chart.
  + **Radius**  
    This node lists the value that you add to show as the bubble size.
* **Back-to-back chart options**  
  Designer displays the following options for a back-to-back chart.
  + **Show Values**  
    Designer enables this option only for a 2-D back-to-back chart. Select it if you want to specify the values on the origin left and right of the value axis in the chart respectively.
    - **Left**  
      This box lists the value that you specify to show on the origin left of the value axis. You can only add one value.
    - **Right**  
      This box lists the value that you specify to show on the origin right of the value axis. You can only add one value.
  + **Series Values**  
    Designer enables this option after you add a series field to the chart. Select it if you want to specify the series values on the origin left/right of the value axis in the chart manually.
    - **Left**/**Right**  
      This box lists the series values that you add on the origin left/right of the value axis. You can edit either the Left box or the Right box.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif)**Move Up button**  
      Select to move the specified value higher in the value list.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif)**Move Down button**  
      Select to move the specified value lower in the value list.
    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif)**Add button**  
      Select to add a new value line. Double-click in the line to specify the value.
    - ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**  
      Select to delete the specified value line.
  + **Series Conditions**  
    Designer enables this option after you add a series field to the chart. Select it if you want to specify the series values on the origin left/right of the value axis in the chart using condition.
    - **Left**/**Right**  
      This box lists the condition expression which you add to define the series values on the origin left/right of the value axis. You can edit either the Left box or Right box.
    - ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420556150039/btn_edit.gif)**Edit button**  
      Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664456727-Edit-Conditions-Dialog-Box) to edit the condition which defines the series values on the origin left/right of the value axis.
    - ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**  
      Select to delete the added condition.

#### For Organization Chart

![Chart Wizard - Org Display](https://devnet.logianalytics.com/hc/article_attachments/4420550951319/chtwzd_dsply_org.gif)

**Node**

Specify the field the values of which to display as the nodes in the org chart.

**Parent**

Specify the field which shows the "reporting to" relationship among the node field values.

**Resources**

This box lists the resources in and related to the specified query resource, which you can add to display in each node in the org chart. You can also add images and labels to the nodes.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to display in the org chart.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the org chart.

**Properties**

This box presents a node model for specifying the information you want to display in each node in the org chart.

#### For Heat Map

![Chart Wizard - Heat Map Display](https://devnet.logianalytics.com/hc/article_attachments/4420542177687/chtwzd_dsply_htmp.gif)

**Resources**

This box lists the resources in and related to the specified query resource, which you can use for the heat map.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to display in the heat map.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the heat map.

**Area**

This box lists the groups that you add for the heat map. There should be at least one group.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif)**Move Up button**  
  Select to move the specified group to a higher group level.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified group to a lower group level.
* **Color By**  
  Select to use the group to determine the fill color of the rectangles.
* **Label By**  
  Select to show the values of the group in the innermost rectangles.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664591383-User-Defined-Group-Dialog-Box) to define how to group information.
* **Special Function**  
  Select to open the [Special Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661724823-Special-Function-Dialog-Box) to define special function to a group.
* **Order/Select N**   
  Select to open the [Group Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661615767-Group-Options-Dialog-Box) to specify the sort order of the group values and define the number of the group values to display in the heat map.

**Property**

This box lists the summaries that you add to calculate data in the heat map based on the lowest group.

* **Size By**  
  Select to use the summary to determine the size of the rectangles.
* **Color By**  
  Select to use the summary to determine the fill color of the rectangles.
* **Label By**  
  Select to show the values of the summary in the innermost rectangles.

### Filter Screen

Designer displays the Filter screen only when you use the dialog box for creating a chart. You can use this screen to narrow down the data to display in the chart.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661510295-Edit-Filter-Dialog-Box).

![Chart Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420550951831/chtwzd_fltr.gif)

### Layout Screen

Use this screen to specify the layout of the chart elements. Designer does not display some options for certain chart types. For more information about the options, [select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664387479-Inserting-Charts-in-a-Report#Layout).

![Chart Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4420556219159/chtwzd_layout.gif)

### Style Screen

Use this screen to specify the style of the chart.

![Chart Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4420542176407/chtwzd_sty.gif)

**Style**

This box lists the styles that you can apply to the chart. Select the style for the chart.

* **<Custom>**  
  This style contains no information. Designer uses it to support reports that was built with previous versions which did not bind any style, or when Designer cannot find the bound style in the style list.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the chart.

**Inherit Style**

Designer displays this option only when you use the dialog box for editing a chart and the chart is inside a banded object. Select it if you want the chart to inherit the style of its parent.

**Page Setup**

Designer displays this button only when you use the dialog box for creating a chart in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664543511-Page-Setup-Dialog-Box) to specify page properties for the report tab.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664433559-Chart-Iterator-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661466135-Choose-Data-Dialog-Box)
