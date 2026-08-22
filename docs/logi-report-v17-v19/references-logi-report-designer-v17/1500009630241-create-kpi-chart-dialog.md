---
title: "Create KPI Chart Dialog"
id: 1500009630241
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630241-Create-KPI-Chart-Dialog
updated_at: 2021-07-24T16:04:53Z
---

# Create KPI Chart Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607562-Create-Geographic-Map-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630261-Create-Query-s-Username-and-Password-Dialog)

# Create KPI Chart Dialog

The Create KPI Chart wizard helps you [insert a KPI chart into a KPI](https://devnet.logianalytics.com/hc/en-us/articles/1500009629121-KPIs). It appears when you right-click in the blank area of a KPI and then select Insert KPI Chart from the shortcut menu.

The wizard contains the following screens: [Data](#Data), [Type](#Type), [Display](#Display), [Layout](#Layout) and [Style.](#Style)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Inserts the KPI chart into the KPI and closes the wizard.

**Cancel**

Does not retain changes and closes the wizard.

**Help**

Displays the help document about this feature.

## Data

Shows the business view bound to the KPI. The business view will be used as the data source of the KPI chart.

![Create KPI Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/4404916809623/crtkpicht_dt.gif)

## Type

Specifies the type of the chart. The following 2-D chart types are supported in KPI charts: Bar, Bench, Line, Area, Pie, and Bullet. You can refer to the section [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/1500009629021-Chart-Types) for the corresponding chart types in detail.

![Create KPI Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/4404904368151/crtkpicht_type.gif)

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
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
   Removes the selected chart type from the Chart Type Groups box.

## Display

Specifies the data to display on the chart.

![Create KPI chart - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904368407/crtkpicht_dsply.gif)

**Title**

Specifies the title of the chart.

**Resources**

Lists the resources in and related to the bound business view, which can be used to create the chart. You can also [create dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) to use in the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)

Adds the selected fields to be displayed in the chart.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)

Removes the selected fields from the chart if they are not required.

**Category**/**Series box**

Lists the field to display on the category/series axis of the chart.

For a real time chart, if no category field is specified, the text Use System Refresh Time will be automatically displayed in the Category box, namely the time at which the chart refreshes itself will be used as the category value; the series axis will be disabled.

* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009610722-User-Defined-Group-Dialog) dialog to define how to group information.
* **Order/Select N**   
   Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009630421-Category-Options-Dialog) dialog or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009633341-Series-Options-Dialog) dialog to specify the sort order of the category or series values and define the number of the category or series values to show on the chart.

**Show Values box**

Lists the values you want to show in the chart.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404904261015/btn_edit1.gif)  
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009630601-Edit-Additional-Value-Dialog) dialog to edit an additional value. Available only when a constant value or an average value is selected.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)  
   Moves the selected value one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)  
   Moves the selected value one step down.

**Motion Bar for Playable Chart**

Lists the field used as the motion field. A motion field can only be of the Integer, Date or Time data type. Available to single bar and bench charts in KPI charts only.

* **Special Function**  
   Opens the [Special Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009633701-Special-Function-Dialog) dialog to define special function to the motion field. Available only when the motion field is of the Date data type.

**Real Time**

Specifies to run the chart in real time mode. Available to single bar, bench, line, and area charts only.

* **Use System Time for Category**  
   Specifies to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
   Specifies the time interval at which the chart will get data and refresh itself automatically.
* **Show Most Recent N Points**  
   Specifies the number of points that will be kept for the real time data on the chart.
* **Incremental Fetch**  
   Opens the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009610762-Unique-Key-dialog-Dialog) dialog to configure a unique key for the real time chart.

## Layout

Specifies the layout of the chart elements. Some layout options may not be available for certain chart types. For details about the options, [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009628941-Inserting-Charts-in-a-Report#Layout).

![Create KPI chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904368919/crtkpicht_layout.gif)

## Style

Specifies the style of the chart.

![Create KPI chart - Style](https://devnet.logianalytics.com/hc/article_attachments/4404916810135/crtkpicht_sty.gif)

**Style**

Specifies the style of the chart.

**Preview**

Displays the selected style and layout effects.

**Inherit Style**

Specifies whether to make the chart take the style of the parent KPI.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607562-Create-Geographic-Map-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630261-Create-Query-s-Username-and-Password-Dialog)
