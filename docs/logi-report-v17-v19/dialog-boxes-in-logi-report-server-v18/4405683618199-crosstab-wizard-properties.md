---
title: "Crosstab Wizard Properties"
id: 4405683618199
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683618199-Crosstab-Wizard-Properties
updated_at: 2022-01-27T07:58:36Z
---

# Crosstab Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683617175-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683620247-Customize-Gauge-Angle-Dialog-Box-Properties)

# Crosstab Wizard Properties

You can use the Crosstab Wizard dialog box to [create a crosstab report](https://devnet.logianalytics.com/hc/en-us/articles/4405683950743-Creating-Page-Reports#Crosstab). This topic describes the properties in the dialog box.

This topic contains the following sections:

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Query Filter Screen](#Filter)
* [Style Screen](#Style)

**Back**

Select to go to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to create the crosstab and exit the wizard.

**Cancel**

Select to close the wizard without creating a crosstab.

**Help**

Select to view information about the dialog box.

## Data Screen

Specify the business view you want to use to create the crosstab. Server hides this screen when there is only one business view in the current catalog.

![Crosstab Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4420447341591/crstbwzd_data.gif)

**Available Data Resources**

Select a business view in the current catalog, using which you want to create the crosstab.

## Display Screen

Specify the fields to display in the crosstab.

![Crosstab Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4420453503767/crstbwzd_dsply.gif)

**Resources**

Server displays the view elements in the selected business view. Select a non-folder resource.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif)**Add button**

Select to add the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) to display on the column header of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4420453428375/btn_addrow.gif)**Add button**

Select to add the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) to display on the row header of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4420461488791/btn_addsum.gif)**Add button**

Select to add the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4420461476503/btn_bvaggrgtn.gif) to be the aggregate field of the crosstab.

**Columns/Rows**

* **Field**  
   Server lists the group objects you added to display on the column/row headers of the crosstab.
* **Display Name**  
   Specify the labels for the column/row headers. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.
* **Sort**  
   Select the sort order of the group objects.
* ![Add Compound Group](https://devnet.logianalytics.com/hc/article_attachments/4420453504151/btn_pgrpt_addparal.gif)**Add Compound Group button**  
   Select to add a column/row compound group.

**Summaries**

* **Field**  
   Server lists the aggregation objects you added as the aggregate fields of the crosstab.
* **Display Name**  
   Specify the labels for the aggregations. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected field or compound group higher in the list. For fields in a compound group, you can only change their order within the current group.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected field or compound group lower in the list. For fields in a compound group, you can only change their order within the current group.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)**Remove button**

Select to remove the selected field or compound group that you do not want in the crosstab.

## Query Filter Screen

Specify the filter that you want to apply to the selected business view.

![Crosstab Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4420461717399/crstbwzd_qryfltr.gif)

Server displays the predefined filters of the business view in the **Query Filter** list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the list, and then define it.

If the selected business view contains parameters, Server displays the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683625623-Enter-Parameter-Values-Dialog-Box-Properties) for you to specify the parameter values before displaying the **Query Filter** screen.

For more information, see the [Query Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690522007-Query-Filter-Dialog-Box-Properties).

## Style Screen

Specify the style of the crosstab. Server hides this screen when there is only one style available to the crosstab.

![Crosstab Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4420461717655/crstbwzd_style.gif)

**Style**

Select a style you want to apply to the crosstab.

**Inherit Style**

Select to take the style of the parent component. The property is available when you insert the crosstab into a banded object.

**Preview**

Server shows a preview of the crosstab in the selected style.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683617175-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683620247-Customize-Gauge-Angle-Dialog-Box-Properties)
