---
title: "Customized Function Dialog Box"
id: 5735522295831
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735522295831-Customized-Function-Dialog-Box
updated_at: 2022-11-02T04:35:16Z
---

# Customized Function Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513478935-Customized-Control-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735528927383-Data-Buffer-Information-Dialog-Box)

# Customized Function Dialog Box

You can use the Customized Function dialog box to define [customized special functions](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables#Customized). This topic describes the options in the dialog box.

Designer displays the Customized Function dialog box when you select Customize from the Special Function drop-down list in the [New Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524043927-New-Summary-Dialog-Box), [Edit Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529231895-Edit-Summary-Dialog-Box), or in the Group screen of the component wizard, and provides you with different options in the dialog box according to the different data type of the selected group-by field: [Numeric](#Numeric), [String](#String), or [Date/Time](#Date).

---

When the group-by field is Numeric type, Designer displays the following options in the dialog box:

![Customized Function dialog box - Numeric](https://devnet.logianalytics.com/hc/article_attachments/9898465023383/cstmzdfctn_nmrc.gif)

**By Intervals**

Select to group data by intervals.

* **Numerical Value**  
   Specify the intervals of the group.

**Within Range**

Select to group data within certain range.

* **Within**  
  Specify the range. You also need to select how to apply the range from the drop-down list: to increasing data or decreasing data.

**Keep values outside of the range in special group**

Select to put values that do not fall within the defined intervals or range in a new special group.

* **Special Group Name**  
  Specify the name of the special group. By default, the group name is Others. You can double-click in the text box to rename it.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

When the group-by field is String type, Designer displays the following options in the dialog box:

![Customized Function dialog box - String](https://devnet.logianalytics.com/hc/article_attachments/9898515655959/cstmzdfctn_strg.gif)

**First/Last N letters**

Specify the intervals with which to group the report data. "N" should be an integer no larger than 255.

**Case sensitive when grouping**

Select to distinguish between uppercase and lowercase characters for the groups.

**Convert group name to**

Designer enables this option when you do not select "Case sensitive when grouping". You can use it to specify how you want to convert the group name.

* **Uppercase**  
  Select to convert the group names to uppercase.
* **Lowercase**  
  Select to convert the group names to lowercase.
* **No Conversion**  
  Select if you do not want to convert any group names.

**Keep values outside of the range in special group**

Select to put values that do not fall within the defined intervals in a new special group.

* **Special Group Name**  
  Specify the name of the special group. By default, the group name is "Others". You can double-click in the text box to rename it.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

When the group-by field is Date/Time type, Designer displays the following options in the dialog box:

![Customized Function dialog box - Date/Time](https://devnet.logianalytics.com/hc/article_attachments/9898515663255/cstmzdfctn_dttm.gif)

**Time**

Specify the time intervals. The unit of the time intervals can be: second, minute, hour, day, week, month, quarter, half year, or year.

**The Offset of Time Grouping**

Specify the offset with which you want to group the data.

* **1/1/1970 00:00:00**  
  Select to use the default offset that Logi Report defines.
* **Customized Value**  
  Select it and you can select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/9898458896919/btn_clndr.gif) to define your required offset using the calendar widget.

**The First Day of the Week**

Specify which day is the first day of a week.

**Keep values outside of the range in special group**

Select to put values that do not fall within the defined intervals in a new special group.

* **Special Group Name**  
  Specify the name of the special group. By default, the group name is "Others". You can double-click in the text box to rename it.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513478935-Customized-Control-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735528927383-Data-Buffer-Information-Dialog-Box)
