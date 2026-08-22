---
title: "Calendar Dialog"
id: 1500009564742
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564742-Calendar-Dialog
updated_at: 2021-07-24T05:55:35Z
---

# Calendar Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564622-Business-View-Editor-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586241-Category-Options-Dialog)

# Calendar Dialog

The Calendar dialog appears when you select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404889299735/btn_clndr.gif) while specifying value to a Date, DateTime, or Time parameter which allows for type-in values. It helps you to [create a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500009590141-Using-Built-in-Functions-to-Set-Date-and-Time-Parameter-Values) using either the calendar or an expression.

The dialog is divided into two sections: the left section is a calendar for selecting date and time, the right section is for editing an expression by using built-in formula functions. The expression has higher priority than the value specified in the calendar. If you cannot see the expression settings, select **>>** at the bottom left corner. [See the dialog](javascript:%20void(null)).

![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893827735/clndr.gif)

**Calendar**

Specifies the month, year, day and time from the calendar. The time setting is available to DateTime or Time type parameters. The date/time in the calendar can be synchronized with the date/time calculated by a valid expression.

**Display Time Format**

Specifies in which format to display the time, 12-hour or 24-hour. It is available to DateTime type parameters only. Each time when the calendar is accessed, the default selected format is always 12-hour format.

**>>**/**<<**

Displays or hides the expression settings.

**Template**

You can choose an existing expression template and then either use it directly or edit your expression based on it. The Template name field does not support typing directly into it. If you would like to create an expression all by yourself, select the first blank row from the drop-down list.

**Expression**

Displays the expression. You can edit the expression directly in the text box.

![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif)

Opens the [Expression](https://devnet.logianalytics.com/hc/en-us/articles/1500009565502-Expression-Dialog) dialog to insert built-in Date/Time formula functions into the expression.

**Preview**

Displays the value result based on the specified expression, or gives error information if the expression is not correct.

**OK**

Sets either the value selected in the calendar or the expression as the parameter value. Expression has higher priority.

**Cancel**

Does not retain any changes and closes the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564622-Business-View-Editor-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586241-Category-Options-Dialog)
