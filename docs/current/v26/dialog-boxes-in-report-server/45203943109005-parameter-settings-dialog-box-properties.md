---
title: "Parameter Settings Dialog Box Properties"
id: 45203943109005
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203943109005-Parameter-Settings-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:15Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Parameter Settings Dialog Box Properties

This topic describes how you can use the Parameter Settings dialog box to customize the default parameter values for a report.

Parameters

Server lists all the parameters the report uses. Edit the values as you want.

If the report uses no parameter, Server displays "No Parameter Needed" here.

Save as default

Select if you want to save current parameter values as the default parameter values for the report. Server displays this property when you did not clear Enable Setting Default Parameter Values For the corresponding report type in the server profile.

This property is a user-report level setting. It is an action and takes effect after you select Submit in the dialog box. Its initial status is always cleared.

Import parameter data with xml file
Added an export button on the page, which allows you to save the current values of parameters on the current page as an XML file and export them when clicked.

A menu item called 'load XML' has been added to the dropdown list of the reset button. After clicking it can import parameter data with xml file instead of manually type in.

Re-enable Parameter Screen 

Select if you want to display the Enter Parameter Values dialog box when you run the report  on the Server Console.

Clear this property if you want the report to use the default parameter values directly without displaying the Enter Parameter Values dialog box when you run the report on the Server Console. However, if the default values cannot completely match the report parameters, Server will still display the Enter Parameter Values dialog box. You can select this property to show the Enter Parameter Values dialog box again after hiding it.

This property is a user-report level setting. It is available when you did not clear Enable Hiding Initial Parameter Dialog For the corresponding report type in the server profile.

OK

Select to apply any changes you made here and exit the dialog box.

Reset

Select to reset the parameter values. This button varies with different situations:

- When Server displays Save as default in the dialog box, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button, Server resets the values to the original default values.  
    
- 
Original Default Values
        The default values defined in the parameters' definition.

- 
User Defined Default Values
        The default values you saved last time.

- When you do not see Save as default in the dialog box, the Reset button contains only the text part. Selecting it will reset the values to the original default values. 

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
