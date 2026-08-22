---
title: "Data Format Dialog"
id: 1500010030282
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010030282-Data-Format-Dialog
updated_at: 2021-07-24T10:39:01Z
---

# Data Format Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065321-Data-Buffer-Information-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030302-Data-Label-Editor-Dialog)

# Data Format Dialog

The Data Format dialog helps you to specify the data format of the values on a chart. It appears when you select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) to specify the data format for a chart platform or legend in the Report Inspector. The options in the dialog vary according to different sources it is opened from.

When you open the dialog to specify the data format for objects except the category axis (the X axis) in a chart, the options in the dialog are as follows.

![Data Format dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901272087/dtfmt.gif)

To specify a format, first select a category from the Category box, then select the required format of this category from the Format box. The selected format will be displayed in the Properties text box. You can further edit the format if you want. Then, select the **Add** button to add the format to the Stack box. Repeat the steps to specify formats for other categories. Only one format can be defined for each category.

The following are details about options in the dialog:

**Category & Format**

Lists the category types and formats available for each category.

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
|  | 0.00E00 | Formats a decimal number to a number in scientific notation. The mantissa is often in the range 1.0 <= x < 10.0, and the number of digit characters after the exponent character (E) gives the minimum exponent digit count (1.23E04). |
|  | ##0.0E0 | Formats a decimal number to a number in scientific notation. The minimum number of integer in the mantissa is 1, and the number of digit characters after the exponent character (E) gives the minimum exponent digit count (12.34E3). |
|  | $0 | Format a decimal number to an integer, prefixed with a currency symbol $ ($123456). |
|  | $#,##0 | Formats a decimal number to a digit grouped integer, prefixed with a currency symbol $ ($123,456). |
|  | $#,##0;-$#,##0 | Formats a decimal number to a digit grouped integer, prefixed with a currency symbol $. A minus sign is used as the negative prefix ($123,456/-$123,456). |
|  | $0.00 | Formats a decimal number to a fixed-point number retaining 2 digits after decimal separator, prefixed with a currency symbol $  ($123456.00). |
|  | $#,##0.00 | Formats a decimal number to a digit grouped number retaining 2 digits after decimal separator, prefixed with a currency symbol $ ($123,456.00). |
|  | $#,##0.00;  -$#,##0.00 | Formats a decimal number to a digit grouped number retaining 2 digits after decimal separator, prefixed with a currency symbol $. A minus sign is used as the negative prefix ($123,456.00/-$123,456.00). |
|  | $0.00E00 | Formats a decimal number to a number in scientific notation, prefixed with a currency symbol $. The mantissa is often in the range 1.0 <= x < 10.0, and the number of digit characters after the exponent character (E) gives the minimum exponent digit count ($1.23E$04). |
|  | $##0.0E0 | Formats a decimal number to a number in scientific notation, prefixed with a currency symbol $. The minimum number of integer in the mantissa is 1, and the number of digit characters after the exponent character (E) gives the minimum exponent digit count ($12.34E$3). |
|  | 0% | Formats a decimal number to percentage: multiplied by 100 and shown as an integer percentage (12%). |
|  | 0.00% | Formats a decimal number to percentage: multiplied by 100 and shown as a fixed-point number percentage retaining 2 digits after decimal separator (12.34%). |
|  | **Notes:**   * The number of 0 that appears in a pattern indicates the minimum digits, show 0 if that digit is zero. The number of # that appears after the decimal point in a pattern indicates the maximum digits of decimal, zero shows as absent. * Use ' (single quotation mark) to quote special characters in a prefix or suffix, for example, '#'# formats 123 to #123. To create the single quote itself, use two in a row: # o''clock. | |
| Date/Time |  | Re-formats the date/time value (For example, Wednesday, December 25, 00:00:00 GMT-08:00 2002) |
|  | G | Formats a date to era designator (AD). |
|  | yyyy | Formats a date to year (2002). |
|  | yy | Formats a date to year in short form (02). |
|  | yyyy G | Formats a date to year, tagged with era designator (2002 AD) |
|  | MM | Formats a date to month in year, shown in number format (12). |
|  | MMM | Formats a date to month in year, shown in the abbreviated form (Dec). |
|  | MMMMMMMM | Formats a date to month in year, shown in the full form (December). |
|  | dd/MM/yy | Formats a date to a simple date form (25/12/02). |
|  | dd-MMM-yy | Formats a date to a simple date form (25-Dec-02). |
|  | dd-MMM | Formats a date to a simple date form (25-Dec). |
|  | MMM-yy | Formats a date to a simple date form (Dec-02). |
|  | MMM yyyy | Formats a date to a simple date form (Dec 2002). |
|  | dd | Formats a date to day in month (25). |
|  | DDD | Formats a date to day in year (359). |
|  | ww | Formats a date to week in year (52). |
|  | W | Formats a date to week in month (4). |
|  | EEE | Formats a date to day in week, in short form (Wed). |
|  | EEEEEE | Formats a date to day in week (Wednesday). |
|  | HH | Formats a date to hour in day, 0~23 (00). |
|  | kk | Formats a date to hour in day, 1~24 (24). |
|  | KK a | Formats a date to hour in am/pm, 0~11, with am/pm marker (00 AM) |
|  | hh a | Formats a date to hour in am/pm, 1~12, with am/pm marker (12 AM) |
|  | mm | Formats a date to minute in hour (00). |
|  | hh:mm a | Formats a date to hour in am/pm, 1~12, minutes in an hour, with am/pm marker (12:00 AM). |
|  | ss | Formats a date to second in minute (00). |
|  | hh:mm:ss | Formats a date to hour in am/pm 1~12, minutes in an hour, and second in minute (12:00:00). |
|  | hh:mm:ss a | Formats a date to hour in am/pm 1~12, minutes in an hour, and second in minute, with am/pm marker (12:00:00 AM). |
|  | mm:ss | Formats a date to minute in hour and second in minute (00:00). |
|  | MMMMM dd yyyy G (EEEEEE) hh:mm:ss aa z | Formats a date to a full form date, which contains month in year (shown in full form), days in a month, year, era designator, day in week (shown in the full form), hour in a day, 1~12, minutes in an hour, second in minute, am/pm marker, and time zone (December 25 2002 AD (Wednesday) 12:00:00 AM GMT-08:00). |
|  | **Notes:**   * Any characters in the pattern that are not in the ranges of ['a'..'z'] and ['A'..'Z'] will be treated as quoted text. For instance, characters such as ':', '.', ' ', '#' and '@' will appear in the resulting time text even they are not embraced within single quotes. * A pattern containing any invalid pattern letter cannot be added to the filter stack. | |
| Text |  | Specifies the length of the value. |
|  | Default Length | Uses the length of the string Default Length, which is 14, as the length of the string. Any letters that exceed this length will be cut. You can modify this string, adding or deleting letters to increase or decrease the length limit. For example, type Teddy, the label displayed may probably be Wed D, which originally could be Wed December 25 2002. If you want to show all, you can type Teddy is a lovely bear!, where the length is longer than the length of string Wed December 25 2002. |
| Mapping |  | Maps new value to one or more values. |
|  | One-to-one Mapping | Maps a new value to one value. Type the argument number that you want to replace, and then specify the new value in the Map to box. For example, if you want to replace the second data label on the X axis, which is Thu Jul 04 2002, with a new string US National Day, just type 2 in the Argument# box, type US National Day in the Map to box, and then select Add to add it to the Filter Stack. If you want to map more values, repeat this procedure. |
|  | Range Mapping | Maps a new value to a range of values. Type the argument numbers to define the range you want to map together, and then specify the new value in the Map to box. For example, if you want to replace the data labels from the second one to the fifth with a new name My Holiday, just type 2 in the first Argument# box and 5 in the second Argument# box, then type My Holiday in the Map to box, and finally select Add to add it to the Stack. If you want to map ranges that are not consecutive, repeat this procedure. |
|  | Text Mapping | Changes the data in the axis data label to a customized string. For example, if you want to change Chen in the first data label of the X axis to Jinfonet, type Chen in the Original Text box, type Jinfonet in the Map to box, and then select Add to add it to the Stack. You can only change the data one by one. Make sure that your spelling in the Original Text box is exactly the same as the data shown in the axis label. |
|  | Prefix | Adds a string before the text in the data label of the axis. For example, if you want to add NA before the text in the data label of the X axis, type NA in the Map to box, and select Add to add it to the Stack. |
|  | Suffix | Adds a string behind the text in the data label of the axis. For example, if you want to add NA behind the text in the data label of the X axis, type NA in the Map to box, and select Add to add it to the Stack. |
|  | **Note:** The data labels along each axis count from 0, which means the number of the first data label you see on the axis will be 0, the second will be 1, the third will be 2, and so on. | |

