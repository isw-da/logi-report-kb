---
title: "Chart Wizard Properties"
id: 4405690500375
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690500375-Chart-Wizard-Properties
updated_at: 2022-01-27T07:58:35Z
---

# Chart Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683613719-Chart-Definition-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690501271-Color-List-Dialog-Box-Properties)

# Chart Wizard Properties

You can use the Chart Wizard dialog box to [create a chart report](https://devnet.logianalytics.com/hc/en-us/articles/4405683950743-Creating-Page-Reports#Chart). This topic describes the properties in the dialog box.

This topic contains the following sections:

* [Data Screen](#Data)
* [Type Screen](#Type)
* [Display Screen](#Display)
* [Query Filter Screen](#Filter)
* [Style Screen](#Style)

**Back**

Select to return to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to create the chart and exit the wizard.

**Cancel**

Select to close the wizard without creating a chart.

**Help**

Select to view information about the dialog box.

## Data Screen

Select the business view you want to use to create the chart. Server hides this screen when there is only one business view in the current catalog.

![Chart Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4420447345687/chtwzd_data.gif)

**Available Data Resources**

Select a business view in the current catalog, which you use to create the chart.

## Type Screen

Specify the type of the chart.

![Chart Wizard - Type screen](https://devnet.logianalytics.com/hc/article_attachments/4420453503383/chtwzd_type.gif)

**Chart Type**

Select a chart type.

**Subtype**

Select a subtype of the selected chart type.

**Chart Type Groups**

Server lists the subtype you selected for the chart.

If you want to create a combo chart, select **<Add Combo Type>** under **Primary Axis** or **Secondary Axis**. Server adds an additional subtype. To change the additional subtype, select it, then select another chart type and its subtype respectively. To add more subtypes, repeat the procedure.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)**Remove button**

Select to remove the selected subtype. At least one type should remain for the **Primary Axis** to create the chart.

## Display Screen

Specify the fields you want to display in the chart.

![Chart Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4420447168279/chtwzd_dsply.gif)

**Resources**

Server displays the view elements in the selected business view. Select one non-folder resource, and then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif) beside the Category, Series, or Show Values box to add it into the corresponding box.

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

## Query Filter Screen

Specify the filter which you want to apply to the selected business view.

![Chart Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4420453661975/chtwzd_qryfltr.gif)

Server displays the predefined filters of the business view in the **Query Filter** list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the list, and then define it.

If the selected business view contains parameters, Server displays the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683625623-Enter-Parameter-Values-Dialog-Box-Properties) for you to specify the parameter values before displaying the **Query Filter** screen.

For more information, see the [Query Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690522007-Query-Filter-Dialog-Box-Properties).

## Style Screen

Select a style for the chart. Server hides this screen when there is only one style available.

![Chart Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4420461719959/chtwzd_style.gif)

**Style**

Select the style you want to apply to the chart.

**Inherit Style**

Specify to take the style of the parent component. The property is available when you insert the chart into a banded object or table.

**Preview**

Server displays a diagram to illustrate the effect of the selected style on the component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683613719-Chart-Definition-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690501271-Color-List-Dialog-Box-Properties)
