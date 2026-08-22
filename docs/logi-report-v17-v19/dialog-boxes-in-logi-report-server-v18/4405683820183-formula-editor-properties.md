---
title: "Formula Editor Properties"
id: 4405683820183
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683820183-Formula-Editor-Properties
updated_at: 2022-01-27T07:59:16Z
---

# Formula Editor Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690588951-Format-Wall-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683849239-Group-Footer-Properties)

# Formula Editor Properties

This topic describes how you can use the Formula Editor dialog box to create or edit a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/4405684037271-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-) in a web report, or create an expression to control the value of the specified property.

Server displays the dialog box when you do either of the following:

* Navigate to Dynamic Resources > Formulas in the Resources panel of Web Report Studio or the Resources box of the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties). Then, select <Add Formula…>, or right-click a dynamic formula and select **Edit** from the shortcut menu.
* Select the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447036695/btn_wbrpt_fmla.gif) in the value cell, and then select <Edit Expression> or <Create Formula> from the value drop-down list when setting property values in the Inspector panel.

![Formula Editor dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447093911/fmlaedtr.gif)

**Formula Name**

Specify the name of the formula. Disabled when you are creating an expression.

**Use As**

Select a [view element type](https://devnet.logianalytics.com/hc/en-us/articles/4405684032791-An-Introduction-to-Business-Views) that you want to use the formula as: Group, Detail, or Aggregation. When you are creating a dynamic formula, the default value is blank, which means that Logi Report defines whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object.

Disabled when you are creating an expression.

**Fields box**

Server lists the fields that are available to formulas. The fields include the group, detail, and aggregation objects in the current business view, the dynamic formulas and aggregations that you have created in the report, ![This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.](https://devnet.logianalytics.com/hc/article_attachments/4420461527063/___newv18.3.jpg "New for version 18.3.")and local/global parameters. You can double-click a field to insert it into the editing box at the insertion point.

**Functions box**

Server lists the Logi Report built-in functions and user defined functions that are available to formulas. You can double-click a function to insert it into the editing box at the insertion point completely with its required syntax items (such as parentheses and commas).

**Operators box**

Server lists the operators that are available to formulas. You can double-click an operator to insert it into the editing box at the insertion point.

**Editing box**

In this box, you can build and edit your formula, using several ways:

* Double-click an item in the Fields, Functions, and Operators boxes to insert it in the formula.
* Type your formula directly.
* Paste formula contents here.

**![Check button](https://devnet.logianalytics.com/hc/article_attachments/4420461616919/btn_wbrpt_check.gif)****Check button**

Select to test the formula syntax. If it is incorrect, you need to correct the errors.

![Operator button](https://devnet.logianalytics.com/hc/article_attachments/4420453537943/btn_wbrpt_oprtr.gif)**Add Operators button**

Select a general operator you want to use in the formula.

**![Color Palette](https://devnet.logianalytics.com/hc/article_attachments/4420453538199/btn_wbrpt_color.gif)****Color Converter button**

Select to open a color palette. Then, select a color, or select **More Colors** to specify a color in the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties). Server inserts the HEX code of the color in your formula.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690588951-Format-Wall-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683849239-Group-Footer-Properties)
