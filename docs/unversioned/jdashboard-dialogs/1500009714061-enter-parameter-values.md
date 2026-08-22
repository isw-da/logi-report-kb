---
title: "Enter Parameter Values"
id: 1500009714061
section: "JDashboard Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009714061-Enter-Parameter-Values
updated_at: 2021-11-03T06:57:55Z
---

# Enter Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714041-Edit-URL-Frame)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714081-Enter-Values)

# Enter Parameter Values

The Enter Parameter Values dialog enables you to [specify the values](https://devnet.logianalytics.com/hc/en-us/articles/1500009686902-Specifying-Parameter-Values-for-a-Dashboard) to re-run the dashboard. This dialog appears after you select ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4412139509783/btn_dshbrd_prm.gif) on the toolbar when a dashboard contains parameters. If the Show Enter Parameter Values Dialog option is enabled in the JDashboard profile, this dialog also pops up when you run a dashboard with parameters. In this dialog, all the parameters used in the current dashboard are listed. Same-name parameters are allowed when they are from different library components.

![Enter Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131484439/enterprmvlu.gif)

**Parameters**

Displays parameters of all the library components in the dashboard. Edit the values according to your requirements.

**Save as default**

Saves current parameter values as the default values for all the library components in the dashboard. Unavailable when [Enable Setting Default Parameter Values For Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#DefaultParam) is not selected in the server profile. The option Save as default is an action and it takes effect after you select Submit in the dialog. Its initial status is always unselected.

**Submit**

Closes this dialog and applies the specified values to run the dashboard.

**Reset**

Resets the parameter values. This button varies according to different situations:

* When Save as default is available in the dialog, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
  + **Original Default Values**  
     The default values defined in the parameters' definition.
  + **User-Defined Default Values**  
     Your last-time saved default values.
* When Save as default is unavailable in the dialog, the Reset button contains only the text part. Selecting it will reset the values to the original default values.

**Cancel**

Cancels changing the parameter values and closes this dialog.

![Use Saved Values button](https://devnet.logianalytics.com/hc/article_attachments/4412131484695/btn_dshbrd_ussvvlu.gif)**Use Saved Values**

If it is available, you can select the previously saved parameter values to apply to the dashboard and save parameter values for reuse later.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714041-Edit-URL-Frame)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714081-Enter-Values)
