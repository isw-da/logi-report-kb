---
title: "Enter Parameter Values"
id: 1500009714641
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009714641-Enter-Parameter-Values
updated_at: 2021-11-03T06:57:44Z
---

# Enter Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009688702-Encrypt)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714661-Enter-Values)

# Enter Parameter Values

The Enter Parameter Values dialog allows you to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009692442-Specifying-Parameter-Values) to run the report. It appears when you run a report with parameters.

![Enter Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131468439/enterprmvlu.gif)

**Parameters**

Lists all the parameters used by the report. [Edit the values](https://devnet.logianalytics.com/hc/en-us/articles/1500009692442-Specifying-Parameter-Values) according to your requirement.

**![Use Saved Values button](https://devnet.logianalytics.com/hc/article_attachments/4412131415319/btn_srv_ussvvlu.gif) Use Saved Values**

If it is available, you can select the previously saved parameter values to apply to the report and [save parameter values for reuse later](https://devnet.logianalytics.com/hc/en-us/articles/1500009692442-Specifying-Parameter-Values#Reuse).

**Save as default**

Saves current parameter values as the default values for the report. Not available when [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#DefaultParam) the corresponding report type is unchecked in the server profile.

This option is a user-report level setting. It is an action and takes effect after the task is submitted. Its initial status is always unchecked.

**Do not show this screen again**

When this option is selected, the next time the report runs via operation in the Logi JReport Server console, it will use the default parameter values directly without popping up this dialog, which could be the default values specified in the parameters' definition or the default values you saved last time for the report on Logi JReport Server. However, if the default values cannot completely match the current report parameters, the dialog will still be displayed.

This option is a user-report level setting. It is not available when  [Enable Hiding Initial Parameter Dialog For](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#HideParam)  the corresponding report type is unchecked in the server profile.

**Submit**

Closes this dialog and applies the specified values to run the report.

**Reset**

Resets the parameter values. This button varies according to different situations:

* When Save as default is available in the dialog, the button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
  + **Original Default Values**  
     The default values defined in the parameters' definition.
  + **User-Defined Default Values**  
     Your last-time saved default values.
* When Save as default is unavailable in the dialog, the button contains only the text part. Selecting it will reset the values to the original default values.

**Cancel**

Cancels running the report and closes this dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009688702-Encrypt)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714661-Enter-Values)
