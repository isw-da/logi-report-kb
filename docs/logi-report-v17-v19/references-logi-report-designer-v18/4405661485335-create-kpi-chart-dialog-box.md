---
title: "Create KPI Chart Dialog Box"
id: 4405661485335
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661485335-Create-KPI-Chart-Dialog-Box
updated_at: 2022-01-27T20:36:19Z
---

# Create KPI Chart Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661484311-Create-Geographic-Map-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664440983-Create-Query-s-Username-and-Password-Dialog-Box)

# Create KPI Chart Dialog Box

You can use the Create KPI Chart dialog box to [insert a KPI chart into a KPI](https://devnet.logianalytics.com/hc/en-us/articles/4405661382551-Working-with-KPIs). This topic describes the options in the dialog box.

Designer displays the Create KPI Chart dialog box when you right-click in the blank area of a KPI and select Insert KPI Chart from the shortcut menu.

The dialog box contains the following screens:

* [Data Screen](#Data)
* [Type Screen](#Type)
* [Display Screen](#Display)
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

## Data Screen

This screen shows that the KPI chart inherits the dataset bound with the KPI. You cannot change the dataset.

![Create KPI Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/4420402506007/crtkpicht_dt.gif)

## Type Screen

Use this screen to specify the type of the KPI chart. You can create a KPI chart in any of the following 2-D types: Bar, Bench, Line, Area, Pie, and Bullet. See [Chart Types](https://devnet.logianalytics.com/hc/en-us/articles/4405664391703-Chart-Types) for more information about the chart types.

![Create KPI Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/4420394841623/crtkpicht_type.gif)

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
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif)**Remove button**  
  Select to delete the specified chart type from the Chart Type Groups box.

## Display Screen

Use this screen to specify the data to display in the chart.

![Create KPI chart - Display](https://devnet.logianalytics.com/hc/article_attachments/4420410814231/crtkpicht_dsply.gif)

**Title**

Specify the title of the chart.

**Resources**

This box lists the resources in and related to the bound business view, which you can use for the chart. You can also [create dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/4405661937559-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) to use in the chart.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif)**Add button**

Select to move the specified field in the Resources box to the chart axis.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420394644119/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the chart.

**Category**/**Series**

This box lists the field that you add to display on the category/series axis of the chart.

For a real time chart, if you do not specify the category field, Designer displays the text "Use System Refresh Time" in the Category box by default, meaning Designer uses the time at which the chart refreshes itself as the category value. Designer disables the Series box in this case.

* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664591383-User-Defined-Group-Dialog-Box) to define how to group information.
* **Order/Select N**   
  Select to open the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661493527-Category-Options-Dialog-Box) or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661699223-Series-Options-Dialog-Box) to specify the sort order of the category or series values and define the number of the category or series values to show in the chart.

**Show Values**

This box lists the values that you add to show in the chart.

* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420394656407/btn_edit.gif)**Edit button**  
  Select to open the [Edit Additional Value dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664454935-Edit-Additional-Value-Dialog-Box) to edit an additional value. Designer enables this button only when you select a constant value or an average value in the Show Values box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**  
  Select to move the specified value higher in the display order.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified value lower in the display order.

**Motion Bar for Playable Chart**

Designer enables this option only when the KPI chart is of the single bar or bench type. Select it and then add a field as the motion field to make the chart a motion chart. A motion field can only be of the Integer, Date, or Time data type.

* **Special Function**  
  Designer enables this button when the motion field is of the Date data type. Select it to open the [Special Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661724823-Special-Function-Dialog-Box) to define special function to the motion field.

**Real Time**

Designer enables this option only when the KPI chart is of the single bar, bench, line, or area type. Select it to run the chart in real time mode.

* **Use System Time for Category**  
  Select to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
  Specify the time interval at which the chart gets data and refreshes itself automatically.
* **Show Most Recent N Points**  
  Specify the number of points to keep for the real time data in the chart.
* **Incremental Fetch**  
  Select to open the [Unique Key dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661742743-Unique-Key-Dialog-Box) to configure a unique key for the real time chart.

## Layout Screen

Use this screen to specify the layout of the chart elements. Designer does not display some options for certain chart types. For more information about the options, [select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664387479-Inserting-Charts-in-a-Report#Layout).

![Create KPI chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/4420402507415/crtkpicht_layout.gif)

## Style Screen

Use this screen to specify the style of the chart.

![Create KPI chart - Style](https://devnet.logianalytics.com/hc/article_attachments/4420402507671/crtkpicht_sty.gif)

**Style**

This box lists the styles that you can apply to the chart. Select the style for the chart.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the chart.

**Inherit Style**

Select to apply the style of the parent KPI to the KPI chart.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661484311-Create-Geographic-Map-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664440983-Create-Query-s-Username-and-Password-Dialog-Box)
