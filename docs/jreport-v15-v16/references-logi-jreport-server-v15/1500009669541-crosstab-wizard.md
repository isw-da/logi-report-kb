---
title: "Crosstab Wizard"
id: 1500009669541
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669541-Crosstab-Wizard
updated_at: 2021-07-24T20:55:13Z
---

# Crosstab Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644982-Crosstab-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645002-Customized-Page)

# Crosstab Wizard

The Crosstab Wizard guides you through the process of [creating a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009673901-Creating-Page-Reports#Crosstab). It contains the following screens:

* [Data](#Data)
* [Display](#Display)
* [Query Filter](#Filter)
* [Style](#Style)

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Data

Specifies the business view to use to create the crosstab. This screen is hidden when there is only one business view in the current catalog. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920642711/crstbwzd_data.gif)

**Available Data Resources**

Lists all the available business views in the current catalog, with which you can create the crosstab.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Display

Specifies the fields to be displayed in the crosstab. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920482327/crstbwzd_dsply.gif)

**Resources**

Displays the view elements in the selected business view. Select one non-folder resource each time and then select a proper arrow button to add it into the corresponding box.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif)

Adds the selected group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) to be displayed on the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920379799/btn_addrow.gif)

Adds the selected group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) to be displayed on the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920380311/btn_addsum.gif)

Adds the selected aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) to be the aggregate field of the crosstab.

**Columns/Rows**

* **Field**  
   Lists the group objects that will be displayed on the columns/rows of the crosstab.
* **Display Name**  
   Specifies the display names of the added group objects. You can select the cells to edit them if required.
* **Sort**  
   Specifies the sort order of the group objects.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920482839/btn_pgrpt_addparal.gif)  
   Adds a column/row compound group.

**Summaries**

* **Field**  
   Lists the aggregation objects that will be the aggregate fields of the crosstab.
* **Display Name**  
   Specifies the display names of the aggregation objects. You can select the cells to edit them if required.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif)

Moves the selected field or compound group  one step up. For fields in a compound group, their order can be changed within the current group only.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif)

Moves the selected field or compound group one step down. For fields in a compound group, their order can be changed within the current group only.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif)

Removes the selected field or compound group that is not required from the crosstab.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Query Filter

Specifies the filter which you want to apply to the selected business view. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920643223/crstbwzd_qryfltr.gif)

In this screen, all the predefined filters of the business view are listed in the Query Filter drop-down list. You can choose one of them to apply. If you prefer to define a filter on your own, select **User-Defined** from the drop-down list, and then define it according to your requirements.

If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009669621-Enter-Parameter-Values) dialog to specify values to the parameters before the Query Filter screen is displayed.

For details about options in the screen, refer to [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009645642-Query-Filter) dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Style

Specifies the style of the crosstab. This screen is hidden when there is only one style available to be applied to the crosstab. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926778007/crstbwzd_style.gif)

**Style**

Lists all the available styles for you to select from.

**Inherit Style**

Specifies to take the style of the parent component. The option is available only when you specify to insert the crosstab into a banded object.

**Preview**

Shows a preview of the selected style.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644982-Crosstab-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009645002-Customized-Page)
