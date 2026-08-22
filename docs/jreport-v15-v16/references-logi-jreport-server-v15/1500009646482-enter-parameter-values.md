---
title: "Enter Parameter Values"
id: 1500009646482
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009646482-Enter-Parameter-Values
updated_at: 2021-07-24T20:54:49Z
---

# Enter Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646462-Encrypt)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646502-Enter-Values)

# Enter Parameter Values

The Enter Parameter Values dialog appears when you run a report with parameters. It allows you to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values) to run the report. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920574103/enterprmvlu.gif)

**Parameters**

Displays parameters of the report with your last-time saved default values, which could be the values saved in this dialog last time, or in the [Parameter Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009646702-Parameter-Settings) dialog, or when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009670701-Advanced-Run#Parameter) or [scheduling](https://devnet.logianalytics.com/hc/en-us/articles/1500009646762-Schedule#Parameter) the report, and for a web report, could also be the values saved in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009650342-Applying-Parameters#Panel). Edit the values according to your requirement. [You may specify parameter values in these ways](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values#Value).

If you have not yet set the default values on the server, or if you did but your saved default values cannot fully match the current parameters, all the parameters will use their default values specified in the parameters' definition as the initial values.

**![](https://devnet.logianalytics.com/hc/article_attachments/4404920430231/btn_srv_ussvvlu.gif) Use Saved Values**

If it is available, you can select the previously saved parameter values to apply to the report and [save parameter values for reuse later](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values#Save).

**Save as default**

Saves current parameter values as the default values for the report. Available when [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#DefaultParam) the corresponding report type is selected in the Profile > Customize Server Preferences > Advanced tab.

This option is a user-report level setting. It is an action and takes effect after the task is submitted. Its initial status is always unselected.

**Do not show this screen again**

When this option is selected, the next time the report runs via operation on the console, it will use the last-time saved default parameter values directly without popping up this dialog. However, if the last-time saved default values cannot completely match the current report parameters, the dialog will still be displayed. It is a user-report level setting.

This option is available when  [Enable Hiding Initial Parameter Dialog For](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#HideParam)  the corresponding report type is selected in the Profile > Customize Server Preferences > Advanced tab.

**Submit**

Closes this dialog and applies the specified values to run the report.

**Reset**

When Save as default is available in the dialog, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.

* **Original Default Values**  
   The default values defined in the parameters' definition.
* **User-Defined Default Values**  
   Your last-time saved default values.

When Save as default is unavailable in the dialog, the Reset button contains only the text part. Selecting it will reset the values to the original default values.

**Cancel**

Cancels running the report and closes this dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646462-Encrypt)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646502-Enter-Values)
