---
title: "Mailing Label Wizard Dialog"
id: 1500009632361
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009632361-Mailing-Label-Wizard-Dialog
updated_at: 2021-07-24T16:04:23Z
---

# Mailing Label Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009632341-Link-Data-Container-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632401-Manage-Customized-Controls-Dialog)

# Mailing Label Wizard Dialog

The Mailing Label Wizard helps you to [create a page report with a cross banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page), which is in the form of a mailing label layout. It appears when you select the Mailing Label layout in the [Select Component for Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009633461-Select-Component-for-Page-Report-Dialog) dialog or [Select Component for Page Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009633501-Select-Component-for-Page-Report-Tab-Dialog) dialog and then select OK.

The wizard consists of the following screens: [Data](#Data), [Display](#Display), [Group](#Group), [Summary](#Summary), [Chart](#Chart), [Filter](#Filter), [Layout](#Layout) and [Style](#Style).

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

Specifies the dataset using which to create the banded object.

![Mailing Label Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404916782743/mllblwzd_dt.gif)

**Data resource box**

Lists the predefined data resources in the current catalog. Select one and a dataset based on it is created automatically for the banded object.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the banded object.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog).
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. You can select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog).

## Display

Specifies the detail fields to display in the banded object.

![Mailing Label Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904256663/mllblwzd_dsply.gif)

**Resources**

Lists the DBFields in the specified data resource, as well as the valid formulas and parameters for these DBFields in the current catalog that can be used as detail fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected field from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected field one step down.

**Display Fields**

Lists the detail fields of the banded object.

**Display Name**

Specifies the labels of the detail columns, which by default are the display names of the added fields. You can select in text boxes to edit the labels.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009633661-Sort-Fields-By-Dialog) dialog to specify how to sort the detail data in the banded object.

## Group

Specifies the criteria for grouping data in the banded object.

![Mailing Label Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404904256919/mllblwzd_grp.gif)

**Resources**

Lists the DBFields in the specified data resource, as well as the valid formulas and parameters for these DBFields in the current catalog that can be used as group-by fields in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box as the group-by field in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected group-by field from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected group one step down.

**Group By**

Lists the group-by fields of the banded object.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Special Group**  
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009610722-User-Defined-Group-Dialog) dialog to define grouping information.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009607602-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Special Function**

For a group-by field of the Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables#Function) for it to specify to which level data will be grouped by. Select Customize to set the function in the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009630341-Customized-Function-Dialog) dialog.

**Custom Sort**

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sort manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009610362-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009631861-Group-Filter-Dialog) dialog to specify the group filter condition.

## Summary

Specifies the fields on which to create summaries in the banded object.

![Mailing Label Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904257175/mllblwzd_sum.gif)

**Resources**

Lists the DBFields in the specified data resource, as well as the valid formulas for these DBFields in the current catalog that can be used to create summaries in the banded object.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)**

Adds the selected field in the Resources box based on which to create a summary in the banded object.

**![Rremove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**

Removes the selected summary from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif)

Moves the selected summary one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif)

Moves the selected summary one step down.

**Summarized Fields**

Lists all the fields that have been added to create summaries in the banded object.

**Aggregate Function**

Specifies the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) used for the summaries.

**Distinct On**

Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the text box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.

**Break Field**

Displays the groups on which the summaries will be calculated. If a summary is added for the Banded Object level, the break field is null and the summary will be calculated on the whole dataset.

**Position**

Works together with the Column option to specify the location where a summary will be placed.

* **Header**  
   Specifies to put the summary in the header panel. If the summary is added for a specific group, it will be put in the group's header panel; if the summary is added for the Banded Object level, it will be put in the banded header panel.
* **Footer**  
   Specifies to put the summary in the footer panel. If the summary is added for a specific group, it will be put in the group's footer panel; if the summary is added for the Banded Object level, it will be put in the banded footer panel.

**Column**

Works together with the Position option to specify the location where a summary will be placed.

* **Detail**  
   The summary and its name label will be put in the first two detail columns.
* **Summary**  
   The summary will be displayed in a separate summary column.

## Chart

Specifies to create a chart together with the banded object, which will be placed in the banded header panel. This screen is available only when there is at least one group and one summary added for this group in the banded object.

![Mailing Label Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404904257559/mllblwzd_cht.gif)

**No Chart**

Specifies not to create a chart.

**Bar Chart**

Specifies to create a Clustered Bar 2-D chart together with the banded object.

**Line Chart**

Specifies to create a Line 2-D chart together with the banded object.

**Pie Chart**

Specifies to create a Clustered Pie chart together with the banded object.

**Category**

Lists the group-by fields of the banded object on which summaries are added. Choose the field you want to display on the category (X) axis of the chart from the drop-down list.

**Series**

Lists the fields that have been added as the group-by fields of the banded object. Choose the field you want to display on the series (Z) axis of the chart from the drop-down list.

**Show Values**

Lists the summaries which are calculated based on the field you choose to display on the category axis of the chart. Choose the value you want to display in the chart from the drop-down list.

## Filter

Specifies to filter data displayed in the banded object. The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009607882-Edit-Filter-Dialog) dialog.

![Mailing Label Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904258071/mllblwzd_fltr.gif)

## Layout

Specifies the layout of the banded object.

![Mailing Label Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904258583/mllblwzd_layout.gif)

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

Specifies the style of the banded object.

![Mailing Label Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404916782999/mllblwzd_sty.gif)

**Style**

Specifies the style of the banded object.

**Preview**

Displays the selected tyle effects.

**Create a Banded Report**

Creates a restricted version of a flow layout report, one that can contain a single banded object only. This layout option is intended to provide compatibility with Logi Report Version 7 report templates.

**Create a Flow Layout Report Containing a Banded Object**

Creates a report that contains a banded object mapped to the specified dataset. This layout option is specified by default.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog to specify page properties.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009632341-Link-Data-Container-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632401-Manage-Customized-Controls-Dialog)
