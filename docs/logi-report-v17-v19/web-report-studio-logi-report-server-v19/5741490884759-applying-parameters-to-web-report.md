---
title: "Applying Parameters to Web Report"
id: 5741490884759
section: "Web Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741490884759-Applying-Parameters-to-Web-Report
updated_at: 2022-10-31T17:18:35Z
---

# Applying Parameters to Web Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741490590615-Adding-Conditional-Formats-to-Data-Fields-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741456130199-Applying-CSS-Styles-in-Web-Report)

# Applying Parameters to Web Report

When you run a web report with parameters, Server displays a dialog box for you to specify the parameter values. The runtime parameter dynamically controls your report data. This topic describes how you can change the parameter values in the Parameters panel and specify multiple values for a parameter after you open a report in Web Report Studio.

You can also use [parameter controls](https://devnet.logianalytics.com/hc/en-us/articles/5741484852887-Using-Web-Controls-in-Web-Report#Parameter) or [parameter form controls](https://devnet.logianalytics.com/hc/en-us/articles/5741484852887-Using-Web-Controls-in-Web-Report#Form) to change the parameter values for reports.

The Parameters panel is available when the current web report uses parameters. It lists all the parameters that the report uses.

![Parameters Panel](https://devnet.logianalytics.com/hc/article_attachments/9905617400215/wbrpt_edt_prm_pnl.gif)

Edit the values according to your requirement and then select **Apply** to run the report with the specified parameter values.

The way to specify a parameter value varies according to the type and properties of the parameter. Here are several ways you can use to specify parameter values:

* In the parameter value combo box, select the down arrow ![More button](https://devnet.logianalytics.com/hc/article_attachments/9905617425559/btn_dshbrd_more1.gif) and then select a value from the drop-down list.

  To ensure performance, Server lists at most 500 values by default. When the listed values are just a part of the values of the parameter, after you scroll down to the bottom of the list, Server loads more values (500 at most) automatically into the drop-down list.

  For a parameter that is bound with a column, you can make use of the Sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905629589015/btn_sort1.gif) to display the values in the ascending or descending order for easy look-up, and search for the required values conveniently in the search box. To cancel the search, clear the input text or select the delete button ![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif) in the search box.

  When encrypting a parameter's values, Server disables the value drop-down list. In this case, if Server displays **Hide Parameter Value**, you can clear it to enable the drop-down list to view and select a value.
* Type the value manually in the parameter value text box if the parameter enables type-in values but not multiple values.
* Select in the parameter value combo box to [specify multiple values](#MultiValue) if the parameter enables multiple values.
* Select or clear the checkbox to specify a Yes or No value.
* Select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/9905617212951/btn_clndr.gif) to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values#DateTime).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)You should not use blank as the thousands separator in Number-type parameter values under French locale, otherwise Server does not correctly recognize your input because of a JVM bug. For more information, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

See the usages about the other options in the panel:

* **Save as default**  
   Select **Save as default** to save current parameter values as the default parameter values for the report. Server displays this option when you did not clear [Enable Setting Default Parameter Values For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#DefaultParam) in the server profile.
* **Re-enable Parameter Screen**  
  Clear this option if you do not want the Enter Parameter Values dialog box to pop up next time you run the report from the Server Console, but instead want the report to run with the default parameter values directly. However, if the default values cannot completely match the report parameters, Server still displays the dialog box. You can select the option to show the Enter Parameter Values dialog box again after you hide it.

  This option is not available when you did not clear [Enable Hiding Initial Parameter Dialog For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#HideParam) in the server profile.

  The **Save as default** and **Re-enable Parameter Screen** options are user-report level settings. They take effect when both the same user and report are matched. This also applies to administrators, and therefore administrators cannot customize the settings for all users.
* **Reset**  
   Reset the parameter values. This button varies according to different situations:
  + When **Save as default** is available in the panel, the button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values reset to the original default values.
    - **Original Default Values**  
       The default values defined in the parameters' definition.
    - **User Defined Default Values**  
       The default values that you saved last time.
  + When **Save as default** is unavailable in the panel, the button contains only the text part. Selecting it will reset the values to the original default values.

## Specifying Multiple Values for a Parameter

For a parameter that enables multiple values (the parameter's **Allow Multiple Values** property is true), you can specify one or more values to it.

1. Select in the value combo box of the parameter. Server displays the [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/5741444626711-Enter-Values-Dialog-Box-Properties) dialog box.

   ![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/9905617455127/entervlu.gif)
2. If the parameter's **Enable the "All Values" Option** property is true, **All Values** is available. Server selects it by default. It means to apply all values to the parameter. When you inserted the parameter as a field into a report and selected **All Values**, the field shows the string **All**. If you do not want to apply all values to the parameter, clear **All Values** and then specify the values you want as follows.
3. Select the values you want in the **Available Values** box and select the Add button ![Add Values](https://devnet.logianalytics.com/hc/article_attachments/9905629799831/btn_add2.gif) to add them to the **Selected Values** box; to add all the listed values, select the Add All button ![Add All Values](https://devnet.logianalytics.com/hc/article_attachments/9905617492119/btn_addall1.gif).

   To ensure performance, by default Server lists at most 500 values in the Available Values box. When the listed values are just a part of the values of the parameter, after you scroll down to the bottom of the list, Server automatically loads more values (500 at most) into the list. You can make use of the Sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif) to display the values in the ascending or descending order for easy look-up, and the Search button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif) to search for the required values conveniently. To cancel the search and close the search box, select the delete button ![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif) in it.

   For values you do not want, select them in the Selected Values box and select the button ![Remove Values](https://devnet.logianalytics.com/hc/article_attachments/9905617508119/btn_rmv1.gif) to remove them; to remove all added values, select the button ![Remove All Values](https://devnet.logianalytics.com/hc/article_attachments/9905629846167/btn_rmvall1.gif).
4. When the parameter's **Allow Type-in of Value** property is true, the **Enter Values** text box is available. You can type a value manually and select the button ![Add Values](https://devnet.logianalytics.com/hc/article_attachments/9905629799831/btn_add2.gif) next to add it to the Selected Values box. When the parameter is bound with a column, but the display column is different from the bound column, make sure the value you type is that of the bound column. If the parameter is of the Date, DateTime, or Time type, you can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/9905617212951/btn_clndr.gif) to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values#DateTime).
5. Select **OK** to select the specified values for the parameter.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741490590615-Adding-Conditional-Formats-to-Data-Fields-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741456130199-Applying-CSS-Styles-in-Web-Report)
