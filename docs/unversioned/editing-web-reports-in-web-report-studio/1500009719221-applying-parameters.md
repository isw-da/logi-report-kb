---
title: "Applying Parameters"
id: 1500009719221
section: "Editing Web Reports in Web Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719221-Applying-Parameters
updated_at: 2021-11-03T06:56:26Z
---

# Applying Parameters

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719101-Adding-Conditional-Formats-to-Data-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692862-Applying-CSS-Styles)

# Applying Parameters

When running a web report with parameters, a dialog is displayed for you to specify the parameter values. The runtime parameter dynamically controls your report result. After the report is opened in Web Report Studio, you can change the parameter values in the Parameters panel. You can also use [parameter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009719281-Using-Web-Controls#Parameter) or [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/1500009719281-Using-Web-Controls#Form) to change the parameter values for the report.

The Parameters panel is available when the current web report uses parameters. It lists all the parameters used by the report.

![Parameters Panel](https://devnet.logianalytics.com/hc/article_attachments/4412131379863/wbrpt_edt_prm_pnl.gif)

Edit the values according to your requirement and then select **Apply** to make the report run with the specified parameter values.

The way to specify a parameter value varies according to the type and properties of the parameter. Here are several ways you can use to specify parameter values:

* In the parameter value combo box, select the required one from the drop-down list or input the value manually.

  When a parameter's values are encrypted, the value drop-down list will be disabled. In this case, if the Hide Parameter Value checkbox is available, you can uncheck it to enable the drop-down list to view and select the required value.
* Select or unselect the checkbox to specify a Yes/No value.
* Select the button ![Select Values](https://devnet.logianalytics.com/hc/article_attachments/4412112488471/btn_chsr1.gif) to [specify multiple values](#MultiValue) if the parameter allows for multiple values.
* Select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif) to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500009692442-Specifying-Parameter-Values#DateTime).

**Note:** You are recommended not to use blank as the thousands separator in Number-typed parameter values under French locale, otherwise your input will not be correctly recognized because of a JVM bug. For details, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

**Tip:** Administrators can limit the number of values shown in the value list of the parameters that are bound with columns by setting the [Max Records in Parameter Value List](https://devnet.logianalytics.com/hc/en-us/articles/1500009712361-Configuring-Advanced-Server-Settings#ParameterMaxRecords) option in the Administration > Configuration > Advanced page in the server console.

Below shows the usages about the other options in the panel:

* **Save as default**  
   Saves current parameter values as the default values for the report. Not available when [Enable Setting Default Parameter Values For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#DefaultParam) the corresponding report type is unchecked in the server profile.
* **Re-enable Parameter Screen**  
  When this option is unselected, the next time the report runs via operation in the Logi JReport Server console, it will use the default parameter values directly without popping up the Enter Parameter Values dialog. However, if the default values cannot completely match the report parameters, the dialog will still be displayed. You can check it to show the Enter Parameter Values dialog again after it has been hidden.

  This option is not available when [Enable Hiding Initial Parameter Dialog For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#HideParam)  is unchecked in the server profile.

  The Save as default and Re-enable Parameter Screen options are user-report level settings, that is to say, they take effect when both the same user and report are matched. This also applies to admin users, and therefore admin users cannot customize the settings for all users.
* **Reset**  
   Resets the parameter values. This button varies according to different situations:
  + When Save as default is available in the panel, the button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
    - **Original Default Values**  
       The default values defined in the parameters' definition.
    - **User-Defined Default Values**  
       Your last-time saved default values.
  + When Save as default is unavailable in the panel, the button contains only the text part. Selecting it will reset the values to the original default values.

## Specifying Multiple Values for a Parameter

For a parameter that allows for multiple values (the parameter's Allow Multiple Values property is true), you can specify one or more values to it.

1. Select ![Enter Values](https://devnet.logianalytics.com/hc/article_attachments/4412112488471/btn_chsr1.gif) in the value text box of the parameter. The [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009716061-Enter-Values) dialog appears.

   ![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112488727/entervlu.gif)
2. If the parameter's Enable the "All" Option property is true, the All checkbox is available and by default it is selected. It means to apply the "All" value to the parameter. When the parameter is inserted as a field into a report and All is selected as the value, the field will show the string "All". If you do not want to apply the "All" value to the parameter, deselect the **All** checkbox, then check the **Custom** option and specify the desired values as shown in the following steps.
3. Select the required values in the Available Values box and select ![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4412139489687/btn_add2.gif) to add them to the Selected Values box; to add all the available values, select ![Add All Values](https://devnet.logianalytics.com/hc/article_attachments/4412112488983/btn_addall1.gif). You can make use of the Search button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif) to search for the required values among the available values: select the ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif) button to display the search text box, type in the keyword
   and the available values that contain the keyword will be listed with the keyword highlighted in the values.

   If some added values are not wanted, select them in the Selected Values box and select ![Remove Values](https://devnet.logianalytics.com/hc/article_attachments/4412131380119/btn_rmv1.gif) to remove them; to remove all added values, select ![Remove All Values](https://devnet.logianalytics.com/hc/article_attachments/4412131380375/btn_rmvall1.gif).
4. When the parameter's Allow Type-in of Value property is true, you can add values for the parameter manually: select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4412131380631/btn_add1.gif), type in a value in the displayed text box, then press **Enter** to add it to the Selected Values box. When the parameter is bound with a column, but the display column is different from the bound column, make sure the value you enter is that of the bound column. After finishing adding the values manually, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif) in the text box to close it. If the parameter is of the Date, Time or DateTime type, you can also select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif) to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500009692442-Specifying-Parameter-Values#DateTime).
5. Select **OK** to select the specified values for the parameter.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719101-Adding-Conditional-Formats-to-Data-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692862-Applying-CSS-Styles)
