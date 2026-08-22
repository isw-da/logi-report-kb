---
title: "Create Chart Dialog (Business View Based)"
id: 1500009564882
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564882-Create-Chart-Dialog-Business-View-Based
updated_at: 2021-07-24T05:55:34Z
---

# Create Chart Dialog (Business View Based)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585961-Create-Banded-Object-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585981-Create-Chart-Dialog-Query-Based-)

# Create Chart Dialog (Business View Based)

The Create Chart dialog that is based on business view differs for [a normal chart](#Normal) and [a KPI chart](#KPI).

## For Normal Chart

This wizard appears when you select Insert > Chart, or drag the button of the desired chart type from the Components panel into a report that is created using business views. It helps you to [create a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009563242-Inserting-a-Chart#Web) in the report, and consists of the following screens:

* [Data](#Data)
* [Type](#Type)
* [Display](#Display)
* [Filter](#Filter)
* [Layout](#Layout)
* [Style](#Style)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating a chart and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

### Data

Specifies the business view that you want to use to create the chart. [See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404893942423/crtcht_dt_wb.gif)

**Resources**

Lists all the business views in the current catalog. Specify the one you want to use.

### Type

Specifies the type of the chart. You can refer to the section [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500009563282-Chart-Types) which describes each of the chart type in detail. Only the 2-D chart types are supported.

[See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Type screen](https://devnet.logianalytics.com/hc/article_attachments/4404889381399/crtcht_type_wb.gif)

**Single chart**

Specifies to create a single chart.

* **Chart Type**  
   Lists all the chart types that can be used to create a single chart.
* **Subtype**  
   Lists all the subtypes of the selected chart type. Hover the mouse pointer on a subtype icon and you will see its name.

**Combo chart**

Specifies to make more than one type use the primary or secondary axis. The types should be featured as Combination charts. Two types of data markers are used to represent different data values.

* **Chart Type**  
   Lists all the chart types that can be added as a combo chart.
* **Subtype**  
  Lists all the subtypes of the selected chart type. Hover the mouse pointer on a subtype icon and you will see its name.

* **Chart Type Groups**  
   Lists all the chart types that are to be used in the combo chart.
  + **Primary Axis**  
    - **<Add Combo Type>**  
       Adds a chart type to the primary axis.
  + **Secondary Axis**  
    - **<Add Combo Type>**  
       Adds a chart type to the secondary axis.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes a specified chart type from the Chart Type Groups box.

### Display

The Display screen differs with chart type: [common chart types](#ChartDisplay), [organization chart](#OrgDisplay), or [heat map](#htmpDisplay).

#### For common chart types

Specifies the data displayed on the chart. [See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Diaplay screen for common chart types](https://devnet.logianalytics.com/hc/article_attachments/4404893942679/crtcht_dsply_wb.gif)

**Title**

Specifies the title of the chart.

**Resources**

Lists all the available data resources in the selected business view. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected fields to be displayed in the chart.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)

Removes the selected fields from the chart if they are not required.

**Category/Series box**

The box lists the field you want to display on the category/series axis of the chart.

For a real time chart, if no category field is specified, Use System Refresh Time will be automatically displayed in the category box, namely, the time at which the chart refreshes itself will be used as the category value; the series axis will be disabled.

* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define how to group information.
* **Order/Select N**   
   Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009586241-Category-Options-Dialog) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009567342-Series-Options-Dialog) dialog to specify the sort order of the category or series values and define the number of the category or series values that will be displayed in the chart.

**Show Value box**

The box lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be summary fields.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893928215/btn_edit1.gif)  
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009586341-Edit-Additional-Value-Dialog) dialog to edit an additional value. Available only when a constant value or an average value is selected.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the selected value one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the selected value one step down.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new pair of Y Axis and Radius for the bubble chart.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected field from the bubble chart if they are not required.
* **X-Axis**  
   Lists the value you want to show on the X axis of the bubble chart.
* **Y-Axis**  
   Lists the value you want to show on the Y axis of the bubble chart.
* **Size**  
   Lists the value you want to show as the bubble size.

**Motion Bar for Playable Chart**

Lists the field you want to use as the motion field. A motion field can only be of Integer, Date or Time data type. Available to single bar, bench and bubble charts in web reports and library components only.

* **Special Function**  
   Opens the [Special Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009588861-Special-Function-Dialog) dialog to define some special function to the motion field. Available only when the motion field is of Date data type.

**Real Time**

Specifies to run the chart in real time mode, which means it will be updated automatically by using real time data after it is published to Logi JReport Server. Available to single bar, bench, line, and area charts in web reports and library components only.

* **Use System Time for Category**  
   Specifies to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
   Specifies the time interval at which the chart will get data and refresh itself automatically.
* **Show Most Recent N Points**  
   Specifies the number of points that will be kept for the real time data on the chart.
* **Incremental Fetch**  
   Opens the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009567822-Unique-Key-dialog-Dialog) dialog to configure a unique key for the real time chart.

#### For organization chart

Specifies the data displayed on the chart. [See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Display for orgnization chart](https://devnet.logianalytics.com/hc/article_attachments/4404893942935/crtcht_orgdsply_wb.gif)

**Node**

Specify a field from the drop-down list which identifies the entity.

**Parent**

Specify a field from the drop-down list which shows the "reporting to" relationship among the entity members, that is, which child field member reports to or belongs to which child field member.

**Resources**

Lists all the available resources that can be added to the organization chart. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the chart.

**Properties**

The Properties box presents a node model of the organization chart. Data fields, labels and images can be inserted into the node as the information about the entity in the organization chart.

#### For heat map

Specifies the data displayed on the chart. [See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Display screen for heat map](https://devnet.logianalytics.com/hc/article_attachments/4404893943191/crtcht_htmpdsply_wb.gif)

**Resources**

Lists all the available data resources in the selected dataset. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the chart.

**Area**

Lists the fields used to group the data to different areas. There should be at least one group. When there are multiple groups, their levels are defined by their positions from top down. The group at the top is of the highest level and the bottom the lowest.

* **Color By**  
   Specifies whether to color by a group. 0-n groups can be used as the color-by fields.
* **Label By**  
   Specifies whether to show the group name in the innermost rectangle.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define how to group information.
* **Order/Select N**  
   Opens the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009566322-Group-Options-Dialog) dialog to specify the sort order of the group values and define the number of the group values that will be displayed in the chart.

**Property**

Lists the summaries used to do size-by/color-by or displayed in the innermost rectangle.

When no group is specified in the Groups box, you can insert any static summary, and its group-by field will be inserted into the Groups box automatically. When there are multiple groups, static summaries should match the lowest-level group. For example, if the groups level is A > B > C, the static summaries grouped by C can be inserted into the Summaries box, but the static summaries grouped by A, B or other fields cannot.

* **Size By**  
   Specifies to size by one summary or none.
* **Color By**  
   Specifies to color by one summary or none.
* **Label By**  
   Specifies whether to show a summary in the innermost rectangle.

### Filter

Specifies to filter the data used in the chart. [See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404893943447/crtcht_fltr_wb.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

### Layout

The Layout screen differs with chart type: [common chart types](#ChartLayout), [organization chart](#OrgLayout), or [heat map](#htmpLayout).

#### For common chart types

Specifies settings of some of the chart elements. [See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Layout screen for common chart types](https://devnet.logianalytics.com/hc/article_attachments/4404893941911/crtcht_layout.gif)

**Data**

* **Category Start Offset**  
   Specifies the start offset of category from which the chart will be displayed.
* **Category End Offset**  
   Specifies the end offset of category to which the chart will be displayed.
* **Series Start Offset**  
   Specifies the start offset series from which the chart will be displayed.
* **Series End Offset**  
   Specifies the end offset of series to which the chart will be displayed.
* **Reverse Category**  
   Specifies whether to reverse the display order of the categories.
* **Reverse Series**  
   Specifies whether to reverse the display order of the series.
* **Swap Groups**  
  Specifies to display values from different data fields by switching data between the category and series axes, the category and values axes.

**Notes:**

* If values are set to be less than 0, it means the categories or series will be displayed without any offset.
* If values are set to be greater than 0 and the value of Category/Series Start Offset is greater than that of Category/Series End Offset, all of the categories or series will be displayed.

**Title**

* **Chart Title**  
   Specifies the title of the chart.
* **Category (X) Axis Title**  
   Specifies the title of the X-axis.
* **Value (Y) Axis Title**  
   Specifies the title of the Y-axis.
* **Value (Y2) Axis Title**  
   Specifies the title of the Y2-axis.

**Axis**

* **Show Category (X) Axis**  
   Specifies whether to show the category (X) axis in this chart.
* **Show Value (Y) Axis**  
   Specifies whether to show the value (Y) axis in this chart.
* **Show Value (Y2) Axis**  
   Specifies whether to show the value (Y2) axis in this chart.
* **Show Series (Z) Axis**  
   Specifies whether to show the series (Z) axis in this chart.

**Wall**

* **Show Wall**  
   Specifies whether to show the wall in this chart.
* **Show Floor**  
   Specifies whether to show the floor in this chart.

**Gridlines**

* **Show Category (X) Axis Gridlines**  
   Specifies whether to show the gridlines of category (X) axis.
* **Show Value (Y) Axis Gridlines**  
   Specifies whether to show the gridlines of value (Y) axis.
* **Show Value (Y2) Axis Gridlines**  
   Specifies whether to show the gridlines of value (Y2) axis.
* **Show Series (Z)** **Axis Gridlines**  
   Specifies whether to show the gridlines of series (Z) axis.

**Legend**

* **Show Legend**  
   Specifies whether to show the legend in this chart.

**Export**

* **Mapping Component**  
   This option is disabled when creating a chart. It specifies the component to which the chart will be mapped (for details, see [Creating Dynamic Chart in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009583421-Creating-Dynamic-Charts-in-Excel)).

#### For organization chart

Specifies the layout of the chart elements. [See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Layout screen for orgnization chart](https://devnet.logianalytics.com/hc/article_attachments/4404889380631/crtcht_layoutorg.gif)

**Type**

Specifies the layout mode of the organization chart.

* **Top down**  
   The organization chart tree expands from top to bottom.
* **Bottom up**  
   The organization chart tree expands from bottom to top. It is the reverse of the top down type.
* **Left right**  
   The organization chart tree expands from left to right.

**Title**

* **Chart Title**  
   Specifies the title of the chart.

**Export**

* **Mapping Component**  
   Specifies the component to which the chart will be mapped. For details, see [Creating Dynamic Chart in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009583421-Creating-Dynamic-Charts-in-Excel).

#### For heat map

Specifies the layout of the chart elements. [See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Layout screen for heat map](https://devnet.logianalytics.com/hc/article_attachments/4404889380887/crtcht_layouthtmp.gif)

**Title**

* **Chart Title**  
   Specifies the title of the chart.

**Legend**

* **Show Legend**  
   Specifies whether to show the legend in this chart.

### Style

Specifies the style of the chart. [See the screen](javascript:%20void(null)).

![Create Chart wizard based on business view - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404889381655/crtcht_sty_wb.gif)

**Style**

Specifies the style of the chart.

**Preview**

Displays the selected style and layout effects.

**Inherit Style**

Specifies whether to make the chart take the style of its parent. This options is available only when the chart is inserted in a banded object in a page report.

## For KPI Chart

The wizard appears when you right-click in the blank area of a KPI component and then select Insert KPI Chart from the shortcut menu. It helps you [insert a KPI chart into a KPI component](https://devnet.logianalytics.com/hc/en-us/articles/1500009583981-KPI-Components) and consists of the following screens:

* [Data](#Data1)
* [Type](#Type1)
* [Display](#Display1)
* [Filter](#Filter1)
* [Layout](#Layout1)
* [Style](#Style1)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Inserts the KPI chart into the KPI component and closes the wizard.

**Cancel**

Does not retain changes and closes the wizard.

**Help**

Displays the help document about this feature.

### Data

Shows the business view bound to the KPI component. The business view will be used as the data source of the KPI chart.  [See the screen](javascript:%20void(null)).

![Create Chart wizard for KPI chart - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889381911/crtcht_dt_wb-kpi.gif)

### Type

Specifies the type of the chart. You can refer to the section [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500009563282-Chart-Types) for the corresponding chart types in detail in detail. The following 2-D chart types are supported in KPI charts: Bar, Bench, Line, Area, Pie, and Bullet. [See the screen](javascript:%20void(null)).

![Create Chart wizard for KPI chart - Type screen](https://devnet.logianalytics.com/hc/article_attachments/4404893943703/crtcht_type_wb-kpi.gif)

**Single chart**

Specifies to create a single chart.

* **Chart Type**  
   Lists all the chart types that can be used to create a single chart.
* **Subtype**  
   Lists all the subtypes of the selected chart type.

**Combo chart**

Specifies to make more than one type use the primary or secondary axis. The types should be featured as combination charts. Two types of data markers are used to represent different data values.

* **Chart Type**  
   Lists all the chart types that can be added as a combo chart.
* **Subtype**  
   Lists all the subtypes of the selected chart type.
* **Chart Type Groups**  
   Lists all the chart types that are to be used in the combo chart.
  + **Primary Axis**
    - **<Add Combo Type>**  
       Adds a chart type to the primary axis.
  + **Secondary Axis**
    - **<Add Combo Type>**  
       Adds a chart type to the secondary axis.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes a specified chart type from the Chart Type Groups box.

### Display

Specifies the data displayed on the chart. [See the screen](javascript:%20void(null)).

![Create Chart wizard for KPI chart - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404889382167/crtcht_dsply_wb-kpi.gif)

**Title**

Specifies the title of the chart.

**Resources**

Lists all the available data resources in the bound business view. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected fields to be displayed in the chart.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)

Removes the selected fields from the chart if they are not required.

**Category****/Series**

The box lists the field you want to display on the category/series axis of the chart.

For a real time chart, if no category field is specified, Use System Refresh Time will be automatically displayed in the Category box, namely, the time at which the chart refreshes itself will be used as the category value; the series axis will be disabled.

* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define how to group information.
* **Order/Select N**   
   Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009586241-Category-Options-Dialog) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009567342-Series-Options-Dialog) dialog to specify the sort order of the category or series values and define the number of the category or series values that will be displayed in the chart.

**Show Values**

Lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be summary fields.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893928215/btn_edit1.gif)  
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009586341-Edit-Additional-Value-Dialog) dialog to edit an additional value. Available only when a constant value or an average value is selected.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the selected value one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the selected value one step down.

**Motion Bar for Playable Chart**

Lists the field you want to use as the motion field. A motion field can only be of Integer, Date or Time data type. Available to single bar and bench charts in KPI charts only.

* **Special Function**  
   Opens the [Special Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009588861-Special-Function-Dialog) dialog to define some special function to the motion field. Available only when the motion field is of Date data type.

**Real Time**

Specifies to run the chart in real time mode, which means it will be updated automatically by using real time data after it is published to Logi JReport Server. Available to single bar, bench, line, and area charts in web reports and library components only.

* **Use System Time for Category**  
   Specifies to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
   Specifies the time interval at which the chart will get data and refresh itself automatically.
* **Show Most Recent N Points**  
   Specifies the number of points that will be kept for the real time data on the chart.
* **Incremental Fetch**  
   Opens the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009567822-Unique-Key-dialog-Dialog) dialog to configure a unique key for the real time chart.

### Filter

Specifies to filter the data used in the chart. [See the screen](javascript:%20void(null)).

![Create Chart wizard for KPI chart - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404889382423/crtcht_fltr_wb-kpi.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

### Layout

Specifies the layout of the chart elements. [See the screen](javascript:%20void(null)).

![Create Chart wizard for KPI chart - Layout screen](https://devnet.logianalytics.com/hc/article_attachments/4404889382679/crtcht_layout-kpi.gif)

**Data**

* **Category Start Offset**  
   Specifies the start offset of category from which the chart will be displayed.
* **Category End Offset**  
   Specifies the end offset of category to which the chart will be displayed.
* **Series Start Offset**  
   Specifies the start offset of series from which the chart will be displayed.
* **Series End Offset**  
   Specifies the end offset of series to which the chart will be displayed.
* **Reverse Category**  
   Specifies whether to reverse the display order of the categories.
* **Reverse Series**  
   Specifies whether to reverse the display order of the series.
* **Swap Groups**  
  Specifies to display values from different data fields by switching data between the category and series axes, the category and values axes.

**Notes:**

* If values are set to be less than 0, it means the categories or series will be displayed without any offset.
* If values are set to be greater than 0 and the value of Category/Series Start Offset is greater than that of Category/Series End Offset, all of the categories or series will be displayed.

**Title**

* **Chart Title**  
   Specifies the title of the chart.

**Wall**

* **Show Wall**  
   Specifies whether to show the wall in this chart.

**Export**

* **Mapping Component**  
   Specifies the component to which the chart will be mapped. For details, see [Creating Dynamic Chart in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009583421-Creating-Dynamic-Charts-in-Excel).

### Style

Specifies the style of the chart. [See the screen](javascript:%20void(null)).

![Create Chart wizard for KPI chart - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404889382935/crtcht_sty_wb-kpi.gif)

**Style**

Specifies the style of the chart.

**Preview**

Displays a diagram illustrating the effect of the selected style on the chart.

**Inherit Style**

Specifies whether to make the chart take the style of the parent KPI component.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585961-Create-Banded-Object-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585981-Create-Chart-Dialog-Query-Based-)
