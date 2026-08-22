---
title: "Crosstab Properties"
id: 5741434505367
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741434505367-Crosstab-Properties
updated_at: 2022-10-31T17:17:18Z
---

# Crosstab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985324126999-Crosstab-Formula-Editor-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741428630807-Crosstab-Wizard-Properties)

# Crosstab Properties

This topic describes how you can use the Crosstab Properties dialog box to update the properties of a crosstab. Server displays the dialog box when you right-click a crosstab and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Border Tab Properties](#Border)
* [Crosstab Tab Properties](#Crosstab)
* [Others Tab Properties](#Others)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## General Tab Properties

Specify the general properties of the crosstab.

![Crosstab Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905734132631/crstbprpty_gnrl.gif)

**Name**

Specify the display name of the crosstab.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Horizontal Alignment**

Select the horizontal justification of the crosstab.

* **Left**  
  Select to align the crosstab on the left of the tabular cell.
* **Right**  
  Select to align the crosstab on the right of the tabular cell.
* **Center**  
  Select to align the crosstab in the center of the tabular cell.

**Background**

Specify the background color of the crosstab.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

## Border Tab Properties

Specify the border properties of the crosstab.

![Crosstab Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/9905755981719/crstbprpty_border.gif)

**Color**

Specify the border color.

**Width**

Specify the border width in inches.

**Top Line**

Select the style of the top border line.

**Bottom Line**

Select the style of the bottom border line.

**Left Line**

Select the style of the left border line.

**Right Line**

Select the style of the right border line.

## Crosstab Tab Properties

Specify the layout-related properties of the crosstab.

![Crosstab Properties dialog - Crosstab tab](https://devnet.logianalytics.com/hc/article_attachments/9905756023191/crstbprpty_crstb.gif)

**Row Totals on Top**

Select to display the Total row in the first row of the crosstab.

**Column Totals on Left**

Select to display the Total column in the first column in the crosstab.

**Suppress Column Header**

Select to suppress the column headers.

**Suppress Row Header**

Select to suppress the row headers.

**Aggregate**

Specify the layout of the aggregate fields.

* **Vertical Layout**  
  Select to arrange the aggregate fields vertically.
  + **Number of Rows**  
     Specify the number of rows to hold the aggregate fields in the crosstab. By default, it is -1 which means that Server places each aggregate field in a row so that the aggregate fields are in one column vertically. Server treats a number equal to or larger than the number of aggregate fields in the crosstab as -1. If you set the number of rows (3 for example) less than the number of aggregate fields (6 for example), there will be 3 rows to hold the 6 fields with each row containing 2 fields.
* **Horizontal Layout**  
   Select to arrange the aggregate fields horizontally. When you have multiple aggregate fields in the crosstab, using horizontal layout can make the report more readable.
  + **Number of Columns**  
     Specify the number of columns to hold the aggregate fields in the crosstab. By default, it is -1 which means that Server places each aggregate field in a column so that the aggregate fields are in one row horizontally. Server treats a number equal to or larger than the number of aggregate fields in the crosstab as -1. If you set the number of columns (3 for example) less than the number of aggregate fields (6 for example), there will be 3 columns to hold the 6 fields with each column containing 2 fields.

## Others Tab Properties

Configure some miscellaneous settings.

![Crosstab Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/9905756044567/crstbprpty_other.gif)

**Current Row Block Index**

Specify the vertical index of the data block that will display. 0 means the first block index, 1 the second, and so on.

**Current Column Block Index**

Specify the horizontal index of the data block that will display. 0 means the first block index, 1 the second, and so on.

**Items per Row Block**

Specify the number of rows of records in each data block.

**Items per Column Block**

Specify the number of columns of records in each data block.

These four properties work together to control the data of the crosstab to display in the continuous page mode.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985324126999-Crosstab-Formula-Editor-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741428630807-Crosstab-Wizard-Properties)
