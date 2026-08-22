---
title: "A Detailed Chart Property Reference"
id: 1500009569442
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference
updated_at: 2021-07-24T05:54:14Z
---

# A Detailed Chart Property Reference

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569462-Properties-of-Chart-Label-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591341-Properties-of-Crosstab-in-Page-Report)

# A Detailed Chart Property Reference

This topic introduces the Chart Property Reference.

## Border Type

Specifies the border type of an object. Can be one of the following:

* **none**  
   The object has no visible border lines.
* **raised**  
   The object has 3-D borders that appear as if they are raised off the page.
* **recess**  
   The object has 3-D borders that appear as if they are pressed into the page.
* **shadow**  
   The object has two shadowed borders, beneath and to the right of the object.
* **solid**  
   The object has single-line borders.

## Data Format

Specifies the data format for the labels of the axes or legend as required. Applies to chart platforms and legends.

Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell and select the data format in the [Data Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009565042-Data-Format-Dialog) dialog as required:

| Format Type | Option | Description (Sample) |
| --- | --- | --- |
| Scale |  | Obtains a new value by a calculation on the value. |
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

## Border End Caps

Specifies the ending style of the border line. Can be one of the following:

* **butt**  
   Ends unclosed subpaths and dash segments with no added decoration.
* **round**  
   Ends unclosed subpaths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **square**  
   Ends unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

## Fill Type

Specifies the fill pattern of an object. Applies to the platform, paper, legend, wall, floor, axes, tick marks, labels, fonts and icons of a chart. Can be one of the following:

* **none**  
   No fill (default).
* **color**  
   Fills with a specified color.
* **texture**  
   Fills with a specified texture.
* **gradient**  
   Fills with gradient colors.
* **image**  
   Fills with a specified image (not available for legend icons).

## Font Effect

Specifies the special effect for the text. Applies to fonts. Can be one of the following:

* **none**  
   Does not apply any special effect to the text (default).
* **embossed**  
   Makes the text appearing as if it is raised off the page.
* **engraved**  
   Makes the text appearing as if it is imprinted or pressed into the page.
* **shadowed**  
   Adds a shadow behind, beneath and to the right of the text.
* **outlined**  
   Displays the inner and outer borders of each character.
* **shadowed & outlined**  
   Makes the text to be outlined and shadowed.

## Font Script

Specifies superscript/subscript form for the text. Applies to fonts. Can be one of the following:

* **none**  
   Does not apply superscript or subscript form to the text (default).
* **superscript**  
   Makes the text to be shown above the baseline and changes it to a smaller size.
* **subscript**  
   Makes the text to be shown below the baseline and changes it to a smaller size.

## Font Strikethrough

Specifies the style for the horizontal line with which the text is struck through. Applies to fonts. Can be one of the following:

* **none**  
   Does not draw any line through the text (default).
* **thin line**  
   Draws a normal line through the text.
* **bold line**  
   Draws a bold line through the text.
* **double lines**  
   Draws two lines through the text.

## Font Underline

Specifies the style for the horizontal line under the text. Applies to fonts. Can be one of the following. Note that JDashboard and Web Report Studio don’t support underlining chart text.

* **none**  
   No underline (default).
* **single**  
   Draws a single line under the text.
* **single lower**  
   Draws a single line under the text at a lower position.
* **bold line**  
   Draws a bold line under the text.
* **bold lower**  
   Draws a bold line under the text at a lower position.
* **double lines**  
   Draws two lines under the text.
* **bold double**  
   Draws two bold lines under the text.
* **patterned line**  
   Draws a line under the text, using the pattern of the text font.
* **bold patterned**  
   Draws a bold line under the text, using the pattern of the text font.

## Hyperlink

This property is used to add a hyperlink, which refers to another report or a website, to the chart data markers. For chart in a page report, you can also control the hyperlink property with a formula, which will be a good way to get required data from another report.

For example, you have two reports ReportA and ReportB in the SampleReports.cat catalog. In ReportA, the data in a banded object is grouped by customer country and a bar chart is used to illustrate the count of Customer\_ID in every group. ReportB shows the information of customer, such as ID, Name, and Annual Sales. Then we build a link between the two reports. After publishing the reports to Logi JReport Server, run ReportA and select the bar of a country, ReportB will then appear, only showing the data of the specific country. The steps are:

