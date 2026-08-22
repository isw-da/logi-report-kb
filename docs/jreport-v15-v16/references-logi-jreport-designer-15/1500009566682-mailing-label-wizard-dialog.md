---
title: "Mailing Label Wizard Dialog"
id: 1500009566682
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566682-Mailing-Label-Wizard-Dialog
updated_at: 2021-07-24T05:55:03Z
---

# Mailing Label Wizard Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566642-Link-Data-Container-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587761-Manage-Customized-Controls-Dialog)

# Mailing Label Wizard Dialog

The Mailing Label Wizard appears when you select the Mailing Label layout in the [Select Component for Page Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009588661-Select-Component-for-Page-Report-Tab-Dialog) dialog or [Select Component for Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009567422-Select-Component-for-Page-Report-Dialog) dialog and then select OK. It helps you to [create a page report with a cross banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report), which is in the form of a mailing label layout, and consists of the following screens.

* [Data](#Data)
* [Display](#Display)
* [Group](#Group)
* [Summary](#Summary)
* [Chart](#Chart)
* [Filter](#Filter)
* [Layout](#Layout)
* [Style](#Style)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating the mailing label report and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Data

Specifies the dataset used to create the banded object. [See the screen](javascript:%20void(null)).

![Mailing Label Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404889329943/mllblwzd_dt.gif)

**Define a dataset for the object**

Specifies the dataset on which the banded object will be built.

* **New**  
   If checked, select a data source from the catalog resources to create a dataset that will be used to build the banded object. When you choose to create the dataset from a query, you can select the Modify button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) if required.
* **Existing**  
   If checked, select a dataset from the ones existing in the open report to create the banded object. Select the Modify button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if required.

## Display

Specifies the data fields displayed in the banded object. [See the screen](javascript:%20void(null)).

![Mailing Label Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404893868439/mllblwzd_dsply.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Display Fields**

Lists the fields that have been selected to display in the banded object.

**Display Name**

Shows the display names of the selected fields. You can select the name cells to edit them if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog to specify how to sort data in the banded object.

## Group

Specifies the fields to group data in the banded object. [See the screen](javascript:%20void(null)).

![Mailing Label Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404889330199/mllblwzd_grp.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified group one step down.

**Group By**

Lists the fields that are used to group data in the banded object.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define grouping information.

  For example, if you placed a field named Region for grouping, and this field contains all 50 states of the United States; and if you want to see the data between Maryland (MD) and New York (NY), you can define the criteria by selecting the between operator to further define your grouping information.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009586161-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Special Function**

If the group by field is of Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field) for the field in the Special Function column to further specify to which level the data will be grouped by.

If Customize is selected, the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009586201-Customized-Function-Dialog) dialog will be displayed, in which you can set the function by your own.

**Custom Sort**

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sorting manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009566302-Group-Filter-Dialog) dialog to specify the group filter condition.

## Summary

Specifies the fields on which to create aggregate functions. [See the screen](javascript:%20void(null)).

![Mailing Label Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404893868823/mllblwzd_sum.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the summary field to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected summary field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified summary field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified summary field one step down.

**Summarized Fields**

Lists all the fields that you want to display and to be summarized in the banded object.

**Aggregate Function**

Specifies the function to summarize the selected field.

**Break Field**

Displays a defined field on which the summary will be calculated. If a summary field is added below the Banded Object node, the break field is null and the summary will be calculated on the whole dataset.

## Chart

Specifies to create a chart together with the banded object, which will be placed in the banded header panel. This screen is available only when there is at least one group by field and one summary field which is calculated on this group by field in the banded object. [See the screen](javascript:%20void(null)).

![Mailing Label Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404893869079/mllblwzd_cht.gif)

**No Chart**

Specifies not to create a chart.

**Bar Chart**

Specifies to create a Clustered Bar 2-D chart together with the banded object.

**Line Chart**

Specifies to create a Line 2-D chart together with the banded object.

**Pie Chart**

Specifies to create a Clustered Pie chart together with the banded object.

**Category**

Lists the group by fields of the banded object on which the summary fields are calculated. Choose the field you want to display on the category (X) axis of the chart from the drop-down list.

**Series**

Lists the fields that have been added as the group by fields of the banded object. Choose the field you want to display on the series (Z) axis of the chart from the drop-down list.

**Show Values**

Lists the summary fields which are calculated based on the field you choose to display on the category axis of the chart. Choose the value you want to display in the chart from the drop-down list.

## Filter

Specifies to filter data displayed in the banded object. [See the screen](javascript:%20void(null)).

![Mailing Label Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404893869335/mllblwzd_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

## Layout

Specifies the layout of the banded object.  [See the screen](javascript:%20void(null)).

![Mailing Label Wizard - Layout Screen](https://devnet.logianalytics.com/hc/article_attachments/4404889330583/mllblwzd_layout.gif)

**Label Size**

Specifies the size for the labels in the banded object.

* **Width**  
   Specifies the width of the labels.
* **Height**  
   Specifies the height of the labels.

**Gap Between Labels**

Specifies the gap between each two labels.

* **Horizontal Gap**  
   Specifies the horizontal gap between two labels.
* **Vertical Gap**  
   Specifies the vertical gap between two labels.

**Preview**

Displays the selected layout for the label.

## Style

Specifies the style of the banded object. [See the screen](javascript:%20void(null)).

![Mailing Label Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404889330839/mllblwzd_sty.gif)

**Style**

Specifies the style of the banded object.

**Preview**

Displays the selected style effects.

**Create a Banded Report**

Creates a restricted version of a flow layout report, one that can contain a single banded object only. This layout option is intended to provide compatibility with Logi JReport Version 7 report templates.

**Create a Flow Layout Report Containing a Banded Object**

Creates a report that contains a banded object mapped to the specified dataset. This layout option is specified by default.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) dialog to specify page properties.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566642-Link-Data-Container-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587761-Manage-Customized-Controls-Dialog)
