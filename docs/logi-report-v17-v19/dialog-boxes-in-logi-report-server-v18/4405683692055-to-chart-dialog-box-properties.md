---
title: "To Chart Dialog Box Properties"
id: 4405683692055
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683692055-To-Chart-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:51Z
---

# To Chart Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690529943-Top-N-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683693207-To-Crosstab-Dialog-Box-Properties)

# To Chart Dialog Box Properties

You can use the To Chart dialog box to [convert a crosstab into a chart](https://devnet.logianalytics.com/hc/en-us/articles/4405683959319-Manipulating-Data-Components-in-Page-Report#ToChart). This topic describes the properties in the dialog box.

This topic contains the following sections:

* [Chart Type Tab Properties](#ChartType)
* [Display Tab Properties](#Display)
* [Style Tab Properties](#Style)

You see these elements on all the tabs:

**Back**

Select to go to the previous tab.

**Next**

Select to go to the next tab.

**OK**

Select to convert the crosstab to a chart.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Chart Type Tab Properties

Specify the type of the chart.

![To Chart dialog box - Chart Type tab](https://devnet.logianalytics.com/hc/article_attachments/4420447148567/tochart_type.gif)

**Chart Type**

Select a chart type.

**Subtype**

Select a subtype of the selected chart type.

**Chart Type Groups**

Server lists the subtype you selected for the chart.

If you want to create a combo chart, select **<Add Combo Type>** under **Primary Axis** or **Secondary Axis**. Server adds an additional subtype. To change the additional subtype, select it, then select another chart type and its subtype respectively. To add more subtypes, repeat the procedure.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)**Remove button**

Select to remove the selected subtype. At least one type should remain for the **Primary Axis** to create the chart.

## Display Tab Properties

Specify the fields you want to display in the chart.

![To Chart dialog box - Display tab](https://devnet.logianalytics.com/hc/article_attachments/4420447149463/tochart_dsply.gif)

**Resources**

Server displays all the view elements used in the crosstab. Select a field, and then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif) beside the Category, Series, or Show Values box to add it into the corresponding box.

**Category**

Server lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) you want to display on the category axis of the chart. To remove a resource from the box, select it and select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif) on the left.

**Series**

Server lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) you want to display on the series axis of the chart. To remove a resource from the box, select it and select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif) on the left.

**Show Values**

Server lists the aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4420461476503/btn_bvaggrgtn.gif) you want to display on the value axis of the chart.

For a combo chart, specify resources for each chart type. To add a resource to a chart type, first select the resource and the chart type separately, then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).

To remove a resource from the box, select it and select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif) on the left.

**Order/Select N**

Select to open the [Order/Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683670423-Order-Select-N-Dialog-Box-Properties) to define the sort order and Select N condition in the chart.

## Style Tab Properties

Select a style for the chart. Server hides this tab when there is only one style available.

![To Chart dialog box - Style tab](https://devnet.logianalytics.com/hc/article_attachments/4420453614999/tochart_style.gif)

**Style**

Select the style you want to apply to the component.

* **Custom**  
   There is no style information in this style. Server only uses it to support reports you created in previous versions when they do not bind any style or their styles are not in the style list.

**Preview**

Server displays a diagram to illustrate the effect of the selected style on the component.

**Inherit Style**

Specify to take the style of the parent component. The property is available when the crosstab is in a banded object.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690529943-Top-N-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683693207-To-Crosstab-Dialog-Box-Properties)
