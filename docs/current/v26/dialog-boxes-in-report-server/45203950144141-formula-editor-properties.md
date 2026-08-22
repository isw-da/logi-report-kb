---
title: "Formula Editor Properties"
id: 45203950144141
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203950144141-Formula-Editor-Properties
updated_at: 2026-04-30T14:09:41Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Formula Editor Properties

This topic describes how you can use the Formula Editor dialog box to create or edit a dynamic formula in a web report, or create an expression to control the value of the specified property. 

Server displays the dialog box when you do either of the following:

- Navigate to Dynamic Resources > Formulas in the Resources panel of Web Report Studio or the Resources box of the Web Report Wizard. Then, select <Add Formula…>, or right-click a dynamic formula and select Edit from the shortcut menu.
            

- Select the formula button  in the value cell, and then select <Edit Expression> or <Create Formula> from the value drop-down list when setting property values in the Inspector panel.
            

Formula Name

Specify the name of the formula. Server disables Formula Name when you are creating an expression.

Use As

Select a view element type that you want to use the formula as: Group, Detail, or Aggregation. When you are creating a dynamic formula, the default value is blank, which means that Report defines whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object.

Disabled when you are creating an expression. 

Fields box

Server  lists the fields that are available to formulas. You can double-click a field to insert it into the editing box at the insertion point.

Functions box

Server  lists the Report built-in functions and user defined functions that are available to formulas. You can double-click a function to insert it into the editing box at the insertion point completely with its required syntax items (such as parentheses and commas).

Operators box

Server lists the operatorsoperators that are available to formulas. You can double-click an operator to insert it into the editing box at the insertion point.

Editing box

In this box, you can build and edit your formula, using several ways:

- Double-click an item in the Fields, Functions, and Operators boxes to insert it in the formula.

- Type your formula directly.

- Paste formula contents here.

Check button

Select to test the formula syntax. If it is incorrect, you need to correct the errors.

Add Operators button

Select a general operator you want to use in the formula.

Color Converter button

Select to open a color palette. Then, select a color, or select More Colors to specify a color in the Color Picker dialog box. Server inserts the HEX code of the color in your formula.

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
