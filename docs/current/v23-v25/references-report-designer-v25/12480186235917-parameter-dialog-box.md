---
title: "Parameter Dialog Box"
id: 12480186235917
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480186235917-Parameter-Dialog-Box
updated_at: 2026-02-25T23:48:57Z
source_host: docs-report.zendesk.com
---
# 
Parameter Dialog Box

You can use the Parameter dialog box to define the parameter values using which to run a library component as a response to the message the current data component receives at runtime. This topic describes the options in the dialog box.
    

Designer displays different options in the dialog box according to the different sources where you open it.

If you open the Parameter dialog box by selecting 0003 - Parameter from the drop-down list of the Message ID column and selecting the ellipsis  in the Actions column of the Receive Message dialog box, you can use it to define the built-in Parameter message for the current data component to receive at runtime.

Designer displays these options:

Add button

Select to add a line to specify parameter value. 

Remove button

 Select to delete the specified parameter line.

Move Up button

 Select to move the specified parameter line higher in the list.

Move Down button

  Select to move the specified parameter line lower in the list.

 Designer disables the four buttons when you select the Customized type for the parameter message in the Receive Message dialog box.

Parameter Name

This column shows the parameters that you add to run the library component containing the data component with.

Operator

This column shows the operator to compose the parameter condition. It can only be "=".

Value

This column shows the values that you specify for the parameters.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

If you open the Parameter dialog box by selecting a user-defined message from the drop-down list of the Message ID column, selecting the ellipsis  in the Actions column of the Receive Message dialog box, and then selecting *Parameter and selecting OK in the Web Action List dialog box, you can use it edit the user-defined Parameter message for the current data component  to receive at runtime.

Designer displays these options:

Submit Action to Handler

Specify the handler to receive the parameters of the web action.

- 
Default Handler in Current Server
Select to submit the action to the current server to handle.

- 
Customized Path
Select to submit the action to a customized path to handle, for example, http://127.0.0.1:8888/.

Get Input From

Designer does not enable this option for defining a parameter message.

Apply Action To

Specify the target to which to apply the action involved in the message.

- 
Library Component 
Select to run a specified library component using the parameter values defined in the dialog box when the data component receives the message. You can select Browse to the specify the library component or type the path and file name of the library component in the text box.- 
Web Control
Designer does not enable this option for defining a parameter message.

- 
Target Frame
Select the window or frame to open the library component.
    
- 
<Input>
Select and type the window or frame name in the text box. 

- 
Constant
- 
blank
Select to load the library component into a new blank window. This window is not named.

- 
self
Select to load the library component into the window from which the message is sent out (the active window).

- 
parent
Select to load the library component into the immediate parent window of the active window. If there is no parent window, the active window is used.

- 
top
Select to load the library component into the topmost window.

- 
Refresh Current Library Component
Select to rerun the current library component using the parameter values defined in the dialog box when the data component receives the message.

Add button

Select to add a line to specify parameter value.

Remove button

 Select to delete the specified parameter line.

Move Up button

 Select to move the specified parameter line higher in the list.

Move Down button

  Select to move the specified parameter line lower in the list. 

Parameter Name

This column shows the parameters that you add to run the specified or current library component with.

Operator

This column shows the operator to compose the parameter condition. It can only be "=".

Value

This column shows the values that you specify for the parameters.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
