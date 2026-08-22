---
title: "Customized Control – Web Action Builder Dialog Box"
id: 12480050379917
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480050379917-Customized-Control-Web-Action-Builder-Dialog-Box
updated_at: 2026-02-25T23:49:53Z
source_host: docs-report.zendesk.com
---
# 
Customized Control – Web Action Builder Dialog Box

You can use the Customized Control-Web Action Builder dialog box to bind, create, or edit a customized control. This topic describes the options in the dialog box.
    

Designer displays the Customized Control-Web Action Builder dialog box when you do one of the following:

- Select Customized Control and then select OK in the Web Action List dialog box.

- In the Manage Customized Controls dialog box, select Add , then in the New Customized Control File dialog box, provide a file name and select OK.

- In the Manage Customized Controls dialog box, right-click a customized control file and select Edit from the shortcut menu.

Designer displays these options:

Size

You can specify the size of the customized control shown in the browser window at runtime in this box.

- 
Auto
Select to automatically size the customized control according to its content.

- 
Width
Designer enables this option when you do not select Auto. Type a number to specify the width of the control in pixels.

- 
Height
Designer enables this option when you do not select Auto. Type a number to specify the height of the control in pixels.

Position

You can specify the position of the customized control in the browser window at runtime in this box.

- 
In the center of the browser window
Select  to place the customized control in the center of the browser window at runtime.

- 
According to mouse position
Select to place the customized control where you select the mouse. This option is useful when the event is concerned with mouse action.

- 
Relative to the trigger component
Select to place the customized control where the trigger object is. 

- 
Absolute
Select it and you can customize the location of the customized control.
    
- 
Position X
Specify the absolute X position in pixels.

- 
Position Y
Specify the absolute Y position in pixels.

Contents

Specify HTML fragment with JavaScript code. The HTML fragment should be plain text that is children DOM element of HTML Body.

Save As

Select to open the New Customized Control File dialog box to save the customized control definition into a file.

OK

- Select to save the customized control definition into the web action and exits the Customized Control-Web Action Builder dialog box, if you open the dialog box by selecting Customized Control and then selecting OK in the Web Action List dialog box.

- Select to save the customized control definition into the specified file and exits the Customized Control-Web Action Builder dialog box, if you open the dialog box  by selecting  in the Customized Control Manger dialog box and then providing a file name and selecting OK in the New Customized Control File dialog box.

- Select to save the changes to the customized control file, if you open the Customized Control-Web Action Builder dialog box by right-clicking a customized control file and then selecting Edit from the shortcut menu in the Customized Control Manger dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
