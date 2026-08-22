---
title: "Enter Parameter Values"
id: 1500009670301
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009670301-Enter-Parameter-Values
updated_at: 2021-07-24T20:54:57Z
---

# Enter Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646002-Edit-URL-Frame)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646022-Enter-Values)

# Enter Parameter Values

The Enter Parameter Values dialog appears after you select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398103/btn_dshbrd_prm.gif) on the toolbar when a dashboard contains parameters. If the Show Enter Parameter Values Dialog option is checked in the Profile > Configure Profile > JDashboard > Properties tab, this dialog also pops up when you run a dashboard with parameters. In this dialog, all the parameters used in the current dashboard are listed. Same-name parameters are allowed when they are from different library components. You can [specify the values](https://devnet.logianalytics.com/hc/en-us/articles/1500009644722-Specifying-Parameter-Values) to re-run the dashboard. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926756247/enterprmvlu.gif)

**Parameters**

Displays parameters of all the library components in the dashboard with their default values.

If you have not yet set the default values for the parameters in JDashboard using the [save as default](#SaveDefault) action, or if any of the parameters cannot find a matched validated value from the saved default values, all the parameters will use their default values specified in the parameters' definition as the initial values.

**Save as default**

Saves current parameter values as the default values for all the library components in the dashboard. It is a user-dashboard level setting.

If later you change the [parameter sharing](https://devnet.logianalytics.com/hc/en-us/articles/1500009644722-Specifying-Parameter-Values#Share) setting in the dashboard, the saved default values will be cancelled and the default values specified in the parameters' definition will be used.

JDashboard remembers the last-time saved result of a dashboard and displays the exact result the next time the dashboard is opened. In the case a dashboard user sets USA as the default parameter value and then filters the result with Canada and saves the dashboard, the next time the dashboard will run with Canada, though the saved default parameter value is still kept as USA.

This option is an action and it takes effect after you select Submit in the dialog. Its initial status is always unselected.

This option is available when [Enable Setting Default Parameter Values For Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#DefaultParam) is selected in the Profile > Customize Server Preferences > Advanced tab.

**Submit**

Closes this dialog and applies the specified values to run the dashboard.

**Reset**

When Save as default is available in the dialog, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.

* **Original Default Values**  
   The default values defined in the parameters' definition.
* **User-Defined Default Values**  
   The default values specified using the [save as default](#SaveDefault) action.

When Save as default is unavailable in the dialog, the Reset button contains only the text part. Selecting it will reset the values to the original default values.

**Cancel**

Cancels changing the parameter values and closes this dialog.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920594583/btn_dshbrd_ussvvlu.gif)**Use Saved Values**

If it is available, you can select the previously saved parameter values to apply to the dashboard and save parameter values for reuse later. For details, see [Saving parameter values for reuse](https://devnet.logianalytics.com/hc/en-us/articles/1500009644722-Specifying-Parameter-Values#Save).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920501783/btn_help.gif)

Displays the help document about this feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926700311/btn_close.gif)

Ignores the setting and closes this dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646002-Edit-URL-Frame)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646022-Enter-Values)
