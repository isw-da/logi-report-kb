---
title: "Chart Definition"
id: 1500009719162
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719162-Chart-Definition
updated_at: 2021-07-25T07:20:10Z
---

# Chart Definition

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719142-Button-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745261-Chart-Wizard)

# Chart Definition

The Chart Definition dialog box is used to [modify the definition of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009723442-Manipulating-Data-Components#Chart).

There are the following tabs in this dialog box: [Chart Type](#Type), [Display](#Display) and [Style](#Style).

**OK**

Applies the settings and closes the dialog box.

**Cancel**

Cancels the settings and closes the dialog box.

**Help**

Displays the help document about this feature.

## Chart Type

This tab allows you to set the type of the chart.

![Chart Definition dialog - Chart Type tab](https://devnet.logianalytics.com/hc/article_attachments/4404942490391/chtdef_type.gif)

**Chart Type**

Lists all the chart types.

**Subtype**

Shows subtypes of the selected chart type in thumbnail form.

**Chart Type Groups**

Lists the subtypes defined for the chart.

To replace a chart type with another one, first select it, then select the wanted chart type and a sub type.

If you want to create a combo chart, select **<Add Combo Type>** of Primary Axis or Secondary Axis in the Chart Type Groups box, and an additional subtype will be added. To replace the additional subtype, select it, then specify the required type and subtype respectively. To add more subtypes, repeat the procedures.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif)

Removes the selected subtype. At least one type should remains for the Primary Axis so as to create the chart.

## Display

This tab allows you to set the fields that will be displayed in the chart.

![Chart Definition dialog - Display tab](https://devnet.logianalytics.com/hc/article_attachments/4404936779159/chtdef_dsply.gif)

**Resources**

Displays all the group objects and aggregation objects used in the chart.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif)

Adds the selected view element to the chart.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936742039/btn_rmvitem.gif)

Removes the selected view element.

**Category**

Lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) that will be displayed on the category axis of the chart.

**Series**

Lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) that will be displayed on the series axis of the chart.

**Show Values**

Lists the aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) and additional values ![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404936740759/btn_wbrpt_adtnl.gif) that will be displayed on the value axis of the chart.

* ![Edit Additional Values](https://devnet.logianalytics.com/hc/article_attachments/4404936751127/btn_pgrpt_edit.gif)  
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009719222-Edit-Additional-Values) dialog box to edit an additional value. Available only when an additional value is selected in the Show Values box.

**Order/Select N**

Opens the [Order/Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009746101-Order-Select-N) dialog box to define the sort order and Select N condition in the chart.

## Style

This tab allows you to select a style for the chart. It is hidden when there is only one style available.

![Chart Definition dialog - Style tab](https://devnet.logianalytics.com/hc/article_attachments/4404942603671/chtdef_style.gif)

**Style**

Lists the available styles.

* **Custom**  
   There is no style information in this style and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the chart.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719142-Button-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745261-Chart-Wizard)
