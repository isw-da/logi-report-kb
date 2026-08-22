---
title: "Specifying Parameter Values"
id: 1500009692442
section: "Running and Scheduling Reports Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692442-Specifying-Parameter-Values
updated_at: 2021-11-03T06:56:35Z
---

# Specifying Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692522-Importing-and-Exporting-Scheduled-Tasks)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719001-Web-Report-Studio)

# Specifying Parameter Values

When running or scheduling reports with parameters, you need to specify values for the parameters. The way to specify a parameter value varies according to the type and properties of the parameter. Here are several ways you can use to specify parameter values:

* In the parameter value combo box, select the required one from the drop-down list or input the value manually.

  When a parameter's values are encrypted, the value drop-down list will be disabled. In this case, if the Hide Parameter Value checkbox is available, you can uncheck it to enable the drop-down list to view and select the required value.
* Select or unselect the checkbox to specify a Yes/No value.
* Select the button ![Enter Values](https://devnet.logianalytics.com/hc/article_attachments/4412112530711/btn_chsr3.gif) to [specify multiple values](#MultiValue) if the parameter allows for multiple values.
* Select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif) to [specify a date and time value](#DateTime).

**Note:** You are recommended not to use blank as the thousands separator in Number-typed parameter values under French locale, otherwise your input will not be correctly recognized because of a JVM bug. For details, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

**Tip:** Administrators can limit the number of values shown in the value list of the parameters that are bound with columns by setting the [Max Records in Parameter Value List](https://devnet.logianalytics.com/hc/en-us/articles/1500009712361-Configuring-Advanced-Server-Settings#ParameterMaxRecords) option in the Administration > Configuration > Advanced page in the server console.

Below is a list of the sections covered in this topic:

* [Specifying Multiple Values for a Parameter](#MultiValue)
* [Setting Values for Date/Time/DateTime Parameters](#DateTime)
* [Customizing the Default Parameter Values](#DefaultParam)
* [Saving Parameter Values for Reuse](#Reuse)

## Specifying Multiple Values for a Parameter

For a parameter that allows for multiple values (the parameter's Allow Multiple Values property is true), you can specify one or more values to it.

1. Select ![Enter Values](https://devnet.logianalytics.com/hc/article_attachments/4412112530711/btn_chsr3.gif) next to the value text box of the parameter. The [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009714661-Enter-Values) dialog appears.

   ![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112530967/entervlu.gif)
2. If the parameter's Enable the "All" Option property is true, the All checkbox is available and by default it is selected. It means to apply the "All" value to the parameter. When the parameter is inserted as a field into a report and All is selected as the value, the field will show the string "All". If you do not want to apply the "All" value to the parameter, deselect the **All** checkbox and then specify the
   desired values as shown in the following steps.
3. Select the required values in the Available Values box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4412112531223/btn_add.gif) to add them to the Selected Values box; to add all the available values, select ![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4412112531479/btn_addall.gif). You can make use of the Search text box to
   search for the required values among the available values: type in the keyword
   and the available values that contain the keyword will be listed with the keyword highlighted in the values.

   If some added values are not wanted, select them in the Selected Values box and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4412112531735/btn_rmv.gif) to remove them; to remove all added values, select ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4412112531991/btn_rmvall.gif).
4. When the parameter's Allow Type-in of Value property is true, the Search text box will be replaced by the Enter Values text box. You can type in a value manually and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4412112531223/btn_add.gif) next to add it to the Selected Values box. When the parameter is bound with a column, but the display column is different from the bound column, make sure the value you enter is that of the bound column. If the parameter is of the Date, Time or DateTime type, you can also select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif) to specify a date and time value.

   ![Enter Values dialog - allow type in](https://devnet.logianalytics.com/hc/article_attachments/4412131414551/wkrpt_prmtr_entervlu.gif)
5. Select **OK** to select the specified values for the parameter.

## Setting Values for Date/Time/DateTime Parameters

When specifying value for a parameter of the Date, Time or DateTime type which allows for type-in values (the parameter's Allow Type-in of Value property is true), you can make use of the calendar to select a date and time as the value, or customize a dynamic date and time value by creating an expression using Logi JReport's built-in Date/Time functions. For example you might want the start date to always be 7 days ago and the end date to be today, you can then customize the value for the start date parameter as `dateadd('d', -7, today())` and `today()` for the end date parameter. The expression has higher priority than the value specified using the calendar.

**To select a date and time value from the calendar:**

1. Select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif) next to the value text box of the parameter. The following dialog appears.

   ![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112532375/wkrpt_prmtr_clndr.gif)
2. In the calendar specify the month, year and day accordingly.
3. To make the calendar always shows the current date when it is accessed, check the **Use Today as Default** option. When this option is unchecked, the default is the same as the value shown in the parameter's value box.
4. If the parameter is of DateTime type, the time setting is available. From the Display Time Format drop-down list, specify in which format to display the time, 12 hour or 24 hour (each time when the calendar is accessed, the default selected format is always 12 hour), then select the hour, minute and second time from the corresponding drop-down lists and choose whether it is AM or PM.

   ![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131414807/wkrpt_prmtr_clndrtm.gif)
5. Select **OK** to add the value.

**To customize a dynamic date and time value by creating an expression:**

1. Select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif) next to the value text box of the parameter. The following dialog appears (if the right section of the dialog is not displayed, select **>>** on the bottom left corner to expand it).

   ![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4412139522711/wkrpt_prmtr_exprsn.gif)
2. The Template drop-down list provides some predefined expressions for you to use. You can customize your own expression either based on an existing template or by directly editing the contents in the Expression text box.
3. You can make use of Logi JReport's built-in Date/Time functions in the expression. First put the cursor where you want to insert the function in the Expression text box, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4412139488919/btn_chsr2.gif) next to the Template drop-down list to access the function list, and then select the required function to insert it in the Expression text box.
4. The Preview box calculates the result of the current expression. Each time you modify the expression, you can select in the box to refresh the result. The date/time in the calendar on the right can be synchronized with the date/time calculated by a valid expression. If it is an invalid expression, an error message will be shown in the box and no change will be made to the calendar and the currently selected date/time will be remained in the calendar.
5. Select **OK** to add the value.

After you use an expression to specify the value, when you hover the mouse pointer over this value, a tip will appear showing its expression. Select on the value, the expression will be displayed in the value text box. You can edit the expression in the text box directly if you want. After editing, when you select elsewhere outside of the value text box:

* If the edited expression is correct, a new value calculated by the expression will be displayed in the parameter value text box.
* If the edited expression is wrong, no value will be created and the expression itself will be displayed and highlighted in red in the value text box. Correct the expression, or select the calendar button to specify a value.

When running reports via URLs, you can also use expressions to specify date and time parameter values. The format is
Parameter\_Name={"exp":"Complete\_Expression\_String", "SelectedDate":"'MM/dd/yyyy"}. If the expression does not contain the function SelectedDate(), there is no need to add this part - "SelectedDate":"'MM/dd/yyyy" and the format is Parameter\_Name={"exp":"Complete\_Expression\_String"}. For example, to specify p\_EndDate=today(), write it as `p_EndDate={"exp":"today()"}`. The following is an example:

`http://localhost:8888/jinfonet/runReport.jsp?jrs.cmd=jrs.web_vw&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fABC.cls&jrs.param$P_StartDate=01/01/2016&jrs.param$p_EndDate={"exp":"today()"}&jrs.result_type=8`

## Customizing the Default Parameter Values

Logi JReport Server allows you to pre-customize the default parameter values for a report before running it. However to use this feature, you should make sure both [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#DefaultParam) and [Enable Hiding Initial Parameter Dialog For](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#HideParam) the corresponding report type are selected in the server profile.

1. Browse to the target report, then do one of the following:
   * Put the mouse pointer over the report row and select the **Parameter Settings** button ![Parameter Settings button](https://devnet.logianalytics.com/hc/article_attachments/4412131415063/btn_srv_prmset.gif) on the floating toolbar.
   * Select the report row, right-click in the row and select **Parameter Settings** from the shortcut menu.
   * Select the row the report is in, then on the task bar of the Resources page, select **Tools** > **Parameter Settings**.

   The [Parameter Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009688942-Parameter-Settings) dialog is then displayed.

   ![Parameter Settings dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112532631/prmset.gif)
2. All the parameters of the report are listed. Specify the value for each parameter as required.
3. Check **Save as default** to save the specified values as the default values for the parameters (this option is not available when [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#DefaultParam) the corresponding report type is unchecked in the server profile).

   The Save as default option is an action and takes effect after the task is submitted. Its initial status is always unchecked.
4. Check **Re-enable Parameter Screen**  to show the Enter Parameter Values dialog again after it has been hidden if required. When this option is unchecked, the next time the report runs via operation in the Logi JReport Server console, the Enter Parameter Values dialog will not be prompted, instead Logi JReport Server will apply the default values of the parameters in the parameters' definition or the last-time saved default values for the parameters on Logi JReport Server to run the report directly. However, if the last-time saved default values cannot completely match the report parameters, the Enter Parameter Values dialog will still be displayed.
5. To reset the parameters, use the Reset button, which varies on different situations:
   * When Save as default is available in the dialog, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
     + **Original Default Values**  
        The default values defined in the parameters' definition.
     + **User-Defined Default Values**  
        Your last-time saved default values.
   * When Save as default is unavailable in the dialog, the Reset button contains only the text part. Selecting it will reset the values to the original default values.
6. Select **OK** to apply the parameter values for the report.

The Save as default and Re-enable Parameter Screen options in the dialog are user-report level settings, that is to say, they take effect when both the same user and report are matched. This also applies to admin users, and therefore admin users cannot customize the settings for all users.

**Note:** If you just edit the parameter values in the dialog and select OK, the new values will be meaningless. Only when you check Save as default and select OK, can the values be saved as default values to the report.

## Saving Parameter Values for Reuse

When specifying parameter values for reports, you may want to save the specified parameter values for reuse next time. Logi JReport provides two ways of saving. One is users decide when and which parameter values to save, the other is Logi JReport saves each applied or submitted parameter values automatically. When the saved number in either way reaches the maximum, the oldest record will be removed. The number is calculated on a user-report basis. Take a report with two parameters for an example, supposing the maximum number is set to 3. Each user can save at most three groups of parameter values for the report, with each group containing the values of the two parameters.

To switch on the function of saving parameter values, you need to configure the server profile: check the **Yes** checkbox for the option [Enable Saving Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#SaveParam), select a way to do the saving: Manually or Automatically, and then specify a maximum number to limit the saved value groups via the option [Maximum Number of Auto Complete Parameters List](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#MaxNo) for each user-report pair.

**Manually saving parameter values**

When you have chosen to manually save parameter values, the Use Saved Values button **![Use Saved Values button](https://devnet.logianalytics.com/hc/article_attachments/4412131415319/btn_srv_ussvvlu.gif)** will be available at the upper right corner of the parameter page. By selecting this button, you will get the following:

* **Value list**  
   The value list contains all the parameter value groups you have saved for the report. Select a group to apply all the values in the group to the corresponding parameters. You can also remove any of the unwanted value group by selecting it from the list and then selecting ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112483991/btn_dltobj.gif) next to the value list.
* **![Save button](https://devnet.logianalytics.com/hc/article_attachments/4412112482455/btn_save.gif) Save Values**  
   Saves the current displayed parameter values as a group for reuse afterwards. To do this, type a name for the group in the text box which shows "Save current values into list" and then select **![Save button](https://devnet.logianalytics.com/hc/article_attachments/4412112482455/btn_save.gif)**. The saved group will then be added into the value list.

**Using automatically saved parameter values**

When you have chosen to automatically save parameter values, each time a user submits a group of parameter values to a report, the group is saved by Logi JReport automatically. The next time the same user runs the report, the auto saved parameter values will be available in the parameters' value lists for selection.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692522-Importing-and-Exporting-Scheduled-Tasks)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719001-Web-Report-Studio)
