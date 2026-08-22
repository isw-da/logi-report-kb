---
title: "Enter Parameter Values Dialog Box Properties"
id: 5741441420695
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741441420695-Enter-Parameter-Values-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:40Z
---

# Enter Parameter Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741426072471-Edit-URL-Frame-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741412804759-Enter-Values-Dialog-Box-Properties)

# Enter Parameter Values Dialog Box Properties

Use the Enter Parameter Values dialog box to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/5741423625879-Specifying-Parameter-Values-for-a-Dashboard) to rerun the dashboard. This topic describes how to specify parameter values.

Server displays the dialog box after you select the Enter Parameters Values button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/9905575308823/btn_dshbrd_prm.gif) on the toolbar when a dashboard uses parameters. If you have enabled **Show Enter Parameter Values Dialog** in the JDashboard profile, Server also displays this dialog box when you run a dashboard with parameters. In this dialog box, Server lists all the parameters used in the current dashboard. Server allows same-name parameters when they are from different library components.

![Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905772383511/enterprmvlu.gif)

**Parameters**

Server displays the parameters of all the library components in the dashboard. Edit the values according to your requirements.

**Save as default**

Select if you want to save the current parameter values as the default parameter values for the dashboard. It takes effect after you select **Submit** in the dialog box.

This property's initial status is always cleared.

Server displays this property when you did not clear [Enable Setting Default Parameter Values For Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#DefaultParam) in the server profile.

**Submit**

Select to run the dashboard using the parameter values you specified here.

**Reset**

Select to reset the parameter values. This button varies with different situations:

* When Server displays **Save as default** in the dialog box, the **Reset** button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button, Server resets the values to those you applied last time.
  + ****Last Values****  
     The values you applied last time.
  + **User Defined Default Values**  
     The default values you saved last time.
* When you do not see **Save as default** in the dialog box, the **Reset** button contains only the text part. Selecting it will reset the values to those you applied last time.

**Cancel**

Select to close the dialog box without changing the parameter values.

![Use Saved Values button](https://devnet.logianalytics.com/hc/article_attachments/9905772399895/btn_dshbrd_ussvvlu.gif)**Use Saved Values button**

If you see this icon, you can select the previously saved parameter values to apply to the dashboard and save parameter values for reuse later.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the Enter Parameter Values dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without changing the parameter values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741426072471-Edit-URL-Frame-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741412804759-Enter-Values-Dialog-Box-Properties)
