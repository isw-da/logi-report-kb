---
title: "Banded Wizard Properties"
id: 4405683611159
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683611159-Banded-Wizard-Properties
updated_at: 2022-01-27T07:58:36Z
---

# Banded Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683610135-Banded-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690499479-Bottom-N-Dialog-Box-Properties)

# Banded Wizard Properties

You can use the Banded Wizard dialog box to [create a banded report](https://devnet.logianalytics.com/hc/en-us/articles/4405683950743-Creating-Page-Reports#Banded). This topic describes the properties in the dialog box.

This topic contains the following sections:

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Group Screen](#Group)
* [Summary Screen](#Summary)
* [Query Screen](#Filter)
* [Style Screen](#Style)

You see these elements on all the screens:

**Back**

Select to return to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to create the banded object and exit the wizard.

**Cancel**

Select to close the wizard without creating a banded object.

**Help**

Select to view information about the dialog box.

## Data Screen

Select the business view you want to use to create the banded object. Server hides this screen when there is only one business view in the current catalog.

![Banded Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4420461569175/bdwzd_data.gif)

**Available Data Resources**

Select a business view in the current catalog, which you use to create the banded object.

## Display Screen

Select the detail fields you want to display in the banded object.

![Banded Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4420447163543/bdwzd_dsply.gif)

**Resources**

Server displays all the group and detail objects in the selected business view. To add an object to display as the detail field in the banded object, select it, and then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).

**Display Fields**

Server lists the group and detail objects you have added to display as detail fields in the banded object. To remove an added object, select it, and then select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif).

**Display Name**

Specify the labels of the detail fields, which by default are their display names. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.

The downward order of the added objects determines the order of the detail columns in the banded object from left to right. You can use the following two buttons to adjust the order.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

## Group Screen

Specify the fields to group the data in the banded object.

![Banded Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4420447163799/bdwzd_grp.gif)

**Resources**

Server displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) you can use to group the data in the banded object. To add a group object as a group field, select it, and then select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).

**Group By**

Server lists all the group objects that you have added as the group fields. To cancel a group object from being a group field, select it, and then select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif).

**Sort**

Select the sort order for each group: Ascend, Descend, or No Sort.

The downward order of the added group fields determines the order of the groups in the banded object from first to last. You can use the following two buttons to adjust the order.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

## Summary Screen

Specify summary fields that calculate data based on a group or on the whole banded object.

![Banded Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4420453499031/bdwzd_sum.gif)

**Resources**

Server displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4420461476503/btn_bvaggrgtn.gif) that you can use as summary fields. You can add summary fields for a group or for the whole banded object. To add for a group, first select the group field in the right box, then select the desired aggregation object in the left box, and select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif). To add for the whole banded object, first make sure you select no group fields in the right box, then select the desired aggregation in the left box, and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).

**Summarized Fields**

Server lists the groups in the banded object and the aggregation objects that you have added to summarize data in the groups and for the whole banded object.

To remove an aggregation object, select it, and then select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif).

**Display Name**

Specify the labels of the summary fields, which by default are their display names. You can select a text box to edit the label, or select the **Auto Map Field Name** checkbox beside the text box to automatically map the label to the dynamic display name of the object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

## Query Filter Screen

Specify the filter which you want to apply to the selected business view.

![Banded Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4420447164183/bdwzd_qryfltr.gif)

Server displays the predefined filters of the business view in the **Query Filter** list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the list, and then define it.

If the selected business view contains parameters, Server displays the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683625623-Enter-Parameter-Values-Dialog-Box-Properties) for you to specify the parameter values before displaying the **Query Filter** screen.

For more information, see the [Query Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690522007-Query-Filter-Dialog-Box-Properties).

## Style Screen

Specify the style of the banded object. Server hides this screen when there is only one style available to the banded object.

![Banded Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4420447346199/bdwzd_style.gif)

**Style**

Select a style you want to apply to the banded object.

**Inherit Style**

Select to take the style of the parent component. The property is available when you insert the banded object into another banded object.

**Preview**

Server shows a preview of the banded object in the selected style.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683610135-Banded-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690499479-Bottom-N-Dialog-Box-Properties)
