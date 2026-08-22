---
title: "Insert Link Dialog Box Properties"
id: 45203973247885
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203973247885-Insert-Link-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:55Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Insert Link Dialog Box Properties

This topic describes how you can use the Insert Link dialog box to link the selected object to a specified target. Server displays the dialog box when you right-click an object and select Link on the shortcut menu. 

Conditional Link

Select if you want to link the object to different targets based on different conditions.

- 
Add button
    Select to add a new condition using the Edit Conditions dialog box.

- 
Edit button
 Select to edit the selected condition.

- 
Remove button
    Select to remove the selected condition.

- 
Move Up button
    Select to move the selected condition higher in the list.

- 
Move Down button
    Select to move the selected condition lower in the list.

- 
Others
 Select if you want to define the link target of the object when none of the conditions you have specified is met.

Link Type

Specify the type of the link target for the object if it is not a conditional link or for the object under the selected condition if it is a conditional link. Select one of the following:

- Report

- URL

- E-mail

- Content

More

Select to display more link options. This button is available only to the Report and Content link types.

OK

Select to add the link to the object and close the dialog box.

Cancel

Select to close the dialog box without adding a link.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without adding a link.

## 
Report

Link the object to a report.

 Report

Specify the target linked report. Select Browse to select the report you want in the Select a Report dialog box. 

Target

Specify the window or frame in which you want to load the linked report.

- 
<Server Setting>
    Select to load the linked report according to setting of Target of Detail Table Report and Links in the Web Report Studio profile.

- 
Same Frame
 Select to load the linked report into the current frame. 

- 
Whole Window
    Select to load the linked report into the full browser window. Not available for links in charts.

- 
New Window
    Select to load the linked report into a new window. This window is not named. 

- 
Parent Frame
    Select to load the linked report into the parent frame of the frame that contains the link. Not available for links in charts.

- 
Other Frame
    Select to load the linked report into some other specified frame. If it cannot find the frame name, Server loads the linked file into a new window. 

Filter tab

Specify the filter conditions based on which you want to set up the link relationship between the primary report and the linked report.

- 
Components
    Specify the components in the linked report that you want to interlink with the primary report. 
    
- 
Add Component button
        Select to add a component in the linked report to interlink with the primary report.

- 
Remove Component button
        Select to remove the selected component. 

- 
Default Linked Component
    Specify the component you want to display by default in the linked report when you trigger the link in the exported output.

- 
Field Conditions
    Specify the link conditions between the primary report and the linked report.
- 
Mapping Table button
 The button is available when you select a linked data component in the Components box. Select this button to customize the mapping relationship between Current Field in the primary report and Corresponding Field in the linked report, using the Mapping Table dialog box.

- 
Add Condition button
               Select to add a new condition line.

- 
Remove Condition button
               Select to remove the selected condition lines. 

- 
Fields (Primary)
        Fields in the business view used by the selected component in the primary report. You may see these items:
- 
Current Field
Select to use the field that is related to the trigger object of the link.

- 
Current Category
Available to charts. Select to dynamically use the group field that displays on the category axis of the chart at runtime.

- 
Current Series
Available to charts. Select to dynamically use the group field that displays on the series axis of the chart at runtime.

- 
OP
  Specify the operator to compose the condition. It can be "=", "<>", "<", ">", "<=", ">=", or "IN".

- 
Fields (Linked)
      Fields in the business views of the linked report which are of the same data type as the selected fields in the primary report. Select Corresponding Field if you want to use the runtime field dynamically. When Corresponding Field is not available, you can select the Mapping Table button  to define a mapping relationship for Corresponding Field.

- 
Pass on-screen filters to the linked components
       Select to apply the on-screen filters, which includes the filters created via the Filter panel and filter controls in the primary report, to the selected components of the linked report.
  - 
Mapping Table
             Select to open the Mapping Table dialog box to define the mapping relationship based on which you want to pass the on-screen filters in the primary report to the linked report. Server activates this property when the trigger component in the primary report and the selected component in the linked report use different business views.

Parameters tab

This tab is available when the linked report uses parameters. You can assign values to the parameters of the linked report automatically.

- 
Parameter from Linked Report
    Server lists all parameters contained in the linked report.

