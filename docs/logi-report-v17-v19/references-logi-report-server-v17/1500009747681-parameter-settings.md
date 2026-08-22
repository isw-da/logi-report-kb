---
title: "Parameter Settings"
id: 1500009747681
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747681-Parameter-Settings
updated_at: 2021-07-25T07:19:38Z
---

# Parameter Settings

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720762-Page-Report-Studio-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009720782-Preference)

# Parameter Settings

The Parameter Settings dialog box is used to [customize the default parameter values for a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values#DefaultParam).

![Parameter Settings dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942485271/prmset.gif)

**Parameters**

Lists all the parameters used by the report. [Edit the values](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values) according to your requirement.

If no parameter is used in the report, Report Server displays "No Parameter Needed" here.

**Save as default**

Saves current parameter values as the default values for the report. Not available when [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#DefaultParam) the corresponding report type is unselected in the server profile.

This option is a user-report level setting. It is an action and takes effect after the task is submitted. Its initial status is always unselected.

**Re-enable Parameter Screen**

When this option is unselected, the next time the report runs via operation in the Logi Report Server console, it will use the default parameter values directly without popping up the Enter Parameter Values dialog box. However, if the default values cannot completely match the report parameters, the dialog box will still be displayed. You can select it to show the Enter Parameter Values dialog box again after it has been hidden.

This option is a user-report level setting. It is not available when [Enable Hiding Initial Parameter Dialog For](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#HideParam) the corresponding report type is unselected in the server profile.

**OK**

Applies the settings and exits the dialog box.

**Reset**

Resets the parameter values. This button varies according to different situations:

* When Save as default is enabled in the dialog box, the button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
  + **Original Default Values**  
     The default values defined in the parameters' definition.
  + **User Defined Default Values**  
     Your last-time saved default values.
* When Save as default is disabled in the dialog box, the button contains only the text part. Selecting it will reset the values to the original default values.

**Cancel**

Closes the dialog box and discards any changes.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720762-Page-Report-Studio-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009720782-Preference)
