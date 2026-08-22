---
title: "Crosstab Properties"
id: 1500009719202
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719202-Crosstab-Properties
updated_at: 2021-07-25T07:20:09Z
---

# Crosstab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719182-Conditional-Formatting)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745321-Crosstab-Wizard)

# Crosstab Properties

The Crosstab Properties dialog box is used to edit the properties of a crosstab.

There are the following tabs in this dialog box: [General](#General), [Border](#Border), [Crosstab](#Crosstab) and [Others](#Others).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the crosstab.

![Crosstab Properties Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404942602903/crstbprpty_gnrl.gif)

**Name**

Specifies the display name of the crosstab.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Position**

Displays the position mode of the crosstab. If the crosstab is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The crosstab's position will be decided by its X and Y property values.
* **Static**: The crosstab will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

**X**

Specifies the X coordinate of the crosstab, in inches.

**Y**

Specifies the Y coordinate of the crosstab, in inches.

**Width**

Specifies the width of the crosstab, in inches.

**Height**

Specifies the height of the crosstab, in inches.

**Background**

Specifies the background color of the crosstab.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

## Border

This tab shows information about borders of the crosstab.

![Crosstab Properties Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404936949783/crstbprpty_border.gif)

**Color**

Specifies the color of the borders. To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the border transparent, type Transparent in the text box.

**Has Border**

Specifies whether or not to show the borders.

## Crosstab

This tab shows the layout-related information of the crosstab.

![Crosstab Properties Properties dialog - Crosstab tab](https://devnet.logianalytics.com/hc/article_attachments/4404936950039/crstbprpty_crstb.gif)

**Horizontal Gap**

Specifies the space between the content and left/right edge of a crosstab cell.

**Vertical Gap**

Specifies the space between the content and top/bottom edge of a crosstab cell.

**Block Gap**

Specifies the spacing between each part of the crosstab if the crosstab will be split into more than one part.

**Row Totals on Top**

Specifies whether or not to display the Total row in the first row of the crosstab.

**Column Totals on Left**

Specifies whether or not to display the Total column in the first column in the crosstab.

**Repeat Column Header**

Specifies whether or not to repeat column headings on every page.

**Avoid Orphan Header**

Sometimes the column header happens to be at the bottom of a page. To keep the column header together with the data in the next page, set this property to true.

**Expand Data**

Specifies whether or not to enable Page Report Studio users to expand or collapse dimensions in the crosstab.

**Suppress Row Header**

Specifies whether or not to hide the row headers.

**Outside Aggregate Title**

Specifies whether or not to place the titles of aggregate fields outside.

**Suppress Column Header**

Specifies whether or not to hide the column headers.

**Table Style**

Specifies whether or not to add headers to the Total rows and columns.

**Repeat Aggregate**

Specifies whether or not to repeat the crosstab for different aggregate fields. For more information, refer to Repeat Aggregate in the *Logi Report Designer Guide*.

**Aggregate**

Specifies the layout of the aggregate fields.

* **Vertical Layout**  
   If selected, the aggregate fields will be arranged vertically.
  + **Number of Rows**   
     Specifies the number of rows to be displayed in the crosstab. By default, it is -1, which means that there is only one column with which to arrange the aggregate fields vertically; if it is set to 1, that means there will be only one row to arrange the aggregate fields horizontally; if it is set to a number larger than 1, that means there will be this number of aggregate rows; if this number is larger than the number of aggregate fields in the crosstab, it will be treated as -1.
* **Horizontal Layout**  
   If selected, the aggregate fields will be arranged horizontally.
  + **Number of Columns**   
     Specifies the number of columns to be displayed in the crosstab. By default, it is -1, which means that there is only one row with which to arrange the aggregate fields horizontally; if it is set to 1, that means there will be only one column to arrange the aggregate fields vertically; if it is set to a number larger than 1, that means there will be this number of aggregate columns; if this number is larger than the number of aggregate fields in the crosstab, it will be treated as -1.

## Others

You can use this tab to view and configure some miscellaneous settings.

![Crosstab Properties Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404936950295/crstbprpty_other.gif)

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

**Current Row Block Index**

Specifies the vertical index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.

**Current Column Block Index**

Specifies the horizontal index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.

**Items per Row Block**

Specifies the number of rows of records in each data block.

**Items per Column Block**

Specifies the number of columns of records in each data block.

The four properties work together to control the data of the crosstab to be displayed in continuous page mode: Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.

**TOC Anchor**

Specifies whether or not to add the node that represents the crosstab to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the crosstab in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, the crosstab will be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog box).

**Export to CSV**

If true, the crosstab will be exported when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719182-Conditional-Formatting)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745321-Crosstab-Wizard)
