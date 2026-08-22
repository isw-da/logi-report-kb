---
title: "Enter Parameter Values Dialog Box Properties"
id: 45203938744845
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203938744845-Enter-Parameter-Values-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:47Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Enter Parameter Values Dialog Box Properties 

Use the Enter Parameter Values dialog box  to  specify the parameter values to rerun the dashboard. This topic describes how to specify parameter values.

Server displays the dialog box after you select the Enter Parameters Values button  on the toolbar when a dashboard uses parameters. If you have enabled Show Enter Parameter Values Dialog in the JDashboard profile, Server also displays this dialog box when you run a dashboard with parameters. In this dialog box, Server lists all the parameters used in the current dashboard. Server allows same-name parameters when they are from different library components. 

Parameters

Server displays the parameters of all the library components in the dashboard. Edit the values according to your requirements. 

Save as default

Select if you want to save the current parameter values as the default parameter values for the dashboard. It takes effect after you select Submit in the dialog box.

This property's initial status is always cleared.

Server displays this property when you did not clear Enable Setting Default Parameter Values For Dashboard in the server profile. 

Submit

Select to run the dashboard using the parameter values you specified here.

Reset

Select to reset the parameter values. This button varies with different situations:

- When Server displays Save as default in the dialog box, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button, Server resets the values to those you applied last time. 
    
- 
Last Values
        The values you applied last time.

- 
User Defined Default Values
        The default values you saved last time.

- When you do not see Save as default in the dialog box, the Reset button contains only the text part. Selecting it will reset the values to those you applied last time. 

Cancel

Select to close the dialog box without changing the parameter values.

Use Saved Values button

If you see this icon, you can select the previously saved parameter values to apply to the dashboard and save parameter values for reuse later.

Help button

Select to view information about the Enter Parameter Values dialog box.

Close button

Select to close the dialog box without changing the parameter values.
