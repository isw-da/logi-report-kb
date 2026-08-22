---
title: "Customized Function Dialog Box"
id: 1500010096021
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096021-Customized-Function-Dialog-Box
updated_at: 2021-07-23T19:15:11Z
---

# Customized Function Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096001-Customized-Control-Web-Action-Builder-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058522-Data-Buffer-Information-Dialog-Box)

# Customized Function Dialog Box

You can use the Customized Function dialog box to define [customized special functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Customized). This topic describes the options in the dialog box.

Designer displays the Customized Function dialog box when you select the Customize item in the Special Function drop-down list in the [New Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098061-New-Summary-Dialog-Box), [Edit Summary dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096441-Edit-Summary-Dialog-Box), or the Group screen of the report wizard, and provides you with different options in the dialog box according to the different data type of the selected group-by field: [Numeric](#Numeric), [String](#String), or [Date/Time](#Date).

---

If the group-by field is of Numeric type, Designer displays the following options in the dialog box:

![Customized Function dialog box - Numeric](https://devnet.logianalytics.com/hc/article_attachments/4404856984727/cstmzdfctn_nmrc.gif)

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

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

If the group-by field is of String type, Designer displays the following options in the dialog box:

![Customized Function dialog box - String](https://devnet.logianalytics.com/hc/article_attachments/4404856985111/cstmzdfctn_strg.gif)

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

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

If the group-by field is of Date/Time type, Designer displays the following options in the dialog box:

![Customized Function dialog box - Date/Time](https://devnet.logianalytics.com/hc/article_attachments/4404856985495/cstmzdfctn_dttm.gif)

**Time**

Specify the time which Designer applies as the intervals to group data. Select the unit of time from the drop-down list to the right of the text box. It can be second, minute, hour, day, week, month, quarter, half year, or year.

**The Offset of Time Grouping**

You can use the option to specify the offset used to group the data.

* **1/1/1970 00:00:00**  
  Select to use the default offset that Logi Report defines.
* **Customized Value**  
  Select it and you can select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to define your required offset using the calendar.

**The First Day of the Week**

Specify which day is the first day of a week.

**Keep values outside of the range in special group**

Select to put values that do not fall within the defined interval in a new special group.

* **Special Group Name**  
  Specify the name of the special group. By default, the group name is "Others". You can double-click in the text box to rename it.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096001-Customized-Control-Web-Action-Builder-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058522-Data-Buffer-Information-Dialog-Box)
