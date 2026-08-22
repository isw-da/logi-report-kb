---
title: "Customized Function Dialog"
id: 1500010065221
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065221-Customized-Function-Dialog
updated_at: 2021-07-24T10:39:03Z
---

# Customized Function Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030182-Customized-Control-Web-Action-Builder-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065321-Data-Buffer-Information-Dialog)

# Customized Function Dialog

The Customized Function dialog helps you to define [customized special functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Customized). It appears when you select the Customize item in the Special Function drop-down list in the [New Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010031922-New-Summary-Dialog) dialog, [Edit Summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010030602-Edit-Summary-Dialog) dialog, or the Group screen of the report wizard.

Options in the dialog vary according to the data type of the selected group-by field.

If the group-by field is of Numeric type, the dialog appears as follows:

![Customized Function dialog - Numeric](https://devnet.logianalytics.com/hc/article_attachments/4404901274903/cstmzdfctn_nmrc.gif)

**By Intervals**

Specifies to group the data by intervals.

* **Numerical Value**  
   Specifies the intervals of the group.

**Within Range**

Specifies to group data within certain range. If this option is checked, you need to enter a value as the range in the Within text box and specify how to apply the range, to increasing data or decreasing data, by selecting the item from the drop-down list.

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

![Customized Function dialog - String](https://devnet.logianalytics.com/hc/article_attachments/4404901275159/cstmzdfctn_strg.gif)

**First/Last N letters**

Specifies the intervals with which to group the report data. N should be an integer no larger than 255.

**Case sensitive when grouping**

If checked, Logi JReport will distinguish between uppercase and lowercase characters when grouping.

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

If the group-by field is of Date/Time type, the dialog appears as follows:

![Customized Function dialog - Date/Time](https://devnet.logianalytics.com/hc/article_attachments/4404901275415/cstmzdfctn_dttm.gif)

**Time**

Specifies the time which will be applied as the intervals to group data. Select the unit of time from the drop-down list to the right of the text box. It could be second, minute, hour, day, week, month, quarter, half year and year.

**The Offset of Time Grouping**

Specifies the offset used to group the data.

* **1/1/1970 00:00:00**  
   The default offset defined by Logi JReport.
* **Customized Value**  
   If checked, you can define your required offset by selecting the calendar button.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030182-Customized-Control-Web-Action-Builder-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065321-Data-Buffer-Information-Dialog)
