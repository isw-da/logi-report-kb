---
title: "Create Crosstab Dialog Box"
id: 5735522178583
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735522178583-Create-Crosstab-Dialog-Box
updated_at: 2022-11-02T08:16:34Z
---

# Create Crosstab Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735528726551-Create-Connection-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513397271-Create-Data-Mapping-File-Dialog-Box)

# Create Crosstab Dialog Box

You can use the Create Crosstab dialog box to [create a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/5735527515799-Inserting-Crosstabs-in-a-Report) in a report. This topic describes the options in the dialog box.

Designer displays the Create Crosstab dialog box when you navigate to Insert > Crosstab, or drag the Crosstab icon ![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/9898532400023/icon_crstb.gif) from the Components panel into a report, and provides you with different options in the dialog box according to the type of the data resource you use for the crosstab: [business view](#BV) or [query resource](#Query).

## Create Crosstab Dialog Box - Business View Based

When you use the Create Crosstab dialog box for creating a crosstab using a business view, Designer displays the following screens in the dialog box:

* [Data Screen](#BVData)
* [Display Screen](#BVDisplay)
* [Dataset Filter Screen](#BVFilter)
* [Layout Screen](#BVLayout)
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

Use this screen to specify the dataset for the crosstab.

![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/9898532404247/crtcrstab_dt_bv.gif)

**Business view box**

This box lists the predefined business views in the current catalog. Select one and Designer automatically creates a dataset based on it for the crosstab.

* ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**<New Business View...>**  
  Select to create a business view in the catalog using the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box). Designer does not display this option when you use the dialog box in a library component.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**More Options**/**Less Options**

Select to show or hide the options for specifying the dataset you want to use. Designer does not display this pair of buttons when you use the dialog box in a library component.

* **New Dataset**  
  Select to create a dataset based on a business view in the current catalog.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current report.
  + **<New Dataset...>**  
    Select to create a dataset in the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option when the parent object where you have specified to insert the crosstab already applies a dataset. Select it if you want the crosstab to inherit the dataset from its parent.

![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**Edit**

Select to edit the specified business view in the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box) or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box). Designer does not display this button when you use the dialog box in a library component.

### Display Screen

Use this screen to specify the column, row, and aggregate fields to display in the crosstab.

![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/9898532409239/crtcrstab_dsply_bv.gif)

**Title**

Specify the title of the crosstab.

**Resources**

This box lists the available data fields that you can use to create the crosstab.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add Column button**

Select to add the specified field in the Resources box to display on the column header of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/9898516002199/btn_addrow.gif)**Add Row button**

Select to add the specified field in the Resources box to display on the row header of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/9898516016791/btn_addsum.gif)**Add Summary button**

Select to add the specified field in the Resources box to create aggregations in the crosstab.

**Columns**/**Rows**

* **Field**  
  This column shows the fields that you add on the column/row headers of the crosstab.
* **Label**  
  This column shows the labels for the column/row headers. By default, Designer does not add labels for the column/row headers. You can double-click the text boxes to edit the labels, or select the **Auto Map Field Name** checkboxes in the text boxes to apply the display names of the fields and map the labels to the dynamic display names of the fields at runtime if the Server administrator defines them.
* **Color**  
  This column shows the background colors that you select for the fields. Double-click in the text box and select the color from the drop-down list.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9898516023063/btn_sort1.gif)**Sort button**  
  Select a field and select the button to specify the order to sort values of the field, ascending or descending.

**Summaries**

* **Field**  
  This column shows the fields that you add as aggregate fields to create aggregations in the crosstab.
* **Aggregate**  
  This column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) that you select for the aggregate fields to calculate data.
* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box).
* **Label**  
  This column shows the labels for the aggregations. By default, Designer does not add labels for the aggregations. You can double-click the text boxes to edit the labels, or select the **Auto Map Field Name** checkboxes in the text boxes to apply the display names of the fields and map the labels to the dynamic display names of the fields at runtime if the Server administrator defines them.
* **Comparison Function**  
  Select to open the [Comparison Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508270871-Comparison-Function-Dialog-Box) to add a comparison function for the selected aggregate field.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified field from the crosstab.

### Dataset Filter Screen

Use this screen to filter the dataset the crosstab applies.

Designer displays the same options in the Dataset Filter screen as those in the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522534039-Edit-Dataset-Filter-Dialog-Box).

