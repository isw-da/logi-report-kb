---
title: "Crosstab Wizard Properties"
id: 5741424076567
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741424076567-Crosstab-Wizard-Properties
updated_at: 2022-10-31T17:16:13Z
---

# Crosstab Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741402255511-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741396975255-Customize-Gauge-Angle-Dialog-Box-Properties)

# Crosstab Wizard Properties

You can use the Crosstab Wizard dialog box to [create a crosstab report](https://devnet.logianalytics.com/hc/en-us/articles/5741469017879-Creating-Page-Reports#Crosstab). This topic describes the properties in the dialog box.

This topic contains the following sections:

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Dataset Filter Screen](#Filter)
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

Specify the business view or dataset you want to use to create the crosstab. Server hides this screen when there is only one business view or dataset in the current catalog.

![Crosstab Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/9905816984855/crstbwzd_data.gif)

**Available Data Resources**

Select a business view or dataset in the current catalog, using which you want to create the crosstab.

* **Inherit from the Parent**  
  Select if you want the data component to inherit the dataset of the parent object. Available only when you are inserting the data component into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel.

## Display Screen

Specify the fields to display in the crosstab.

![Crosstab Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/9905675047959/crstbwzd_dsply.gif)

**Resources**

Server displays the view elements in the selected business view or the business view of the selected dataset. Select a non-folder resource.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif)**Add button**

Select to add the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) to display on the column header of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/9905620190103/btn_addrow.gif)**Add button**

Select to add the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) to display on the row header of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/9905620225559/btn_addsum.gif)**Add button**

Select to add the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/9905618017943/btn_bvaggrgtn.gif) to be the aggregate field of the crosstab.

**Columns/Rows**

* **Field**  
   Server lists the group objects you added to display on the column/row headers of the crosstab.
* **Display Name**  
   Specify the labels for the column/row headers. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.
* **Sort**  
   Select the sort order of the group objects.
* ![Add Compound Group](https://devnet.logianalytics.com/hc/article_attachments/9905713527831/btn_pgrpt_addparal.gif)**Add Compound Group button**  
   Select to add a column/row compound group.

**Summaries**

* **Field**  
   Server lists the aggregation objects you added as the aggregate fields of the crosstab.
* **Display Name**  
   Specify the labels for the aggregations. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif)**Move Up button**

Select to move the selected field or compound group higher in the list. For fields in a compound group, you can only change their order within the current group.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**

Select to move the selected field or compound group lower in the list. For fields in a compound group, you can only change their order within the current group.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**

Select to remove the selected field or compound group that you do not want in the crosstab.

## Dataset Filter Screen

Specify the filter that you want to apply to the dataset of the crosstab.

![Crosstab Wizard - Dataset Filter screen](https://devnet.logianalytics.com/hc/article_attachments/9905817000471/crstbwzd_dtstfltr.gif)

Server displays the predefined filters of the business view in the **Filter** list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the list, and then define it.

If the selected business view contains parameters, Server displays the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741410399895-Enter-Parameter-Values-Dialog-Box-Properties) for you to specify the parameter values before displaying the **Dataset Filter** screen.

For more information, see the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985324060055-Edit-Dataset-Filter-Dialog-Box-Properties).

## Style Screen

Specify the style of the crosstab. Server hides this screen when there is only one style available to the crosstab.

![Crosstab Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/9905778310551/crstbwzd_style.gif)

**Style**

Select a style you want to apply to the crosstab.

**Inherit Style**

Select to take the style of the parent component. The property is available when you insert the crosstab into a banded object.

**Preview**

Server shows a preview of the crosstab in the selected style.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741402255511-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741396975255-Customize-Gauge-Angle-Dialog-Box-Properties)
