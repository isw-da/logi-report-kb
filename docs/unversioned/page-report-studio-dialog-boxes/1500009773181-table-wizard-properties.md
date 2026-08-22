---
title: "Table Wizard Properties"
id: 1500009773181
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773181-Table-Wizard-Properties
updated_at: 2021-07-24T00:49:01Z
---

# Table Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745182-Table-Row-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773161-Tabular-Cell-Properties)

# Table Wizard Properties

You can use the Table Wizard to [create a table report](https://devnet.logianalytics.com/hc/en-us/articles/1500009748862-Creating-Page-Reports#Table). This topic describes the options in the wizard.

Select the following screens in this wizard:

* [Data](#Data)
* [Display](#Display)
* [Group](#Group)
* [Summary](#Summary)
* [Query Filter](#Filter)
* [Style](#Style)

**Back**

Returns to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Creates a report containing the table and closes the wizard.

**Cancel**

Closes the wizard without creating a report.

**Help**

Displays the help document about this feature.

## Data

Specifies the business view to use to create the table. This screen is hidden when there is only one business view in the current catalog.

![Table Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404885540631/tblwzd_data.gif)

**Available Data Resources**

Lists all the available business views in the current catalog, with which you can create the table.

## Display

Specifies the detail fields to be displayed in the table.

![Table Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404880278167/tblwzd_dsply.gif)

**Resources**

Displays the group and detail objects in the selected business view.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected object to be displayed in the table.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

Removes the selected object.

**Display Fields**

Lists the group and detail objects that have been added to the table as detail fields.

**Display Name**

Specifies the text for the labels of the detail columns, which by default are the display names of the added objects. You can select in the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected object higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected object lower in the list.

## Group

Specifies the fields to group the data.

![Table Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404880278679/tblwzd_grp.gif)

**Resources**

Displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) you can use to group the data in the table.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected group object as a group field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

Removes the selected group object.

**Group By**

Lists all the group objects that have been added as group fields.

**Sort**

Specifies the sort order for each group: Ascend, Descend, or No Sort.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected group higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected group lower in the list.

## Summary

Specifies the fields on which to create aggregation functions.

![Table Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404880279191/tblwzd_sum.gif)

**Resources**

Displays all the available aggregation objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) you can use to create aggregation functions in the table.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected aggregation object as the summary field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

Removes the selected aggregation object.

**Summarized Fields**

Lists the groups that have been created in the table and the aggregation objects you have added to summarize data in each group.

**Display Name**

Specifies the text for the labels of the summary fields, which by default are the display names of the added objects. You can select in the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects. Available only when the table is not Group Left type.

**Row**

Specifies to put the summary field in the header or footer row. If the summary is calculated on a group-by field, it will be put in the group header or footer of the corresponding group; if the summary is calculated on the table, it will be put in the table header or footer. Available only when the table is Group Left type.

**Column**

Specifies to put the summary field in the specified detail column. If no column is selected, the summary field will be displayed in a separate summary column. Available only when the table is Group Left type.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected aggregation object higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected aggregation object lower in the list.

## Query Filter

Specifies the filter which you want to apply to the selected business view.

![Table Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404885540887/tblwzd_qryfltr.gif)

In this screen, Studio displays the predefined filters of the business view in the **Query Filter** drop-down list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the drop-down list, and then define it according to your requirements.

If the selected business view contains parameters, Studio displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009772161-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify values to the parameters before it displays the **Query Filter** screen.

For more information, see [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009744982-Query-Filter-Dialog-Box-Properties) dialog box.

## Style

Specifies the style of the table. This screen is hidden when there is only one style available to be applied to the table.

![Table Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404880471831/tblwzd_style.gif)

**Style**

Lists all table styles for you to select one from.

**Inherit Style**

Specifies to take the style of the parent component. The option is available only when you specify to insert the table into a banded object.

**Preview**

Shows a preview of the selected style.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745182-Table-Row-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773161-Tabular-Cell-Properties)
