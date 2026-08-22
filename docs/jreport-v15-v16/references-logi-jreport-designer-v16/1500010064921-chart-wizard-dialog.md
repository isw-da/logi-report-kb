---
title: "Chart Wizard Dialog"
id: 1500010064921
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064921-Chart-Wizard-Dialog
updated_at: 2021-07-24T10:39:07Z
---

# Chart Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029942-Chart-Iterator-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029902-Choose-Data-Dialog)

# Chart Wizard Dialog

The Chart Wizard helps you to [create a page report tab with a chart in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page), [create a library component with a chart in it,](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#LC) or [edit an existing chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063621-Modifying-Charts#Edit)  in a report. It varies with the data resource type used by the chart: [business view](#BV) or [query resource](#Query).

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or editing the chart and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Chart Wizard - Business View Based

When the wizard is used for creating or editing a chart using a business view, it consists of the following screens: [Data](#BVData), [Type](#BVType), [Display](#BVDisplay), [Filter](#BVFilter), [Layout](#BVLayout) and [Style](#BVStyle). The Filter screen is available only when the wizard is used for creating a chart.

### Data

The screen lists all the predefined business views in the current catalog. Select the one you want to use for the chart.

![Chart Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404901288471/chtwzd_dt_bv.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the chart is in any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

### Type

Specifies the type of the chart. You can refer to the section [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500010029042-Chart-Types) which describes each of the chart type in detail. When using business view as the chart data source, only the 2-D chart types are supported.

![Chart Wizard - Type](https://devnet.logianalytics.com/hc/article_attachments/4404909242391/chtwzd_type_bv.gif)

**Single chart**

Specifies to create a single chart.

* **Chart Type**  
   Lists all the chart types that can be used to create a single chart.
* **Subtype**  
   Lists all the subtypes of the selected chart type. Hover the mouse pointer on a subtype icon and you will see its name.

**Combo chart**

Specifies to make more than one type use the primary or secondary axis. The types should be featured as combination charts. Two types of data markers are used to represent different data values.

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
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Removes the selected chart type from the Chart Type Groups box.

### Display

Specifies the data to display on the chart. The screen differs according to the chart type: [common chart types](#BVCommon), [organization chart](#BVOrg) or [heat map](#BVHeatMap).

#### For common chart types

![Chart Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404901288727/chtwzd_dsply_bv.gif)

**Title**

Specifies the title of the chart.

**Resources**

Lists the resources in and related to the specified business view, which can be used for the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)

Removes the selected field from the chart.

**Category****/Series**

Lists the field to display on the category/series axis of the chart. For a gauge chart, you can select the Advanced button to show or hide the Category/Series box.

For a real time chart, if no category field is specified, the text Use System Refresh Time will be automatically displayed in the Category box, namely the time at which the chart refreshes itself will be used as the category value; the series axis will be disabled.

* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog) dialog to define how to group information.
* **Order/Select N**   
   Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010065241-Category-Options-Dialog) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010032382-Series-Options-Dialog) dialog to specify the sort order of the category or series values and define the number of the category or series values to show on the chart.

**Show Values**

Lists the values you want to show in the chart.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404909175191/btn_edit1.gif)  
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500010065461-Edit-Additional-Value-Dialog) dialog to edit an additional value. Available only when a constant value or an average value is selected.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
   Moves the selected value one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
   Moves the selected value one step down.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
   Adds a new pair of Y-Axis and Size for the bubble chart.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Removes the selected value from the bubble chart.
* **X-Axis**  
   Lists the value you want to show on the X axis of the bubble chart.
* **Y-Axis**  
   Lists the value you want to show on the Y axis of the bubble chart.
* **Size**  
   Lists the value you want to show as the bubble size.

**Motion Bar for Playable Chart**

Lists the field used as the motion field. A motion field can only be of the Integer, Date or Time data type. Available to single bar, bench and bubble charts in web reports and library components only.

* **Special Function**  
   Opens the [Special Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010032742-Special-Function-Dialog) dialog to define special function to the motion field. Available only when the motion field is of the Date data type.

**Real Time**

Specifies to run the chart in real time mode. Available to single bar, bench, line, and area charts in web reports and library components only.

* **Use System Time for Category**  
   Specifies to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
   Specifies the time interval at which the chart will get data and refresh itself automatically.
* **Show Most Recent N Points**  
   Specifies the number of points that will be kept for the real time data on the chart.
* **Incremental Fetch**  
   Opens the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500010032922-Unique-Key-dialog-Dialog) dialog to configure a unique key for the real time chart.

#### For organization chart

