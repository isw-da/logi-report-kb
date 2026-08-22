---
title: "Crosstab Wizard Properties"
id: 1500009744202
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744202-Crosstab-Wizard-Properties
updated_at: 2021-07-24T00:49:20Z
---

# Crosstab Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772041-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772061-Customize-Gauge-Angle-Dialog-Box-Properties)

# Crosstab Wizard Properties

You can use the Crosstab Wizard to [create a crosstab report](https://devnet.logianalytics.com/hc/en-us/articles/1500009748862-Creating-Page-Reports#Crosstab). This topic describes the options in the dialog box.

Select the following screens in this wizard:

* [Data](#Data)
* [Display](#Display)
* [Query Filter](#Filter)
* [Style](#Style)

**Back**

Returns to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Creates the crosstab and closes the wizard.

**Cancel**

Closes the wizard without creating a crosstab.

**Help**

Displays the help document about this feature.

## Data

Specifies the business view to use to create the crosstab. Studio hides this screen when there is only one business view in the current catalog.

![Crosstab Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404880549527/crstbwzd_data.gif)

**Available Data Resources**

Lists all the available business views in the current catalog, with which you can create the crosstab.

## Display

Specifies the fields to display in the crosstab.

![Crosstab Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404885404823/crstbwzd_dsply.gif)

**Resources**

Displays the view elements in the selected business view. Select one non-folder resource each time and then select a proper arrow button to add it into the corresponding box.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) to display on the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404880172823/btn_addrow.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) to display on the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404880173207/btn_addsum.gif)

Adds the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) to be the aggregate field of the crosstab.

**Columns/Rows**

* **Field**  
   Lists the group objects to display on the column/row headers of the crosstab.
* **Display Name**  
   Specifies the text of the labels for the column/row headers. You can select the text boxes to edit the label text, or select the **Auto Map Field Name** check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Sort**  
   Specifies the sort order of the group objects.
* ![Add Compound Group](https://devnet.logianalytics.com/hc/article_attachments/4404885405079/btn_pgrpt_addparal.gif)  
   Adds a column/row compound group.

**Summaries**

* **Field**  
   Lists the aggregation objects that will be the aggregate fields of the crosstab.
* **Display Name**  
   Specifies the text of the labels for the aggregations. You can select the text boxes to edit the label text, or select the **Auto Map Field Name** check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected field or compound group higher in the list. For fields in a compound group, you can only change their order within the current group.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected field or compound group lower in the list. For fields in a compound group, you can only change their order within the current group.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected field or compound group that you do not want in the crosstab.

## Query Filter

Specifies the filter which you want to apply to the selected business view.

![Crosstab Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404885597719/crstbwzd_qryfltr.gif)

In this screen, Studio displays the predefined filters of the business view in the **Query Filter** drop-down list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the drop-down list, and then define it according to your requirements.

If the selected business view contains parameters, Studio displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009772161-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify values to the parameters before it displays the **Query Filter** screen.

For more information, see [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009744982-Query-Filter-Dialog-Box-Properties) dialog box.

## Style

Specifies the style of the crosstab. Studio hides this screen when there is only one style available to the crosstab.

![Crosstab Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404880550039/crstbwzd_style.gif)

**Style**

Lists all the available styles for you to select from.

**Inherit Style**

Specifies to take the style of the parent component. The option is available only when you specify to insert the crosstab into a banded object.

**Preview**

Shows a preview of the selected style.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772041-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772061-Customize-Gauge-Angle-Dialog-Box-Properties)
