---
title: "Specifying Parameter Values"
id: 1500009649882
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values
updated_at: 2021-07-24T20:53:44Z
---

# Specifying Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674801-Importing-and-Exporting-Scheduled-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio)

# Specifying Parameter Values

This topic introduces how to specify parameter values.

Below is a list of the sections covered in this topic:

* [Defining Parameter Values](#Value)
* [Saving Parameter Values for Reuse](#Reuse)
* [Customizing Default Parameter Values](#DefaultParam)
* [Using Built-In Functions to Set Date and Time Parameter Values](#DateTime)

## Defining Parameter Values

When running or scheduling reports with parameters, you may need to specify values for the parameters. The way to specify a parameter value varies with the type and properties of the parameter. Here are several ways you can use to specify parameter values:

* In the parameter value combo box, input the value manually or select the required one from the drop-down list. If you have chosen to [automatically save parameter values](#Auto), the saved value groups will be available on the top of the parameters' value lists for selection.
* Select or unselect the checkbox to specify a Yes/No value.
* Select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920370839/btn_chsr2.gif) to specify multiple values in the [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009646502-Enter-Values) dialog.
* Select the calendar button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401431/btn_clndr.gif) to specify a date and time value using either calendar or [expression](#DateTime) in the Calendar dialog. If you use an expression to specify the value, when you hover the mouse pointer over this value, a tip will appear showing its expression. Select on the value, the expression will be displayed in the value text box and you can edit the expression in the text box directly if you want. After editing, when you select elsewhere outside of the value text box:
  + If the edited expression is correct, a new value calculated by the expression will be displayed in the parameter value text box.
  + If the edited expression is wrong, no value will be created and the expression itself will be displayed and highlighted in red in the value text box. Correct the expression, or select the calendar button to specify a value.
* Select the **Use Saved Values**  button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920430231/btn_srv_ussvvlu.gif) and select a previously saved parameter value group to apply to the report. For details, see [Manually Saving Parameter Values](#Manual).

**Note:** You are recommended not to use blank as the thousands separator in Number-typed parameter values under French locale, otherwise your input will not be correctly recognized because of a JVM bug. For details, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

This document also introduces some useful techniques for setting parameter values.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Saving Parameter Values for Reuse

When specifying parameter values for reports, you may want to save the specified parameter values for reuse next time. Logi JReport provides two ways of saving. One is users decide when and which parameter values to save, the other is Logi JReport saves each applied or submitted parameter values automatically. When the saved number in either way reaches the maximum, the oldest record will be removed. The number is calculated on a user-report basis. Take a report with two parameters for an example, supposing the maximum number is set to 3. Each user can save at most three groups of parameter values for the report. Each group contains the values of the two parameters.

To switch on the function of saving parameter values, you need to configure the server profile. Go to the Profile > Customize Server Preferences > Advanced tab, select **Yes** to the option [Enable Saving Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#SaveParam), select a way to do the saving: Manually or Automatically, and then specify a maximum number to limit the saved value groups which is called the auto complete parameters list for each user-report pair.

**Manually saving parameter values**

When you have chosen to manually save parameter values, the Use Saved Values button **![](https://devnet.logianalytics.com/hc/article_attachments/4404920430231/btn_srv_ussvvlu.gif)** will be available on the upper right corner of the parameter page. By selecting this button, you will get the following:

* **Value List**  
   The value list contains all the parameter value groups you have saved for the report. Select a group to apply all the values in the group to the corresponding parameters. You can also remove any of the unwanted value group by selecting it from the list and then selecting
  ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360855/btn_dltobj.gif) next to the value list.
* **![](https://devnet.logianalytics.com/hc/article_attachments/4404926628119/btn_save.gif) Save Values**  
   Saves the current displayed parameter values as a group for reuse afterwards. To do this, type a name for the group in the text box which shows "Save current values into list" and then select **![](https://devnet.logianalytics.com/hc/article_attachments/4404926628119/btn_save.gif)**. The saved group will then be added into the value list above. Once it reaches the maximum number, the latest group will replace the oldest.

**Using automatically saved parameter values**

When you have chosen to automatically save parameter values, each time a user submits a group of parameter values to a report, the group is saved by Logi JReport automatically. The next time the same user runs the report, the auto saved parameter values will be available in the parameters' value lists for selection on the parameter page.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Customizing Default Parameter Values

When specifying parameter values for a report, if you would like the current specified parameter values to be saved as the default values for the parameters next time when you run or schedule the report, select the **Save as default** option on the parameter page (to make this option available, you need to make sure the [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#DefaultParam) option is selected for the corresponding report type in the Profile > Customize Server Preferences > Advanced tab).

If you want the saved default parameter values to be applied directly to the report next time when you run it without popping up the Enter Parameter Values dialog, select the option **Do not show the screen again** in the dialog (to make this option available, you need to make sure the Enable Hiding Initial Parameter Dialog For option is selected for the corresponding report type in the Profile > Customize Server Preferences > Advanced tab). However, if the last-time saved default values cannot completely match the current report parameters, the dialog will still be displayed. This option only hides the parameter dialog popped from operation on the console. It does not affect the case of running report using URL way.

In addition, Logi JReport provides you with the [Parameter Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009646702-Parameter-Settings) dialog which allows you to pre-customize the default parameter values for a report before running it. This dialog can also be used to show the Enter Parameter Values dialog again after it has been hidden. To do this, check **Re-enable Parameter Screen** in the dialog.

The above options are user-report level settings, that is to say, they take effect when both the same user and report are matched. This also applies to admin users, and therefore admin cannot customize the settings for all users.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Using Built-In Functions to Set Date and Time Parameter Values

For a parameter of the Date, DateTime, or Time type, you can customize a dynamic date and time value by creating an expression using built-in functions.

**To do this:**

1. In the places where you are able to specify a value for the parameter, you may see the calendar button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401431/btn_clndr.gif). Select this button and the [Calendar](https://devnet.logianalytics.com/hc/en-us/articles/1500009670741-Calendar) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926665239/clndr.gif)
2. The Template drop-down list on the right provides some predefined expressions for you to use. You can customize your own expression either based on an existing template or by directly editing the contents in the Expression text box.

   If you cannot see the Template label on the right, select **>>** on the bottom left corner.
3. Logi JReport's built-in [Date/Time formula functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009672761-Date-Time) are available for inserting into your expression. To make use of them, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920370839/btn_chsr2.gif) to display the functions.
4. The Preview box calculates the result of the current expression. Each time you modify the expression, you can select in the box to refresh the result. If it is an invalid expression, an error message will be shown in the box and no change will be made to the calendar and the currently selected date/time will be remained in the calendar.
5. When done, select **OK** to add the value.

When running reports via URLs, you can also use expressions to specify date and time parameter values. The format is
Parameter\_Name={"exp":"Complete\_Expression\_String", "SelectedDate":"'MM/dd/yyyy"}. If the expression does not contain the function SelectedDate(), there is no need to add this part - "SelectedDate":"'MM/dd/yyyy" and the format is Parameter\_Name={"exp":"Complete\_Expression\_String"}. For example, to specify p\_EndDate=today(), write it as `p_EndDate={"exp":"today()"}`. The following is an example of running the CustomerAnalysis.cls:

`http://localhost:8888/jinfonet/runReport.jsp?jrs.cmd=jrs.web_vw&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.param$P_StartDate=01/01/2010&jrs.param$p_EndDate={"exp":"today()"}&jrs.result_type=8`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674801-Importing-and-Exporting-Scheduled-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio)
