---
title: "Data Format Dialog Box"
id: 28897985047309
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897985047309-Data-Format-Dialog-Box
updated_at: 2024-09-30T09:13:02Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Data Format Dialog Box

You can use the Data Format dialog box to specify the data format of the values in a chart. This topic describes the options in the dialog box.
    

Designer displays the Data Format dialog box when you select the ellipsis  to specify the data format for objects in a chart in the Report Inspector, and provides you with different options in the dialog box according to the different objects in the chart for which you specify to set the format.

When you use the Data Format dialog box to specify the data format for objects except the category axis (the X axis) in a chart, Designer displays the following options in the dialog box:

Category & Format

The two boxes list the category types and the formats of each category that Designer provides by default. Select a category and a format for this category, then select Add to add it as the format of the category. You can add only one format for each category.

| Category | Format | Description (Sample) |
| --- | --- | --- |
| Scale |  | Divides the value by hundreds, thousands, and so on. |
|  | Logarithm | Calculates ten to the power of the value. |
|  | Hundreds | Divides the value by one hundred. |
|  | Thousands | Divides the value by one thousand. |
|  | Millions | Divides the value by one million. |
|  | Billions | Divides the value by one billion. |
|  | Trillions | Divides the value by one trillion. |
| Number |  | Re-formats the number value (original example: 123456) |
|  | 0 | Formats a decimal number to an integer (123456). |
|  | #,##0 | Formats a decimal number to a digit grouped integer (123,456). |
|  | #,##0;-#,##0 | Formats a decimal number to a digit grouped integer. A minus sign is used as the negative prefix (123,456/-123,456). |
|  | 0.00 | Formats a decimal number to a fixed-point number retaining 2 digits after decimal separator (123456.00). |
|  | #,##0.00 | Formats a decimal number to a digit grouped number retaining 2 digits after decimal separator (123,456.00). |
|  | #,##0.00;-#,##0.00 | Formats a decimal number to a digit grouped number retaining 2 digits after decimal separator. A minus sign is used as the negative prefix (123,456.00/-123,456.00). |
|  | 0.00E00 | Formats a decimal number to a number in scientific notation. The mantissa is often in the range 1.0 Properties

This text box shows properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select Add to add it as the format of the category.

Auto Scale in Number

Specify whether to automatically scale the Number values  that fall into the two ranges:

- When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).

- When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property on the chart in the Report Inspector for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

Sample

This box displays a sample for the selected format.

Stack

This box lists all the formats that you select from different categories.

Add

Select to add a format to the Stack box.

Remove

Select to remove the specified format from the Stack box.

Apply

Select to apply the specified format to the object.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

When you use the Data Format dialog box to specify the data format for the category axis (the X axis) in a chart, Designer displays the following tabs in the dialog box (to open the dialog box, locate Chart Object in the Report Inspector, select the ellipsis  beside the value text box  of the Category Format property in the Data group):

- Major Label Tab

- Minor Label Tab

Designer displays these buttons in all the tabs:

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
Major Label Tab

Use this tab to specify the data format of the major tick mark labels on the axis.

Category & Format

These two boxes list the category types and the formats of each category that Designer provides by default. Select a category and a format for this category, then select Add to add it as the format of the category. You can add only one format for each category.

Properties

This text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select Add to add it as the format of the category.

Auto Scale in Number

Specify whether to automatically scale the Number values that fall into the two ranges:

- When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).

- When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property on the chart in the Report Inspector for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

Sample

This box displays a sample for the selected format.

Stack

This box lists all the formats that you select from different categories.

Add

Select to add a format to the Stack box.

Remove

Select to remove the specified format from the Stack box.

Apply

Select to apply the specified format to the major tick mark labels.

Truncate

Select to truncate the label text that is longer than 10 characters and only show the first 7 characters.

## 
Minor Label Tab

Use this tab to specify the data format of the minor tick mark labels on the axis.

Correlate with Major Label

Select to apply the data format that you specify for the major tick mark labels to the minor tick mark labels. Clear it if you want to apply separate data format for the minor tick mark labels.

Category & Format

These two boxes list the category types and the formats of each category that Designer provides by default. Select a category and a format for this category, then select Add to add it as the format of the category. You can add only one format for each category.

Properties

This text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select Add to add it as the format of the category.

Auto Scale in Number

Specify whether to automatically scale the Number values that fall into the two ranges:

- When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).

- When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property on the chart in the Report Inspector for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

Sample

This box displays a sample for the selected format.

Stack

This box lists all the formats that you select from different categories.

Add

Select to add a format to the Stack box.

Remove

Select to remove the specified format from the Stack box.

Apply

Select to apply the specified format to the minor tick mark labels.

Previous Topic  Next Topic