1. In Logi JReport Designer open ReportA.cls. Create a new formula named Link\_b. It might be:

   |  |
   | --- |
   | ``` string t="http://localhost:8888/jinfonet/tryView.jsp?&jrs.report=ReportB.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8&jrs.authorization=YWRtaW46YWRtaW4%3D&"; string t1="jrs.param$PCOUNTRY="; string url=t+t1+"@INNER"+"&jrs.result_type=1"; return url ``` |

   **Notes:**

   * Make sure that the paths of the catalog and the report in the URL are corresponding with their paths on the server.
   * The built-in parameter INNER is used for representing the category data. In addition, you can use OUTER for the series data.
   * For the X HyperLink and Z HyperLink properties, you can use @XDIM and @ZDIM respectively instead of @INNER and @OUTER.
2. In the Report Inspector, set the Hyperlink property of the chart platform to **Link\_b**.
3. Publish the two reports with the catalog to Logi JReport Server.
4. Run ReportA, point to a bar and select it, the corresponding records in ReportB will be displayed. You can also view the information of the other countries by selecting the corresponding bars in ReportA.

## Image Layout

Specifies the layout style of an image. Applies to images. Can be one of the following:

* **tile**  
   Repeats the image over the entire area (default).
* **center**  
   Displays the image in the center of the area.
* **scaled**  
   Stretches the image to cover the entire area.

## Line Joint

Specifies the line joint style. Can be one of the following:

* **miter**  
   Joins path segments by extending their outside edges until they meet.
* **round**  
   Joins path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
   Joins path segments by connecting the outer corners of their wide outlines with a straight segment.
* **joint round**  
   Joins path segments by rounding off the corner at the specified radius. Available only for chart platform.

## Start Offset(1st.Data.Set), End Offset(1st.Data.Set), Start Offset(2nd.Data.Set), and End Offset(2nd.Data.Set)

These four properties are used to control the data source range that appears on the chart.

For 2-level-group charts, record-level charts and all kinds of combination charts, Start Offset(1st.Data.Set) and End Offset(1st.Data.Set) are used to control the starting offset and ending offset of the data series; Start Offset(2ndDataSet) and End Offset(2nd Data.Set) are used to control the range of the categories.

For 1-level-group charts, Start Offset(2nd.Data.Set) and End Offset(2nd.Data.Set) are used to control the starting offset and ending offset of the categories; Start Offset(1st.Data.Set) and End Offset(1st.Data.Set) will not work because there is no series data in chart that contains only one group.

The range of the property values can be -1 (Default, Not Set) or an integer between 0 and Number of Data Series – 1 (or, Number of Categories - 1).

If the value is out of this range, the following rules will be applied to the default value:

| IF | THEN |
| --- | --- |
| Start Offset(1st.Data.Set) < 0 | Start Offset(1st.Data.Set) = 0 |
| Start Offset(1st.Data.Set) > max data number | Start Offset(1st.Data.Set) = max data number |
| End Offset(1st.Data.Set) < 0 | End Offset(1st.Data.Set) = max data number |
| End Offset(1st.Data.Set) > max data number | End Offset(1st.Data.Set) = max data number |
| Start Offset(1st.Data.Set) > End Offset(1st.Data.Set) and EndOffset(1st.Data.Set) >=0 | Start Offset(1st.Data.Set) = 0, End Offset(1st.Data.Set) = max data number |

Same rules apply to Start Offset(2nd.Data.Set) and End Offset(2nd.Data.Set).

## Threshold Line Style

Specifies the style for the threshold lines. Applies to chart paper. Stock charts, radar charts, scatter charts and bubble charts have no threshold lines.

A threshold line marks a specific data point that is specified by the user. It is usually used by the user for comparing with data series to see whether the data is higher or lower than this point. For example, if you want to see whether the production zones successfully accomplished their production tasks, you can set a threshold line to represent the goal output, and another to represent the lowest acceptable output quantity. By using the threshold lines, you can spot out the zones that are out of the range at a glance.

For 3-D chart, the threshold line value is represented by a plane.

Can be one of the following:

| Option | Description |
| --- | --- |
| Style1 | Use two threshold areas (Threshold Line1 and Threshold Line2) to emphasize the data series that are higher than the first threshold line or lower than the second threshold line. |
| Style2 | Use a single threshold area (Threshold Line1) to emphasize the data series that are between the higher and the lower threshold lines. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569462-Properties-of-Chart-Label-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591341-Properties-of-Crosstab-in-Page-Report)
