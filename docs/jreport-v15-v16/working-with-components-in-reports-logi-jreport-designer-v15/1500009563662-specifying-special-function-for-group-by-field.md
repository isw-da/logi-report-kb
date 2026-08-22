---
title: "Specifying Special Function for Group by Field"
id: 1500009563662
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field
updated_at: 2021-07-24T05:55:56Z
---

# Specifying Special Function for Group by Field

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584401-Setting-the-Sort-Manner)

# Specifying Special Function for Group by Field

If the field which is added as the grouping criterion is of Numeric/String/Date/Time type, you can select a special function for the field in the Special Function column to group the data as required. This is called "grouping data by intervals" in Logi JReport. It enables you to group data more clearly and logically, and to summarize data more effectively.

The following is a short description of each special function.

**Functions for Numeric-typed group by fields**

| Function | Description |
| --- | --- |
| None | All the records that have the same field value will be displayed together as a group. |
| Up to 5 | The records will be grouped by intervals of 5. |
| Up to 10 | The records will be grouped by intervals of 10. |
| Up to 50 | The records will be grouped by intervals of 50. |
| Up to 100 | The records will be grouped by intervals of 100. |
| Up to 500 | The records will be grouped by intervals of 500. |
| Up to 1000 | The records will be grouped by intervals of 1000. |
| Up to 5000 | The records will be grouped by intervals of 5000. |
| Up to 10000 | The records will be grouped by intervals of 10000. |

**Functions for String-typed group by fields**

| Function | Description |
| --- | --- |
| None | All the records that have the same field value will be displayed together as a group. |
| For 1st letter | The records, of which the field values' first letter is the same, will be grouped together. |
| For first 2 letters | The records, of which the field values' first two letters are the same, will be grouped together. |
| For first 3 letters | The records, of which the field values' first three letters are the same, will be grouped together. |
| For first 4 letters | The records, of which the field values' first four letters are the same, will be grouped together. |
| For first 5 letters | The records, of which the field values' first five letters are the same, will be grouped together. |
| For last 1 letter | The records, of which the field values' last letter is the same, will be grouped together. |
| For last 2 letters | The records, of which the field values' last two letters are the same, will be grouped together. |
| For last 3 letters | The records, of which the field values' last three letters are the same, will be grouped together. |
| For last 4 letters | The records, of which the field values' last four letters are the same, will be grouped together. |
| For last 5 letters | The records, of which the field values' last five letters are the same, will be grouped together. |

**Functions for Date/Time-typed group by fields**

| Function | Description |
| --- | --- |
| None | All the records that have the same field value will be displayed together as a group. |
| For each second | The records, of which the field values are in the same second, will be grouped together. |
| For each minute | The records, of which the field values are in the same minute, will be grouped together. |
| For each hour | The records, of which the field values are in the same hour, will be grouped together. |
| For each day | The records, of which the field values are in the same day, will be grouped together. |
| For each week | The records, of which the field values are in the same week, will be grouped together. |
| For each bi-week | The records, of which the field values are in the same bi-week, will be grouped together. |
| For each half month | The records, of which the field values are in the same half month, will be grouped together. |
| For each month | The records, of which the field values are in the same month, will be grouped together. |
| For each quarter | The records, of which the field values are in the same quarter, will be grouped together. |
| For each half year | The records, of which the field values are in the same half year, will be grouped together. |
| For each year | The records, of which the field values are in the same year, will be grouped together. |

## Customized function

In the special function list for all the above data types, there is an item called Customize. By selecting this item, you can define special functions.

* **Defining special function for Numeric type fields**
  1. Select a Numeric-typed group by field and then select **Customize** in the Special Function drop-down list. The [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009586201-Customized-Function-Dialog) dialog appears.

     ![Customized Function for Numeric type](https://devnet.logianalytics.com/hc/article_attachments/4404893933079/cstmzdfctn_nmrc.gif)
  2. Specify the way in which you want to group the data.

     If you want to group the data by intervals, check the **By Intervals** radio button, then define the interval in the Numerical Value text box.

     If you want to group data by a range, check the **Within Range** radio button, specify the range in the Within text box and select how to apply the range: apply to increasing data or decreasing data.
  3. Check **Keep values outside of the range in special group** if you want to put values that do not fall within the specified interval or range in a new group, then give a name for the group in the Special Group Name text box.
  4. Select **OK** to save the settings.

  **Note:** When grouping Numeric typed data by intervals, Logi JReport follows this rule: all values in each range are >= the minimum value in the range and < the maximum value in the range, and 0 is the offset for the intervals.

  For example, if you specify to group the following values by intervals of 5: -8, -6, -5, -3, -1, 0, 1, 3, 4, 5, 8, the results will be as follows:

  | Ranges | Values |
  | --- | --- |
  | -10 to -5 | -8, -6 |
  | -5 to 0 | -5, -3, -1 |
  | 0 to 5 | 0, 1, 3, 4 |
  | 5 to 10 | 5, 8 |
* **Defining special function for String type fields**
  1. Select a String-typed group by field and then select **Customize** in the Special Function drop-down list to display the Customized Function dialog.

     ![Customized Function for String type](https://devnet.logianalytics.com/hc/article_attachments/4404893933335/cstmzdfctn_strg.gif)
  2. Specify the group intervals as required.

     For example, to group records by the first N letters of the group by field values, select **First** from the drop-down list and then enter **N** in the text box. Note that the number of letters should be an integer no larger than 255.
  3. If you want to distinguish between uppercase and lowercase characters when grouping, check **Case sensitive when grouping**; otherwise, check in which way you want to convert the group names: Uppercase, Lowercase or No Conversion.

     **Note:** If you check Case sensitive when grouping, No Conversion will be checked as the default converting method.
  4. Check **Keep values outside of the range in special group** if you want to put values that do not fall within the specified interval in a new group, then give a name for the group in the Special Group Name text box.
  5. Select **OK** to save the settings.
* **Defining special function for Date/Time type fields**
  1. Select a Date/Time-typed group by field and then select **Customize** in the Special Function drop-down list to display the Customized Function dialog.

     ![Customized Function for Date and Time type](https://devnet.logianalytics.com/hc/article_attachments/4404889372439/cstmzdfctn_dttm.gif)
  2. Specify the group intervals by inputting a value in the Time text box and then selecting the required item from the drop-down list behind.
  3. Define the offset with which you want to group the data.

     By default, Logi JReport takes 1/1/1970 00:00:00 as the offset. If you want to define the offset by your own, check the **Customized Value** radio button and then select the calendar button to choose the required offset.
  4. Specify which day will be used as the first day of a week as required.
  5. Check **Keep values outside of the range in special group** if you want to put values that do not fall within the specified interval in a new group, then give a name for the group in the Special Group Name text box.
  6. Select **OK** to save the settings.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584401-Setting-the-Sort-Manner)
