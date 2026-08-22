---
title: "Table Wizard Dialog (for Web Report)"
id: 1500009589101
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589101-Table-Wizard-Dialog-for-Web-Report
updated_at: 2021-07-24T05:54:45Z
---

# Table Wizard Dialog (for Web Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589121-Table-Wizard-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589141-Tabular-Wizard-Dialog)

# Table Wizard Dialog (for Web Report)

The Table Wizard dialog for web report appears when you right-click a table and select Table Wizard on the shortcut menu. It helps you to [modify an existing table](https://devnet.logianalytics.com/hc/en-us/articles/1500009584421-Modifying-a-Table).

The wizard is different according to the following table types:

* [Group Left, Group Above and Group Left Above](#GroupTable)
* [Summary Table](#SummaryTable)

## For Group Left, Group Above and Group Left Above

The wizard consists of the following screens:

* [Data](#Data)
* [Display](#Display)
* [Group](#Group)
* [Style](#Style)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes modifying the table and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

### Data

Specifies the business view used by the table.  [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889316759/tblwzd_dt_wb.gif)

**Available data resources**

Lists all the business views in the current catalog. Specify the one you want to use.

### Display

Specifies the data fields to display in the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889317271/tblwzd_dsply_wb.gif)

**Title**

Specifies the title of the table.

**Resources**

Lists all the available data resources. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected field in the table with the specified field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Show Table Group Structure**

Specifies whether to show the group structure of the table.

**Display Fields**

Lists the fields that you have selected to display in the table.

**Display Name**

Shows the display names of the selected fields. You can select the name cells to edit them if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog to specify how to sort data in the table.

### Group

Specifies the fields that you want to use to group the data. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893848087/tblwzd_grp_wb.gif)

**Resources**

Lists all the available data resources. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected group by field in the table with the specified field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified group one step down.

**Group By**

Lists the fields that are used to group data in the table.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009586161-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog to specify the Select N condition.

### Style

Specifies the style of the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889317527/tblwzd_sty_wb.gif)

**Style**

Specifies the style of the table.

* **<Custom>**  
  There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the table.

## For Summary Table

The wizard consists of the following screens:

* [Data](#Data1)
* [Columns](#Columns)
* [Summary](#Summary1)
* [Style](#Style1)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes modifying the table and closes this wizard.

**Cancel**

Does not retain changes and closes this dialog.

**Help**

Displays the help document about this feature.

### Data

Specifies the business view used by the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889317911/tblwzd_dt_wb1.gif)

**Available data resources**

Lists all the business views in the current catalog. Specify the one you want to use.

### Columns

Specifies the fields that you want to display in the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893848343/tblwzd_clmn_wb.gif)

**Resources**

Lists all the available data resources. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the table.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected field in the table with the specified field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Column**

Lists the fields that have been selected to display in the table.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009586161-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog to specify the Select N condition.

### Summary

Specifies to insert aggregations to the header/footer rows of the table and groups. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893848599/tblwzd_sum_wb1.gif)

**Resources**

Displays the aggregations selected in the [Columns screen](#Columns).

**Summarized Fields**

Displays the group fields selected in the Columns screen under the Table node.

**Header**

Represents the table header or the group header of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding header rows.

**Footer**

Represents the table footer or the group footer of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding footer rows.

### Style

Specifies the style of the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889318167/tblwzd_sty_wb1.gif)

**Style**

Specifies the style of the table.

* **<Custom>**  
  There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays the selected layout and style effects.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589121-Table-Wizard-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589141-Tabular-Wizard-Dialog)
