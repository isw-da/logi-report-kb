---
title: "Customized Function Dialog Box"
id: 4405664448023
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664448023-Customized-Function-Dialog-Box
updated_at: 2022-01-27T20:35:41Z
---

# Customized Function Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661489687-Customized-Control-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661495575-Data-Buffer-Information-Dialog-Box)

# Customized Function Dialog Box

You can use the Customized Function dialog box to define [customized special functions](https://devnet.logianalytics.com/hc/en-us/articles/4405664404503-Grouping-the-Data-in-Tables#Customized). This topic describes the options in the dialog box.

Designer displays the Customized Function dialog box when you select Customize from the Special Function drop-down list in the [New Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664535575-New-Summary-Dialog-Box), [Edit Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664467223-Edit-Summary-Dialog-Box), or in the Group screen of the component wizard, and provides you with different options in the dialog box according to the different data type of the selected group-by field: [Numeric](#Numeric), [String](#String), or [Date/Time](#Date).

---

If the group-by field is of Numeric type, Designer displays the following options in the dialog box:

![Customized Function dialog box - Numeric](https://devnet.logianalytics.com/hc/article_attachments/4420394831383/cstmzdfctn_nmrc.gif)

**By Intervals**

Select to group the data by intervals.

* **Numerical Value**  
   Specify the intervals of the group.

**Within Range**

Select to group data within certain range. If you select this option, you need to specify a value as the range in the Within text box and specify how to apply the range, to increasing data or decreasing data, by selecting the item from the drop-down list.

**Keep values outside of the range in special group**

Select to put values that do not fall within the defined interval or range in a new special group.

* **Special Group Name**  
  Specify the name for the special group. By default, the group name is Others. You can double-click in the text box to rename it.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

If the group-by field is of String type, Designer displays the following options in the dialog box:

![Customized Function dialog box - String](https://devnet.logianalytics.com/hc/article_attachments/4420410803735/cstmzdfctn_strg.gif)

**First/Last N letters**

Specify the intervals with which to group the report data. "N" should be an integer no larger than 255.

**Case sensitive when grouping**

Select to distinguish between uppercase and lowercase characters for the groups.

**Convert group name to**

Designer enables this option only when you do not select "Case sensitive when grouping". Use it to specify how to convert the group name.

* **Uppercase**  
  Select to convert the group names to uppercase.
* **Lowercase**  
  Select to convert the group names to lowercase.
* **No Conversion**  
  Select if you do not want to convert any group names.

**Keep values outside of the range in special group**

Select to put values that do not fall within the defined interval in a new special group.

* **Special Group Name**  
  Specify the name of the special group. By default, the group name is "Others". You can double-click in the text box to rename it.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

If the group-by field is of Date/Time type, Designer displays the following options in the dialog box:

![Customized Function dialog box - Date/Time](https://devnet.logianalytics.com/hc/article_attachments/4420410803991/cstmzdfctn_dttm.gif)

**Time**

Specify the time which Designer applies as the intervals to group data. Select the unit of time from the drop-down list to the right of the text box. It can be second, minute, hour, day, week, month, quarter, half year, or year.

**The Offset of Time Grouping**

You can use this option to specify the offset used to group the data.

* **1/1/1970 00:00:00**  
  Select to use the default offset that Logi Report defines.
* **Customized Value**  
  Select it and you can select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4420402355351/btn_clndr.gif) to define your required offset using the calendar widget.

**The First Day of the Week**

Specify which day is the first day of a week.

**Keep values outside of the range in special group**

Select to put values that do not fall within the defined interval in a new special group.

* **Special Group Name**  
  Specify the name of the special group. By default, the group name is "Others". You can double-click in the text box to rename it.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661489687-Customized-Control-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661495575-Data-Buffer-Information-Dialog-Box)
