---
title: "Table Wizard Dialog (for Library Component)"
id: 1500009589081
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589081-Table-Wizard-Dialog-for-Library-Component
updated_at: 2021-07-24T05:54:45Z
---

# Table Wizard Dialog (for Library Component)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567762-Table-Type-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589121-Table-Wizard-Dialog-for-Page-Report-)

# Table Wizard Dialog (for Library Component)

The Table Wizard dialog for library component appears when you select a table type in the component type box and select OK in the [Select Component for Library Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009567402-Select-Component-for-Library-Component-Dialog) dialog, or right-click a table and select Table Wizard on the shortcut menu. It helps you to [create a table in a library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component) or [modify an existing table](https://devnet.logianalytics.com/hc/en-us/articles/1500009584421-Modifying-a-Table).

The wizard is different according to the following table types:

* [Group Left, Group Above and Group Left Above](#GroupTable)
* [Summary Table](#SummaryTable)

## For Group Left, Group Above and Group Left Above

The wizard consists of the following screens:

* [Data](#Data)
* [Display](#Display)
* [Group](#Group)
* [Summary](#Summary)
* [Filter](#Filter)
* [Style](#Style)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or modifying the table and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

### Data

Specifies the business view used by the table.  [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893848855/tblwzd_dt_lc.gif)

**Available data resources**

Lists all the business views in the current catalog. Specify the one you want to use.

### Display

Specifies the data fields to display in the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893849111/tblwzd_dsply_lc.gif)

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

![](https://devnet.logianalytics.com/hc/article_attachments/4404893849367/tblwzd_grp_lc.gif)

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

### Summary

Specifies the fields on which to create aggregate functions. This screen is available only when you create a table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893849751/tblwzd_sum_lc.gif)

**Resources**

Lists all the available data resources. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the summary field to the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected summary field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified summary field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified summary field one step down.

**Summarized Fields**

Lists all the fields that you want to display and to be summarized in the table.

**Position**

Works together with the Column option to specify the location where the summary field will be put. Not available when the table type is Group Above.

* **Header**  
   Specifies to put the summary field in the header row. If the summary is calculated on a group by field, it will be put in the group header row of the corresponding group; if the summary is calculated on the whole dataset, it will be put in the table header row.
* **Footer**  
   Specifies to put the summary field in the footer row. If the summary is calculated on a group by field, it will be put in the group footer row of the corresponding group; if the summary is calculated on the whole dataset, it will be put in the table footer row.

**Column**

Works together with the Position option to specify the location where the summary field will be put. Not available when the table type is Group Above.

* **Detail**  
   The summary field with its label will be put in in the first two detail columns.
* **Summary**  
   The summary field will be displayed in a separate summary column.

### Filter

Specifies to filter data displayed in the table. This screen is available only when you create a table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893850007/tblwzd_fltr_lc.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

### Style

Specifies the style of the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893850263/tblwzd_sty_lc.gif)

**Grow Report**

Specifies the layout of the table.

* **Vertically**  
   Creates a vertical table.

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
* [Filter](#Filter1)
* [Style](#Style1)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or modifying the table and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

### Data

Specifies the business view used by the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893850519/tblwzd_dt_lc1.gif)

**Available data resources**

Lists all the business views in the current catalog. Specify the one you want to use.

### Columns

Specifies the fields that you want to display in the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893850775/tblwzd_clmn_lc.gif)

**Resources**

Lists all the available data resources. You can also [create dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the table.

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

![](https://devnet.logianalytics.com/hc/article_attachments/4404893851031/tblwzd_sum_lc1.gif)

**Resources**

Displays the aggregations selected in the Columns screen.

**Summarized Fields**

Displays the group fields selected in the Columns screen under the Table node.

**Header**

Represents the table header or the group header of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding header rows.

**Footer**

Represents the table footer or the group footer of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding footer rows.

### Filter

Specifies to filter data displayed in the table. This screen is available only when you create a table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889318423/tblwzd_fltr_lc1.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

### Style

Specifies the style of the table. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889318679/tblwzd_sty_lc1.gif)

**Grow Report**

Specifies the layout of the table.

* **Vertically**  
   Creates a vertical table.

**Style**

Specifies the style of the table.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the table.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567762-Table-Type-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589121-Table-Wizard-Dialog-for-Page-Report-)
