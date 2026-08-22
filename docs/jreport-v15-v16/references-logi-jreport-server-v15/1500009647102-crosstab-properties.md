---
title: "Crosstab Properties"
id: 1500009647102
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009647102-Crosstab-Properties
updated_at: 2021-07-24T20:54:36Z
---

# Crosstab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009671621-Convert-to-Table)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009647122-Crosstab-Wizard)

# Crosstab Properties

The Crosstab Properties dialog appears when you right-click a crosstab and select Properties from the shortcut menu. It helps you to specify the properties of the crosstab and contains the following tabs:

* [General](#General)
* [Border](#Border)
* [Crosstab](#Crosstab)
* [Others](#Others)

**OK**

Applies the settings and closes this dialog.

**Cancel**

Cancels the settings and closes this dialog.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920501783/btn_help.gif)

Displays the help document about this feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926700311/btn_close.gif)

Ignores the setting and closes this dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## General

This tab shows some general information of the crosstab. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920551319/crstbprpty_gnrl.gif)

**Name**

Specifies the display name of the crosstab, which will be shown on the shortcut menu of the crosstab.

**Show NLS Value**

Specifies to show the translated name of the display name of the crosstab in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the crosstab is not modified.

**Horizontal Alignment**

Specifies the horizontal justification of the crosstab. Choose an option from the drop-down list.

* **Left**: Aligns the crosstab on the left of the tabular cell.
* **Right**: Aligns the crosstab on the right of the tabular cell.
* **Center**: Aligns the crosstab in the center of the tabular cell.

**Background**

Specifies the background color of the crosstab.

To change the color, select the color indicator to select a color, or select **More Colors** in the color indicator to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009671641-Color-Picker-) dialog in which you can select a color within a wider range or input a color string in the format #RRGGBB. If you want to make the background transparent, input Transparent in the text box.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Border

This tab shows information about borders of the crosstab. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920551703/crstbprpty_border.gif)

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Crosstab

This tab shows the layout-related information of the crosstab. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920551959/crstbprpty_crstb.gif)

**Row Total on Top**

Specifies whether or not to display the Total row in the first row of the crosstab.

**Column Total on Left**

Specifies whether or not to display the Total column in the first column in the crosstab.

**Suppress Column Header**

Specifies whether or not to suppress the column headers.

**Suppress Row Header**

Specifies whether or not to suppress the row headers.

**Aggregate**

Specifies the layout of the aggregate fields.

* **Vertical Layout**  
   If selected, the aggregate fields will be arranged vertically.
  + **Number of Rows**   
     Specifies the number of rows to be displayed in the crosstab. By default, it is -1, which means that there is only one column with which to arrange the aggregate fields vertically; if it is set to 1, that means there will be only one row to arrange the aggregate fields horizontally; if it is set to a number larger than 1, that means there will be this number of aggregate rows; if this number is larger than the number of aggregate fields in the crosstab, it will be treated as -1.
* **Horizontal Layout**  
   If selected, the aggregate fields will be arranged horizontally.
  + **Number of Columns**   
     Specifies the number of columns to be displayed in the crosstab. By default, it is -1, which means that there is only one row with which to arrange the aggregate fields horizontally; if it is set to 1, that means there will be only one column to arrange the aggregate fields vertically; if it is set to a number larger than 1, that means there will be this number of aggregate rows; if this number is larger than the number of aggregate fields in the crosstab, it will be treated as -1.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Others

You can use this tab to view and configure some miscellaneous settings. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920552343/crstbprpty_other.gif)

**Current Row Block Index**

Specifies the vertical index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.

**Current Column Block Index**

Specifies the horizontal index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.

**Items per Row Block**

Specifies the number of rows of records in each data block.

**Items per Column Block**

Specifies the number of columns of records in each data block.

The four properties work together to control the data of the crosstab to be displayed in continuous page mode: Current Row Block Index, Current Column Block Index, Items per Row Block, and Items per Column Block.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009671621-Convert-to-Table)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009647122-Crosstab-Wizard)
