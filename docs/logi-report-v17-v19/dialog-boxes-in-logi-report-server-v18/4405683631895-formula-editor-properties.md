---
title: "Formula Editor Properties"
id: 4405683631895
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683631895-Formula-Editor-Properties
updated_at: 2022-01-27T07:58:39Z
---

# Formula Editor Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683655703-Format-Value-Y2-Axis-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683657367-Group-Properties)

# Formula Editor Properties

You can use the Formula Edit dialog box to create or edit a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/4405690650263-Using-Dynamic-Resources-in-Page-Report#Formula) in a report. This topic describes the properties in the dialog box.

![Formula Editor dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420453496855/fmlaedtr.gif)

**Formula Name**

Specify the name of the formula.

**Use As**

Select a [view element type](https://devnet.logianalytics.com/hc/en-us/articles/4405684032791-An-Introduction-to-Business-Views) that you want to use the formula as: Group, Detail, or Aggregation. When you are creating a dynamic formula, the default value is blank, which means that Logi Report defines whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object.

**Fields**

Server lists the fields that are available to formulas. The fields include the group, detail, and aggregation objects in the current business view, the dynamic formulas and aggregations that you have created in the report, ![This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.](https://devnet.logianalytics.com/hc/article_attachments/4420461527063/___newv18.3.jpg "New for version 18.3.")and local/global parameters. You can double-click a field to insert it into the editing box at the insertion point.

**Functions**

Server lists the Logi Report built-in functions and user defined functions that are available to formulas. You can double-click a function to insert it into the editing box at the insertion point completely with its required syntax items (such as parentheses and commas).

**Operators**

Server lists the operators that are available to formulas. You can double-click an operator to insert it into the editing box at the insertion point.

**Editing box**

In this box, you can build and edit your formula, using several ways:

* Double-click an item in the Fields, Functions, and Operators boxes to insert it in the formula.
* Type your formula directly.
* Paste formula contents here.

**![Check button](https://devnet.logianalytics.com/hc/article_attachments/4420453437335/btn_pgrpt_check.gif) Check button**

Select to test the formula syntax. If it is incorrect, you need to correct the errors.

![Add Operators button](https://devnet.logianalytics.com/hc/article_attachments/4420447296151/btn_pgrpt_oprtr.gif)**Add Operators button**

Select a general operator you want to use in the formula.

**![Color Converter button](https://devnet.logianalytics.com/hc/article_attachments/4420461692695/btn_pgrpt_color.gif) Color Converter button**

Select to open the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a color. Server inserts the HEX code of the color in your formula.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683655703-Format-Value-Y2-Axis-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683657367-Group-Properties)
