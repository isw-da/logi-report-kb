---
title: "Enter Parameter Values Dialog Box Properties"
id: 45203941872781
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203941872781-Enter-Parameter-Values-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:08Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Enter Parameter Values Dialog Box Properties

Use the Enter Parameter Values dialog box to specify the parameter values to run a report. This topic describes how to specify parameter values.

Server displays the dialog box when you run a report with parameters.

Parameters

Server displays the parameters that the report uses. Edit the values according to your requirement.

 Use Saved Values

If you see this icon, you can select the previously saved parameter values to apply to the report and save parameter values for reuse later.

Save as default

Select if you want to save the current parameter values as the default parameter values for the report. Server displays this option when you did not clear Enable Setting Default Parameter Values For the corresponding report type in the server profile. 

This option is a user-report level setting. It is an action and takes effect after you select Submit in the dialog box. Its initial status is always cleared.

Do not show this screen again

When you select this option, the next time you run the report from the Server Console, it will use the default parameter values directly without popping up this dialog box, which could be the default values specified in the parameters' definition or the default values you saved last time for the report on Server. However, if the default values cannot completely match the current report parameters, Server still displays this dialog box.

This option is a user-report level setting. You can see it when you did not clear Enable Hiding Initial Parameter Dialog For the corresponding report type in the server profile.

Submit

Select to run the report using the parameter values you specified here.

Reset

Select to reset the parameter values. This button varies according to different situations: 

- When Server displays Save as default in the dialog box, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, Server resets the values to the original default values. 
    
- 
Original Default Values
        The default values defined in the parameters' definition.

- 
User Defined Default Values
        The default values you saved last time.

- When you do not see Save as default in the dialog box, the Reset button contains only the text part. Selecting it will reset the values to the original default values. 

Cancel

Select to close the dialog box without running the report.

Help

Select to view information about the Enter Parameter Values dialog box.