![Chart Wizard - Org Display](https://devnet.logianalytics.com/hc/article_attachments/4404909242647/chtwzd_dsply_org_bv.gif)

**Node**

Specifies the field the values of which to display as the nodes in the org chart.

**Parent**

Specifies the field which shows the "reporting to" relationship among the node field values.

**Resources**

Lists the resources in and related to the specified business view, which can be added to display in each node in the org chart. You can also add images and labels to the nodes.

**Properties**

The Properties box presents a node model for specifying the information you want to display in each node in the org chart.

#### For heat map

![Chart Wizard - Heat Map Display](https://devnet.logianalytics.com/hc/article_attachments/4404909242903/chtwzd_dsply_htmp_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used for the heat map.

**Area**

Lists the groups of the heat map. There should be at least one group.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
   Moves the selected group one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
   Moves the selected group one step down.<
* **Color By**  
   Specifies whether to color by a group.
* **Label By**  
   Specifies whether to show the values of a group in the innermost rectangles.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog) dialog to define how to group information.
* **Order/Select N**  
   Opens the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010031322-Group-Options-Dialog) dialog to specify the sort order of the group values and define the number of the group values to display in the heat map.

**Property**

Lists the aggregations added to calculate data based on the lowest group of the heat map.

* **Size By**  
   Specifies to use the aggregation to determine the size of the rectangles.
* **Color By**  
   Specifies to use the aggregation to determine the fill color of the rectangles.
* **Label By**  
   Specifies whether to show the values of an aggregation in the innermost rectangles.

### Filter

Specifies to filter data displayed in the chart. This screen is available only when you create a chart, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Chart Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404901288983/chtwzd_fltr_bv.gif)

### Layout

Specifies the layout of the chart elements. Some layout options may not be available for certain chart types. For details about the options, [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010063601-Inserting-Charts-in-a-Report#Layout).

![Chart Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404909243159/chtwzd_layout.gif)

### Style

Specifies the style of the chart.

![Chart Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404909243415/chtwzd_styl_bv.gif)

**Style**

Specifies the style of the chart.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the chart.

**Inherit Style**

Specifies whether to make the chart take the style of its parent. This options is available only when the chart is inserted in a banded object in a page report.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500010067381-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a chart in a page report.

## Chart Wizard - Query Based

When the wizard is used for creating or editing a chart using a query resource, it consists of the following screens: [Data](#Data), [Type](#Type), [Display](#Display), [Filter](#Filter), [Layout](#Layout) and [Style](#Style). The Filter screen is available only when the wizard is used for creating a chart.

## Data

Specifies the dataset for the chart.

![Chart Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404901289367/chtwzd_dt.gif)

**Resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the chart.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the chart.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog) if required.
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010030342-Dataset-Editor-Dialog) if required.
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

## Type

Specifies the type of the chart. You can refer to the section [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500010029042-Chart-Types) which describes each of the chart type in detail.

![Chart Wizard - Type](https://devnet.logianalytics.com/hc/article_attachments/4404909243671/chtwzd_type.gif)

**Single chart**

Specifies to create a single chart.

* **Chart Type**  
   Lists all the chart types that can be used to create a single chart.
* **Subtype box**   
   Lists all the subtypes of the selected chart type.

**Combo chart**

Specifies to make more than one type use the primary or secondary axis. The types should be featured as Combination charts. Two types of data markers are used to represent different data values.

* **Chart Type**  
   Lists all the chart types that can be added as a combo chart.
* **Subtype****box**  
   Lists all the subtypes of the selected chart type.
* **Chart Type Groups**  
   Lists all the chart types that are to be used in the combo chart.
  + **Primary Axis**
    - **<Add Combo Type>**  
       Adds a chart type to the primary axis.
  + **Secondary Axis**
    - **<Add Combo Type>**  
       Adds a chart type to the secondary axis.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Removes the selected chart type from the Chart Type Groups box.

## Display

Specifies the data to display on the chart. The screen differs according to the chart type: [common chart types](#Common), [organization chart](#Org) or [heat map](#HeatMap).

### For common chart types

![Chart Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404901289623/chtwzd_dsply.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used for the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)

Removes the selected field from the chart.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404901173527/btn_replace.gif)

Replaces the selected field in the chart with the specified field in the Resources box.

**Category/Series**

Lists the field to display on the category/series axis of the chart. For a gauge chart, you can select the Advanced button to show or hide the Category/Series box.

For a real time chart, if no category field is specified, the text Use System Refresh Time will be automatically displayed in the Category box, namely the time at which the chart refreshes itself will be used as the category value; the series axis will be disabled.

* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog) dialog to define how to group information.
* **Special Function**  
   Opens the [Special Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010032742-Special-Function-Dialog) dialog to define special function to the field.
