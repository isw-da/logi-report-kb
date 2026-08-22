---
title: "Applying Parameters"
id: 1500009724862
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724862-Applying-Parameters
updated_at: 2021-07-25T07:18:33Z
---

# Applying Parameters

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724722-Adding-Conditional-Formats-to-Data-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724882-Applying-CSS-Styles)

# Applying Parameters

When running a web report with parameters, Report Server displays a dialog box for you to specify the parameter values. The runtime parameter dynamically controls your report result. After the report is opened in Web Report Studio, you can change the parameter values in the Parameters panel. You can also use [parameter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009751581-Using-Web-Controls#Parameter) or [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/1500009751581-Using-Web-Controls#Form) to change the parameter values for the report.

The Parameters panel is available when the current web report uses parameters. It lists all the parameters used by the report.

![Parameters Panel](https://devnet.logianalytics.com/hc/article_attachments/4404942452375/wbrpt_edt_prm_pnl.gif)

Edit the values according to your requirement and then select **Apply** to make the report run with the specified parameter values.

The way to specify a parameter value varies according to the type and properties of the parameter. Here are several ways you can use to specify parameter values:

* In the parameter value combo box, select the down arrow ![More button](https://devnet.logianalytics.com/hc/article_attachments/4404942452631/btn_dshbrd_more1.gif) and then select the required value from the drop-down list.

  ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")To ensure performance, by default at most 500 values are listed. When the listed values are just a part of the values of the parameter, after you scroll down to the bottom of the list, more values (500 at most) will be automatically loaded into the drop-down list.

  For a parameter that is bound with a column, you can make use of the Sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936723095/btn_sort1.gif) to display the values in the ascending or descending order for easy look-up, and search for the required values conveniently in the search box. To cancel the search, clear the input text or select ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif) in the search box.

  When a parameter's values are encrypted, the value drop-down list will be disabled. In this case, if the Hide Parameter Value check box is available, you can clear it to enable the drop-down list to view and select the required value.
* Type the value manually in the parameter value text box if the parameter allows for type-in values but not multiple values.
* Click in the parameter value combo box to [specify multiple values](#MultiValue) if the parameter allows for multiple values.
* Select or clear the check box to specify a Yes/No value.
* Select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values#DateTime).

**Note:** You are recommended not to use blank as the thousands separator in Number-typed parameter values under French locale, otherwise your input will not be correctly recognized because of a JVM bug. For details, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

See the usages below about the other options in the panel:

* **Save as default**  
   Saves current parameter values as the default values for the report. Not available when [Enable Setting Default Parameter Values For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#DefaultParam) the corresponding report type is unselected in the server profile.
* **Re-enable Parameter Screen**  
  When this option is unselected, the next time the report runs via operation in the Logi Report Server console, it will use the default parameter values directly without popping up the Enter Parameter Values dialog box. However, if the default values cannot completely match the report parameters, the dialog box will still be displayed. You can select it to show the Enter Parameter Values dialog box again after it has been hidden.

  This option is not available when [Enable Hiding Initial Parameter Dialog For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#HideParam)  is unselected in the server profile.

  The Save as default and Re-enable Parameter Screen options are user-report level settings, that is to say, they take effect when both the same user and report are matched. This also applies to admin users, and therefore admin users cannot customize the settings for all users.
* **Reset**  
   Resets the parameter values. This button varies according to different situations:
  + When Save as default is available in the panel, the button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
    - **Original Default Values**  
       The default values defined in the parameters' definition.
    - **User Defined Default Values**  
       Your last-time saved default values.
  + When Save as default is unavailable in the panel, the button contains only the text part. Selecting it will reset the values to the original default values.

## Specifying Multiple Values for a Parameter

For a parameter that allows for multiple values (the parameter's Allow Multiple Values property is true), you can specify one or more values to it.

1. Click in the value combo box of the parameter. Report Server displays the [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009721582-Enter-Values) dialog box.

   ![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942453143/entervlu.gif)
2. If the parameter's Enable the "All Values" Option property is true, the All Values check box is available and by default it is selected. It means to apply all values to the parameter. When the parameter is inserted as a field into a report and All Values is selected as the value, the field will show the string "All". If you do not want to apply all values to the parameter, deselect the **All Values** check box and then specify the desired values as shown in the following steps.
3. Select the required values in the Available Values box and select ![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4404942453399/btn_add2.gif) to add them to the Selected Values box; to add all the listed values, select ![Add All Values](https://devnet.logianalytics.com/hc/article_attachments/4404942453655/btn_addall1.gif).

   ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")To ensure performance, by default at most 500 values are listed in the Available Values box. When the listed values are just a part of the values of the parameter, after you scroll down to the bottom of the list, more values (500 at most) will be automatically loaded into the list. You can make use of the Sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936713367/btn_sort.gif) to display the values in the ascending or descending order for easy look-up, and the Search button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif) to search for the required values conveniently. To cancel the search and close the search box, select ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif) in it.

   If some added values are not wanted, select them in the Selected Values box and select ![Remove Values](https://devnet.logianalytics.com/hc/article_attachments/4404936723991/btn_rmv1.gif) to remove them; to remove all added values, select ![Remove All Values](https://devnet.logianalytics.com/hc/article_attachments/4404936724247/btn_rmvall1.gif).
4. When the parameter's Allow Type-in of Value property is true, the Enter Values text box is available. You can type a value manually and select ![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4404942453399/btn_add2.gif) next to add it to the Selected Values box. When the parameter is bound with a column, but the display column is different from the bound column, make sure the value you type is that of the bound column. If the parameter is of the Date, DateTime, or Time type, you can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values#DateTime).
5. Select **OK** to select the specified values for the parameter.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724722-Adding-Conditional-Formats-to-Data-Fields)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724882-Applying-CSS-Styles)
