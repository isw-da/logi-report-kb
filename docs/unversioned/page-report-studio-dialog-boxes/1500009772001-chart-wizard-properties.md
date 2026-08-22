---
title: "Chart Wizard Properties"
id: 1500009772001
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772001-Chart-Wizard-Properties
updated_at: 2021-07-24T00:49:22Z
---

# Chart Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744102-Chart-Definition-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744162-Color-List-Dialog-Box-Properties)

# Chart Wizard Properties

You can use the Chart Wizard dialog box to [create a chart report](https://devnet.logianalytics.com/hc/en-us/articles/1500009748862-Creating-Page-Reports#Chart). This topic describes the options in the dialog box.

Select the following screens in the wizard:

* [Data](#Data)
* [Type](#Type)
* [Display](#Display)
* [Query Filter](#Filter)
* [Style](#Style)

**Back**

Returns to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Creates the chart and closes the wizard.

**Cancel**

Closes the wizard without creating a chart.

**Help**

Displays the help document about this feature.

## Data

Specifies the business view to use to create the chart. Studio hides this screen when there is only one business view in the current catalog.

![Chart Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404880553623/chtwzd_data.gif)

**Available Data Resources**

Lists all the available business views in the current catalog, with which you can create the chart.

## Type

Specifies the type of the chart.

![Chart Wizard - Type screen](https://devnet.logianalytics.com/hc/article_attachments/4404880279575/chtwzd_type.gif)

**Chart Type**

Lists all the chart types.

**Subtype**

Shows subtypes of the selected chart type in thumbnail form.

**Chart Type Groups**

Lists the subtypes defined for the chart.

A default chart type exists in the **Chart Type Groups** box. To replace it with another one, first select it, then select chart type you want and a sub type.

If you want to create a combo chart, select **<Add Combo Type>** of Primary Axis or Secondary Axis in the Chart Type Groups box. Studio adds an additional subtype. To replace the additional subtype, select it, then specify the required type and subtype respectively. To add more subtypes, repeat the procedure.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected subtype. At least one type should remain for the Primary Axis to create the chart.

## Display

Specifies the fields to display in the chart.

![Chart Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404885403927/chtwzd_dsply.gif)

**Resources**

Displays the view elements in the selected business view. Select one non-folder resource each time and then select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif) beside the Category, Series, or Show Values box to add it into the corresponding box.

**Category**

Lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) you want to display on the category axis of the chart. If you do not want the current resource, select it and select ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif) on the left to remove it.

**Series**

Lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) you want to display on the series axis of the chart. If you do not want the current resource, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif) on the left to remove it.

**Show Values**

Lists the aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) and additional values ![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404880175511/btn_wbrpt_adtnl.gif) you want to display on the value axis of the chart. For a combo chart, specify resources for each chart type. To add a resource to a chart type, first select the resource and the chart type separately, then select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif).

To remove a resource from the box, select it and select ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif) on the left.

* ![Edit Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404880196759/btn_pgrpt_edit.gif)  
   Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009772081-Edit-Additional-Values-Dialog-Box-Properties) dialog box to edit an additional value. Available only when you select an additional value in the **Show Values** box.

**Order/Select N**

Opens the [Order/Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009772821-Order-Select-N-Dialog-Box-Properties) dialog box to define the sort order and Select N condition in the chart.

## Query Filter

Specifies the filter which you want to apply to the selected business view.

![Chart Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404880553879/chtwzd_qryfltr.gif)

In this screen, Studio displays the predefined filters of the business view in the **Query Filter** drop-down list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the drop-down list, and then define it according to your requirements.

If the selected business view contains parameters, Studio displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009772161-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify values to the parameters before it displays the **Query Filter** screen.

For more information, see [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009744982-Query-Filter-Dialog-Box-Properties) dialog box.

## Style

Specifies the style of the chart. Studio hides this screen when there is only one style available to the chart.

![Chart Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404880554263/chtwzd_style.gif)

**Style**

Lists all the available styles for you to select from.

**Inherit Style**

Specifies to take the style of the parent component. The option is available only when you specify to insert the chart into a banded object or table.

**Preview**

Shows a preview of the selected style.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744102-Chart-Definition-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744162-Color-List-Dialog-Box-Properties)
