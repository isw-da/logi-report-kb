---
title: "Create KPI Chart Dialog Box"
id: 5735528774039
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735528774039-Create-KPI-Chart-Dialog-Box
updated_at: 2022-11-02T08:16:37Z
---

# Create KPI Chart Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513407639-Create-Geographic-Map-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522220695-Create-Query-s-Username-and-Password-Dialog-Box)

# Create KPI Chart Dialog Box

You can use the Create KPI Chart dialog box to [insert a KPI chart into a KPI](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs). This topic describes the options in the dialog box.

Designer displays the Create KPI Chart dialog box when you right-click in the blank area of a KPI and select Insert KPI Chart from the shortcut menu.

The dialog box contains the following screens:

* [Data Screen](#Data)
* [Type Screen](#Type)
* [Display Screen](#Display)
* [Layout Screen](#Layout)
* [Style Screen](#Style)

Designer displays these buttons in all the screens:

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

## Data Screen

This screen shows that the KPI chart inherits the dataset bound with the KPI. You cannot change the dataset.

![Create KPI Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/9898515898903/crtkpicht_dt.gif)

## Type Screen

Use this screen to specify the type of the KPI chart. You can create a KPI chart in any of the following 2-D types: Bar, Bench, Line, Area, Pie, and Bullet. See [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/5735527491351-Chart-Types) for more information about the chart types.

![Create KPI Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/9898532315927/crtkpicht_type.gif)

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
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
  Select to delete the specified chart type from the Chart Type Groups box.

## Display Screen

Use this screen to specify the data to display in the KPI chart.

![Create KPI chart - Display](https://devnet.logianalytics.com/hc/article_attachments/9898515907351/crtkpicht_dsply.gif)

**Title**

Specify the title of the KPI chart.

**Resources**

This box lists the available data fields that you can use for the KPI chart. You can also [create dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report) to use in the KPI chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to move the specified field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the KPI chart.

**Category**/**Series**

This box lists the field that you add to display on the category/series axis of the KPI chart.

For a real time chart, if you do not specify the category field, Designer displays the text "Use System Refresh Time" in the Category box by default, meaning Designer uses the time at which the chart refreshes itself as the category value. Designer disables the Series box in this case.

* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544779031-User-Defined-Group-Dialog-Box) to define how to group information.
* **Order/Select N**   
  Select to open the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522351383-Category-Options-Dialog-Box) or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735531110807-Series-Options-Dialog-Box) to specify the sort order of the category or series values and define the number of the category or series values to show in the chart.

**Show Values**

This box lists the values that you add to show in the KPI chart.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif)**Edit button**  
  Designer enables this button when you select a constant value or an average value in the Show Values box. Select it to open the [Edit Additional Value dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565591447-Edit-Additional-Value-Dialog-Box) to edit the value.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**  
  Select to move the specified value higher in the display order.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified value lower in the display order.

**Motion Bar for Playable Chart**

Designer enables this option only when the KPI chart is of the single bar or bench type. Select it and then add a field as the motion field to make the chart a motion chart. A motion field can only be of the Integer, Date, or Time data type.

* **Special Function**  
  Designer enables this button when the motion field is Date data type. Select it to open the [Special Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735531370903-Special-Function-Dialog-Box) to define special function to the motion field.

**Real Time**

Designer enables this option only when the KPI chart is of the single bar, bench, line, or area type. Select it to run the chart in real time mode.

* **Use System Time for Category**  
  Select to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
  Specify the time interval at which the chart gets data and refreshes itself automatically.
* **Show Most Recent N Points**  
  Specify the number of points to keep for the real time data in the chart.
* **Incremental Fetch**  
  Select to open the [Unique Key dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515926551-Unique-Key-Dialog-Box) to configure a unique key for the real time chart.

## Layout Screen

Use this screen to specify the layout of the chart elements. Designer does not display some options for certain chart types. For more information about the options, [select here](https://devnet.logianalytics.com/hc/en-us/articles/5735512245143-Inserting-Charts-in-a-Report#Layout).

![Create KPI chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/9898515909783/crtkpicht_layout.gif)

## Style Screen

Use this screen to specify the style of the KPI chart.

![Create KPI chart - Style](https://devnet.logianalytics.com/hc/article_attachments/9898532327191/crtkpicht_sty.gif)

**Style**

This box lists the styles you can apply. Select the style for the KPI chart.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the KPI chart.

**Inherit Style**

Select to apply the style of the parent KPI to the KPI chart.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513407639-Create-Geographic-Map-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522220695-Create-Query-s-Username-and-Password-Dialog-Box)
