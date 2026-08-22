---
title: "Crosstab Properties"
id: 1500009746862
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746862-Crosstab-Properties
updated_at: 2021-07-24T00:48:32Z
---

# Crosstab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746822-Convert-to-Table-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775081-Crosstab-Wizard-Properties)

# Crosstab Properties

This topic describes how you can use the Crosstab Properties dialog box to update the properties of a crosstab. Server displays the dialog box when you right-click a crosstab and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Border Tab Properties](#Border)
* [Crosstab Tab Properties](#Crosstab)
* [Others Tab Properties](#Others)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Crosstab Properties dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

## General Tab Properties

This tab shows some general information of the crosstab.

![Crosstab Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880398743/crstbprpty_gnrl.gif)

**Name**

Specifies the display name of the crosstab.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Horizontal Alignment**

Specifies the horizontal justification of the crosstab. Choose an option from the drop-down list.

* **Left**: Aligns the crosstab on the left of the tabular cell.
* **Right**: Aligns the crosstab on the right of the tabular cell.
* **Center**: Aligns the crosstab in the center of the tabular cell.

**Background**

Specifies the background color of the crosstab.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.

## Border Tab Properties

This tab shows information about borders of the crosstab.

![Crosstab Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880398999/crstbprpty_border.gif)

**Color**

Specifies the color of the borders.

**Width**

Specifies the width of the borders.

**Top Line**

Specifies the line style of the top border. Choose a style from the drop-down list.

**Bottom Line**

Specifies the line style of the bottom border. Choose a style from the drop-down list.

**Left Line**

Specifies the line style of the left border. Choose a style from the drop-down list.

**Right Line**

Specifies the line style of the right border. Choose a style from the drop-down list.

## Crosstab Tab Properties

This tab shows the layout-related information of the crosstab.

![Crosstab Properties dialog - Crosstab tab](https://devnet.logianalytics.com/hc/article_attachments/4404885490455/crstbprpty_crstb.gif)

**Row Totals on Top**

Specifies whether to display the Total row in the first row of the crosstab.

**Column Totals on Left**

Specifies whether to display the Total column in the first column in the crosstab.

**Suppress Column Header**

Specifies whether to suppress the column headers.

**Suppress Row Header**

Specifies whether to suppress the row headers.

**Aggregate**

Specifies the layout of the aggregate fields.

* **Vertical Layout**  
  Select this option to arrange the aggregate fields vertically.
  + **Number of Rows**  
     Specifies the number of rows to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a row so that the aggregate fields are positioned in one column vertically. A number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of rows (3 for example) less than the number of aggregate fields (6 for example), there will be 3 rows to hold the 6 fields with each row containing 2 fields.
* **Horizontal Layout**  
   Select this option to arrange the aggregate fields horizontally. When you have multiple aggregate fields in the crosstab, using horizontal layout can make the report more readable.
  + **Number of Columns**  
     Specifies the number of columns to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a column so that the aggregate fields are positioned in one row horizontally. A number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of columns (3 for example) less than the number of aggregate fields (6 for example), there will be 3 columns to hold the 6 fields with each column containing 2 fields.

## Others Tab Properties

You can use this tab to view and configure some miscellaneous settings.

![Crosstab Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404880399255/crstbprpty_other.gif)

**Current Row Block Index**

Specifies the vertical index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.

**Current Column Block Index**

Specifies the horizontal index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.

**Items per Row Block**

Specifies the number of rows of records in each data block.

**Items per Column Block**

Specifies the number of columns of records in each data block.

The four properties work together to control the data of the crosstab to be displayed in continuous page mode: Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746822-Convert-to-Table-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775081-Crosstab-Wizard-Properties)