**Properties**

Specifies the properties for the selected format.

**Auto Scale in Number**

Enabled when specifying data format for an object that is of the Number data type. It specifies whether to
automatically scale the object values that fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Sample**

Displays the selected format effects.

**Stack**

Lists all the formats that you selected from different categories.

**Add**

Adds a format to the Stack box.

**Remove**

Removes a format from the Stack box.

**Apply**

Applies the specified format to values on the chart.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

When you open the dialog by selecting ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) besides the Category Format text box in Data group for a chart platform to specify the data format for the category axis (the X axis) in a chart, it consists of two tabs: [major label](#Majorfmt) tab and [minor label](#Minorfmt) tab.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

## Major Label

Specifies the data format of the major tick mark labels on the axis.

![Data Format dialog - Major Label tab](https://devnet.logianalytics.com/hc/article_attachments/4404901272343/dtfmt_major.gif)

To specify a format, first select a category from the Category box, then select the required format of this category from the Format box. The selected format will be displayed in the Properties text box. You can further edit the format if you want. Then, select the **Add** button to add the format to the Stack box. Repeat the steps to specify formats for other categories. Only one format can be defined for each category.

The following are details about options in the tab:

**[Category & Format](#DataFormat)**

Lists the category types and formats available for each category.

**Properties**

Specifies the properties for the selected format.

**Auto Scale in Number**

Enabled when the major tick mark labels are of the Number data type. It specifies whether to
[automatically scale big and small numbers](#AutoScale).

**Sample**

Displays the selected format effects.

**Stack**

Lists all the formats that you selected from different categories.

**Add**

Adds a format to the Stack box.

**Remove**

Removes a format from the Stack box.

**Apply**

Applies the specified format to values on the chart.

**Truncate**

Specifies whether to truncate label text longer than 10 characters and only show the first 7 characters.

## Minor Label

Specifies the data format of the minor tick mark labels on the axis.

![Data Format dialog - Minor Label tab](https://devnet.logianalytics.com/hc/article_attachments/4404909227543/dtfmt_minor.gif)

To specify a format, first select a category from the Category box, then select the required format of this category from the Format box. The selected format will be displayed in the Properties text box. You can further edit the format if you want. Then, select the **Add** button to add the format to the Stack box. You can also check **Correlate with Major Label** to specify that the data format of the minor tick mark labels correlates with that of the major tick mark labels. Repeat the steps to specify formats for other categories. Only one format can be defined for each category.

The following are details about options in the tab:

**Correlate with Major Label**

If checked, the data format of the minor tick mark labels will correlate with that of the major tick mark labels automatically. Only when it is unchecked can the format properties of the minor tick mark labels take effect.

**[Category & Format](#DataFormat)**

Lists the category types and formats available for each category.

**Properties**

Specifies the properties for the selected format.

**Auto Scale in Number**

Enabled when the minor tick mark labels are of the Number data type. It specifies whether to [automatically scale big and small numbers](#AutoScale).

**Sample**

Displays the selected format effects.

**Stack**

Lists all the formats that you selected from different categories.

**Add**

Adds a format to the Stack box.

**Remove**

Removes a format from the Stack box.

**Apply**

Applies the specified format to values on the chart.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065321-Data-Buffer-Information-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010030302-Data-Label-Editor-Dialog)
