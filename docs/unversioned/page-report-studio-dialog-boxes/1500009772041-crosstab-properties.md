---
title: "Crosstab Properties"
id: 1500009772041
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772041-Crosstab-Properties
updated_at: 2021-07-24T00:49:19Z
---

# Crosstab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744122-Conditional-Formatting-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744202-Crosstab-Wizard-Properties)

# Crosstab Properties

You can use the Crosstab Properties dialog box to edit the properties of a crosstab. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Border Tab Properties](#Border)
* [Crosstab Tab Properties](#Crosstab)
* [Others Tab Properties](#Others)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows general information of the crosstab.

![Crosstab Properties Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880550423/crstbprpty_gnrl.gif)

**Name**

Specifies the display name of the crosstab.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

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

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

## Border Tab Properties

This tab shows information about borders of the crosstab.

![Crosstab Properties Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404885598487/crstbprpty_border.gif)

**Color**

Specifies the color of the borders. To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the border transparent, type Transparent in the text box.

**Has Border**

Specifies whether to show the borders.

## Crosstab Tab Properties

This tab shows the layout-related information of the crosstab.

![Crosstab Properties Properties dialog - Crosstab tab](https://devnet.logianalytics.com/hc/article_attachments/4404880551191/crstbprpty_crstb.gif)

**Horizontal Gap**

Specifies the space between the content and left/right edge of a crosstab cell.

**Vertical Gap**

Specifies the space between the content and top/bottom edge of a crosstab cell.

**Block Gap**

Specifies the spacing between each part of the crosstab if the crosstab will be split into more than one part.

**Row Totals on Top**

Specifies whether to display the Total row in the first row of the crosstab.

**Column Totals on Left**

Specifies whether to display the Total column in the first column in the crosstab.

**Repeat Column Header**

Specifies whether to repeat column headings on every page.

**Avoid Orphan Header**

Sometimes the column header happens to be at the bottom of a page. To keep the column header together with the data in the next page, set this property to true.

**Expand Data**

Specifies whether to enable Page Report Studio users to expand or collapse dimensions in the crosstab.

**Suppress Row Header**

Specifies whether to hide the row headers.

**Outside Aggregate Title**

Specifies whether to place the titles of aggregate fields outside.

**Suppress Column Header**

Specifies whether to hide the column headers.

**Table Style**

Specifies whether to add headers to the Total rows and columns.

**Repeat Aggregate**

Specifies whether to repeat the crosstab for different aggregate fields. For more information, see Repeat Aggregate in the *Logi Report Designer Guide*.

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

You can view and configure the miscellaneous settings.

![Crosstab Properties Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404880551447/crstbprpty_other.gif)

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

**Current Row Block Index**

Specifies the vertical index of the data block. 0 means the first block index, and 1 the second, and so on.

**Current Column Block Index**

Specifies the horizontal index of the data block. 0 means the first block index, and 1 the second, and so on.

**Items per Row Block**

Specifies the number of rows of records in each data block.

**Items per Column Block**

Specifies the number of columns of records in each data block.

The four properties work together to control the data of the crosstab to display in continuous page mode: Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.

**TOC Anchor**

Specifies whether to add the node that represents the crosstab to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the crosstab in the report result when Server returns no record to its parent data component.

**Export to XLS**

If true, Server will export the component when you save the report result as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

If true, Server will export the component when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744122-Conditional-Formatting-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744202-Crosstab-Wizard-Properties)
