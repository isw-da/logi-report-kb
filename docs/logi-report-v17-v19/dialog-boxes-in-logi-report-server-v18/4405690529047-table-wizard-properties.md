---
title: "Table Wizard Properties"
id: 4405690529047
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690529047-Table-Wizard-Properties
updated_at: 2022-01-27T07:58:50Z
---

# Table Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690528151-Table-Row-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683688855-Tabular-Cell-Properties)

# Table Wizard Properties

You can use the Table Wizard to [create a table report](https://devnet.logianalytics.com/hc/en-us/articles/4405683950743-Creating-Page-Reports#Table). This topic describes the properties in the wizard.

This topic contains the following sections:

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Group Screen](#Group)
* [Summary Screen](#Summary)
* [Query Filter Screen](#Filter)
* [Style Screen](#Style)

You see these elements on all the screens:

**Back**

Select to return to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to create the table and exit the wizard.

**Cancel**

Select to close the wizard without creating a table.

**Help**

Select to view information about the dialog box.

## Data Screen

Select the business view you want to use to create the table. Server hides this screen when there is only one business view in the current catalog.

![Table Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4420461693335/tblwzd_data.gif)

**Available Data Resources**

Select a business view in the current catalog, which you use to create the table.

## Display Screen

Select the detail fields you want to display in the table.

![Table Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4420447167639/tblwzd_dsply.gif)

**Resources**

Server displays all the group and detail objects in the selected business view. To add an object to display as the detail field in the table, select it, and then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).

**Display Fields**

Server lists the group and detail objects you have added to display as detail fields in the table. To remove an added object, select it, and then select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif).

**Display Name**

Specify the labels of the detail fields, which by default are their display names. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

## Group Screen

Specify the fields to group the data in the table.

![Table Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4420453502487/tblwzd_grp.gif)

**Resources**

Server displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) you can use to group the data in the table. To add a group object as a group field, select it, and then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).

**Group By**

Server lists all the group objects that you have added as the group fields. To cancel a group object from being a group field, select it, and then select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif).

**Sort**

Specify the sort order for each group: Ascend, Descend, or No Sort.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

## Summary Screen

Specify summary fields that calculate data based on a group or on the whole table.

![Table Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4420453502871/tblwzd_sum.gif)

**Resources**

Server displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4420461476503/btn_bvaggrgtn.gif) that you can use as summary fields. You can add summary fields for a group or for the whole table. To add for a group, first select the group field in the right box, next select the desired aggregation object in the left box, and then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif). To add for the whole table, first make sure you select no group fields in the right box, next select the desired aggregation in the left box, and then select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).

**Summarized Fields**

Server lists the groups in the table and the aggregation objects that you have added to summarize data in the groups and for the whole table.

To remove an aggregation object, select it, and then select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif).

**Display Name**

Specify the labels of the summary fields, which by default are their display names. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object. Available only when the table is not Group Left type.

**Row**

Specify to place the summary field in the header or footer row. If the summary is for a group-by field, Server places it in the group header or footer; if the summary is for the table, Server places it in the table header or footer.

This property is available only when the table is Group Left type.

**Column**

Select a detail column where you want to place a summary field. This property is available only when the table is Group Left type.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

## Query Filter Screen

Specify the filter which you want to apply to the selected business view.

![Table Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4420447299735/tblwzd_qryfltr.gif)

Server displays the predefined filters of the business view in the **Query Filter** list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the list, and then define it.

If the selected business view contains parameters, Server displays the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683625623-Enter-Parameter-Values-Dialog-Box-Properties) for you to specify the parameter values before displaying the **Query Filter** screen.

For more information, see the [Query Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690522007-Query-Filter-Dialog-Box-Properties).

## Style Screen

Specify the style of the table. Server hides this screen when there is only one style available to the table.

![Table Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4420453618583/tblwzd_style.gif)

**Style**

Select a style you want to apply to the table.

**Inherit Style**

Select to take the style of the parent component. The property is available when you insert the table into a banded object.

**Preview**

Server shows a preview of the table in the selected style.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690528151-Table-Row-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683688855-Tabular-Cell-Properties)
