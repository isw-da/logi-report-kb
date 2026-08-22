---
title: "Create Chart Dialog"
id: 1500010030062
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010030062-Create-Chart-Dialog
updated_at: 2021-07-24T10:39:04Z
---

# Create Chart Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065101-Create-Banded-Object-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030082-Create-Connection-Dialog)

# Create Chart Dialog

The Create Chart wizard helps you to [create a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063601-Inserting-Charts-in-a-Report) in a report. It appears when you select Insert > Chart, or drag a chart type from the Components panel into a report.

The wizard varies with the data resource type used to create the chart: [business view](#BV) or [query resource](#Query).

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating the table and closes this dialog.

**Cancel**

Does not retain changes and closes this dialog.

**Help**

Displays the help document about this feature.

## Create Chart - Business View Based

When the wizard is used for creating a chart using a business view, it consists of the following screens: [Data](#BVData), [Type](#BVType), [Display](#BVDisplay), [Filter](#BVFilter), [Layout](#BVLayout) and [Style](#BVStyle).

### Data

The screen lists all the predefined business views in the current catalog. Select the one using which to create the chart.

![Create Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/4404909235863/crtcht_dt_bv.gif)

**Inherit from the Parent**

Specifies to inherit data from the business view used by the parent object. Available only when the chart is to be inserted into any of the following panels in a banded object in a web report: banded header panel, banded footer panel, group header panel and group footer panel.

### Type

Specifies the type of the chart. You can refer to the section [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500010029042-Chart-Types) which describes each of the chart type in detail. When using business view as the chart data source, only the 2-D chart types are supported.

![Create Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/4404901281687/crtcht_type_bv.gif)

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
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Removes the selected chart type from the Chart Type Groups box.

### Display

Specifies the data to display on the chart. This screen differs according to the chart type: [common chart types](#BVCommon), [organization chart](#BVOrg) or [heat map](#BVHeatMap).

#### For common chart types

![Create Chart - Display](https://devnet.logianalytics.com/hc/article_attachments/4404901281943/crtcht_dsply_bv.gif)

**Title**

Specifies the title of the chart.

**Resources**

Lists the resources in and related to the specified business view, which can be used to create the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)

Removes the selected field from the chart.

**Category/Series box**

Lists the field to display on the category/series axis of the chart. For a gauge chart, you can select the Advanced button to show or hide the Category/Series box.

For a real time chart, if no category field is specified, the text Use System Refresh Time will be automatically displayed in the Category box, namely the time at which the chart refreshes itself will be used as the category value; the series axis will be disabled.

* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog) dialog to define how to group information.
* **Order/Select N**   
   Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010065241-Category-Options-Dialog) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010032382-Series-Options-Dialog) dialog to specify the sort order of the category or series values and define the number of the category or series values to show on the chart.

**Show Value box**

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

![Create Chart - Org Display](https://devnet.logianalytics.com/hc/article_attachments/4404909236119/crtcht_dsply_org_bv.gif)

**Node**

Specifies the field the values of which to display as the nodes in the org chart.

**Parent**

Specifies the field which shows the "reporting to" relationship among the node field values.

**Resources**

Lists the resources in and related to the specified business view, which can be added to display in each node in the org chart. You can also add images and labels to the nodes.

**Properties**

The Properties box presents a node model for specifying the information you want to display in each node in the org chart.

#### For heat map

![Create Chart - Heat Map Display](https://devnet.logianalytics.com/hc/article_attachments/4404909236375/crtcht_dsply_htmp_bv.gif)

**Resources**

Lists the resources in and related to the specified business view, which can be used to create the heat map.

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

Specifies to filter data displayed in the chart. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Create Chart - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404909236631/crtcht_fltr_bv.gif)

### Layout

Specifies the layout of the chart elements. Some layout options may not be available for certain chart types. For details about the options, [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010063601-Inserting-Charts-in-a-Report#Layout).

![Create Chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404901282199/crtcht_layout.gif)

### Style

Specifies the style of the chart.

![Create Chart - Style](https://devnet.logianalytics.com/hc/article_attachments/4404901282583/crtcht_sty.gif)

**Style**

Specifies the style of the chart.

**Preview**

Displays the selected style and layout effects.

**Inherit Style**

Specifies whether to make the chart take the style of its parent. This options is available only when the chart is to be inserted in a banded object in a page report.

## Create Chart - Query Based

When the wizard is used for creating a chart using a query resource, it consists of the following screens: [Data](#Data), [Type](#Type), [Display](#Display), [Filter](#Filter), [Layout](#Layout) and [Style](#Style).

### Data

Specifies the dataset using which to create the chart.

![Create Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/4404909236887/crtcht_dt.gif)

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the chart.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the chart.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog) if required.
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010030342-Dataset-Editor-Dialog) if required.
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

### Type

Specifies the type of the chart. You can refer to the section [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500010029042-Chart-Types) which describes each of the chart type in detail.

![Create Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/4404901282839/crtcht_type.gif)

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
* **Subtype box**  
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

### Display

Specifies the data to display on the chart. The screen differs according to the chart type: [common chart types](#Common), [organization chart](#Org) or [heat map](#HeatMap).

#### For common chart types

![Create Chart - Display](https://devnet.logianalytics.com/hc/article_attachments/4404909237143/crtcht_dsply.gif)

**Resources**

Lists the data fields in and related to the specified query resource, which can be used to create the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)

Adds the selected field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)

Removes the selected field from the chart.

**Category****/Series**

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
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500010065461-Edit-Additional-Value-Dialog) dialog to edit an additional value. Available only when a constant value or an average value is selected.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
   Moves the selected value one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
   Moves the selected value one step down.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
   Adds a new pair of Y Axis and Radius for the bubble chart.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
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

#### For organization chart

![Create Chart - Org Display](https://devnet.logianalytics.com/hc/article_attachments/4404901283095/crtcht_dsply_org.gif)

**Node**

Specifies the field the values of which to display as the nodes in the org chart.

**Parent**

Specifies the field which shows the "reporting to" relationship among the node field values.

**Resources**

Lists the resources in and related to the specified query resource, which can be added to display in each node in the org chart. You can also add images and labels to the nodes.

**Properties**

The Properties box presents a node model for specifying the information you want to display in each node in the org chart.

#### For heat map

Specifies the data displayed on the chart.

![Create Chart - Heat Map Display](https://devnet.logianalytics.com/hc/article_attachments/4404901283351/crtcht_dsply_htmp.gif)

**Resources**

Lists the resources in and related to the specified query resource, which can be used to create the heat map.

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

### Filter

Specifies to filter data displayed on the chart. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

![Create Chart - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404909237399/crtcht_fltr.gif)

### Layout

Specifies the layout of the chart elements. Some layout options may not be available for certain chart types. For details about the options, [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010063601-Inserting-Charts-in-a-Report#Layout).

![Create Chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404901282199/crtcht_layout.gif)

### Style

Specifies the style of the chart.

![Create Chart - Style](https://devnet.logianalytics.com/hc/article_attachments/4404901282583/crtcht_sty.gif)

**Style**

Specifies the style of the chart.

**Preview**

Displays the selected style and layout effects.

**Inherit Style**

Specifies whether to make the chart take the style of its parent. Available only when the chart is to be inserted into a banded object.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065101-Create-Banded-Object-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030082-Create-Connection-Dialog)
