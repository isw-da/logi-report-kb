---
title: "Chart Wizard Dialog Box"
id: 1500010058202
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058202-Chart-Wizard-Dialog-Box
updated_at: 2022-03-28T09:20:48Z
---

# Chart Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058182-Chart-Iterator-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095701-Choose-Data-Dialog-Box)

# Chart Wizard Dialog Box

You can use the Chart Wizard dialog box to [create a page report tab with a chart in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page), [create a library component with a chart in it,](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#LC) or [edit an existing chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010094661-Modifying-Charts#Edit) in a report. This topic describes the options in the dialog box.

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

Select to finish creating or editing the chart and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the business view for the chart. You can select from all the predefined business views in the current catalog.

![Chart Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404857005079/chtwzd_dt_bv.gif)

**Inherit from the Parent**

Designer displays and enables the option only when you use the dialog box for editing a chart that is inside any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel. Select it if you want the chart to inherit the business view that its parent banded object uses.

### Type Screen

Use this screen to specify the type of the chart. You can refer to [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500010094681-Chart-Types) which describes each of the chart type in detail. When using business view as the data resource, you can only create a 2-D chart.

![Chart Wizard - Type](https://devnet.logianalytics.com/hc/article_attachments/4404857005335/chtwzd_type_bv.gif)

**Single chart**

Select to create a single chart.

* **Chart Type**  
  The box lists all the chart types that you can use to create a single chart. Select the type you want.
* **Subtype**  
  The box lists all the subtypes of the selected chart type. Select the subtype for the chart. You can hover the mouse pointer on a subtype icon to get its name.

**Combo chart**

Select to create more than one type using the primary or secondary axis. The types should be featured as a combination chart.

* **Chart Type**  
  The box lists all the chart types that you can use in a combo chart. Select the type you want.
* **Subtype**  
  The box lists all the subtypes of the selected chart type. Select the subtype for the combo chart. You can hover the mouse pointer on a subtype icon to get its name.
* **Chart Type Groups**  
  The box lists the chart types that you select to use in the combo chart.
  + **Primary Axis**
    - **<Add Combo Type>**  
      Select to add a chart type to the primary axis.
  + **Secondary Axis**
    - **<Add Combo Type>**  
      Select to add a chart type to the secondary axis.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Removve button**  
  Select to delete the specified chart type from the Chart Type Groups box.

### Display Screen

Use this screen to specify the data to display in the chart. Designer displays different options in the screen according to the type of the chart: [common chart types](#BVCommon), [organization chart](#BVOrg), or [heat map](#BVHeatMap).

#### For Common Chart Types

![Chart Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848625815/chtwzd_dsply_bv.gif)

**Title**

Specify the title of the chart.

**Resources**

The box lists the resources in and related to the specified business view, which you can use for the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the chart.

**Category**/**Series**

The box lists the field that you add to display on the category/series axis of the chart. For a gauge chart, you can select the Advanced button to show or hide the Category/Series box.

For a real time chart, if you do not specify the category field, Designer displays the text "Use System Refresh Time" in the Category box by default, meaning Designer uses the time at which the chart refreshes itself as the category value. Designer disables the Series box in this case.

* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) to define how to group information.
* **Order/Select N**   
  Select to open the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058442-Category-Options-Dialog-Box) or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098601-Series-Options-Dialog-Box) to specify the sort order of the category or series values and define the number of the category or series values to show in the chart.

**Show Values**

The box lists the values that you add to show in the chart.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
  Select to open the [Edit Additional Value dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058682-Edit-Additional-Value-Dialog-Box) to edit an additional value. Designer enables the button only when you select a constant value or an average value in the Show Values box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
  Select to move the specified value higher in the display order.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified value lower in the display order.
* **Bubble chart options**  
  Designer displays the following options for a bubble chart.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
    Select to add a new pair of Y-Axis and Size for the bubble chart.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
    Select to delete the specified value or axis from the bubble chart.
  + **X-Axis**  
    The node lists the value that you add to show on the X axis of the bubble chart. By default, Designer applies the field that you add to the category axis of the chart as the value. You can add another value to display instead.
  + **Y-Axis**  
    The node lists the value that you add to show on the Y axis of the bubble chart.
  + **Size**  
    The node lists the value that you add to show as the bubble size.

**Motion Bar for Playable Chart**

Designer enables this option only for single bar, bench, or bubble chart in a web report or library component. Select it and then add a field as the motion field to make the chart a motion chart. A motion field can only be of the Integer, Date, or Time data type.

* **Special Function**  
  Designer enables the button when the motion field is of the Date data type. Select it to open the [Special Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060562-Special-Function-Dialog-Box) to define special function to the motion field.

**Real Time**

Designer enables this option only for single bar, bench, line, or area chart in a web report or library component. Select it to run the chart in real time mode.

* **Use System Time for Category**  
  Select to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
  Specify the time interval at which the chart gets data and refreshes itself automatically.
* **Show Most Recent N Points**  
  Specify the number of points to keep for the real time data in the chart.
* **Incremental Fetch**  
  Select to open the [Unique Key dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099121-Unique-Key-Dialog-Box) to configure a unique key for the real time chart.

#### For Organization Chart

![Chart Wizard - Org Display](https://devnet.logianalytics.com/hc/article_attachments/4404857005719/chtwzd_dsply_org_bv.gif)

**Node**

Specify the field the values of which to display as the nodes in the org chart.

**Parent**

Specify the field which shows the "reporting to" relationship among the node field values.

**Resources**

The box lists the resources in and related to the specified business view, which you can add to display in each node in the org chart. You can also add images and labels to the nodes.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to display in the org chart.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the org chart.

**Properties**

The box presents a node model for specifying the information that you want to display in each node in the org chart.

#### For Heat Map

![Chart Wizard - Heat Map Display](https://devnet.logianalytics.com/hc/article_attachments/4404857005975/chtwzd_dsply_htmp_bv.gif)

**Resources**

The box lists the resources in and related to the specified business view, which you can use for the heat map.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to display in the heat map.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the heat map.

**Area**

The box lists the groups that you add for the heat map. There should be at least one group.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
  Select to move the specified group to a higher group level.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified group to a lower group level.
* **Color By**  
  Select to use the group to determine the fill color of the rectangles.
* **Label By**  
  Select to show the values of the group in the innermost rectangles.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) to define how to group information.
* **Order/Select N**  
  Select to open the [Group Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097481-Group-Options-Dialog-Box) to specify the sort order of the group values and define the number of the group values to display in the heat map.

**Property**

The box lists the aggregations that you add to calculate data in the heat map based on the lowest group.

* **Size By**  
  Select to use the aggregation to determine the size of the rectangles.
* **Color By**  
  Select to use the aggregation to determine the fill color of the rectangles.
* **Label By**  
  Select to show the values of the aggregation in the innermost rectangles.

### Filter Screen

Designer displays the Filter screen only when you use the dialog box for creating a chart. You can use this screen to narrow down the data to display in the chart.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Chart Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848626071/chtwzd_fltr_bv.gif)

### Layout Screen

Use this screen to specify the layout of the chart elements. Designer does not display some options for certain chart types. For more information about the options, [select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report#Layout).

![Chart Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404848626839/chtwzd_layout.gif)

### Style Screen

Use this screen to specify the style of the chart.

![Chart Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404857006487/chtwzd_styl_bv.gif)

**Style**

The box lists the styles that you can apply to the chart. Select the style for the chart.

* **<Custom>**  
  This style contains no information. It is only used to support reports that was built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the chart.

**Inherit Style**

Designer displays the option only when the chart is inside a banded object, or to be inserted into a banded object. Select it if you want the chart to inherit the style of its parent.

**Page Setup**

Designer displays the button only when you use the dialog box for creating a chart in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) to specify page properties for the report tab.

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

Select to finish creating or modifying the chart and closes the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the chart.

![Chart Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404848627479/chtwzd_dt.gif)

**Data resource box**

The box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the chart.

**More Options**/**Less Options**

Select to show or hide the options for specifying a dataset for the chart.

* **New Dataset**  
  Select to create a dataset based on the current catalog data resources. When you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box).
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select the Edit button to edit the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select <New Dataset...> to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option only when you use the dialog box for editing a chart and the parent object containing the chart already applies a dataset. Select it if you want the chart to inherit the dataset from its parent.

### Type Screen

Use this screen to specify the type of the chart. You can refer to [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500010094681-Chart-Types) which describes each of the chart type in detail.

![Chart Wizard - Type](https://devnet.logianalytics.com/hc/article_attachments/4404848627735/chtwzd_type.gif)

**Single chart**

Select to create a single chart.

* **Chart Type**  
  The box lists all the chart types that you can use to create a single chart. Select the type you want.
* **Subtype**  
  The box lists all the subtypes of the selected chart type. Select the subtype for the chart. You can hover the mouse pointer on a subtype icon to get its name.

**Combo chart**

Select to create more than one type using the primary or secondary axis. The types should be featured as a combination chart.

* **Chart Type**  
  The box lists all the chart types that you can use in a combo chart. Select the type you want.
* **Subtype**  
  The box lists all the subtypes of the selected chart type. Select the subtype for the combo chart. You can hover the mouse pointer on a subtype icon to get its name.
* **Chart Type Groups**  
  The box lists the chart types that you select to use in the combo chart.
  + **Primary Axis**
    - **<Add Combo Type>**  
      Select to add a chart type to the primary axis.
  + **Secondary Axis**
    - **<Add Combo Type>**  
      Select to add a chart type to the secondary axis.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Removve button**  
  Select to delete the specified chart type from the Chart Type Groups box.

### Display Screen

Use this screen to specify the data to display in the chart. Designer displays different options in the screen according to the type of the chart: [common chart types](#Common), [organization chart](#Org), or [heat map](#HeatMap).

#### For Common Chart Types

![Chart Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404857006871/chtwzd_dsply.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use for the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the chart.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)**Replace button**

Select to replace the specified field in the chart with the selected field in the Resources box. Designer displays the button only when you use the dialog box for modifying a chart.

**Category**/**Series**

The box lists the field that you add to display on the category/series axis of the chart. For a gauge chart, you can select the Advanced button to show or hide the Category/Series box.

For a real time chart, if you do not specify the category field, Designer displays the text "Use System Refresh Time" in the Category box, meaning Designer uses the time at which the chart refreshes itself as the category value. Designer disables the Series box in this case.

* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) to define how to group information.
* **Special Function**  
  Select to open the [Special Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060562-Special-Function-Dialog-Box) to define special function to the field.
* **Order/Select N**   
  Select to open the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058442-Category-Options-Dialog-Box) or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098601-Series-Options-Dialog-Box) to specify the sort order of the category or series values and define the number of the category or series values to show in the chart.

**Show Values**

The box lists the values that you add to show in the chart. For a back-to-back bench chart, you can only add one value.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
  Select to open the [Edit Additional Value dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058682-Edit-Additional-Value-Dialog-Box) to edit an additional value. Designer enables the button only when you select a constant value or an average value in the Show Values box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
  Select to move the specified value higher in the display order.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified value lower in the display order.
* **Bubble chart options**  
  Designer displays the following options for a bubble chart.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
    Select to add a new pair of Y Axis and Radius for the bubble chart.
  + ![Trash Can nutton](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
    Select to delete the specified value or axis from the bubble chart.
  + **X Axis**  
    The node lists the value that you add to show on the X axis of the bubble chart. By default, Designer applies the field that you add to the category axis of the chart as the value. You can add another value to display instead.
  + **Y Axis**  
    The node lists the value that you add to show on the Y axis of the bubble chart.
  + **Radius**  
    The node lists the value that you add to show as the bubble size.
* **Back-to-back chart options**  
  Designer displays the following options for a back-to-back chart.
  + **Show Values**  
    Designer enables this option only for a 2-D back-to-back chart. Select it if you want to specify the values on the origin left and right of the value axis in the chart respectively.
    - **Left**  
      The box lists the value that you specify to show on the origin left of the value axis. You can only add one value.
    - **Right**  
      The box lists the value that you specify to show on the origin right of the value axis. You can only add one value.
  + **Series Values**  
    Designer enables this option after you add a series field to the chart. Select it if you want to specify the series values on the origin left/right of the value axis in the chart manually.
    - **Left**/**Right**  
      The box lists the series values that you add on the origin left/right of the value axis. You can edit either the Left box or the Right box.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
      Select to move the specified value higher in the value list.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
      Select to move the specified value lower in the value list.
    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
      Select to add a new value line. Double-click in the line to specify the value.
    - ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
      Select to delete the specified value line.
  + **Series Conditions**  
    Designer enables this option after you add a series field to the chart. Select it if you want to specify the series values on the origin left/right of the value axis in the chart using condition.
    - **Left**/**Right**  
      The box lists the condition expression which you add to define the series values on the origin left/right of the value axis. You can edit either the Left box or Right box.
    - ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
      Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box) to edit the condition which defines the series values on the origin left/right of the value axis.
    - ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
      Select to delete the added condition.

#### For Organization Chart

![Chart Wizard - Org Display](https://devnet.logianalytics.com/hc/article_attachments/4404857007127/chtwzd_dsply_org.gif)

**Node**

Specify the field the values of which to display as the nodes in the org chart.

**Parent**

Specify the field which shows the "reporting to" relationship among the node field values.

**Resources**

The box lists the resources in and related to the specified query resource, which you can add to display in each node in the org chart. You can also add images and labels to the nodes.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to display in the org chart.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the org chart.

**Properties**

The box presents a node model for specifying the information you want to display in each node in the org chart.

#### For Heat Map

![Chart Wizard - Heat Map Display](https://devnet.logianalytics.com/hc/article_attachments/4404848628375/chtwzd_dsply_htmp.gif)

**Resources**

The box lists the resources in and related to the specified query resource, which you can use for the heat map.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to display in the heat map.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the heat map.

**Area**

The box lists the groups that you add for the heat map. There should be at least one group.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
  Select to move the specified group to a higher group level.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified group to a lower group level.
* **Color By**  
  Select to use the group to determine the fill color of the rectangles.
* **Label By**  
  Select to show the values of the group in the innermost rectangles.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) to define how to group information.
* **Special Function**  
  Select to open the [Special Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060562-Special-Function-Dialog-Box) to define special function to a group.
* **Order/Select N**   
  Select to open the [Group Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097481-Group-Options-Dialog-Box) to specify the sort order of the group values and define the number of the group values to display in the heat map.

**Property**

The box lists the summaries that you add to calculate data in the heat map based on the lowest group.

* **Size By**  
  Select to use the summary to determine the size of the rectangles.
* **Color By**  
  Select to use the summary to determine the fill color of the rectangles.
* **Label By**  
  Select to show the values of the summary in the innermost rectangles.

### Filter Screen

Designer displays the Filter screen only when you use the dialog box for creating a chart. You can use this screen to narrow down the data to display in the chart.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Chart Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404857007383/chtwzd_fltr.gif)

### Layout Screen

Use this screen to specify the layout of the chart elements. Designer does not display some options for certain chart types. For more information about the options, [select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report#Layout).

![Chart Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404848626839/chtwzd_layout.gif)

### Style Screen

Use this screen to specify the style of the chart.

![Chart Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848628759/chtwzd_styl.gif)

**Style**

The box lists the styles that you can apply to the chart. Select the style for the chart.

* **<Custom>**  
  This style contains no information. It is only used to support reports that was built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the chart.

**Inherit Style**

Designer displays the option only when the chart is inside another banded object, or to be inserted into another banded object. Select it if you want the chart to inherit the style of its parent.

**Page Setup**

Designer displays the button only when you use the dialog box for creating a chart in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) to specify page properties for the report tab.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058182-Chart-Iterator-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095701-Choose-Data-Dialog-Box)
