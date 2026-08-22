---
title: "Data Format Dialog Box Properties"
id: 5741457762839
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741457762839-Data-Format-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:19Z
---

# Data Format Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741422604311-Customize-Gauge-Angle-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741444402455-Edit-Additional-Value-Dialog-Box-Properties)

# Data Format Dialog Box Properties

This topic describes how you can use the Data Format dialog box to specify the data format for a chart. The dialog box varies according to different objects to which the data format will apply: [the category axis](#Axis) and [objects other than the category axis](#Other).

Server displays the dialog box when you select the ellipsis button ![Data Format](https://devnet.logianalytics.com/hc/article_attachments/9905656493591/btn_chsr1.gif) in the value cell of the Data Format property in the Inspector panel.

---

When you open the dialog box to specify the data format for the category axis (the X axis) in a chart, it consists of two tabs: [Major Label](#Majorfmt) and [Minor Label](#Minorfmt).

You see these elements on both tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## Major Label

Specify the data format of the major tick mark labels on the axis.

![Data Format dialog - Major Label](https://devnet.logianalytics.com/hc/article_attachments/9905733980183/dtfmt_major.gif)

To specify a format, first select a category from the Category box, then select the required format of this category from the Format box. Server displays the selected format in the Properties text box. You can further edit the format if you want. Then, select **Add** to add the format to the Stack box. Repeat the steps to specify formats for other categories. You can define only one format for each category.

**Category & Format**

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
|  | 0.00E00 | Format a decimal number to a number in scientific notation. The mantissa is often in the range 1.0 <= x < 10.0, and the number of digit characters after the exponent character (E) gives the minimum exponent digit count (1.23E04). |
|  | ##0.0E0 | Format a decimal number to a number in scientific notation. The minimum number of integers in the mantissa is 1, and the number of digit characters after the exponent character (E) gives the minimum exponent digit count (12.34E3). |
|  | $0 | Format a decimal number to an integer, prefixed with a currency symbol $ ($123456). |
|  | $#,##0 | Format a decimal number to a digit grouped integer, prefixed with a currency symbol $ ($123,456). |
|  | $#,##0;-$#,##0 | Format a decimal number to a digit grouped integer, prefixed with a currency symbol $. Use a minus sign as the negative prefix ($123,456/-$123,456). |
|  | $0.00 | Format a decimal number to a fixed-point number retaining 2 digits after decimal separator, prefixed with a currency symbol $ ($123456.00). |
|  | $#,##0.00 | Format a decimal number to a digit grouped number retaining 2 digits after decimal separator, prefixed with a currency symbol $ ($123,456.00). |
|  | $#,##0.00;  -$#,##0.00 | Format a decimal number to a digit grouped number retaining 2 digits after decimal separator, prefixed with a currency symbol $. A minus sign is used as the negative prefix ($123,456.00/-$123,456.00). |
|  | $0.00E00 | Format a decimal number to a number in scientific notation, prefixed with a currency symbol $. The mantissa is often in the range 1.0 <= x < 10.0, and the number of digit characters after the exponent character (E) gives the minimum exponent digit count ($1.23E$04). |
|  | $##0.0E0 | Format a decimal number to a number in scientific notation, prefixed with a currency symbol $. The minimum number of integers in the mantissa is 1, and the number of digit characters after the exponent character (E) gives the minimum exponent digit count ($12.34E$3). |
|  | 0% | Format a decimal number to percentage: multiply by 100 and show as an integer percentage (12%). |
|  | 0.00% | Format a decimal number to percentage: multiply by 100 and show as a fixed-point number percentage retaining 2 digits after decimal separator (12.34%). |
|  | Note icon   * The number of 0 in a pattern indicates the minimum digits, and show 0 if that digit is zero. The number of # after the decimal point in a pattern indicates the maximum digits of decimal, and zero shows as absent. * Use single quotation marks to quote special characters in a prefix or suffix, for example, '#'# formats 123 to #123. To create the single quote itself, use two in a row: # o''clock. | |
| Date/Time |  | Reformat the date/time value (for example, Wednesday, December 25, 00:00:00 GMT-08:00 2021) |
|  | G | Format a date to era designator (AD). |
|  | yyyy | Format a date to year (2021). |
|  | yy | Format a date to year in short form (21). |
|  | yyyy G | Format a date to year, tagged with era designator (2021 AD) |
|  | MM | Format a date to month in year, in number format (12). |
|  | MMM | Format a date to month in year, in the abbreviated form (Dec). |
|  | MMMMMMMM | Format a date to month in year, in the full form (December). |
|  | dd/MM/yy | Format a date to a simple date form (25/12/21). |
|  | dd-MMM-yy | Format a date to a simple date form (25-Dec-21). |
|  | dd-MMM | Format a date to a simple date form (25-Dec). |
|  | MMM-yy | Format a date to a simple date form (Dec-21). |
|  | MMM yyyy | Format a date to a simple date form (Dec 2021). |
|  | dd | Format a date to day in month (25). |
|  | DDD | Format a date to day in year (359). |
|  | ww | Format a date to week in year (52). |
|  | W | Format a date to week in month (4). |
|  | EEE | Format a date to day in week, in short form (Wed). |
|  | EEEEEE | Format a date to day in week (Wednesday). |
|  | HH | Format a date to hour in day, 0~23 (00). |
|  | kk | Format a date to hour in day, 1~24 (24). |
|  | KK a | Format a date to hour in am/pm, 0~11, with am/pm marker (00 AM) |
|  | hh a | Format a date to hour in am/pm, 1~12, with am/pm marker (12 AM) |
|  | mm | Format a date to minute in hour (00). |
|  | hh:mm a | Format a date to hour in am/pm, 1~12, minutes in an hour, with am/pm marker (12:00 AM). |
|  | ss | Format a date to second in minute (00). |
|  | hh:mm:ss | Format a date to hour in am/pm 1~12, minutes in an hour, and second in minute (12:00:00). |
|  | hh:mm:ss a | Format a date to hour in am/pm 1~12, minutes in an hour, and second in minute, with am/pm marker (12:00:00 AM). |
|  | mm:ss | Format a date to minute in hour and second in minute (00:00). |
|  | MMMMM dd yyyy G (EEEEEE) hh:mm:ss aa z | Format a date to a full form date, which contains month in year (in full form), days in a month, year, era designator, day in week (in the full form), hour in a day, 1~12, minutes in an hour, second in minute, am/pm marker, and time zone (December 25, 2021 AD (Wednesday) 12:00:00 AM GMT-08:00). |
|  | Note icon   * Logi Report treats any characters in the pattern that are not in the ranges of ['a'..'z'] and ['A'..'Z'] as quoted text. For instance, characters such as ':', '.', ' ', '#' and '@' appear in the resulting time text even you did not embrace them within single quotes. * You cannot add a pattern containing any invalid pattern letter to the filter stack. | |
| Text |  | Specify the length of the value. |
|  | Default Length | Use the length of the string Default Length, which is 14, as the length of the string. Server hides any letters that exceed this length. You can modify this string, adding or deleting letters to increase or decrease the length limit. For example, type Teddy, the label displayed may probably be Wed D, which originally could be Wed December 25 2021. If you want to show all, you can type Teddy is a lovely bear!, where the length is longer than the length of string Wed December 25 2021. |
| Mapping |  | Map a new value to one or more values. |
|  | One-to-one Mapping | Map a new value to one value. Type the argument number that you want to replace, and then specify the new value in the Map to box. For example, if you want to replace the second data label on the X axis, which is Thu Jul 04 2021, with a new string US National Day, just type "2" in the Argument# box, type "US National Day" in the Map to box, and then select **Add** to add it to the Filter Stack. If you want to map more values, repeat this procedure. |
|  | Range Mapping | Map a new value to a range of values. Type the argument numbers to define the range you want to map together, and then specify the new value in the Map to box. For example, if you want to replace the data labels from the second one to the fifth with a new name My Holiday, just type "2" in the first Argument# box and "5" in the second Argument# box, then type "My Holiday" in the Map to box, and then select **Add** to add it to the Stack. If you want to map ranges that are not consecutive, repeat this procedure. |
|  | Text Mapping | Change the data in the axis data label to a customized string. For example, if you want to change "Chen" in the first data label of the X axis to "Jinfonet", type "Chen" in the Original Text box, type "Jinfonet" in the Map to box, and then select **Add** to add it to the Stack. You can only change the data one by one. Make sure that your spelling in the Original Text box is exactly the same as the data shown in the axis label. |
|  | Prefix | Add a string before the text in the data label of the axis. For example, if you want to add "NA" before the text in the data label of the X axis, type "NA" in the Map to box, and select **Add** to add it to the Stack. |
|  | Suffix | Add a string behind the text in the data label of the axis. For example, if you want to add "NA" behind the text in the data label of the X axis, type "NA" in the Map to box, and select **Add** to add it to the Stack. |
|  | Note icon The data labels along each axis count from 0, which means the number of the first data label you see on the axis will be 0, the second will be 1, the third will be 2, and so on. | |

**Properties**

Specify the properties for the selected format.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The default value **auto** means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#AutoScale). When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Logi Report will ignore the **Auto Scale in Number** setting.

**Sample**

Server displays the selected format effect.

**Stack**

Server lists all the formats that you selected from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove a format from the Stack box.

**Apply**

Select to apply the specified format to values in the chart.

## Minor Label

Specify the data format of the minor tick mark labels on the axis.

![Data Format dialog - Major Label](https://devnet.logianalytics.com/hc/article_attachments/9905755813655/dtfmt_minor.gif)

To specify a format, first select a category from the Category box, then select the required format of this category from the Format box. Server displays the selected format in the Properties text box. You can further edit the format if you want. Then, select **Add** to add the format to the Stack box. You can also select **Correlate with Major Label** to specify that the data format of the minor tick mark labels correlates with that of the major tick mark labels. Repeat the steps to specify formats for other categories. You can define only one format for each category.

**Correlate with Major Label**

Select if you want the data format of the minor tick mark labels to correlate with that of the major tick mark labels automatically. Only when you don't select this property can the format properties of the minor tick mark labels take effect.

**[Category & Format](#DataFormat)**

Server lists the category types and formats available for each category.

**Properties**

Specify the properties for the selected format.

**Auto Scale in Number**

Specify whether to [automatically scale big and small numbers](#AutoScale) in the tick mark labels.

**Sample**

Server displays the selected format effect.

**Stack**

Server lists all the formats that you selected from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove a format from the Stack box.

**Apply**

Select to apply the specified format to values in the chart.

---

When you open the dialog box to specify the data format for objects other than the category axis (the X axis) in a chart, it looks like this:

![Data Format dialog](https://devnet.logianalytics.com/hc/article_attachments/9905734037271/dtfmt.gif)

To specify a format, first select a category from the Category box, then select the required format of this category from the Format box. Server displays the selected format in the Properties text box. You can further edit the format if you want. Then, select **Add** to add the format to the Stack box. Repeat the steps to specify formats for other categories. You can define only one format for each category.

**[Category & Format](#DataFormat)**

Server lists the category types and formats available for each category.

**Properties**

Specify the properties for the selected format.

**Auto Scale in Number**

Specify whether to [automatically scale big and small numbers](#AutoScale). Available when the chart object can be bound with a data field.

**Sample**

Server displays the selected format effect.

**Stack**

Server lists all the formats that you selected from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove a format from the Stack box.

**Apply**

Select to apply the specified format to values in the chart.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741422604311-Customize-Gauge-Angle-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741444402455-Edit-Additional-Value-Dialog-Box-Properties)
