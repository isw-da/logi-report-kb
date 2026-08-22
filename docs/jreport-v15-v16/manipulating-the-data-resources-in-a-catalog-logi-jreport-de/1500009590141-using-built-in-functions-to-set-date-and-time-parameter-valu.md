---
title: "Using Built-in Functions to Set Date and Time Parameter Values"
id: 1500009590141
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590141-Using-Built-in-Functions-to-Set-Date-and-Time-Parameter-Values
updated_at: 2021-07-24T05:54:30Z
---

# Using Built-in Functions to Set Date and Time Parameter Values

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590181-Dynamically-Grouping-Sorting-Report-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590101-Editing-the-Display-Sequence-of-Parameters)

# Using Built-in Functions to Set Date and Time Parameter Values

For a parameter of the Date, DateTime, or Time type, you can customize a dynamic date and time value by creating an expression using built-in formula functions. For example you might want the start date to always be 7 days ago and the end date to be today, you can then customize the value for the start date parameter as `dateadd('d', -7, today())` and `today()` for the end date parameter.

**To specify a date and time parameter value using built-in functions:**

1. In the places where you are able to specify a value for the parameter, you will see the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404889299735/btn_clndr.gif). Select this button and the [Calendar](https://devnet.logianalytics.com/hc/en-us/articles/1500009564742-Calendar-Dialog) dialog appears.

   ![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893827735/clndr.gif)
2. The Template drop-down list on the right provides some predefined expressions for you to use. You can customize your own expression either based on an existing template or by directly editing the contents in the Expression text box.

   If you cannot see the Template label on the right, select **>>** on the bottom left corner.
3. Logi JReport's built-in [Date/Time](https://devnet.logianalytics.com/hc/en-us/articles/1500009589521-Date-Time-Functions) functions are available for inserting into your expression. To make use of them, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) and the [Expression](https://devnet.logianalytics.com/hc/en-us/articles/1500009565502-Expression-Dialog) dialog appears.

   ![Expression dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893828119/exprss.gif)
4. The top text box shows the current expression statement. Expand the **Date/Time** node below, double-click the required function to insert it where the cursor is located in the expression. Upon finishing, select **OK** to return to the Calendar dialog.
5. The Preview box calculates the result of the current expression. Each time you modify the expression, you can select in the box to refresh the result. If it is an invalid expression, an error message will be shown in the box and no change will be made to the calendar and the currently selected date/time will be remained in the calendar.
6. When done, select **OK** to add the value.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590181-Dynamically-Grouping-Sorting-Report-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590101-Editing-the-Display-Sequence-of-Parameters)
