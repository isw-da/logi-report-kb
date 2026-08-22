---
title: "Specifying Parameter Values"
id: 28891708429197
section: "Running and Scheduling Reports Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891708429197-Specifying-Parameter-Values
updated_at: 2026-02-26T02:13:43Z
source_host: docs-report.zendesk.com
---
# 
Specifying Parameter Values 

When running or scheduling reports with parameters, you need to specify values for the parameters. This topic describes how you can update one or more values, date and time values, and default values, and save values for parameters.

The way to specify a parameter value varies according to the type and properties of the parameter. Here are several ways you can use to specify parameter values:

- In the parameter value combo box, select the down arrow  and then select a value from the drop-down list.
        To ensure performance, Server lists at most 500 values by default. When the listed values are just a part of the values of the parameter, after you scroll down to the bottom of the list, Server loads more values (500 at most) automatically into the drop-down list.

You can make use of the Sort button  to display the values in the ascending or descending order for easy look-up, and search for the required value conveniently in the search box. To cancel the search, clear the input text or select the delete button  in the search box.

When encrypting a parameter's values, Server disables the value drop-down list. In this case, if Server displays Hide Parameter Value, you can clear it to enable the drop-down list to view and select a value.

- Type the value manually in the parameter value text box if the parameter enables type-in values but not multiple values.

- Select the down arrow  in the parameter value combo box to specify multiple values if the parameter enables multiple values. 

- Select or clear the checkbox to specify a Yes or No value. 

- Select the Calendar icon  to specify a date and time value.

You should not use blank as the thousands separator in Number-typed parameter values under French locale, otherwise Server does not correctly recognize your input because of a JVM bug. For more information, see http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618. 

This topic contains the following sections:

- 
                    Specifying Multiple Values for a Parameter
                

- 
                    Setting Values for Date/Time/DateTime Parameters
                

- 
                    Customizing the Default Parameter Values
                

- 
                    Saving Parameter Values for Reuse
                

## 
Specifying Multiple Values for a Parameter

