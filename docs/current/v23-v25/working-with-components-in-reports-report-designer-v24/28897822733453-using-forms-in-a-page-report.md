---
title: "Using Forms in a Page Report"
id: 28897822733453
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897822733453-Using-Forms-in-a-Page-Report
updated_at: 2024-09-30T09:08:00Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Using Forms in a Page Report

In order to make web controls accept user inputs and submit requests to Server, you can add the web controls to a form and then define properties of the form. This topic introduces how you can use forms in a page report.

This topic contains the following sections:

- Creating Forms in a Page Report 

- Adding Objects to a Form

- Making Web Controls Work in a Form

## 
Creating Forms in a Page Report 

To create a form in a page report, you can do either of the following:

- From the Components panel, drag the Form icon   in the Web Controls category to the report.

- Navigate to Insert > Web Controls > Form.

You can use the following commands on the shortcut menu of a form:

- 
Unmark Form
Select to clear this form.

- 
Delete Form
Select to delete this form.

- 
Remove All Controls
Select to remove all the objects you have added to the form.

- 
Properties
Select to show properties of the form in the Report Inspector.

- 
Save Style
Select to create a CSS style for the form.

## 
Adding Objects to a Form

 To add an object to a form, right-click the object, and on the shortcut menu, select the target form from the Add to Form submenu. You can add the object to a new form or an existing one. In Designer, the icon  represents a form. If you select the icon, you can find that the form and all the objects added to it are enclosed by a red dashed outline.

After you have added an object  to a form, if you want to remove it from the form, you can right-click the object and select Remove from Form from the shortcut menu. You can remove all the objects that you have added to a form simply by right-clicking the form and then selecting Remove All Controls. 

## 
Making Web Controls Work in a Form

After adding web controls to a form, you need to make the web controls cooperate, that is, you must set some properties of the form so as to organize the web controls and define their working mode. To do this, select the form, go to the Report Inspector, and then edit properties of the form. 

The following example illustrates the usage of form. In this example, a text field and a button in a report enable users to search for a particular string using Google.

- Create a page report containing a blank report tab.

- In the report tab, insert two web controls: a Text Field and a Button.

- Right-click the text field, select Display Type from the shortcut menu, then in the Display Type dialog box, set the following options (leave other options to the default values). Name: q
Value: "" (null)
Max Length: 30

- Right-click the button, select Display Type on the shortcut menu and set the following options in the Display Type dialog box. Value: Google
Action: Submit Form

- Select the two web controls, then right-click and navigate to Add to Form > Add to New Form on the shortcut menu.

- Set properties of the form in the Report Inspector.Form Action: http://www.google.com/search
Form Method: get
Form Target: blank

- Save the report.

- Navigate to View > Preview As > Page Report Result to run the report in Page Report Studio. Now you can type a string up to 30 characters in the text field, and then select Google to search for that string. Page Report Studio displays the search results in a new browser window. 

 For a table, if you add a field to a new form, Designer creates the form  in the first cell of the table row which contains the field, and you cannot add fields in the previous table rows to this newly-created form. If you add columns before the first cell, you cannot add fields in these columns of the same table row to the form either.

Previous Topic  Next Topic
