---
title: "Enter Parameter Values Dialog Box Properties"
id: 5741442503831
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741442503831-Enter-Parameter-Values-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:56Z
---

# Enter Parameter Values Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741420715927-Encrypt-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741413870359-Enter-Values-Dialog-Box-Properties)

# Enter Parameter Values Dialog Box Properties

Use the Enter Parameter Values dialog box to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values) to run a report. This topic describes how to specify parameter values.

Server displays the dialog box when you run a report with parameters.

![Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905758454807/enterprmvlu.gif)

**Parameters**

Server displays the parameters that the report uses. [Edit the values](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values) according to your requirement.

**![Use Saved Values button](https://devnet.logianalytics.com/hc/article_attachments/9905671743127/btn_srv_ussvvlu.gif) Use Saved Values**

If you see this icon, you can select the previously saved parameter values to apply to the report and [save parameter values for reuse later](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values#Reuse).

**Save as default**

Select if you want to save the current parameter values as the default parameter values for the report. Server displays this option when you did not clear [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#DefaultParam) the corresponding report type in the server profile.

This option is a user-report level setting. It is an action and takes effect after you select **Submit** in the dialog box. Its initial status is always cleared.

**Do not show this screen again**

When you select this option, the next time you run the report from the Server Console, it will use the default parameter values directly without popping up this dialog box, which could be the default values specified in the parameters' definition or the default values you saved last time for the report on Server. However, if the default values cannot completely match the current report parameters, Server still displays this dialog box.

This option is a user-report level setting. You can see it when you did not clear [Enable Hiding Initial Parameter Dialog For](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#HideParam) the corresponding report type in the server profile.

**Submit**

Select to run the report using the parameter values you specified here.

**Reset**

Select to reset the parameter values. This button varies according to different situations:

* When Server displays **Save as default** in the dialog box, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, Server resets the values to the original default values.
  + **Original Default Values**  
     The default values defined in the parameters' definition.
  + **User Defined Default Values**  
     The default values you saved last time.
* When you do not see **Save as default** in the dialog box, the Reset button contains only the text part. Selecting it will reset the values to the original default values.

**Cancel**

Select to close the dialog box without running the report.

**Help**

Select to view information about the Enter Parameter Values dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741420715927-Encrypt-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741413870359-Enter-Values-Dialog-Box-Properties)
