---
title: "Applying Parameters"
id: 1500009650342
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650342-Applying-Parameters
updated_at: 2021-07-24T20:53:35Z
---

# Applying Parameters

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675181-Adding-Conditional-Formats-to-Fields)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675281-Sorting-Report-Data)

# Applying Parameters

When running a web report with parameters, a dialog is displayed for you to specify the parameter values. The runtime parameter dynamically controls your report result. After the report is opened in Web Report Studio, you can change the parameter values using the following ways.

## Using the Parameters Panel

The Parameters panel is available when the current web report uses parameters. It lists all the parameters used by the report with your last-time saved default values, which could be the values saved in this panel last time, or in the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009646482-Enter-Parameter-Values) dialog, [Parameter Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009646702-Parameter-Settings) dialog, or when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009670701-Advanced-Run#Parameter) or [scheduling](https://devnet.logianalytics.com/hc/en-us/articles/1500009646762-Schedule#Parameter) the report. If you have not yet set the default values on the server, or if you did but your last-time saved default values cannot fully match the current parameters, all the parameters will use their default values specified in the parameters' definition as the initial values.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926635031/wbrpt_edt_prm_pnl.gif)

Edit the values according to your requirement and then select **Apply** to make the report run with the specified parameter values. [You may specify parameter values in these ways](https://devnet.logianalytics.com/hc/en-us/articles/1500009647742-Report-Parameters).

If you want to save the current specified parameter values as the default values for the report, select **Save as default** in the panel (to make this option available, you need to make sure the [Enable Setting Default Parameter Values For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#DefaultParam) is selected in the Profile > Customize Server Preferences > Advanced tab).

If you would like the report to run on the console with the saved default values directly next time, without popping the Enter Parameter Values dialog, unselect **Re-enable Parameter Screen**, which is available when the option [Enable Hiding Initial Parameter Dialog For Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#HideParam) is checked in the Profile > Customize Server Preferences > Advanced tab. Note that if later the last-time saved default values cannot completely match the report parameters, the parameter dialog will still be displayed. You can check this option to show the Enter Parameter Values dialog again after it has been hidden.

The above two options are user-report level settings, that is to say, they take effect when both the same user and report are matched. This also applies to admin users, and therefore admin cannot customize the settings for all users.

If you want to reset the parameter values, use the Reset button, which varies on different situations:

* When Save as default is available in the panel, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
  + **Original Default Values**  
     The default values defined in the parameters' definition.
  + **User-Defined Default Values**  
     Your last-time saved default values.
* When Save as default is unavailable in the panel, the Reset button contains only the text part. Selecting it will reset the values to the original default values.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Using Parameter Controls

You can insert a parameter control and bind it with a parameter used by the current report. By specifying values to the parameter in the parameter control, you can pass the parameter values to Logi JReport and run the report with the specified values. For details, see [Using parameter control to specify a parameter to a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009675321-Using-Web-Controls#Parameter).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Using Parameter Form Controls

You can insert a parameter form control, make it run the current report, bind it with one or more parameters used by the report. By specifying values to the parameters in the parameter form control, you can make the report run with the specified parameter values. For details, see [Using parameter form control to run reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009675321-Using-Web-Controls#Form).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675181-Adding-Conditional-Formats-to-Fields)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675281-Sorting-Report-Data)