For a parameter that enables multiple values (the parameter's Allow Multiple Values property is true), you can specify one or more values to it.

- Select the down arrow  in the value combo box of the parameter. Server displays the Enter Values dialog box.
    

- If the parameter's Enable the "All Values" Option property is true, All Values is available. Server selects it by default. It means to apply all values to the parameter. When you inserted the parameter as a field into a report and selected All Values, the field shows the string All. If you do not want to apply all values to the parameter, clear All Values and then specify the values you want as follows.

- Select the values you want in the Available Values box and select the Add button  to add them to the Selected Values box; to add all the listed values, select the Add All button .    To ensure performance, by default, Server lists at most 500 values in the Available Values box. When the listed values are just a part of the values of the parameter, after you scroll down to the bottom of the list, Server automatically loads more values (500 at most) into the list. You can make use of the Sort button  to display the values in the ascending or descending order for easy look-up, and the Search button  to search for the required values conveniently. To cancel the search and close the search box, select the delete button  in it.

For values you do not want, select them in the Selected Values box and select the button  to remove them; to remove all added values, select the button . 

- When the parameter's Allow Type-in of Value property is true, the Enter Values text box is available. You can type a value manually and select the button  next to add it to the Selected Values box. When the parameter is bound with a column, but the display column is different from the bound column, make sure the value you type is that of the bound column. If the parameter is of the Date, DateTime, or Time type, you can also select the Calendar icon  to specify a date and time value using the calendar.
    

- Select OK to select the specified values for the parameter.

## 
Setting Values for Date/Time/DateTime Parameters

When specifying values for a parameter of the Date, DateTime, or Time type which enables type-in values (the parameter's Allow Type-in of Value property is true), you can make use of the calendar to select a date and time as the value, or customize a dynamic date and time value by creating an expression using Report's built-in Date/Time functions. For example you may want the start date to be always 7 days ago and the end date to be today, you can then customize the value for the parameter Start Date by defining the expression as dateadd('d', -7, today()), and use the expression today() for the parameter End Date. Expressions have higher priority than values you selected using the calendar.

To select a date and time value from the calendar:

- Select the Calendar icon  for the parameter. Server displays the following dialog box.
    

- In the calendar specify the month, year, and date accordingly.

- To make the calendar always show the current date when you access it, select Use Today as Default. Otherwise, the default date is the value Server displays in the parameter's value box.

- If the parameter is of DateTime type, the time setting is available. From the Display Time Format drop-down list, select in which format to display the time, 12 hour or 24 hour. However, each time you access the calendar, the default format is always 12 hour.     

- Select the hour, minute, and second time from the corresponding drop-down lists.

- Choose AM or PM.

- Select OK to add the value. 

To customize a dynamic date and time value by creating an expression:

- Select the Calendar icon  for the parameter. Server displays the following dialog box.    

- If Server does not display the right section of the dialog box, select >> at the lower left corner to expand it.

- The Template drop-down list provides predefined expressions for you to use. You can customize your own expression either based on an existing template or by directly editing the contents in the Expression text box.

- You can make use of Report's built-in Date/Time functions in the expression. First put the cursor where you want to insert the function in the Expression text box, select the ellipsis button  next to the Template text box to access the function list, and then select a function to insert it into the Expression text box.

- The Preview box calculates the result of the current expression. Each time you modify the expression, you can select in the box to refresh the result. Server synchronizes the date/time on the left in the calendar with the date/time calculated by a valid expression. If it is an invalid expression, Server displays an error message in the box and does not make changes to the calendar, and the currently selected date/time remains in the calendar.

- Select OK to add the value.

 After you use an expression to specify the value, when you hover the mouse pointer over this value, a tip displays showing its expression. Select on the value, the expression displays in the value text box. You can edit the expression in the text box directly if you want. After editing, when you select elsewhere outside the value text box: 

- If the edited expression is correct, a new value calculated by the expression displays in the parameter value text box.

- If the edited expression has errors, Server does not create a value, and displays the expression itself and highlights it in red in the value text box. Correct the expression, or select the Calendar icon  to specify a value using the calendar.

When running reports via URL, you can also use expressions to specify date and time parameter values. The format is 
 Parameter_Name={"exp":"Complete_Expression_String", "SelectedDate":"'MM/dd/yyyy"}. 

If the expression does not contain the function SelectedDate(), you do not need to add this part - "SelectedDate":"'MM/dd/yyyy", and the format is Parameter_Name={"exp":"Complete_Expression_String"}. For example, to specify p_EndDate=today(), write it as p_EndDate={"exp":"today()"}. See the following example:

http://localhost:8888/jinfonet/runReport.jsp?jrs.cmd=jrs.web_vw&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fABC.cls&jrs.param$P_StartDate=01/01/2016&jrs.param$p_EndDate={"exp":"today()"}&jrs.result_type=8

## 
Customizing the Default Parameter Values

Report Server enables you to pre-customize the default parameter values for a report before running it. To use this feature, make sure you clear neither Enable Setting Default Parameter Values For nor Enable Hiding Initial Parameter Dialog For the corresponding report type in the server profile.

- Browse to the target report, then do one of the following:
    
- Put the mouse pointer over the report row and select the Parameter Settings button  on the floating toolbar.

- Select the report row, right-click in the row and select Parameter Settings from the shortcut menu.

- Select the report row, then select Tools > Parameter Settings on the task bar.

Server displays the Parameter Settings dialog box. 

- Server lists all the parameters of the report. Update the value for each parameter if you want.

- Select Save as default to save the specified values as the default values for the parameters. Server displays this option when you did not clear  Enable Setting Default Parameter Values For the corresponding report type in the server profile.
    The Save as default option is an action and takes effect after you select OK in the dialog box. Its initial status is always cleared.

- Select Re-enable Parameter Screen if you want Server to display the Enter Parameter Values dialog box when you run the report from the Server Console. Otherwise, Server does not display the Enter Parameter Values dialog box, but instead applies the default values of the parameters as in the parameters' definition or the default values that you saved last time for the parameters on Server to run the report directly. However, if the last-time saved default values cannot completely match the report parameters, Server still displays the Enter Parameter Values dialog box.

- To reset the parameters, use the Reset button, which varies with different situations:
    
- When Save as default is available in the dialog box, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, Server resets the values to the original default values.
        
- 
Original Default Values
            The default values defined in the parameters' definition.

- 
User Defined Default Values
            The default values you saved last time.

- When Save as default is unavailable in the dialog box, the Reset button contains only the text part. Selecting it will reset the values to the original default values.

- Select OK to apply the parameter values for the report.

The Save as default and Re-enable Parameter Screen options in the dialog box are user-report level settings. They take effect when both the same user and report are matched. This also applies to administrators, and therefore administrators cannot customize the settings for all users.

If you just edit the parameter values in the dialog box and select OK, the new values are meaningless. Only when you select Save as default and select OK, can Server save the values as default values to the report.

## 
Saving Parameter Values for Reuse

When specifying parameter values for reports, you may want to save the specified parameter values for reuse next time. Report provides two ways of saving. One is that you decide when and which parameter values to save for a report, the other is that Server automatically saves the parameter values  that you applied or submitted each time for a report. When the saved number in either way reaches the maximum, Server removes the oldest record. Server calculates the number on a user-report basis. Take a report with two parameters for an example, supposing the maximum number is 3. Each user can save at most three groups of parameter values for the report, with each group containing the values of the two parameters.

To switch on the function of saving parameter values, you need to configure the server profile: select Yes for the option Enable Saving Parameter Values, select a way to do the saving: Manually or Automatically, and then specify a maximum number to limit the saved value groups via the option Maximum Number of Auto Complete Parameters List for each user-report pair.

Manually saving parameter values

When you have chosen to manually save parameter values, Server displays the Use Saved Values button  at the upper right corner of the parameter page. By selecting this button, you will get the following: 

- 
Value list
    The value list contains all the parameter value groups you have saved for the report. Select a group to apply all the values in the group to the corresponding parameters. You can also remove any of the unwanted value group by selecting it from the list and then selecting the delete button  next to the value list. 

- 
 Save Values
    Saves the current displayed parameter values as a group for reuse afterwards. To do this, type a name for the group in the text box which shows "Save current values into list" and then select the Save Values button . Server adds the saved group into the value list.

Using automatically saved parameter values

When you have chosen to automatically save parameter values, each time a user submits a group of parameter values to a report, Server saves the group automatically. The next time the same user runs the report, the auto saved parameter values will be available in the parameters' value lists for selection.