![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898516053911/crtcrstab_fltr_bv.gif)

### Layout Screen

Use this screen to specify the layout of the crosstab. For more information about the layout settings, see [Customizing the Layout of a Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs#Layout).

![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/9898516076951/crtcrstab_layout_bv.gif)

### Style Screen

Use this screen to specify the style of the crosstab.

![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/9898532524567/crtcrstab_sty_bv.gif)

**Style**

This box lists the styles you can apply. Select the style for the crosstab.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the crosstab.

**Inherit Style**

Designer displays this option and selects it by default when you have specified to insert the crosstab into a banded object. Clear it if you do not want the crosstab to inherit the style of its parent.

## Create Crosstab Dialog Box - Query Based

When you use the Create Crosstab dialog box for creating a crosstab using a query resource, Designer displays the following screens in the dialog box:

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Filter Screen](#Filter)
* [Layout Screen](#Layout)
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

Use this screen to specify the dataset for the crosstab.

![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/9898532549911/crtcrstab_dt.gif)

**Data resource box**

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the crosstab.

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
  Designer enables this option when the parent object where you have specified to insert the crosstab already applies a dataset. Select it if you want the crosstab to inherit the dataset from its parent.

**Edit**

Select to edit the specified query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box) or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box).

### Display Screen

Use this screen to specify the column, row, and aggregate fields to display in the crosstab.

![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/9898532577303/crtcrstab_dsply.gif)

**Resources**

This box lists the available data fields that you can use to create the crosstab.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add Column button**

Select to add the specified field in the Resources box to display on the column header of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/9898516002199/btn_addrow.gif)**Add Row button**

Select to add the specified field in the Resources box to display on the row header of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/9898516016791/btn_addsum.gif)**Add Summary button**

Select to add the specified field in the Resources box on which to create aggregations in the crosstab.

**Columns**/**Rows**

* **Field**  
  This column shows the fields that you add to display on the column/row headers of the crosstab.
* **Label**  
  This column shows the labels for the column/row headers. By default, Designer does not add labels for the column/row headers. You can double-click the text boxes to edit the labels.
* **Color**  
  This column shows the background colors that you select for the fields. Double-click in the text box and select the color from the drop-down list.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9898516023063/btn_sort1.gif)**Sort button**  
  Select a field and select the button to specify the order to sort values of the field, ascending or descending.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898532597911/btn_addparal.gif)**Add Compound Group button**  
  Select to add a compound column/row group.

**Summaries**

* **Field**  
  This column shows the fields that you add as aggregate fields to create aggregations in the crosstab.
* **Aggregate**  
  This column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) that you select for the aggregate fields to calculate data.
* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box).
* **Label**  
  This column shows the labels for the aggregations. By default, Designer does not add labels for the aggregations. You can double-click the text boxes to edit the labels.
* **Comparison Function**  
  Select to open the [Comparison Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508270871-Comparison-Function-Dialog-Box) to add a comparison function for the selected aggregate field.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified field or compound group higher in the display order. For fields in a compound group, you can change their order within the current group only.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified field or compound group lower in the display order. For fields in a compound group, you can change their order within the current group only.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified field or compound group from the crosstab.

### Filter Screen

Use this screen to narrow down the data to display in the crosstab.

Designer displays the same options in the Filter screen as those in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522539031-Edit-Filter-Dialog-Box).

![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898516163095/crtcrstab_fltr.gif)

### Layout Screen

Use this screen to specify the layout of the crosstab. For more information about the layout settings, see [Customizing the Layout of a Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs#Layout).

![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/9898516169751/crtcrstab_layout.gif)

### Style Screen

Use this screen to specify the style of the crosstab.

![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/9898516175895/crtcrstab_sty.gif)

**Style**

This box lists the styles you can apply. Select the style for the crosstab.

**Preview**

This box displays a diagram illustrating the effect of the selected style on the crosstab.

**Inherit Style**

Designer displays this option and selects it by default when you have specified to insert the crosstab into a banded object. Clear it if you do not want the crosstab to inherit the style of its parent.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735528726551-Create-Connection-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513397271-Create-Data-Mapping-File-Dialog-Box)
