---
title: "Parameter Settings"
id: 1500009646702
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009646702-Parameter-Settings
updated_at: 2021-07-24T20:54:46Z
---

# Parameter Settings

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646402-Page-Report-Studio-Profile)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009671101-Publish-to-Local-Server)

# Parameter Settings

The Parameter Settings dialog allows you to customize the default parameter values for a report. It is unavailable when both [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#DefaultParam) and [Enable Hiding Initial Parameter Dialog For](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#HideParam) the corresponding report type are unchecked in the Profile > Customize Server Preferences > Advanced tab.

To access the dialog, on the Logi JReport Console > Resources page, browse to the target report, then do one of the following:

* Select the row the report is in, then on the task bar of the Resources page, select Tools > Parameter Settings.
* Select the report row, right-click in the row and select Parameter Settings from the shortcut menu.
* Put the mouse pointer over the report row and select the Parameter Settings button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920568599/btn_srv_prmset.gif) on the floating toolbar.

[See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926739607/prmset.gif)

**Parameters**

Displays parameters of the report with your last-time saved default values, which could be the values saved in this dialog last time, or in the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009646482-Enter-Parameter-Values) dialog, or when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009670701-Advanced-Run#Parameter) or [scheduling](https://devnet.logianalytics.com/hc/en-us/articles/1500009646762-Schedule#Parameter) the report, and for a web report, could also be the values saved in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009650342-Applying-Parameters#Panel). Edit the values according to your requirement. [You may specify parameter values in these ways](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values#Value).

If you have not yet set the default values on the server, or if you did but your saved default values cannot fully match the current parameters, all the parameters will use their default values specified in the parameters' definition as the initial values.

If no parameter is used in the report, "No Parameter Needed" will be displayed here.

**Save as default**

Saves current parameter values as the default values for the report.

This option is a user-report level setting. It is an action and takes effect after the task is submitted. Its initial status is always unselected.

**Re-enable Parameter Screen**

When this option is unselected, the next time the report runs via operation on the console, it will use the last-time saved default parameter values directly without popping up the Enter Parameter Values dialog. However, if the last-time saved default values cannot completely match the report parameters, the dialog will still be displayed. It is a user-report level setting.

You can check it to show the Enter Parameter Values dialog again after it has been hidden.

**OK**

Applies the settings and exits the dialog.

**Reset**

When Save as default is enabled in the dialog, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.

* **Original Default Values**  
   The default values defined in the parameters' definition.
* **User-Defined Default Values**  
   Your last-time saved default values.

When Save as default is disabled in the dialog, the Reset button contains only the text part. Selecting it will reset the values to the original default values.

**Cancel**

Closes the dialog and discards any changes.

**Help**

Displays the help document about this feature.

**Note:** If you just edit the parameter values in the dialog and select OK, the new values will be meaningless. Only when you check Save as default and select OK, can the values be saved as default values to the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646402-Page-Report-Studio-Profile)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009671101-Publish-to-Local-Server)
