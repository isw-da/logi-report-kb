---
title: "Chart Wizard Dialog (Query Based)"
id: 1500009564722
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564722-Chart-Wizard-Dialog-Query-Based
updated_at: 2021-07-24T05:55:36Z
---

# Chart Wizard Dialog (Query Based)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585841-Chart-Wizard-Dialog-Business-View-Based-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564662-Choose-Data-Dialog)

# Chart Wizard Dialog (Query Based)

The Chart Wizard dialog that is based on query resource appears when you do either of the following:

* In the [Select Component for Page Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009588661-Select-Component-for-Page-Report-Tab-Dialog) dialog or [Select Component for Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009567422-Select-Component-for-Page-Report-Dialog) dialog, select the Chart component and then select OK. In this case, it helps you [create a page report with a chart in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on a query resource.
* Right-click a chart created on a query and select Chart Wizard on the shortcut menu. In this case, it helps you [modify](https://devnet.logianalytics.com/hc/en-us/articles/1500009583701-Modifying-a-Chart) the chart.

The wizard consists of the following screens:

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

Finishes creating or modifying the chart and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Data

Specifies the dataset for the chart. [See the screen](javascript:%20void(null)).

![Chart Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404893949463/chtwzd_dt.gif)

**Resource box**

Lists the available data resources in the current catalog. Select one to create the chart.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the chart.

* **New****Dataset**  
   If checked, select a data resource from the current catalog to create a dataset that will be used to build the chart. When you choose to create the dataset from a query, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) if required.
* **Existing****Dataset**  
   If checked, select a dataset from the ones existing in the open report to create the chart. Select the Edit button to edit the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if required.
* **Current****Dataset**  
   If checked, the current dataset used by the parent object will be applied to the chart.

## Type

Specifies the type of the chart. You can refer to the section [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500009563282-Chart-Types) which describes each of the chart type in detail. [See the screen](javascript:%20void(null)).

![Chart Wizard - Type screen](https://devnet.logianalytics.com/hc/article_attachments/4404893949719/chtwzd_type.gif)

**Single chart**

Specifies to create a single chart.

* **Chart Type**  
   Lists all the chart types that can be used to create a single chart.
* **Sub type box**   
   Lists all the sub types of the selected chart type.

**Combo chart**

Specifies to make more than one type use the primary or secondary axis. The types should be featured as Combination charts. Two types of data markers are used to represent different data values.

* **Chart Type**  
   Lists all the chart types that can be added as a combo chart.
* **Sub type****box**  
   Lists all the sub-types of the selected chart type.
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

## Display

The Display screen differs with chart types: [common chart types](#ChartDisplay), [organization chart](#OrgDisplay), or [heat map](#htmpDisplay).

### For common chart types

Specifies the data displayed on the chart. [See the screen](javascript:%20void(null)).

![Chart Wizard - Display screen for common chart types](https://devnet.logianalytics.com/hc/article_attachments/4404889386903/chtwzd_dsply.gif)

**Resources**

Lists all the available data resources in the selected dataset.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected fields to be displayed in the chart.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)

Removes the selected fields from the chart if they are not required.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected field in the chart with the specified field in the Resources box.

**Category****/Series**

Lists the field you want to display on the category/series axis of the chart.

For a real time chart, if no category field is specified, Use System Refresh Time will be automatically displayed in the Category box, namely, the time at which the chart refreshes itself will be used as the category value; the series axis will be disabled.

* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define how to group information.
* **Special Function**  
   Opens the [Special Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009588861-Special-Function-Dialog) dialog to define some special function to the field.
* **Order/Select N**   
   Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009586241-Category-Options-Dialog) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009567342-Series-Options-Dialog) dialog to specify the sort order of the category or series values and define the number of the category or series values that will be displayed in the chart.

**Show Values**

Lists the values you want to show in the chart. For a back-to-back bench chart, only one value can be added.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893928215/btn_edit1.gif)  
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009586341-Edit-Additional-Value-Dialog) dialog to edit an additional value. Available only when a constant value or an average value is selected in the Show Values box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the selected value one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the selected value one step down.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new pair of Y Axis and Radius for the bubble chart.
* ![Remove nutton](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected field from the bubble chart if they are not required.
* **X Axis**  
   Lists the value you want to show on the X axis of the bubble chart.
* **Y Axis**  
   Lists the value you want to show on the Y axis of the bubble chart.
* **Radius**  
   Lists the value you want to show as the bubble radius.
* **Left**  
  Lists the value you want to show on the origin left of the value axis. Only one value can be added. Available to 2-D back-to-back bench chart only.
* **Right**  
   Lists the value you want to show on the origin right of the value axis. Only one value can be added. Available to 2-D back-to-back bench chart only.

**Series Values**

If checked, you can specify the series values on the origin left/right of the value axis one by one manually. Only one of the Left and Right boxes can be edited. Available only when a back-to-back bench has a series field.

* **Left**  
   Lists the series values on the origin left of the value axis.
* **Right**  
   Lists the series values on the origin right of the value axis.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the selected value one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the selected value one step down.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new value line. Double-click in it to specify the value.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected value line.

**Series Conditions**

If checked, you can specify the series values on the origin left/right of the value axis using condition. Only one of the Left and Right boxes can be edited. Available only when a back-to-back bench has a series field.

* **Left**  
   Lists the condition expression which defines the series values on the origin left of the value axis.
* **Right**  
   Lists the condition expression which defines the series values on the origin right of the value axis.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893928215/btn_edit1.gif)  
   Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog#edit) dialog to edit the condition which defines the series values on the origin left/right of the value axis.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the added condition.

