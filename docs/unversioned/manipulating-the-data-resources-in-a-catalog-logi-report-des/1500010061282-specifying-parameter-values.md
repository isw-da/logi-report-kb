---
title: "Specifying Parameter Values"
id: 1500010061282
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061282-Specifying-Parameter-Values
updated_at: 2021-07-23T19:16:19Z
---

# Specifying Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061262-Importing-Parameter-Values)

# Specifying Parameter Values

When you [preview](https://devnet.logianalytics.com/hc/en-us/articles/1500010101341-Previewing-Reports), [print or, export](https://devnet.logianalytics.com/hc/en-us/articles/1500010060882-Printing-and-Exporting-Reports) a report with parameters, or [preview a query](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog#Preview) that contains parameters, Designer displays the Enter Parameter Values dialog box for you to specify values of the parameters, which lists all the parameters used in the report or query and their prompting information. This topic describes how you can specify values for parameters of different types and customize the display order of the parameters in the Enter Parameter Values dialog box.

This topic contains the following sections:

* [General Methods for Specifying Parameter Values](#General)
* [Specifying Multiple Values for a Parameter](#Multiple)
* [Setting Values for Date/Time/DateTime Parameters](#Date)
* [Customizing the Display Order of Parameters](#Order)

## General Methods for Specifying Parameter Values

The method to specify a parameter value varies with the type and properties of the parameter. The following shows the general methods you can use to specify parameter values.

![Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856854423/enterprmvlu.gif)

* Type the value manually in the parameter value text box if the parameter allows for type-in values but not multiple values.
* Select or clear the checkbox to specify a Yes/No value.
* Select the **calendar** button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to [specify a date and time value](#Date).
* Select the **drop-down** button ![Drop-down button](https://devnet.logianalytics.com/hc/article_attachments/4404848444823/btn_drpdwn.gif) and [specify multiple values](#Multiple) if the parameter allows for multiple values.
* Select ![Drop-down button](https://devnet.logianalytics.com/hc/article_attachments/4404848444823/btn_drpdwn.gif) and then select the required value from the drop-down list. When a parameter's [Encrypt Parameter Value](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog#Encrypt) property is true, Designer disables the value drop-down list by default, in which case, if the [Hide Parameter Value](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog#Unencrypted) checkbox is available, you can clear it to enable the drop-down list.

  You can make use of the icons on the top of the value drop-down list to locate the value you need.

  ![Parameter Value Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4404848445079/prmtr_value_list.gif)

  + To sort the values in ascending or descending order for easy look-up, select the **Sort** icon![Sort icon](https://devnet.logianalytics.com/hc/article_attachments/4404848378007/btn_sort2.gif), then select the corresponding item from the drop-down menu. The default order is No Sort, which means the values are listed as how you add them if the parameter is a type-in parameter, or based on their original order in the database if the parameter is bound with a column. The change of sort order is a one-off action that Designer does not save after you exit the dialog box, meaning, each time when you open the dialog box, Designer always applies No Sort to the values.
  + To search for a value, select the **Search** icon ![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4404856807959/btn_srch.gif). In the search box that appears, type the text you want to search for and Designer lists the values containing the matched text.

  You can make use of the following options in the search box:

  - ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404848393111/btn_srchbox_adv.gif)**Drop-down icon**  
    Select to list more search options.
    * **Highlight All**   
      Select to highlight all matched text.
    * **Match Case**   
      Select to search for text that meets the case of the typed text.
    * **Match Whole Word**   
      Select to search for text that looks the same as the typed text.
  - ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif)**Delete icon**  
    Select to close the search box and cancel the search.+ To close the value drop-down list, select the **Close** icon ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif).

  For performance concern, Designer lists at most 500 values in the drop-down list. When the listed values are just a part of the values of the parameter, after scrolling down to the bottom of the list, you can select the **More** button appearing at the end to load more values (500 at most) into the drop-down list.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) You are recommended not to use blank as the thousands separator in parameter values of the Number type under French locale; otherwise, Logi Report cannot correctly recognize your input due to a JVM bug. For more information, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

## Specifying Multiple Values for a Parameter

For a parameter that allows for multiple values (the parameter's Allow Multiple Values property is true), you can specify one or more values to it.

1. Select ![Drop-down button](https://devnet.logianalytics.com/hc/article_attachments/4404848444823/btn_drpdwn.gif) next to the value text box of the parameter. Designer displays the [Enter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058922-Enter-Values-Dialog-Box).

   ![Enter Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848445463/entervlu.gif)
2. If the Enable the "All Values" Option property of the parameter is true, the **All Values** checkbox is available and selected by default. It means to apply all values to the parameter, which can be all values of the parameter determined by Logi Report, all values in the database, or all the available values according to the [Scope of All Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog#AllScope) setting of the parameter. When you insert the parameter as a field into a report and select All Values as the value, the field shows the string "All" in the report.

   If you do not want to apply all values to the parameter, clear the **All Values** checkbox and then specify the values as shown in the following steps.
3. Select the required values in the **Available Values** box and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404856855063/btn_addarrow1.gif) to add them to the **Selected Values** box; to add all the available values, select the **Add All** button ![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404848446103/btn_addall1.gif). If some added values are not wanted, select them in the Selected Values box and select the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848446359/btn_rmvarrow1.gif) to remove them; to remove all added values, select the **Remove All** button ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404856855319/btn_rmvall1.gif). You can also make use of the **Sort**![Sort icon](https://devnet.logianalytics.com/hc/article_attachments/4404848378007/btn_sort2.gif) and **Search**![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4404856807959/btn_srch.gif) icons above the two boxes to display the values in the ascending or descending order, and to search for the required values as seen above.

   For performance concern, Designer lists at most 500 values in the Available Values box. When the listed values are just a part of the values of the parameter, after scrolling down to the bottom of the list, you can select the down arrow appearing at the end to load more values (500 at most) into the list.
4. When the parameter's Allow Type-in of Value property is true, the **Enter Values** text box is available. You can type a value manually and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404856855063/btn_addarrow1.gif) next to the text box to add it to the Selected Values box. If the parameter is bound with a column, but the display column is different from the bound column, make sure the value you specify is that of the bound column. If the parameter is of the Date, Time, or DateTime type, you can also select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to [specify a date and time value](#Date).
5. Select **OK** to select the specified values for the parameter.

## Setting Values for Date/Time/DateTime Parameters

When specifying value for a parameter of the Date, Time, or DateTime type which allows for type-in values (the parameter's Allow Type-in of Value property is true), you can make use of the calendar widget to select a date and time as the value, or customize a dynamic date and time value by creating an expression using Logi Report's built-in Date/Time functions. By using an expression, the defaults are always the dates that you want to use.
For example, you might want the start date to always be 7 days ago and the end date to be today, you can then customize the value for the start date parameter as `dateadd('d', -7, today())` and `today()` for the end date parameter. The expression has higher priority than the value specified using the calendar.

**To select a date and time value from the calendar:**

1. Select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) for the parameter. Designer displays the following dialog box.

   ![Calendar dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856855703/prmtr_value_clndr.gif)
2. In the calendar on the left, specify the month, year, and day accordingly.
3. If the parameter is of DateTime type, Designer displays the time settings. From the **Display Time Format** drop-down list, specify in which format to display the time, 12 hours or 24 hours (each time when you open the calendar widget, the default selected format is always 12 hours), then select the hour, minute, and second from the corresponding drop-down lists and choose whether it is **AM** or **PM**.
4. Select **OK** to add the value.

**To customize a dynamic date and time value by creating an expression:**

1. Select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) for the parameter. Designer displays the following dialog box (if the right section of the dialog box is not available,
   select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404848446999/btn_addarrow2.gif) on the bottom left corner to expand it).

   ![Calendar dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856855703/prmtr_value_clndr.gif)
2. The **Template** drop-down list provides some predefined expressions for you to use. You can customize your own expression either based on an existing template or by directly editing the contents in the **Expression** text box.
3. Make use of Logi Report's built-in [Date/Time](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#DateTime) functions in the expression. To display the functions, select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) next to the Template drop-down list, Designer then displays the [Expression dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096621-Expression-Dialog-Box).

   ![Expression dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856856087/exprss.gif)
4. The top text box in the Expression dialog box shows the current expression statement if there is. Put the cursor where you want to insert the function in the statement, then double-click the required function to insert it there. Select **OK** to close the dialog box.
5. The **Preview** box calculates the result of the current expression. Each time you modify the expression, you can select in the box to refresh the result. Designer can synchronize the date/time in the calendar on the right with the date/time calculated by a valid expression. If it is an invalid expression, Designer displays an error message in the box and makes no change to the calendar and remains the currently selected date/time in the calendar.
6. Select **OK** to add the value.

After you use an expression to specify the value, when you hover the mouse pointer over this value in the Enter Parameter Values dialog box, Designer displays a tip showing its expression. If you select in the value text box, Designer displays the expression in the text box. You can edit the expression in the text box directly if you want. After editing, when you select elsewhere outside of the value text box:

* If the edited expression is correct, Designer displays a new value calculated by the expression in the parameter value text box.
* If the edited expression is wrong, Designer does not create the value and instead displays the expression in red in the value text box for warning. In this case, you need to correct the expression, or select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to specify a value from the calendar.

## Customizing the Display Order of Parameters

By default, Designer lists the parameters in ascending alphabetic order in the Enter Parameter Values dialog box, thus the parameter "pEndDate" appears before "pStartDate" which would be very confusing to users. Designer enables you to customize the order of the parameters in the dialog box so that they can display in a more reasonable sequence. The order does not affect the display sequence of the parameters in the resource tree, which is determined by the [Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#Sort) setting in the Options dialog box.

You can customize the parameter display order at two levels: catalog and specific report. When you specify the order of parameters in a catalog, Designer applies the order to all reports using the catalog. If you define the order at both levels, the report level order has higher priority than the catalog level one.

**To adjust the parameter order for a catalog:**

1. Open the catalog containing parameters for which you would like to adjust the order.
2. In the Catalog Manager, expand a data source, select the **Parameters** node or any parameter in the node, then select **Parameter Order** on the Catalog Manager toolbar. Designer displays the [Parameter Order dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098221-Parameter-Order-Dialog-Box).

   ![Parameter Order dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856856343/prmodr.gif)
3. Make use of the **Move Up** and **Move Down** buttons to adjust the order of the parameters, or simply drag and drop the parameters in the **Parameters** box.
   When a catalog contains a lot of parameters, it might be much easier by dragging and dropping.
4. Select **OK** to accept the changes.

**To adjust the parameter order for a specific report:**

1. Open the report containing parameters for which you would like to adjust the order.
2. Select **Report** > **Parameter Order** on the menu tab. Designer displays the Parameter Order dialog box, which contains only the parameters used in the currently open report.
3. Make use of the Move Up and Move Down buttons to adjust the order of the parameters, or simply drag and drop a parameter. The parameter order specified in the report overrides the one in the catalog if they are different.
4. Select **OK** to apply the specified order.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061262-Importing-Parameter-Values)
