---
title: "Format Platform Dialog Box Properties"
id: 28891652870541
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891652870541-Format-Platform-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:38Z
source_host: docs-report.zendesk.com
---
# 
Format Platform Dialog Box Properties

You can use the Format Platform dialog box to format the platform of a chart. This topic describes the properties in the dialog box.

This topic contains the following sections:

- General Tab Properties

- Border Tab Properties

- Data Tab Properties

- Others Tab Properties

You see these elements on all the tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
General Tab Properties

Specify the general properties of the chart platform. 

Name

Specify the display name of the platform.

Show NLS Value

Select to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

Position

- 
absolute

Server locates the component  at the position that you specify by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance, it is not affected when you insert text before it.
 The position of an object in a banded object can only be absolute.

- 
rotation(deg)

Specify the rotation degree of the text. 

- 
static

Server positions the component at the location where you insert it. The X and Y coordinate properties are disabled. You cannot move the component to another position other than by moving its insertion point. This can happen when the text flow preceding the insertion point expands.

- 
relative

Server positions the component at an offset to the position at which you insert it. The offset is determined by the X and Y coordinate property values. This value is not available for some types of components.

 Server displays relative in the default value list for the Position option, when the current position is relative. However, relative is no longer available in the value list after you apply static or absolute and reenter the dialog box.

X

Specify the X coordinate of the platform.

Y

Specify the Y coordinate of the platform.

Width

Specify the width of the platform.

Height

Specify the height of the platform.

Fill Type

Specify a type for filling the platform.

Color

Specify the background color of the platform.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

Transparency

Specify the transparency of the chart background color.

Show Legend

Select true to show the legend.

## 
Border Tab Properties

Specify the border properties of the chart platform.

Line Style

Select the line style of the border.

Border Type

Select the type of the border.

Color

Specify the color of the border.

Transparency

Specify the transparency for the color of the border.

Thickness

Specify the thickness of the border, in inches.

## 
Data Tab Properties

You can use this tab to view and configure properties of the chart data. 

Sort Category

Specify the sorting order for the category field values.

Sort Series

Specify the sorting order for the series field values.

Reverse Category

Select true to reverse the category field value sequence.

Reverse Series

Select true to reverse the series field value sequence.

Category Start Offset

Specify the starting offset of the categories.

Category End Offset

Specify the ending offset of the categories.

Series Start Offset

Specify the starting offset of the series.

Series End Offset

Specify the ending offset of the series.

Category Value Encoding

Specify the encoding format for values on the category axis. Formats here usually include BIG5, EUCJIS, GBK, UTF8, and XXXXX.

Series Value Encoding

Specify the encoding format for values on the series axis. Formats here usually include BIG5, EUCJIS, GBK, UTF8, and XXXXX.

Swap Data Group

Select true to display values from different data fields by switching data between the category and series axes or between the category and values axes.

## 
Others Tab Properties

You can use this tab to view and configure some miscellaneous settings.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

TOC Anchor

Select true if you want to add the object to the TOC tree in the TOC Browser.

Suppress When No Records

Select true if you want to hide the object in the report when no record returns to its parent data component. 

Export to XLS

Select true if you want to export the object when you save the report as an XLS file (make sure to check Data Format in the Export dialog box).

Export to CSV

Select true if you want to export the object when you save the report as a TXT file with Delimited Format.
