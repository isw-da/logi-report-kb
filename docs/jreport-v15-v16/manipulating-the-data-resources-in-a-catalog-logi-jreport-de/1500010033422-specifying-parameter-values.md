---
title: "Specifying Parameter Values"
id: 1500010033422
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010033422-Specifying-Parameter-Values
updated_at: 2021-07-24T10:38:08Z
---

# Specifying Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069021-Importing-Parameter-Values)

# Specifying Parameter Values

When you [preview](https://devnet.logianalytics.com/hc/en-us/articles/1500010070941-Previewing-Reports), [print or export](https://devnet.logianalytics.com/hc/en-us/articles/1500010033062-Printing-and-Exporting-Reports) a report with parameters, or [preview a query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Preview) that contains parameters, Logi JReport Designer will prompt you the Enter Parameter Values dialog to specify values for the parameters. All the parameters used in the report or query and the prompting information are listed.

![Enter Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901149079/enterprmvlu.gif)

The way to specify a parameter value varies with the type and properties of the parameter. Here are several ways you can use to specify parameter values:

* In the parameter value combo box, select the required one from the drop-down list or input the value manually.

  When a parameter's [Encrypt Parameter Value](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog#Encrypt) property is true, the value drop-down list will be disabled. In this case, if the [Hide Parameter Value](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog#Unencrypted) checkbox is available, you can uncheck it to enable the drop-down list to view and select the required value.
* Select or unselect the checkbox to specify a Yes/No value.
* Select the button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) to [specify multiple values](#Multiple) if the parameter allows for multiple values.
* Select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404909137175/btn_clndr.gif) to [specify a date and time value](#Date).

**Note:** You are recommended not to use blank as the thousands separator in Number-typed parameter values under French locale, otherwise your input will not be correctly recognized because of a JVM bug. For details, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

The following shows more about specifying parameter values:

* [Specifying Multiple Values for a Parameter](#Multiple)
* [Setting Values for Date/Time/DateTime Parameters](#Date)
* [Customizing the Display Order of Parameters](#Order)

## Specifying Multiple Values for a Parameter

For a parameter that allows for multiple values (the parameter's Allow Multiple Values property is true), you can specify one or more values to it.

1. Select ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the value text box of the parameter. The [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010030722-Enter-Values-Dialog) dialog appears.

   ![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901149335/entervlu.gif)
2. If the parameter's Enable the "All" Option property is true, the All checkbox is available and by default it is selected. It means to apply the "All" value to the parameter, which could be all values of the parameter determined by Logi JReport, all values in the database or all the available values according to the [Scope of All Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog#AllScope) setting of the parameter. When the parameter is inserted as a field into a report and All is selected as the value, the field will show the string "All". If you do not want to apply the "All" value to the parameter, deselect the **All** checkbox and then specify the
   desired values as shown in the following steps.
3. Select the required values in the Available Values box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404909137431/btn_addarrow1.gif) to add them to the Selected Values box; to add all the available values, select ![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404909137687/btn_addall1.gif). You can make use of the Search text box to
   search for the required values among the available values: type in the keyword
   and the available values that contain the keyword will be listed with the keyword highlighted in the values.

   If some added values are not wanted, select them in the Selected Values box and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909137943/btn_rmvarrow1.gif) to remove them; to remove all added values, select ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404901149591/btn_rmvall1.gif).
4. When the parameter's Allow Type-in of Value property is true, the Search text box will be replaced by the Enter Values text box. You can type in a value manually and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404909137431/btn_addarrow1.gif) next to add it to the Selected Values box. When the parameter is bound with a column, but the display column is different from the bound column, make sure the value you enter is that of the bound column. If the parameter is of the Date, Time or DateTime type, you can also select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404909137175/btn_clndr.gif) to [specify a date and time value](#Date).

   ![Enter Values dialog - allow type in](https://devnet.logianalytics.com/hc/article_attachments/4404901149847/prmtr_value_entervlu.gif)
5. Select **OK** to select the specified values for the parameter.

## Setting Values for Date/Time/DateTime Parameters

When specifying value for a parameter of the Date, Time or DateTime type which allows for type-in values (the parameter's Allow Type-in of Value property is true), you can make use of the calendar to select a date and time as the value, or customize a dynamic date and time value by creating an expression using Logi JReport's built-in Date/Time functions. For example you might want the start date to always be 7 days ago and the end date to be today, you can then customize the value for the start date parameter as `dateadd('d', -7, today())` and `today()` for the end date parameter. The expression has higher priority than the value specified using the calendar.

**To select a date and time value from the calendar:**

1. Select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404909137175/btn_clndr.gif) next to the value text box of the parameter. The following dialog appears.

   ![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909138199/prmtr_value_clndr.gif)
2. In the calendar on the left, specify the month, year and day accordingly.
3. If the parameter is of DateTime type, the time setting is available. From the Display Time Format drop-down list, specify in which format to display the time, 12 hours or 24 hours (each time when the calendar is accessed, the default selected format is always 12 hours), then select the hour, minute and second time from the corresponding drop-down lists and choose whether it is AM or PM.
4. Select **OK** to add the value.

**To customize a dynamic date and time value by creating an expression:**

1. Select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404909137175/btn_clndr.gif) next to the value text box of the parameter. The following dialog appears (if the right section of the dialog is not displayed,
   select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909138455/btn_addarrow2.gif)on the bottom left corner to expand it).

   ![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909138199/prmtr_value_clndr.gif)
2. The Template drop-down list provides some predefined expressions for you to use. You can customize your own expression either based on an existing template or by directly editing the contents in the Expression text box.
3. You can make use of Logi JReport's built-in [Date/Time](https://devnet.logianalytics.com/hc/en-us/articles/1500010028442-Appendix-1-Formula-Functions#DateTime) functions in the expression. To display the functions, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the Template drop-down list.
4. The [Expression](https://devnet.logianalytics.com/hc/en-us/articles/1500010065901-Expression-Dialog) dialog appears. The top text box shows the current expression statement if there is. Put the cursor where you want to insert the function in the statement, then double-click the required function to insert it there. Select **OK** to close the dialog.

   ![Expression dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909138711/exprss.gif)
5. The Preview box calculates the result of the current expression. Each time you modify the expression, you can select in the box to refresh the result. The date/time in the calendar on the right can be synchronized with the date/time calculated by a valid expression. If it is an invalid expression, an error message will be shown in the box and no change will be made to the calendar and the currently selected date/time will be remained in the calendar.
6. Select **OK** to add the value.

After you use an expression to specify the value, when you hover the mouse pointer over this value in the Enter Parameter Values dialog, a tip will appear showing its expression. Select in the value text box, the expression will be displayed in the text box. You can edit the expression in the text box directly if you want. After editing, when you select elsewhere outside of the value text box:

* If the edited expression is correct, a new value calculated by the expression will be displayed in the parameter value text box.
* If the edited expression is wrong, no value will be created and the expression itself will be displayed and highlighted in red in the value text box. Correct the expression, or select the calendar button to specify a value.

## Customizing the Display Order of Parameters

By default the parameters are displayed in ascending alphabetic order in the Enter Parameter Values dialog, thus the parameter pEndDate appears before pStartDate which would be very confusing to users. Logi JReport allows you to customize the display order of the parameters in the dialog so that they could be shown in a more reasonable sequence. The order will not affect the display sequence of the parameters in the resource tree, which is determined by the [Sort setting](https://devnet.logianalytics.com/hc/en-us/articles/1500010031962-Options-Dialog#Sort) in the Options dialog.

You can customize the parameter display order at two levels: catalog and specific report. When the order of parameters in a catalog is specified, the order will be applied to all reports using the catalog. When both levels of orders are configured, the report level order has higher priority than the catalog level one.

**To adjust the parameter order for a catalog:**

1. Open the catalog containing parameters for which you would like to adjust the order.
2. In the Catalog Manager, expand a data source, select the **Parameters** node or any parameter in the node, then select **Parameter Order**  on the Catalog Manager toolbar. The [Parameter Order](https://devnet.logianalytics.com/hc/en-us/articles/1500010067421-Parameter-Order-Dialog) dialog appears.

   ![Parameter Order dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909138967/prmodr.gif)
3. Make use of the Move Up and Move Down buttons to adjust the order of the parameters, or simply drag and drop the parameters in the Parameters box.
   When a catalog contains a lot of parameters, it might be much easier by dragging and dropping.
4. Select **OK** to accept the changes.

**To adjust the parameter order for a specific report:**

1. Open the report containing parameters for which you would like to adjust the order, then select **Report** > **Parameter Order**. The Parameter Order dialog appears, listing only the parameters used in the currently open report.
2. Make use of the Move Up and Move Down buttons to adjust the order of the parameters, or simply drag and drop a parameter. The parameter order specified in the report will override the one in the catalog if they are different.
3. Select **OK** to apply the specified order.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069021-Importing-Parameter-Values)
