---
title: "Specifying Parameter Values"
id: 1500009724202
section: "Run and Schedule Reports Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values
updated_at: 2021-07-25T07:18:42Z
---

# Specifying Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751141-Importing-and-Exporting-Scheduled-Tasks)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724642-Web-Report-Studio)

# Specifying Parameter Values

When running or scheduling reports with parameters, you need to specify values for the parameters. The way to specify a parameter value varies according to the type and properties of the parameter. Here are several ways you can use to specify parameter values:

* ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")In the parameter value combo box, select the down arrow ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) and then select the required value from the drop-down list.

  To ensure performance, by default at most 500 values are listed. When the listed values are just a part of the values of the parameter, after you scroll down to the bottom of the list, more values (500 at most) will be automatically loaded into the drop-down list.

  You can make use of the Sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936770711/btn_sort2.gif) to display the values in the ascending or descending order for easy look-up, and search for the required value conveniently in the search box. To cancel the search, clear the input text or select ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif) in the search box.

  When a parameter's values are encrypted, the value drop-down list will be disabled. In this case, if the Hide Parameter Value check box is available, you can clear it to enable the drop-down list to view and select the required value.
* Type the value manually in the parameter value text box if the parameter allows for type-in values but not multiple values.
* Select the down arrow ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) in the parameter value combo box to [specify multiple values](#MultiValue) if the parameter allows for multiple values.
* Select or clear the check box to specify a Yes/No value.
* Select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) to [specify a date and time value](#DateTime).

**Note:** You are recommended not to use blank as the thousands separator in Number-typed parameter values under French locale, otherwise your input will not be correctly recognized because of a JVM bug. For details, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

Select the following links to view the topics:

* [Specifying Multiple Values for a Parameter](#MultiValue)
* [Setting Values for Date/Time/DateTime Parameters](#DateTime)
* [Customizing the Default Parameter Values](#DefaultParam)
* [Saving Parameter Values for Reuse](#Reuse)

## Specifying Multiple Values for a Parameter

For a parameter that allows for multiple values (the parameter's Allow Multiple Values property is true), you can specify one or more values to it.

1. Select the down arrow ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) in the value combo box of the parameter. Report Server displays the [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009747441-Enter-Values) dialog box.

   ![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942483991/entervlu.gif)
2. If the parameter's Enable the "All Values" Option property is true, the All Values check box is available and by default it is selected. It means to apply all values to the parameter. When the parameter is inserted as a field into a report and All Values is selected as the value, the field will show the string "All". If you do not want to apply all values to the parameter, deselect the **All Values** check box and then specify the
   desired values as shown in the following steps.
3. Select the required values in the Available Values box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404942476823/btn_add.gif) to add them to the Selected Values box; to add all the listed values, select ![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404936770967/btn_addall.gif).

   ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")To ensure performance, by default at most 500 values are listed in the Available Values box. When the listed values are just a part of the values of the parameter, after you scroll down to the bottom of the list, more values (500 at most) will be automatically loaded into the list. You can make use of the Sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936770711/btn_sort2.gif) to display the values in the ascending or descending order for easy look-up, and the Search button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif) to search for the required values conveniently. To cancel the search and close the search box, select ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif) in it.

   If some added values are not wanted, select them in the Selected Values box and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404936763159/btn_rmv.gif) to remove them; to remove all added values, select ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404942484247/btn_rmvall.gif).
4. When the parameter's Allow Type-in of Value property is true, the Enter Values text box is available. You can type a value manually and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404942476823/btn_add.gif) next to add it to the Selected Values box. When the parameter is bound with a column, but the display column is different from the bound column, make sure the value you type is that of the bound column. If the parameter is of the Date, DateTime, or Time type, you can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) to specify a date and time value using the calendar.

   ![Enter Values dialog - allow type in](https://devnet.logianalytics.com/hc/article_attachments/4404942484503/wkrpt_prmtr_entervlu.gif)
5. Select **OK** to select the specified values for the parameter.

## Setting Values for Date/Time/DateTime Parameters

When specifying values for a parameter of the Date, DateTime, or Time type which allows for type-in values (the parameter's Allow Type-in of Value property is true), you can make use of the calendar to select a date and time as the value, or customize a dynamic date and time value by creating an expression using Logi Report's built-in Date/Time functions. For example you might want the start date to be always 7 days ago and the end date to be today, you can then customize the value for the Start Date parameter by defining the expression as `dateadd('d', -7, today())`, and use the expression `today()` for the End Date parameter. Expressions have higher priority than values specified using the calendar.

**To select a date and time value from the calendar:**

1. Select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) for the parameter. Report Server displays the following dialog box.

   ![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942484759/wkrpt_prmtr_clndr.gif)
2. In the calendar specify the month, year, and day accordingly.
3. To make the calendar always shows the current date when it is accessed, select the **Use Today as Default** option. When this option is unselected, the default is the same as the value shown in the parameter's value box.
4. If the parameter is of DateTime type, the time setting is available. From the Display Time Format drop-down list, specify in which format to display the time, 12 hour or 24 hour (each time when the calendar is accessed, the default selected format is always 12 hour), then select the hour, minute and second time from the corresponding drop-down lists and choose whether it is AM or PM.

   ![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936771223/wkrpt_prmtr_clndrtm.gif)
5. Select **OK** to add the value.

**To customize a dynamic date and time value by creating an expression:**

1. Select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) for the parameter. Report Server displays the following dialog box (if the right section of the dialog box is not displayed, select **>>** on the bottom left corner to expand it).

   ![Calendar dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942485015/wkrpt_prmtr_exprsn.gif)
2. The Template drop-down list provides some predefined expressions for you to use. You can customize your own expression either based on an existing template or by directly editing the contents in the Expression text box.
3. You can make use of Logi Report's built-in Date/Time functions in the expression. First put the cursor where you want to insert the function in the Expression text box, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404942451479/btn_chsr2.gif) next to the Template drop-down list to access the function list, and then select the required function to insert it in the Expression text box.
4. The Preview box calculates the result of the current expression. Each time you modify the expression, you can select in the box to refresh the result. The date/time in the calendar on the right can be synchronized with the date/time calculated by a valid expression. If it is an invalid expression, an error message will be shown in the box and no change will be made to the calendar and the currently selected date/time will be remained in the calendar.
5. Select **OK** to add the value.

After you use an expression to specify the value, when you hover the mouse pointer over this value, a tip will appear showing its expression. Select on the value, the expression will be displayed in the value text box. You can edit the expression in the text box directly if you want. After editing, when you select elsewhere outside of the value text box:

* If the edited expression is correct, a new value calculated by the expression will be displayed in the parameter value text box.
* If the edited expression is wrong, no value will be created and the expression itself will be displayed and highlighted in red in the value text box. Correct the expression, or select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) to specify a value using the calendar.

When running reports via URLs, you can also use expressions to specify date and time parameter values. The format is
Parameter\_Name={"exp":"Complete\_Expression\_String", "SelectedDate":"'MM/dd/yyyy"}. If the expression does not contain the function SelectedDate(), there is no need to add this part - "SelectedDate":"'MM/dd/yyyy" and the format is Parameter\_Name={"exp":"Complete\_Expression\_String"}. For example, to specify p\_EndDate=today(), write it as `p_EndDate={"exp":"today()"}`. The following is an example:

`http://localhost:8888/jinfonet/runReport.jsp?jrs.cmd=jrs.web_vw&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fABC.cls&jrs.param$P_StartDate=01/01/2016&jrs.param$p_EndDate={"exp":"today()"}&jrs.result_type=8`

## Customizing the Default Parameter Values

Logi Report Server allows you to pre-customize the default parameter values for a report before running it. However to use this feature, you should make sure both [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#DefaultParam) and [Enable Hiding Initial Parameter Dialog For](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#HideParam) the corresponding report type are selected in the server profile.

1. Browse to the target report, then do one of the following:
   * Put the mouse pointer over the report row and select the **Parameter Settings** button ![Parameter Settings button](https://devnet.logianalytics.com/hc/article_attachments/4404936771607/btn_srv_prmset.gif) on the floating toolbar.
   * Select the report row, right-click in the row and select **Parameter Settings** from the shortcut menu.
   * Select the row the report is in, then on the task bar of the Resources page, select **Tools** > **Parameter Settings**.

   The [Parameter Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009747681-Parameter-Settings) dialog box is then displayed.

   ![Parameter Settings dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942485271/prmset.gif)
2. All the parameters of the report are listed. Specify the value for each parameter as required.
3. Select **Save as default** to save the specified values as the default values for the parameters (this option is not available when [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#DefaultParam) the corresponding report type is unselected in the server profile).

   The Save as default option is an action and takes effect after the task is submitted. Its initial status is always unselected.
4. You can select **Re-enable Parameter Screen** to show the Enter Parameter Values dialog box again after it has been hidden. When this option is unselected, the next time the report runs via operation in the Logi Report Server console, the Enter Parameter Values dialog box will not be prompted, instead Logi Report Server will apply the default values of the parameters in the parameters' definition or the last-time saved default values for the parameters on Logi Report Server to run the report directly. However, if the last-time saved default values cannot completely match the report parameters, the Enter Parameter Values dialog box will still be displayed.
5. To reset the parameters, use the Reset button, which varies on different situations:
   * When Save as default is available in the dialog box, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
     + **Original Default Values**  
        The default values defined in the parameters' definition.
     + **User Defined Default Values**  
        Your last-time saved default values.
   * When Save as default is unavailable in the dialog box, the Reset button contains only the text part. Selecting it will reset the values to the original default values.
6. Select **OK** to apply the parameter values for the report.

The Save as default and Re-enable Parameter Screen options in the dialog box are user-report level settings, that is to say, they take effect when both the same user and report are matched. This also applies to admin users, and therefore admin users cannot customize the settings for all users.

**Note:** If you just edit the parameter values in the dialog box and select OK, the new values will be meaningless. Only when you select **Save as default** and select OK, can the values be saved as default values to the report.

## Saving Parameter Values for Reuse

When specifying parameter values for reports, you may want to save the specified parameter values for reuse next time. Logi Report provides two ways of saving. One is users decide when and which parameter values to save, the other is Logi Report saves each applied or submitted parameter values automatically. When the saved number in either way reaches the maximum, the oldest record will be removed. The number is calculated on a user-report basis. Take a report with two parameters for an example, supposing the maximum number is set to 3. Each user can save at most three groups of parameter values for the report, with each group containing the values of the two parameters.

To switch on the function of saving parameter values, you need to configure the server profile: select the **Yes** check box for the option [Enable Saving Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#SaveParam), select a way to do the saving: Manually or Automatically, and then specify a maximum number to limit the saved value groups via the option [Maximum Number of Auto Complete Parameters List](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#MaxNo) for each user-report pair.

**Manually saving parameter values**

When you have chosen to manually save parameter values, the Use Saved Values button **![Use Saved Values button](https://devnet.logianalytics.com/hc/article_attachments/4404942485527/btn_srv_ussvvlu.gif)** will be available at the upper right corner of the parameter page. By selecting this button, you will get the following:

* **Value list**  
   The value list contains all the parameter value groups you have saved for the report. Select a group to apply all the values in the group to the corresponding parameters. You can also remove any of the unwanted value group by selecting it from the list and then selecting ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404942446871/btn_dltobj.gif) next to the value list.
* **![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404942445847/btn_save.gif) Save Values**  
   Saves the current displayed parameter values as a group for reuse afterwards. To do this, type a name for the group in the text box which shows "Save current values into list" and then select **![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404942445847/btn_save.gif)**. The saved group will then be added into the value list.

**Using automatically saved parameter values**

When you have chosen to automatically save parameter values, each time a user submits a group of parameter values to a report, the group is saved by Logi Report automatically. The next time the same user runs the report, the auto saved parameter values will be available in the parameters' value lists for selection.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751141-Importing-and-Exporting-Scheduled-Tasks)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724642-Web-Report-Studio)
