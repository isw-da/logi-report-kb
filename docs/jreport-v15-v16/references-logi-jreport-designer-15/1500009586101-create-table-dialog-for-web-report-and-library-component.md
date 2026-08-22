---
title: "Create Table Dialog (for Web Report and Library Component)"
id: 1500009586101
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586101-Create-Table-Dialog-for-Web-Report-and-Library-Component
updated_at: 2021-07-24T05:55:32Z
---

# Create Table Dialog (for Web Report and Library Component)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564962-Create-Table-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564842-Crosstab-Formula-Editor-Dialog)

# Create Table Dialog (for Web Report and Library Component)

The Create Table dialog for web report and library component appears when you choose a table type and select OK in the [Table Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009567762-Table-Type-Dialog) dialog, or drag the desired table type button from the Components panel into a web report. It helps you to [create a table](https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table#Web) in a web report/library component.

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

Finishes creating the table and closes this dialog.

**Cancel**

Does not retain changes and closes this dialog.

**Help**

Displays the help document about this feature.

### Data

Specifies the data source that you want to use to create the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889374487/crttbl_dt_wb.gif)

**Available data resources**

Lists all the business views in the current catalog. Specify the one you want to use.

### Display

Specifies the fields that you want to display in the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404893936023/crttbl_dsply_wb.gif)

**Title**

Specifies the title of the table.

**Resources**

Lists all the available data resources. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the table.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Display Fields**

Lists the fields that have been selected to display in the table.

**Display Name**

Shows the display names of the selected fields. You can select the name cells to edit them if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog to specify how to sort data in the table.

### Group

Specifies the fields that you want to use to group the data. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404889374743/crttbl_grp_wb.gif)

**Resources**

Lists all the available data resources. You can also [create dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to use in the table.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

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

Specifies the fields on which you want to create aggregate functions. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404893936407/crttbl_sum_wb.gif)

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

Specifies to filter data displayed in the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404889374999/crttbl_fltr_wb.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

### Style

Specifies the style of the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404889375255/crttbl_sty_wb.gif)

**Grow Report**

Specifies the layout of the table.

* **Vertically**  
   Creates a vertical table.

**Style**

Specifies the style of the table.

**Preview**

Displays the selected layout and style effects.

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

Finishes creating the table and closes this dialog.

**Cancel**

Does not retain changes and closes this dialog.

**Help**

Displays the help document about this feature.

### Data

Specifies the data source that you want to use to create the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Data screen of summary table](https://devnet.logianalytics.com/hc/article_attachments/4404893936663/crttbl_dt_wb1.gif)

**Available data resources**

Lists all the business views in the current catalog. Specify the one you want to use.

### Columns

Specifies the fields that you want to display in the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Columns screen of summary table](https://devnet.logianalytics.com/hc/article_attachments/4404893936919/crttbl_clmn_wb.gif)

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

![Create Table wizard for web report and library component - Summary screen of summary table](https://devnet.logianalytics.com/hc/article_attachments/4404889375639/crttbl_sum_wb1.gif)

**Resources**

Displays the aggregations selected in the Columns screen.

**Summarized Fields**

Displays the group fields selected in the Columns screen under the Table node.

**Header**

Represents the table header or the group header of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding header rows.

**Footer**

Represents the table footer or the group footer of a specific group. After an aggregation is selected in the Resources box, you can select the checkboxes in the column to insert the aggregation in the corresponding footer rows.

### Filter

Specifies to filter data displayed in the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Filter screen of summary table](https://devnet.logianalytics.com/hc/article_attachments/4404889375895/crttbl_fltr_wb1.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

### Style

Specifies the style of the table. [See the screen](javascript:%20void(null)).

![Create Table wizard for web report and library component - Style screen of summary table](https://devnet.logianalytics.com/hc/article_attachments/4404889376151/crttbl_sty_wb1.gif)

**Grow Report**

Specifies the layout of the table.

* **Vertically**  
   Creates a vertical table.

**Style**

Specifies the style of the table.

**Preview**

Displays the selected layout and style effects.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564962-Create-Table-Dialog-for-Page-Report-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564842-Crosstab-Formula-Editor-Dialog)
