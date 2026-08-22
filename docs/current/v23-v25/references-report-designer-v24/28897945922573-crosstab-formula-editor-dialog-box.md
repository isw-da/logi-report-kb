---
title: "Crosstab Formula Editor Dialog Box"
id: 28897945922573
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897945922573-Crosstab-Formula-Editor-Dialog-Box
updated_at: 2024-09-30T09:13:49Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Crosstab Formula Editor Dialog Box

You can use the Crosstab Formula Editor dialog box to compose crosstab formulas, which you can use to apply custom aggregate functions in a crosstab in a page or web report, or to control properties of the crosstab. This topic describes the options in the dialog box.
    

Designer displays the Crosstab Formula Editor dialog box when you do any of the following:

- In the Resources box of the crosstab wizard, select <New Crosstab Formula...> under the Crosstab Formulas node, type a name for the new crosstab formula and select OK.

- Select a crosstab component, then in the Data panel, select <New Crosstab Formula...> under the Crosstab Formulas node, type a name for the new crosstab formula and select OK.

- Right-click a crosstab formula in the Data panel and select Edit Formula on the shortcut menu.

- Select <New Crosstab Formula...> in the property value list when editing some properties of a crosstab or an object in the crosstab  in the Report Inspector.

 The following describes all the options Designer provides in the Crosstab Formula Editor dialog box. Some of them are not available when you are working with a business view-based crosstab.

Menu

- 
File
- 
New Formula
Select to create another formula in the catalog or dynamic formula in the current report.

- 
New Summary
Select to open the New Summary dialog box to create a summary in the catalog.

- 
New Parameter
Select to open the New Parameter dialog box to create a parameter in the catalog.

- 
Import UDF Classes
Select to open the UDF Classes dialog box to import user-defined formula classes.

- 
Save
Select to save the crosstab formula.

- 
Save As
Select to save the crosstab formula as a new crosstab formula by specifying a new name.

- 
Close
Select to close the dialog box.

- 
Edit
- 
Undo
Select to undo an action.

- 
Redo
Select to redo an action.

- 
Cut
Select to cut the specified text in the formula expression panel.

- 
Copy
Select to copy the specified text in the formula expression panel.

- 
Paste
Select to paste the text that you cut or copied in the formula expression panel.

- 
Delete
Select to delete the specified ted text in the formula expression panel.

- 
Search
Select to open the Find/Replace dialog box to search for text in the formula expression panel and replace the found text with different text.

- 
View
- 
Fields Panel
Select to show the Fields panel.

- 
Functions Panel
Select to show the Functions panel.

- 
Operators Panel
Select to show the Operators panel.

- 
Sort Tree
Select to sort the functions in the Functions panel and fields in the Fields panel by names.

- 
Formula
- 
Check
Select to test the syntax of the crosstab formula.

- 
Add Bookmark
Select to add a bookmark to a specific position.

- 
Go to Previous Bookmark
Select to go to the previous bookmark.

- 
Go to Next Bookmark
Select to go to the next bookmark.

- 
Clear all Bookmarks
Select to clear all of the bookmarks.

- 
Comment/Uncomment
Select to add or remove comments.

- 
Add Operators
Select to add a general operator in the formula expression panel.

- 
Color Converter
Select to open the color palette to insert the HEX code of a color.

- 
Auto Finish
Select to enable automatic insertion of the other part of a sign pair right after you type the first part when you edit the crosstab formula.

- 
Formula References
Select to show the formulas that reference the selected UDF function in the Functions panel.

- 
Properties
Select to edit properties of the crosstab formula in the Formula Properties dialog box. 
          
- 
Data Type
This property shows the data type of the crosstab formula's return value.

- 
Precision
Specify the precision of the crosstab formula's return value. When you set the precision to 0, Report Engine displays all characters of the return value; when you set it to N, Report Engine only displays the first N characters.

- 
Scale
Specify the number of digits to the right of the decimal point for the crosstab formula's return value.

- 
Help
Select to view information about the dialog box.

Toolbar

- 
New Formula
Select to create another formula in the catalog or dynamic formula in the current report.

- 
New Summary
Select to create a summary in the catalog.

- 
New Parameter
Select to create a parameter in the catalog.

- 
Save
Select to save the crosstab formula.

- 
Save As
Select to save the crosstab formula as a new crosstab formula by specifying a new name.

- 
Properties
Select to show properties of the crosstab formula in the Formula Properties dialog box. 
          
- 
Data Type
This property shows the data type of the return value of the crosstab formula.

- 
Precision
Specify the precision of the return value of the crosstab formula. If the precision is set to 0, all characters of the return value will be displayed; if it is set to N, only the first N characters will be displayed.

- 
Scale
Specify the number of digits to the right of the decimal point for the return value of the crosstab formula.

- 
Sort Tree
Select to sort the functions in the Functions panel and fields in the Fields panel by names.

- 
Fields Panel
Select to show the Fields panel.

- 
Functions Panel
Select  to show the Functions panel.

- 
Operators Panel
Select to show the Operators panel.

- 
Help
Select to view information about the dialog box.

Fields panel

This panel displays the fields that you can reference in the crosstab formula, such as DBFields, parameters, other formulas, and special fields. These fields vary depending on the data resource type of the crosstab, query resource or business view. Select one field and double-click it to insert the field into the formula expression panel at the insertion point.

Functions panel

This panel displays the Report built-in functions and imported user-defined formula functions that you can apply in the crosstab formula. Select one function and double-click it, Designer then inserts the function into the formula expression panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

Operators panel

This panel displays the Report built-in operators that you can apply in the crosstab formula. Select one operator and double-click it to insert the operator into the formula expression panel at the insertion point.

Formula expression panel

You can  edit your crosstab formula in this panel. There are several ways to work with a crosstab formula:

- Select an object from the Fields, Functions, or Operators panel and double-click it, Designer then inserts the object in the crosstab formula.

- Type your crosstab formula in the panel directly.

- Use the preceding two methods together.

- Paste crosstab formula text from the text document of other programs.

The toolbar in this panel provides the following buttons that facilitate the process of composing a formula.

- 
Cut
Select to cut the specified text in the panel.

- 
Copy
Select to copy the specified text in the panel.

- 
Paste
Select to paste the text that you cut or copied in the panel.

- 
Delete
Select to delete the specified text in the panel.

- 
Undo
Select to undo an action.

- 
Redo
Select to redo an action.

- 
Search
Select to open the Find/Replace dialog box to search for text in the panel and replace the found text with different text.

- 
Check
Select to test the syntax of the crosstab formula.

- 
Add Bookmark
Select to add a bookmark to a specific position.

- 
Go to Previous Bookmark
Select to go to the previous bookmark.

- 
Go to Next Bookmark
Select to go to the next bookmark.

- 
Clear All Bookmarks
Select to clear all of the bookmarks.

- 
Comment/Uncomment
Select to add or remove comments.

- 
Add Operators
Select to add a general operator in the panel.

- 
Color Converter
Select to open the color palette to insert the HEX code of a color.

Previous Topic  Next Topic
