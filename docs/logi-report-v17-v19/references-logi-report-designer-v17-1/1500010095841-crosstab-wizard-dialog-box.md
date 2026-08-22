---
title: "Crosstab Wizard Dialog Box"
id: 1500010095841
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095841-Crosstab-Wizard-Dialog-Box
updated_at: 2022-03-28T09:21:12Z
---

# Crosstab Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095821-Crosstab-Formula-Editor-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058422-CSS-Editor-Dialog-Box)

# Crosstab Wizard Dialog Box

You can use the Crosstab Wizard dialog box to [create a page report tab with a crosstab in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page), [create a library component with a crosstab in it,](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#LC) or [edit an existing crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#Edit) in a report. This topic describes the options in the dialog box.

Designer displays different options in the Crosstab Wizard dialog box according to the type of the data resource used for the crosstab: [business view](#BV) or [query resource](#Query).

## Crosstab Wizard Dialog Box - Business View Based

When you use the Crosstab Wizard dialog box for creating or editing a crosstab using a business view, you see the following screens in the dialog box (Designer displays the Filter screens only when you use the dialog box for creating a crosstab):

* [Data Screen](#BVData)
* [Display Screen](#BVDisplay)
* [Filter Screen](#BVFilter)
* [Layout Screen](#BVLayout)
* [Style Screen](#BVStyle)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish creating or modifying the crosstab and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the business view for the crosstab. You can select from all the predefined business views in the current catalog.

![Crosstab Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404857002007/crstbwzd_dt_bv.gif)

**Inherit from the Parent**

Designer displays and enables the option only when you use the dialog box for editing a crosstab that is inside any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel. Select it if you want the crosstab to inherit the business view that its parent banded object uses.

### Display Screen

Use this screen to specify the column, row, and aggregate fields to display in the crosstab.

![Crosstab Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848615191/crstbwzd_dsply_bv.gif)

**Title**

Specify the title of the crosstab.

**Resources**

The box lists the resources in and related to the specified business view, which you can use to create the crosstab.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add Column button**

Select to add the specified field in the Resources box to display on the column header of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/4404848608919/btn_addrow.gif)**Add Row button**

Select to add the specified field in the Resources box to display on the row header of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/4404856993303/btn_addsum.gif)**Add Summary button**

Select to add the specified field in the Resources box to create aggregations in the crosstab.

**Columns**/**Rows**

* **Field**  
  The column shows the fields that you add on the column/row headers of the crosstab.
* **Label**  
  The column shows the labels for the column/row headers. By default, Designer does not add labels for the column/row headers. You can double-click the text boxes to edit the labels, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the labels to the dynamic display names of the fields at runtime.
* **Color**  
  The column shows the background colors that you select for the fields. Double-click in the text box and select the color from the drop-down list.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404856993559/btn_sort1.gif)**Sort button**  
  Select a field and select the button to specify in which manner to sort the values of the field, ascending or descending.

**Summaries**

* **Field**  
  The column shows the fields that you add as aggregate fields to create aggregations in the crosstab.
* **Aggregate**  
  The column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) that you select for the fields to calculate data.
* **Distinct On**  
  Designer enables the option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box).
* **Label**  
  The column shows the labels for the aggregations. By default, Designer does not add labels for the aggregations. You can double-click the text boxes to edit the labels, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the labels to the dynamic display names of the fields at runtime.
* **Comparison Function**  
  Select to open the [Comparison Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058222-Comparison-Function-Dialog-Box) to add a comparison function for the selected aggregate field.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified field from the crosstab.

### Filter Screen

Use this screen to narrow down the data to display in the crosstab.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Crosstab Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848615575/crstbwzd_fltr_bv.gif)

### Layout Screen

Use this screen to specify the layout of the crosstab. For more information about the layout settings, see [Customizing the Layout of a Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#Layout).

![Crosstab Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404857002263/crstbwzd_layout_bv.gif)

### Style Screen

Use this screen to specify the style of the crosstab.

![Crosstab Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848616343/crstbwzd_sty_bv.gif)

**Style**

The box lists the styles that you can apply to the crosstab. Select the style for the crosstab.

* **<Custom>**  
  This style contains no information. It is only used to support reports that was built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the crosstab.

**Inherit Style**

Designer displays the option only when the crosstab is inside a banded object, or to be inserted into a banded object. Select it if you want the crosstab to inherit the style of its parent.

**Page Setup**

Designer displays the button only when you use the dialog box for creating a crosstab in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) to specify page properties for the report tab.

## Crosstab Wizard Dialog Box - Query Based

When you use the Crossatab Wizard dialog box for creating or editing a crosstab using a query resource, you see the following screens in the dialog box (Designer displays some screens only when you use the dialog box for creating a crosstab):

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Chart Screen](#Chart)
* [Filter Screen](#Filter)
* [Layout Screen](#Layout)
* [Style Screen](#Style)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish creating or modifying the crosstab and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the crosstab.

![Crosstab Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404857002519/crstbwzd_dt.gif)

**Data resource box**

The box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the crosstab.

**More Options**/**Less Options**

Select to show or hide the options for specifying a dataset for the crosstab.

* **New Dataset**  
  Select to create a dataset based on the current catalog data resources. When you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box).
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select the Edit button to edit the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select <New Dataset...> to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option only when you use the dialog box for editing a crosstab and the parent object containing the crosstab already applies a dataset. Select it if you want the crosstab to inherit the dataset from its parent.

### Display Screen

Use this screen to specify the column, row, and aggregate fields to display in the crosstab.

![Crosstab Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848617111/crstbwzd_dsply.gif)

**Resources**

The box lists the resources in and related to the specified query resource, which you can use to create the crosstab.

![Add Columns button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add Column button**

Select to add the specified field in the Resources box to display on the column header of the crosstab.

![Add Rows button](https://devnet.logianalytics.com/hc/article_attachments/4404848608919/btn_addrow.gif)**Add Row button**

Select to add the specified field in the Resources box to display on the row header of the crosstab.

![Add Summaries button](https://devnet.logianalytics.com/hc/article_attachments/4404856993303/btn_addsum.gif)**Add Summary button**

Select to add the specified field in the Resources box on which to create aggregations in the crosstab.

**Columns**/**Rows**

* **Field**  
  The column shows the fields that you add to display on the column/row headers of the crosstab.
* **Label**  
  The column shows the labels for the column/row headers. By default, Designer does not add labels for the column/row headers. You can double-click the text boxes to edit the labels.
* **Color**  
  The column shows the background colors that you select for the fields. Double-click in the text box and select the color from the drop-down list.
* ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404856993559/btn_sort1.gif)**Sort button**  
  Select a field and select the button to specify in which manner to sort the values of the field, ascending or descending.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848611095/btn_addparal.gif)**Add Compound Group button**  
  Select to add a compound column/row group.

**Summaries**

* **Field**  
  The column shows the fields that you add as aggregate fields to create aggregations in the crosstab.
* **Aggregate**  
  The column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) that you select for the fields to calculate data. Double-click in the text box and select the function from the drop-down list.
* **Distinct On**  
  Designer enables the option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box).
* **Label**  
  The column shows the labels for the aggregations. By default, Designer does not add labels for the aggregations. You can double-click the text boxes to edit the labels.
* **Comparison Function**  
  Select to open the [Comparison Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058222-Comparison-Function-Dialog-Box) to add a comparison function for the selected aggregate field.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified field or compound group higher in the display order. For fields in a compound group, you can change their order within the current group only.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified field or compound group lower in the display order. For fields in a compound group, you can change their order within the current group only.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified field or compound group from the crosstab.

### Chart Screen

Designer displays the Chart screen when you use the dialog box for creating a crosstab, and enables the options in the screen when you have added at least one field on the column or row header and one aggregate field in the crosstab. You can use the screen to create a chart together with the crosstab, which Designer places above the crosstab in the report body

![Crosstab Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848617367/crstbwzd_cht.gif)

**No Chart**

Select if you do not want to create the chart.

**Bar Chart**

Select to create a Clustered Bar 2-D chart together with the crosstab.

**Line Chart**

Select to create a Line 2-D chart together with the crosstab.

**Pie Chart**

Select to create a Clustered Pie chart together with the crosstab.

**Category**

The drop-down list contains the fields that you add to the column and row headers of the crosstab. Select the field you want to display on the category (X) axis of the chart.

**Series**

The drop-down list contains the fields that you add to the column and row headers of the crosstab. Select the field you want to display on the series (Z) axis of the chart.

**Show Values**

The drop-down list contains the fields that you add as aggregate fields in the crosstab. Select the value you want to display in the chart.

### Filter Screen

Use this screen to narrow down the data to display in the crosstab.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Crosstab Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404857002775/crstbwzd_fltr.gif)

### Layout Screen

Use this screen to specify the layout of the crosstab. For more information about the layout settings, see [Customizing the Layout of a Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#Layout).

![Crosstab Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404848620823/crstbwzd_layout.gif)

### Style Screen

Use this screen to specify the style of the crosstab.

![Crosstab Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404857003287/crstbwzd_sty.gif)

**Style**

The box lists the styles that you can apply to the crosstab. Select the style for the crosstab.

* **<Custom>**  
  This style contains no information. It is only used to support reports that was built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the crosstab.

**Inherit Style**

Designer displays the option only when the crosstab is inside a banded object, or to be inserted into a banded object. Select it if you want the crosstab to inherit the style of its parent.

**Page Setup**

Designer displays the button only when you use the dialog box for creating a crosstab in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) to specify page properties for the report tab.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095821-Crosstab-Formula-Editor-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058422-CSS-Editor-Dialog-Box)
