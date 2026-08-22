---
title: "Banded Wizard Dialog Box"
id: 5735499848471
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735499848471-Banded-Wizard-Dialog-Box
updated_at: 2022-11-02T04:14:20Z
---

# Banded Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513162391-Applet-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513176343-Barcode-Expert-Dialog-Box)

# Banded Wizard Dialog Box

You can use the Banded Wizard dialog box to [create a page report tab with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports#Page), or [edit an existing banded object](https://devnet.logianalytics.com/hc/en-us/articles/5735520497431-Modifying-Banded-Objects). This topic describes the options in the dialog box.

Designer displays different options in the Banded Wizard dialog box according to the type of the data resource you use for the banded object: [business view](#BV) or [query resource](#Query).

## Banded Wizard Dialog Box - Business View Based

When you use the Banded Wizard dialog box for creating or editing a banded object using a business view, Designer displays the following screens in the dialog box (Designer displays some screens only when you use the dialog box for creating a banded object):

* [Data Screen](#BVData)
* [Display Screen](#BVDisplay)
* [Group Screen](#BVGroup)
* [Summary Screen](#BVSummary)
* [Dataset Filter Screen](#BVFilter)
* [Style Screen](#BVStyle)

Designer displays these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the banded object.

![Banded Wizard for business view - Data](https://devnet.logianalytics.com/hc/article_attachments/9898516725655/bdwzd_dt_bv.gif)

**Business view box**

This box lists the predefined business views in the current catalog. Select one and Designer automatically creates a dataset based on it for the banded object.

* ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**<New Business View...>**  
  Select to create a business view in the catalog using the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box) and use it to create the dataset.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**More Options**/**Less Options**

Select to show or hide the options for specifying the dataset you want to use.

* **New Dataset**  
  Select to create a dataset based on a business view in the current catalog.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current report.
  + **<New Dataset...>**  
    Select to create a dataset in the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option when you use the dialog box for editing a banded object and the parent object containing the banded object already applies a dataset. Select it if you want the banded object to inherit the dataset from its parent.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**Edit**

Select to edit the specified business view in the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box) or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box).

### Display Screen

Use this screen to specify the detail fields you want to display in the banded object.

![Banded Wizard for business view - Display](https://devnet.logianalytics.com/hc/article_attachments/9898516730775/bdwzd_dsply_bv.gif)

**Resources**

This box lists the available data fields that you can use as detail fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/9898460510743/btn_replace.gif)**Replace button**

Designer displays this button when you use the dialog box for editing a banded object. Select it to replace the specified field in the banded object with the selected field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Show Banded Group Structure**

Designer displays this option when you use the dialog box for editing a banded object. Select it to show the group structure of the banded object.

**Display Fields**

This column shows the detail fields that you add to display in the banded object.

**Display Name**

This column shows the labels of the detail fields in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or select the **Auto Map Field Name** checkboxes in the text boxes to apply the display names of the fields and map the labels to the dynamic display names of the fields at runtime if the Server administrator defines them.

**Sort Fields By**

Select to open the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567421591-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the banded object.

### Group Screen

Use this screen to specify the criteria for grouping data in the banded object.

![Banded Wizard for business view - Group](https://devnet.logianalytics.com/hc/article_attachments/9898516739735/bdwzd_grp_bv.gif)

**Resources**

This box lists the available data fields that you can use as group-by fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/9898460510743/btn_replace.gif)**Replace button**

Designer displays this button when you use the dialog box for editing a banded object. Select it to replace the specified group-by field in the banded object with the selected field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

**Group By**

This column shows the group-by fields on which you select to group data in the banded object.

**Sort**

This column shows how you want to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565346071-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567350807-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

### Summary Screen

Designer displays the Summary screen when you use the dialog box for creating a banded object. You can use this screen to specify the summaries to calculate data in the banded object.

![Banded Wizard for business view - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898516745751/bdwzd_smry_bv.gif)

**Resources**

This box lists the available data fields that you can use to calculate data in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to calculate data in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

This column shows the fields that you add to calculate data in the banded object.

**Position**

This column shows the position of the summaries. Designer places the summary added for a group level in the group's footer panel; if you add a summary for the Banded Object level, Designer places it in the banded footer panel.

**Column**

This column shows where to place the summaries. By default, Designer places the summaries and their name labels in the first two detail columns.

### Dataset Filter Screen

Designer displays the Dataset Filter screen when you use the dialog box for creating a banded object. You can use this screen to filter the dataset the banded object applies.

Designer displays the same options in the Dataset Filter screen as those in the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522534039-Edit-Dataset-Filter-Dialog-Box).

![Banded Wizard for business view - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898533200279/bdwzd_fltr_bv.gif)

### Style Screen

Use this screen to specify the style of the banded object.

![Banded Wizard for business view - Style](https://devnet.logianalytics.com/hc/article_attachments/9898516761367/bdwzd_sty_bv.gif)

**Style**

This box lists the styles you can apply. Select the style for the banded object.

* **<Custom>**  
  This style contains no information. Designer uses it to support reports that was built with previous versions which did not bind any style, or when Designer cannot find the bound style in the style list.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Designer displays this option when you use the dialog box for editing a banded object and the banded object is inside another banded object. Select it if you want the banded object to inherit the style of its parent.

**Page Setup**

Designer displays this button when you use the dialog box for creating a banded object in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box) to specify page properties for the report tab.

## Banded Wizard Dialog Box - Query Based

When you use the Banded Wizard dialog box for creating or editing a banded object using a query resource, Designer displays the following screens in the dialog box (Designer displays some screens only when you use the dialog box for creating a banded object):

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Group Screen](#Group)
* [Summary Screen](#Summary)
* [Chart Screen](#Chart)
* [Filter Screen](#Filter)
* [Style Screen](#Style)

Designer displays these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the banded object.

![Banded Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/9898533218455/bdwzd_dt.gif)

**Data resource box**

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the banded object.

* **<New XXX...>**/**<Add XXX...>**  
  Select to create or add a data resource of the same type in the catalog.

**More Options**/**Less Options**

Select to show or hide the options for specifying the dataset you want to use.

* **New Dataset**  
  Select to create a dataset based on a data resource in the current catalog.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current report.
  + **<New Dataset...>**  
    Select to create a dataset using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option when you use the dialog box for editing a banded object and the parent object containing the banded object already applies a dataset. Select it if you want the banded object to inherit the dataset from its parent.

**Edit**

Select to edit the specified query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box) or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box).

### Display Screen

Use this screen to specify the detail fields you want to display in the banded object.

![Banded Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/9898533224855/bdwzd_dsply.gif)

**Resources**

This box lists the available data fields that you can use as detail fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/9898460510743/btn_replace.gif)**Replace button**

Designer displays this button when you use the dialog box for editing a banded object. Select it to replace the specified field in the banded object with the selected field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Show Banded Group Structure**

Designer displays this option when you use the dialog box for editing a banded object.
Select it to show the group structure of the banded object.

**Display Fields**

This column shows the detail fields that you add to display in the banded object.

**Display Name**

This column shows the labels of the detail fields in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Select to open the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567421591-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the banded object.

### Group Screen

Use this screen to specify the criteria for grouping data in the banded object.

![Banded Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/9898516792983/bdwzd_grp.gif)

**Resources**

This box lists the available data fields that you can use as group-by fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/9898460510743/btn_replace.gif)**Replace button**

Designer displays this button when you use the dialog box for editing a banded object. Select it to replace the specified group-by field in the banded object with the selected field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

**Group By**

This column shows the group-by fields on which you select to group data in the banded object.

**Sort**

This column shows how you want to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544779031-User-Defined-Group-Dialog-Box) to define grouping information.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565346071-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Special Function**

This column shows the [special functions](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables#Function) that you select for the group-by fields of the Numeric, String, Date, and Time data types. Select a special function from the drop-down list to specify to which level to group the data of the specified field, or select Customize to set the function in the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522295831-Customized-Function-Dialog-Box).

**Custom Sort**

Designer enables this button after you have selected Custom Sort from the Sort column to define the sort manner of groups for the specified group level. Select it to specify how to sort the groups.

**Special Group**

Designer enables this button after you have selected Special Group from the Sort column to define a special group. Select it to specify how to group your information.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567350807-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

**Group Filter**

Select to open the [Group Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530070167-Group-Filter-Dialog-Box) to specify the group filter condition.

### Summary Screen

Designer displays the Summary screen when you use the dialog box for creating a banded object. You can use this screen to specify the fields on which to create summaries in the banded object.

![Banded Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898516798231/bdwzd_smry.gif)

**Resources**

This box lists the available data fields that you can use to create summaries in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box based on which to create a summary in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

This column shows the fields that you add to create summaries in the banded object.

**Aggregate Function**

This column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) that you select to use for the summaries.

**Distinct On**

Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box).

**Break Field**

This column shows the groups on which to calculate the summaries. If you add a summary for the Banded Object level, the break field is null and Designer calculates the summary based on the whole dataset.

**Position**

You can use this option together with the Column option to specify the location where to place a summary.

* **Header**  
  Select to place the summary in the header panel. When you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Banded Object level, Designer places it in the banded header panel.
* **Footer**  
  Select to place the summary in the footer panel. When you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Banded Object level, Designer places it in the banded footer panel.

**Column**

You can use this option together with the Position option to specify the location where to place a summary.

* **Detail**  
  Select to place the summary and its name label in the first two detail columns.
* **Summary**  
  Select to place the summary in a separate summary column.

### Chart Screen

Designer displays the Chart screen when you use the dialog box for creating a banded object, and enables the options in the screen when you have added at least one group and one summary for this group in the banded object. You can use the screen to create a chart together with the banded object, which Designer places in the banded header panel.

![Banded Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/9898516807319/bdwzd_cht.gif)

**No Chart**

Select if you do not want to create the chart.

**Bar Chart**

Select to create a Clustered Bar 2-D chart together with the banded object.

**Line Chart**

Select to create a Line 2-D chart together with the banded object.

**Pie Chart**

Select to create a Clustered Pie chart together with the banded object.

**Category**

This drop-down list contains the group-by fields of the banded object on which you have added summaries. Select the field you want to display on the category (X) axis of the chart.

**Series**

This drop-down list contains the fields that you add as the group-by fields of the banded object. Select the field you want to display on the series (Z) axis of the chart.

**Show Values**

This drop-down list contains the summaries which are calculated based on the field you choose to display on the category axis of the chart. Select the value you want to display in the chart.

### Filter Screen

Designer displays the Filter screen when you use the dialog box for creating a banded object. You can use this screen to narrow down the data to display in the banded object.

Designer displays the same options in the Filter screen as those in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522539031-Edit-Filter-Dialog-Box).

![Banded Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898533258263/bdwzd_fltr.gif)

### Style Screen

Use this screen to specify the style of the banded object.

![Banded Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/9898533263383/bdwzd_sty.gif)

**Style**

This box lists the styles you can apply. Select the style for the banded object.

* **<Custom>**  
  This style contains no information. Designer uses it to support reports that was built with previous versions which did not bind any style, or when Designer cannot find the bound style in the style list.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Designer displays this option when you use the dialog box for editing a banded object and the banded object is inside another banded object. Select it if you want the banded object to inherit the style of its parent.

**Create a Banded Report**

Designer displays this option when you use the dialog box for creating a banded object. Select it if you want to create a restricted version of a flow layout report, one that can contain a single banded object only. This layout option is intended to provide compatibility with Logi Report Version 7 report templates.

**Create a Flow Layout Report Containing a Banded Object**

Designer displays this option when you use the dialog box for creating a banded object. Select it if you want to create a report that contains a banded object mapped to the specified dataset.

**Page Setup**

Designer displays this button when you use the dialog box for creating a banded object in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box) to specify page properties for the report tab.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513162391-Applet-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513176343-Barcode-Expert-Dialog-Box)
