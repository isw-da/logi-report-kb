---
title: "Crosstab Wizard"
id: 1500009745321
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745321-Crosstab-Wizard
updated_at: 2021-07-25T07:20:09Z
---

# Crosstab Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719202-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745361-Customize-Gauge-Angle)

# Crosstab Wizard

The Crosstab Wizard is used to [create a crosstab report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750341-Creating-Page-Reports#Crosstab).

There are the following screens in this wizard: [Data](#Data), [Display](#Display), [Query Filter](#Filter) and [Style](#Style).

**Back**

Returns to the previous tab.

**Next**

Goes to the next tab.

**Finish**

Creates the crosstab and closes the wizard.

**Cancel**

Closes the wizard without creating a crosstab.

**Help**

Displays the help document about this feature.

## Data

Specifies the business view to use to create the crosstab. This screen is hidden when there is only one business view in the current catalog.

![Crosstab Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404936949527/crstbwzd_data.gif)

**Available Data Resources**

Lists all the available business views in the current catalog, with which you can create the crosstab.

## Display

Specifies the fields to be displayed in the crosstab.

![Crosstab Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404936793367/crstbwzd_dsply.gif)

**Resources**

Displays the view elements in the selected business view. Select one non-folder resource each time and then select a proper arrow button to add it into the corresponding box.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) to be displayed on the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404936739735/btn_addrow.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) to be displayed on the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404942464023/btn_addsum.gif)

Adds the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) to be the aggregate field of the crosstab.

**Columns/Rows**

* **Field**  
   Lists the group objects that will be displayed on the column/row headers of the crosstab.
* **Display Name**  
   Specifies the text of the labels for the column/row headers. You can select the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Sort**  
   Specifies the sort order of the group objects.
* ![Add Compound Group](https://devnet.logianalytics.com/hc/article_attachments/4404936793623/btn_pgrpt_addparal.gif)  
   Adds a column/row compound group.

**Summaries**

* **Field**  
   Lists the aggregation objects that will be the aggregate fields of the crosstab.
* **Display Name**  
   Specifies the text of the labels for the aggregations. You can select the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif)

Moves the selected field or compound group one step up. For fields in a compound group, their order can be changed within the current group only.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif)

Moves the selected field or compound group one step down. For fields in a compound group, their order can be changed within the current group only.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif)

Removes the selected field or compound group that is not required from the crosstab.

## Query Filter

Specifies the filter which you want to apply to the selected business view.

![Crosstab Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404942602391/crstbwzd_qryfltr.gif)

In this screen, all the predefined filters of the business view are listed in the Query Filter drop-down list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the drop-down list, and then define it according to your requirements.

If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009719302-Enter-Parameter-Values) dialog box to specify values to the parameters before Report Server displays the Query Filter screen.

For details about options in the screen, refer to [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009719862-Query-Filter) dialog box.

## Style

Specifies the style of the crosstab. This screen is hidden when there is only one style available to be applied to the crosstab.

![Crosstab Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404942602647/crstbwzd_style.gif)

**Style**

Lists all the available styles for you to select from.

**Inherit Style**

Specifies to take the style of the parent component. The option is available only when you specify to insert the crosstab into a banded object.

**Preview**

Shows a preview of the selected style.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719202-Crosstab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745361-Customize-Gauge-Angle)
