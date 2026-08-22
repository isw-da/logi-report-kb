---
title: "Customized Function Dialog"
id: 1500009630341
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630341-Customized-Function-Dialog
updated_at: 2021-07-24T16:04:53Z
---

# Customized Function Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630321-Customized-Control-Web-Action-Builder-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607662-Data-Buffer-Information-Dialog)

# Customized Function Dialog

The Customized Function dialog helps you to define [customized special functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables#Customized). It appears when you select the Customize item in the Special Function drop-down list in the [New Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009609362-New-Summary-Dialog) dialog, [Edit Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009630881-Edit-Summary-Dialog) dialog, or the Group screen of the report wizard.

The dialog varies according to the different data type of the selected group-by field: [Numeric](#Numeric), [String](#String), or [Date/Time](#Date).

---

If the group-by field is of Numeric type, the dialog appears as follows:

![Customized Function dialog - Numeric](https://devnet.logianalytics.com/hc/article_attachments/4404904361495/cstmzdfctn_nmrc.gif)

**By Intervals**

Specifies to group the data by intervals.

* **Numerical Value**  
   Specifies the intervals of the group.

**Within Range**

Specifies to group data within certain range. If this option is selected, you need to specify a value as the range in the Within text box and specify how to apply the range, to increasing data or decreasing data, by selecting the item from the drop-down list.

**Keep values outside of the range in special group**

Specifies to put values that do not fall within the defined interval or range in a new special group.

* **Special Group Name**  
   Specifies the name for the special group. By default, the group name is Others. You can double-click in the text box to rename it.

**OK**

Accepts all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

---

If the group-by field is of String type, the dialog appears as follows:

![Customized Function dialog - String](https://devnet.logianalytics.com/hc/article_attachments/4404904361751/cstmzdfctn_strg.gif)

**First/Last N letters**

Specifies the intervals with which to group the report data. N should be an integer no larger than 255.

**Case sensitive when grouping**

If the option is selected, Logi Report will distinguish between uppercase and lowercase characters when grouping.

**Convert group name to**

Specifies how to convert the group name. If Case sensitive when grouping is selected, this option will be disabled.

* **Uppercase**  
   Specifies to convert the group names to uppercase.
* **Lowercase**  
   Specifies to convert the group names to lowercase.
* **No Conversion**  
   Specifies not to convert any group names.

**Keep values outside of the range in special group**

Specifies to put values that do not fall within the defined interval in a new special group.

* **Special Group Name**  
   Specifies the name for the special group. By default, the group name is Others. You can double-click in the text box to rename it.

**OK**

Accepts all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

---

If the group-by field is of Date/Time type, the dialog appears as follows:

![Customized Function dialog - Date/Time](https://devnet.logianalytics.com/hc/article_attachments/4404904362135/cstmzdfctn_dttm.gif)

**Time**

Specifies the time which will be applied as the intervals to group data. Select the unit of time from the drop-down list to the right of the text box. It could be second, minute, hour, day, week, month, quarter, half year and year.

**The Offset of Time Grouping**

Specifies the offset used to group the data.

* **1/1/1970 00:00:00**  
   The default offset defined by Logi Report.
* **Customized Value**  
   If the option is selected, you can select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404904203031/btn_clndr.gif) define your required offset using the calendar.

**The First Day of the Week**

Specifies which day will be regarded the first day of a week.

**Keep values outside of the range in special group**

Specifies to put values that do not fall within the defined interval in a new special group.

* **Special Group Name**  
   Specifies the name for the special group. By default, the group name is Others. You can double-click in the text box to rename it.

**OK**

Accepts all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630321-Customized-Control-Web-Action-Builder-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607662-Data-Buffer-Information-Dialog)
