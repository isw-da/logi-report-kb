---
title: "Chart Definition Dialog Box Properties"
id: 4405683613719
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683613719-Chart-Definition-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:36Z
---

# Chart Definition Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683612695-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690500375-Chart-Wizard-Properties)

# Chart Definition Dialog Box Properties

You can use the Chart Definition dialog box to [modify the definition of a chart](https://devnet.logianalytics.com/hc/en-us/articles/4405683959319-Manipulating-Data-Components-in-Page-Report#Chart). This topic describes the properties in the dialog box.

This topic contains the following sections:

* [Chart Type Tab Properties](#Type)
* [Display Tab Properties](#Display)
* [Style Tab Properties](#Style)

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Chart Type Tab Properties

Specify the type of the chart.

![Chart Definition dialog box - Chart Type tab](https://devnet.logianalytics.com/hc/article_attachments/4420461558807/chtdef_type.gif)

**Chart Type**

Select a chart type.

**Subtype**

Select a subtype of the selected chart type.

**Chart Type Groups**

Server lists the subtypes you selected for the chart.

If you want to create a combo chart, select **<Add Combo Type>** under **Primary Axis** or **Secondary Axis**. Server adds an additional subtype. To change the additional subtype, select it, then select another chart type and its subtype respectively. To add more subtypes, repeat the procedure.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)**Remove button**

Select to remove the selected subtype. At least one type should remain for the **Primary Axis** to create the chart.

## Display Tab Properties

Specify the fields you want to display in the chart.

![Chart Definition dialog box - Display tab](https://devnet.logianalytics.com/hc/article_attachments/4420447147927/chtdef_dsply.gif)

**Resources**

Server displays all the group objects and aggregation objects in the chart. Select one non-folder resource and then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif) beside the Category, Series, or Show Values box to add it into the corresponding box.

**Category**

Server lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) you want to display on the category axis of the chart. If you do not want the current resource, select it, and then select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif) on the left to remove it.

**Series**

Server lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) you want to display on the series axis of the chart. If you do not want the current resource, select it, and then select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif) on the left to remove it.

**Show Values**

Server lists the aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4420461476503/btn_bvaggrgtn.gif) and additional values ![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4420461490583/btn_wbrpt_adtnl.gif) you want to display on the value axis of the chart.

For a combo chart, specify resources for each chart type. To add a resource to a chart type, first select the resource and the chart type separately, then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).

For an additional value, you can select the **Edit** button ![Edit Additional Values](https://devnet.logianalytics.com/hc/article_attachments/4420461515287/btn_pgrpt_edit.gif)to open the [Edit Additional Value dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690502295-Edit-Additional-Values-Dialog-Box-Properties).

To remove a resource from the box, select it and select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif) on the left.

**Order/Select N**

Select to open the [Order/Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683670423-Order-Select-N-Dialog-Box-Properties) to define the sort order and Select N condition in the chart.

## Style Tab Properties

Select a style for the chart. Server hides this tab when there is only one style available.

![Chart Definition dialog box - Style tab](https://devnet.logianalytics.com/hc/article_attachments/4420453664407/chtdef_style.gif)

**Style**

Select the style you want to apply to the component.

* **Custom**  
   There is no style information in this style. Server only uses it to support reports you created in previous versions when they do not bind any style or their styles are not in the style list.

**Preview**

Server displays a diagram to illustrate the effect of the selected style on the component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683612695-Button-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690500375-Chart-Wizard-Properties)