### For organization chart

Specifies the data displayed on the chart. [See the screen](javascript:%20void(null)).

![Chart Wizard - Display screen for orgnization chart](https://devnet.logianalytics.com/hc/article_attachments/4404893950103/chtwzd_orgdsply.gif)

**Child**

Specify a field from the drop-down list which identifies the entity.

**Parent**

Specify a field from the drop-down list which shows the "reporting to" relationship among the entity members, that is, which child field member reports to or belongs to which child field member.

**Resources**

Lists all the available resources that can be added in the org chart.

**Properties**

The Properties box presents a node model of the org chart. Data fields, labels and images can be inserted into the node as the information about the entity in the org chart.

### For heat map

Specifies the data displayed on the chart. [See the screen](javascript:%20void(null)).

![Chart Wizard - Display screen for heat map](https://devnet.logianalytics.com/hc/article_attachments/4404889387159/chtwzd_htmpdsply.gif)

**Resources**

Lists all the available data resources in the selected dataset.

**Groups**

Lists the fields used to group the data to different areas. There should be at least one group. When there are multiple groups, their levels are defined by their positions from top down. The group at the top is of the highest level and the bottom the lowest.

* **Color By**  
   Specifies whether to color by a group. 0-n groups can be used as the color-by fields.
* **Label By**  
   Specifies whether to show the group name in the innermost rectangle.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define how to group information.
* **Special Function**  
   Opens the [Special Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009588861-Special-Function-Dialog) dialog to define some special function to the field.
* **Order/Select N**   
   Opens the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009566322-Group-Options-Dialog) dialog to specify the sort order of the group values and define the number of the group values that will be displayed in the chart.

**Summaries**

Lists the summaries used to do size-by/color-by or displayed in the innermost rectangle.

When no group is specified in the Groups box, you can insert any static summary, and its group-by field will be inserted into the Groups box automatically. When there are multiple groups, static summaries should match the lowest-level group. For example, if the groups level is A > B > C, the static summaries grouped by C can be inserted into the Summaries box, but the static summaries grouped by A, B or other fields cannot.

* **Size By**  
   Specifies to size by one summary or none.
* **Color By**  
   Specifies to color by one summary or none.
* **Label By**  
   Specifies whether to show a summary in the innermost rectangle.

## Filter

Specifies to filter the data used in the chart. This screen is available only when you create a chart. [See the screen](javascript:%20void(null)).

![Chart Wizard - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404889387415/chtwzd_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Layout

The Layout screen differs with chart type: [common chart types](#ChartLayout), [organization chart](#OrgLayout), or [heat map](#htmpLayout).

### For common chart types

Specifies the layout of the chart elements. [See the screen](javascript:%20void(null)).

![Chart Wizard - Layout screen for common chart types](https://devnet.logianalytics.com/hc/article_attachments/4404893950359/chtwzd_layout.gif)

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
   Specifies the component to which the chart will be mapped. For details, see [Creating Dynamic Chart in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009583421-Creating-Dynamic-Charts-in-Excel).

### For organization chart

Specifies the layout of the chart elements. [See the screen](javascript:%20void(null)).

![Chart Wizard - Layout screen for orgnization chart](https://devnet.logianalytics.com/hc/article_attachments/4404893950615/chtwzd_layoutorg.gif)

**Type**

Specifies the layout mode of the org chart.

* **Top down**  
   The org chart tree expands from top to bottom.
* **Bottom up**  
   The org chart tree expands from bottom to top. It is the reverse of the top down type.
* **Left right**  
   The org chart tree expands from left to right.

**Title**

* **Chart Title**  
   Specifies the title of the chart.

**Export**

* **Mapping Component**  
   Specifies the component to which the chart will be mapped. For details, see [Creating Dynamic Chart in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009583421-Creating-Dynamic-Charts-in-Excel).

### For heat map

Specifies the layout of the chart elements. [See the screen](javascript:%20void(null)).

![Chart Wizard - Layout screen for heat map](https://devnet.logianalytics.com/hc/article_attachments/4404893950871/chtwzd_layouthtmp.gif)

**Title**

* **Chart Title**  
   Specifies the title of the chart.

**Legend**

* **Show Legend**  
   Specifies whether to show the legend in this chart.

## Style

Specifies the style of the chart. [See the screen](javascript:%20void(null)).

![Chart Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404889387671/chtwzd_sty.gif)

**Style**

Specifies the style of the chart.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the chart.

**Inherit Style**

Specifies whether to make the chart take the style of its parent. This options is available only when you modify a chart and the chart is inserted into a banded object or table.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a chart.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585841-Chart-Wizard-Dialog-Business-View-Based-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564662-Choose-Data-Dialog)
