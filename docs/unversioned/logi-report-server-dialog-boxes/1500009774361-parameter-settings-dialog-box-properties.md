---
title: "Parameter Settings Dialog Box Properties"
id: 1500009774361
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009774361-Parameter-Settings-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:44Z
---

# Parameter Settings Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774341-Page-Report-Studio-Profile-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746222-Preference-Dialog-Box-Properties-)

# Parameter Settings Dialog Box Properties

This topic describes how you can use the Parameter Settings dialog box to [customize the default parameter values for a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009778361-Specifying-Parameter-Values#DefaultParam).

![Parameter Settings dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880238103/prmset.gif)

**Parameters**

Lists all the parameters used by the report. [Edit the values](https://devnet.logianalytics.com/hc/en-us/articles/1500009778361-Specifying-Parameter-Values) according to your requirement.

If no parameter is used in the report, Server displays "No Parameter Needed" here.

**Save as default**

Select **Save as default** to save current parameter values as the default parameter values for the report. Server displays this option when you did not clear [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#DefaultParam) the corresponding report type in the server profile.

This option is a user-report level setting. It is an action and takes effect after you select **OK** in the dialog box. Its initial status is always cleared.

**Re-enable Parameter Screen**

When this option is unselected, the next time the report runs via operation in the Server Console, it will use the default parameter values directly without popping up the Enter Parameter Values dialog box. However, if the default values cannot completely match the report parameters, the dialog box will still be displayed. You can select it to show the Enter Parameter Values dialog box again after it has been hidden.

This option is a user-report level setting. It is not available when [Enable Hiding Initial Parameter Dialog For](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#HideParam) the corresponding report type is unselected in the server profile.

**OK**

Applies the settings and exits the dialog box.

**Reset**

Resets the parameter values. This button varies according to different situations:

* When Save as default is enabled in the dialog box, the button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
  + **Original Default Values**  
     The default values defined in the parameters' definition.
  + **User Defined Default Values**  
     The default values you saved last time.
* When Save as default is disabled in the dialog box, the button contains only the text part. Selecting it will reset the values to the original default values.

**Cancel**

Closes the dialog box and discards any changes.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774341-Page-Report-Studio-Profile-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746222-Preference-Dialog-Box-Properties-)
