---
title: "Formula Editor Properties"
id: 1500009775341
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775341-Formula-Editor-Properties
updated_at: 2021-07-24T00:48:26Z
---

# Formula Editor Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775821-Format-Wall-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775841-Group-Footer-Properties)

# Formula Editor Properties

This topic describes how you can use the Formula Editor dialog box to create or edit a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009750082-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-) in a web report, or create an expression to control the value of the specified property.

Server displays the dialog box when you expand the Dynamic Resource > Formulas node in the Resources panel of Web Report Studio or the Resources box of the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776601-Web-Report-Wizard-Properties), then select <Add Formula…>, right-click a dynamic formula and select **Edit** from the shortcut menu, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif) in the value cell and select <Edit Expression> or <Create Formula> from the value drop-down list when setting property values in the Inspector panel.

![Formula Editor dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885343383/fmlaedtr.gif)

**Formula Name**

Specifies the name of the formula. Disabled when creating an expression.

**Use As**

Specifies to use the formula as one of the following [view element types](https://devnet.logianalytics.com/hc/en-us/articles/1500009749982-An-Introduction-to-Business-Views): Group, Detail, or Aggregation. When you are creating a dynamic formula, the default value is blank which means that Logi Report will decide whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object.

Disabled when creating an expression.

**Fields box**

Displays a list of fields that are available to formulas. The fields include the group, detail and aggregation objects in the current business view, and the dynamic formulas and aggregations that have been created in the report. You can select one field and double-click it to insert the field into the editing box at the insertion point.

**Functions box**

Displays a list of the Logi Report built-in functions and user defined functions that are available to formulas. When you select one function and double-click it, Logi Report will insert the selected function into the editing box at the insertion point completely with its required syntax items (parentheses, commas, and so on).

**Operators box**

Displays a list of operators that are available to formulas. Select one operator and double-click it to insert the selected operator into the editing box at the insertion point.

**Editing box**

In this box, you can build and edit your formula. There are several ways to work with formulas:

* Select formula components from the Fields, Functions and Operators boxes in the Formula Editor, and then double-click the components, Logi Report will then insert them in the formula.
* Type your formula in the editing box directly.
* Use the above two methods together.
* Paste formula text from the text document of other programs.

**![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404880316055/btn_wbrpt_check.gif)**

Tests the syntax of your formula. If the syntax is incorrect, Logi Report provides an opportunity to correct the errors.

![Operator button](https://devnet.logianalytics.com/hc/article_attachments/4404885434519/btn_wbrpt_oprtr.gif)

Selects a general operator to be used in the editing box.

**![Color Palette](https://devnet.logianalytics.com/hc/article_attachments/4404880316311/btn_wbrpt_color.gif)**

A color palette is provided for you to insert the HEX code of a color simply by selecting the corresponding color in the color palette instead of typing the HEX code manually.

**OK**

Creates or edits the formula and closes the dialog box.

**Cancel**

Cancels the creating or editing of the formula and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775821-Format-Wall-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775841-Group-Footer-Properties)