- 
Field from Primary Report
    Server lists all the data fields, formulas, summaries, and parameters in the primary report which are of the same data type as the parameters of the linked report. Select the field whose value you want to assign to the parameter of the linked report. If the selected field is a parameter field, you can choose to assign its current value or initial value to the parameter of the linked report.
      
- 
Current Value
                 Select to assign the most recently specified value of the primary report parameter to the parameter of the linked report.

- 
Initial Value
                 Select to assign the original value of the primary report parameter to the parameter of the linked report.

Advanced tab

Specify to pass the values of the filter objects like filter controls in the primary report to those in the linked report.

- 
Add button
           Select to add a new line to pass values between the filter objects in the primary report and the linked report.

- 
Remove button
           Select to remove the selected lines. 

- 
Primary Report Property/Object
    Filter objects in the primary report whose values you want to pass to filter objects in the linked report. Select the ellipsis button  to select a filter object in the primary report in the Select Value dialog box.

- 
Linked Report Property/Object
    Filter objects in the linked report which will adopt the values passed from filter objects in the primary report. Select the ellipsis button  to select a filter object in the linked report in the Select Value dialog box. Make sure that the values of the filter object in the primary report can apply to the filter object in the linked report in the same line.

Pass style group information down to linked report

Select to apply the style group of the primary report to the linked report.

## 
URL

Link the object to URL.

Hyperlink

Specify the URL to link the object to. Fields can work in the hyperlink only when you insert them via "Add Dynamic Field".

- 
Add Dynamic Field
    Select to open the Select Field dialog box to insert a field into the URL.

Target

Specify the window or frame in which you want to load the URL.

- 
<Server Setting>
    Select to load the URL according to setting of Target of Detail Table Report and Links in the Web Report Studio profile. 

- 
Same Frame
    Select to load the URL into the current frame. 

- 
Whole Window
    Select to load the URL into the full browser window.

- 
New Window
    Select to load the URL into a new window. This window is not named.

- 
Parent Frame
 Select to load the URL into the parent frame of the frame that contains the link. 

- 
Other Frame
    Select to load the URL into some other specified frame. If it cannot find the frame name, Server loads the URL into a new window. 

## 
E-mail

Link the object to an email address.

Hyperlink

Specify the email address you want to link the object to. Then after you trigger the link, Server displays an email with the information you specified in the Hyperlink box. You can then further customize the email and send it. 

- 
Add Dynamic Field
  Select to open the Select Field dialog box to insert a field into the email address.

## 
Content

Link the object to a Blob data type field. It is to bind the Blob data type field to the object and display it as a hyperlink. You can download the Blob contents by triggering the link. In Report, Blob could be image, Binary, Blob, Clob, LongBlob, LongClob, Varbinary, or Longvarbinary. 

Query

Specify the business view which contains the Blob data type field you want.

When you set the link type to "Content", Server will check whether there are such kind of business views available. If not, it will disable the properties for this link type.

Content Type 

Specify the content type for the Blob type data. You can select the formula button  to bind it with a string type business view element, or with a dynamic formula in the current report. 

File Name 

Specify the file name for the Blob type data. You can select the formula button  to bind it with a string type business view element, or with a dynamic formula in the current report.

Content

Specify the Blob data type field in the selected business view. 

Filter tab

Specify the link conditions between the business view used by the current report and the business view that contains the linked Blob contents.

- 
Field Conditions 
    Specify the filter conditions between the two business views.
    
- 
Add button
        Select to add a new condition line. 

- 
Remove button
        Select to remove the selected condition lines.

- 
Fields (Primary)
        The fields of the business view that the current report uses.

- 
OP
        Specify the operator to compose the condition. It can be "=", "<>", "<", ">", "<=", ">=", or "IN".

- 
Fields (Linked)
      The fields in the business view that contains the linked Blob contents, which are of the same data type as the selected fields in the business view that the current report uses.

Parameters tab

This tab is available when the business view that contains the linked Blob contents uses parameters. You can assign values to the parameters automatically.

- 
Parameters
    Server lists all parameters that the business view containing the linked Blob contents uses.
  

- 
Value
  Server lists all the view elements in the business view as well as formulas, aggregations, and parameters used by the current report, which are of the same data type as the parameters the business view that contains the linked Blob contents uses. Select a field to assign its value to a parameter.
