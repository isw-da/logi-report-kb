---
title: "Formula Editor Dialog Box"
id: 12480073073165
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480073073165-Formula-Editor-Dialog-Box
updated_at: 2026-02-25T23:49:31Z
source_host: docs-report.zendesk.com
---
# 
Formula Editor Dialog Box

You can use the Formula Editor dialog box to write a formula in a catalog, a custom aggregation in a business view, or a dynamic formula in the current report, to edit an expression to control the value of a property, or to create the formula that defines how you want to fetch pagination data for a JSON schema. This topic describes the options in the dialog box.
    

Designer displays the Formula Editor dialog box when you do one of the following:

- In the Catalog Manager, right-click the Formulas node, select New Formula from the shortcut menu, type a name for the new formula and then select OK, or right-click a formula and select Edit from the shortcut menu.

- In the Data panel, right-click a formula and select Edit Formula from the shortcut menu.

- Select <New Formula…> or <Edit Expression...> where a formula list is available.

- Select Settings in the General tab of the New View Element dialog box or Edit View Element dialog box.

- Select New Formula or  in the Main Formula drop-down list in the Extract JSON Schema screen of the JSON Connection Wizard dialog box.

 The following describes all options in the Formula Editor dialog box. You will not be able to use some of them due to how you might use the formula.

Menu

- 
File
- 
New Formula
Select to create another formula in the catalog or a dynamic formula in the current report.

- 
New Summary
Select to open the New Summary dialog box to create a summary in the catalog.

- 
New Parameter
Select to open the New Parameter dialog box to create a parameter  in the catalog.

- 
Import UDF Classes
Select to open the UDF Classes dialog box to import user-defined formula classes.

- 
Save
Select to save the formula. 

- 
Save As
Select to save the formula with a different name.

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
Select to test the syntax of the formula.

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
Select to enable automatic insertion of the other part of a sign pair right after you type the first part when you edit the formula.

- 
Formula References
Select to show the formulas that reference the selected UDF function in the Functions panel.

- 
Properties
Select to show properties of the formula in the Formula Properties dialog box. 
          
- 
Data Type
This property shows the data type of the return value of the formula.

- 
Precision
Specify the precision of the return value of the formula. If the precision is set to 0, all characters of the return value will be displayed; if it is set to N, only the first N characters will be displayed.

- 
Scale
Specify the number of digits to the right of the decimal point for the return value of the formula.

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
Select to save the formula.

- 
Save As
Select to save the formula as a new formula by specifying a new name.

- 
Properties
Select to edit properties of the formula in the Formula Properties dialog box. 
          
- 
Data Type
This property shows the data type of the formula's return value.

- 
Precision
Specify the precision of the formula's return value. When you set the precision to 0, Report Engine displays all characters of the return value; when you set it to N, Report Engine only displays the first N characters.

- 
Scale
Specify the number of digits to the right of the decimal point for the formula's return value.

- 
Sort Tree
Select to sort the functions in the Functions panel and fields in the Fields panel by names.

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
Help
Select to view information about the dialog box.

- 
Use As
Designer displays this option when you use the dialog box for a dynamic formula. You can use it to specify to use the formula as one of the following view element types: Group, Detail, or Aggregation.

Fields panel

This panel displays the fields that you can reference in the formula, such as DBFields, parameters, other formulas, and special fields. These fields vary depending on how you are going to use the formula. Select one field and double-click it to insert the field into the formula expression panel at the insertion point.

Functions panel

This panel displays the Report built-in functions and imported user-defined formula functions that you can apply in the formula. Select one function and double-click it, Designer then inserts the function into the formula expression panel at the insertion point completely with its required syntax items (parentheses, commas, and so on).

Operators panel

This panel displays the Report built-in operators that you can apply in the formula. Select one operator and double-click it to insert the operator into the formula expression panel at the insertion point.

Formula expression panel

You can edit your formula in this panel. There are several ways to work with a formula:

- Select an object from the Fields, Functions, or Operators panel and double-click it, Designer then inserts the object in the formula.

- Type your formula in the panel directly.

- Use the preceding two methods together.

- Paste formula text from the text document of other programs.

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
Select to test the syntax of the formula.

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
