---
title: "Banded Wizard Properties"
id: 1500009744062
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744062-Banded-Wizard-Properties
updated_at: 2021-07-24T00:49:21Z
---

# Banded Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744042-Banded-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744082-Bottom-N-Dialog-Box-Properties)

# Banded Wizard Properties

You can use the Banded Wizard dialog box to [create a banded report](https://devnet.logianalytics.com/hc/en-us/articles/1500009748862-Creating-Page-Reports#Banded). This topic describes the options in the dialog box.

This topic contains the following sections:

* [Data](#Data)
* [Display](#Display)
* [Group](#Group)
* [Summary](#Summary)
* [Query](#Filter)
* [Style](#Style)

**Back**

Returns to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Creates the banded object and closes the wizard.

**Cancel**

Closes the wizard without creating a banded object.

**Help**

Displays the help document about this feature.

## Data

Specifies the business view to use to create the banded object. Studio hides this screen when there is only one business view in the current catalog.

![Banded Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404880276503/bdwzd_data.gif)

**Available Data Resources**

Lists all the available business views in the current catalog, with which you can create the banded object.

## Display

Specifies the detail fields to display in the banded object.

![Banded Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404880276759/bdwzd_dsply.gif)

**Resources**

Displays all the group and detail objects in the selected business view. To add an object to display as the detail field in the banded object, select it and then select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif).

**Display Fields**

Lists the group and detail objects you have selected to display in the banded object. For an added object which you do not want, select it and then select ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif).

**Display Name**

Specifies the labels of the detail columns in the banded object, which by default are the display names of the added objects. You can select in the text boxes to edit the labels, or select the **Auto Map Field Name** check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.

The downward order of the added objects determines the order of them in the banded object from left to right. You can use the following two arrows to adjust the order.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected object higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected object lower in the list.

## Group

Specifies the fields to group the data in the banded object.

![Banded Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404885402519/bdwzd_grp.gif)

**Resources**

Displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) you can use to group the data in the banded object. To add a group object as a group field, select it and then select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif).

**Group By**

Lists all the group objects that you have added as the group fields. To cancel a group from being a group field, select it and then select ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif).

**Sort**

Specifies the sort order for each group: Ascend, Descend, or No Sort.

The downward order of the added group fields determines the order of the groups in the banded object from first to last. You can use the following two arrows to adjust the order.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected group higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected group lower in the list.

## Summary

Specifies summary fields that calculate data based on a group or on the whole banded object.

![Banded Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404880277399/bdwzd_sum.gif)

**Resources**

Displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) that you can use as summary fields. You can add summary fields into a group or for the whole banded object. To add into a group, first select the group field in the right panel, then select the desired aggregation object in the left panel and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif). To add for the whole banded object, first make sure no group field is selected, then select the desired aggregation and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif).

**Summarized Fields**

Lists the groups in the banded object and the aggregation objects that you have added to summarize data in the groups and for the whole banded object.

To cancel an aggregation object from being added as a summary field, select it in the right panel and then select ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif).

**Display Name**

Specifies the labels of the summary fields in the banded object, which by default are the display names of the added objects. You can select in the text boxes to edit the labels, or select the **Auto Map Field Name** check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the selected aggregation object higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the selected aggregation object lower in the list.

## Query Filter

Specifies the filter which you want to apply to the selected business view.

![Banded Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404880277911/bdwzd_qryfltr.gif)

In this screen, Studio displays the predefined filters of the business view in the **Query Filter** drop-down list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User Defined** from the drop-down list, and then define it according to your requirements.

If the selected business view contains parameters, Studio displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009772161-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify values to the parameters before it displays the **Query Filter** screen.

For more information, see [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009744982-Query-Filter-Dialog-Box-Properties) dialog box.

## Style

Specifies the style of the banded object. Studio hides this screen when there is only one style available to the banded object.

![Banded Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404880556055/bdwzd_style.gif)

**Style**

Lists all the available styles for you to select from.

**Inherit Style**

Specifies to take the style of the parent component. The option is available only when you specify to insert the banded object into another banded object.

**Preview**

Shows a preview of the banded object in the selected style.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744042-Banded-Panel-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744082-Bottom-N-Dialog-Box-Properties)
