---
title: "Data Format Dialog Box Properties"
id: 28891658457101
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891658457101-Data-Format-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:42Z
source_host: docs-report.zendesk.com
---
# 
Data Format Dialog Box Properties

This topic describes how you can use the Data Format dialog box to specify the data format for a chart. The dialog box varies according to different objects to which the data format will apply: the category axis and objects other than the category axis.

Server displays the dialog box when you select the ellipsis button  in the value cell of the Data Format property  in the Inspector panel.

When you open the dialog box to specify the data format for the category axis (the X axis) in a chart, it consists of two tabs: Major Label and Minor Label.

You see these elements on both tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

## 
Major Label

Specify the data format of the major tick mark labels on the axis.

To specify a format, first select a category from the Category box, then select the required format of this category from the Format box. Server displays the selected format in the Properties text box. You can further edit the format if you want. Then, select Add to add the format to the Stack box. Repeat the steps to specify formats for other categories. You can define only one format for each category.

Category & Format

Server lists the category types and formats available for each category.

| Category | Format | Description (Sample) |
| --- | --- | --- |
| Scale |  | Divide the value by hundreds, thousands, and so on. |
|  | Logarithm | Calculate ten to the power of the value. |
|  | Hundreds | Divide the value by one hundred. |
|  | Thousands | Divide the value by one thousand. |
|  | Millions | Divide the value by one million. |
|  | Billions | Divide the value by one billion. |
|  | Trillions | Divide the value by one trillion. |
| Number |  | Reformat the number value (original example: 123456) |
|  | 0 | Format a decimal number to an integer (123456). |
|  | #,##0 | Format a decimal number to a digit grouped integer (123,456). |
|  | #,##0;-#,##0 | Format a decimal number to a digit grouped integer. Use a minus sign as the negative prefix (123,456/-123,456). |
|  | 0.00 | Format a decimal number to a fixed-point number retaining 2 digits after decimal separator (123456.00). |
|  | #,##0.00 | Format a decimal number to a digit grouped number retaining 2 digits after decimal separator (123,456.00). |
|  | #,##0.00;-#,##0.00 | Format a decimal number to a digit grouped number retaining 2 digits after decimal separator. Use a minus sign as the negative prefix (123,456.00/-123,456.00). |
|  | 0.00E00 | Format a decimal number to a number in scientific notation. The mantissa is often in the range 1.0 Properties

Specify the properties for the selected format.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart. When you set the property to true, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Report will ignore the Auto Scale in Number setting.

Sample

Server displays the selected format effect.

Stack

Server lists all the formats that you selected from different categories.

Add

Select to add a format to the Stack box.

Remove

Select to remove a format from the Stack box.

Apply

Select to apply the specified format to values in the chart.

## 
Minor Label

Specify the data format of the minor tick mark labels on the axis.

To specify a format, first select a category from the Category box, then select the required format of this category from the Format box. Server displays the selected format in the Properties text box. You can further edit the format if you want. Then, select Add to add the format to the Stack box. You can also select Correlate with Major Label to specify that the data format of the minor tick mark labels correlates with that of the major tick mark labels. Repeat the steps to specify formats for other categories. You can define only one format for each category.

Correlate with Major Label

Select if you want the data format of the minor tick mark labels to correlate with that of the major tick mark labels automatically. Only when you don't select this property can the format properties of the minor tick mark labels take effect.

Category & Format

Server lists the category types and formats available for each category.

Properties

Specify the properties for the selected format.

Auto Scale in Number

Specify whether to automatically scale big and small numbers in the tick mark labels. 

Sample

Server displays the selected format effect.

Stack

Server lists all the formats that you selected from different categories.

Add

Select to add a format to the Stack box.

Remove

Select to remove a format from the Stack box.

Apply

Select to apply the specified format to values in the chart.

When you open the dialog box to specify the data format for objects other than the category axis (the X axis) in a chart, it looks like this:

To specify a format, first select a category from the Category box, then select the required format of this category from the Format box. Server displays the selected format in the Properties text box. You can further edit the format if you want. Then, select Add to add the format to the Stack box. Repeat the steps to specify formats for other categories. You can define only one format for each category.

Category & Format

Server lists the category types and formats available for each category.

Properties

Specify the properties for the selected format.

Auto Scale in Number

Specify whether to automatically scale big and small numbers. Available when the chart object can be bound with a data field. 

Sample

Server displays the selected format effect.

Stack

Server lists all the formats that you selected from different categories.

Add

Select to add a format to the Stack box.

Remove

Select to remove a format from the Stack box.

Apply

Select to apply the specified format to values in the chart.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