* **Order/Select N**   
   Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010065241-Category-Options-Dialog) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010032382-Series-Options-Dialog) dialog to specify the sort order of the category or series values and define the number of the category or series values to show on the chart.

**Show Values**

Lists the values you want to show in the chart. For a back-to-back bench chart, only one value can be added.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404909175191/btn_edit1.gif)  
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500010065461-Edit-Additional-Value-Dialog) dialog to edit an additional value. Available only when a constant value or an average value is selected in the Show Values box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
   Moves the selected value one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
   Moves the selected value one step down.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
   Adds a new pair of Y Axis and Radius for the bubble chart.
* ![Remove nutton](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Removes the selected field from the bubble chart.
* **X Axis**  
   Lists the value you want to show on the X axis of the bubble chart.
* **Y Axis**  
   Lists the value you want to show on the Y axis of the bubble chart.
* **Radius**  
   Lists the value you want to show as the bubble radius.
* **Left**  
   Lists the value you want to show on the origin left of the value axis on the 2-D back-to-back bench chart. Only one value can be added.
* **Right**  
   Lists the value you want to show on the origin right of the value axis on the 2-D back-to-back bench chart. Only one value can be added.

**Series Values**

If checked, you can specify the series values on the origin left/right of the value axis on the back-to-back bench chart manually. Only one of the Left and Right boxes can be edited.

* **Left**  
   Lists the series values on the origin left of the value axis.
* **Right**  
   Lists the series values on the origin right of the value axis.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
   Moves the selected value one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
   Moves the selected value one step down.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
   Adds a new value line. double-click in it to specify the value.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Removes the selected value line.

**Series Conditions**

If checked, you can specify the series values on the origin left/right of the value axis on the back-to-back bench chart using condition. Only one of the Left and Right boxes can be edited.

* **Left**  
   Lists the condition expression which defines the series values on the origin left of the value axis.
* **Right**  
   Lists the condition expression which defines the series values on the origin right of the value axis.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404909175191/btn_edit1.gif)  
   Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500010065521-Edit-Conditions-Dialog) dialog to edit the condition which defines the series values on the origin left/right of the value axis.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Removes the added condition.

### For organization chart

![Chart Wizard - Org Display](https://devnet.logianalytics.com/hc/article_attachments/4404901290135/chtwzd_dsply_org.gif)

**Node**

Specifies the field the values of which to display as the nodes in the org chart.

**Parent**

Specifies the field which shows the "reporting to" relationship among the node field values.

**Resources**

Lists the resources in and related to the specified query resource, which can be added to display in each node in the org chart. You can also add images and labels to the nodes.

**Properties**

The Properties box presents a node model for specifying the information you want to display in each node in the org chart.

### For heat map

![Chart Wizard - Heat Map Display](https://devnet.logianalytics.com/hc/article_attachments/4404901290391/chtwzd_dsply_htmp.gif)

**Resources**

Lists the resources in and related to the specified query resource, which can be used for the heat map.

**Area**

Lists the groups of the heat map. There should be at least one group.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
   Moves the selected group one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
   Moves the selected group one step down.
* **Color By**  
   Specifies whether to color by a group.
* **Label By**  
   Specifies whether to show the values of a group in the innermost rectangles.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog) dialog to define how to group information.
* **Special Function**  
   Opens the [Special Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010032742-Special-Function-Dialog) dialog to define special function to a group.
* **Order/Select N**   
   Opens the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010031322-Group-Options-Dialog) dialog to specify the sort order of the group values and define the number of the group values to display in the heat map.

**Property**

Lists the summaries added to calculate data based on the lowest group of the heat map.

* **Size By**  
   Specifies to use the summary to determine the size of the rectangles.
* **Color By**  
   Specifies to use the summary to determine the fill color of the rectangles.
* **Label By**  
   Specifies whether to show the values of a summary in the innermost rectangles.

## Filter

Specifies to filter data displayed on the chart. This screen is available only when you create a chart, and it contains the same options as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Chart Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404909243927/chtwzd_fltr.gif)

## Layout

Specifies the layout of the chart elements. Some layout options may not be available for certain chart types. For details about the options, [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010063601-Inserting-Charts-in-a-Report#Layout).

![Chart Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404909243159/chtwzd_layout.gif)

## Style

Specifies the style of the chart.

![Chart Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404909244183/chtwzd_styl.gif)

**Style**

Specifies the style of the chart.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the chart.

**Inherit Style**

Specifies whether to make the chart take the style of its parent. This options is available only when you edit a chart and the chart is inserted into a banded object.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500010067381-Page-Setup-Dialog) dialog to specify page properties. Available only when you create a chart.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029942-Chart-Iterator-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029902-Choose-Data-Dialog)
