---
title: "Banded Wizard Dialog Box"
id: 1500010095621
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095621-Banded-Wizard-Dialog-Box
updated_at: 2022-03-28T09:20:11Z
---

# Banded Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095601-Applet-Parameter-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058082-Barcode-Expert-Dialog-Box)

# Banded Wizard Dialog Box

You can use the Banded Wizard dialog box to [create a page report tab with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) or [modify an existing banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500010094321-Modifying-Banded-Objects). This topic describes the options in the dialog box.

Designer displays different options in the Banded Wizard dialog box according to the type of the data resource used for the banded object: [business view](#BV) or [query resource](#Query).

## Banded Wizard Dialog Box - Business View Based

When you use the Banded Wizard dialog box for creating or editing a banded object using a business view, you see the following screens in the dialog box (Designer displays some screens only when you use the dialog box for creating a banded object):

* [Data Screen](#BVData)
* [Display Screen](#BVDisplay)
* [Group Screen](#BVGroup)
* [Summary Screen](#BVSummary)
* [Filter Screen](#BVFilter)
* [Style Screen](#BVStyle)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish creating or modifying the banded object and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the business view for the banded object. You can select from all the predefined business views in the current catalog.

![Banded Wizard for business view - Data](https://devnet.logianalytics.com/hc/article_attachments/4404857009559/bdwzd_dt_bv.gif)

**Inherit from the Parent**

Designer displays and enables the option only when you use the dialog box for editing a banded object that is inside any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel. Select it if you want the banded object to inherit the business view that its parent banded object uses.

### Display Screen

Use this screen to specify the detail fields to display in the banded object.

![Banded Wizard for business view - Display](https://devnet.logianalytics.com/hc/article_attachments/4404857009815/bdwzd_dsply_bv.gif)

**Resources**

The box lists the resources in and related to the specified business view, which you can use as detail fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)**Replace button**

Select to replace the specified field in the banded object with the selected field in the Resources box. Designer displays the button only when you use the dialog box for modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Show Banded Group Structure**

Designer displays the option only when you use the dialog box for modifying a banded object. Select it if you want to show the group structure of the banded object.

**Display Fields**

The column shows the detail fields that you add to display in the banded object.

**Display Name**

The column shows the labels of the detail fields in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels, or select the Auto Map Field Name checkboxes in the text boxes to automatically map the labels to the dynamic display names of the fields at runtime.

**Sort Fields By**

Select to open the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060542-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the banded object.

### Group Screen

Use this screen to specify the criteria for grouping data in the banded object.

![Banded Wizard for business view - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848631063/bdwzd_grp_bv.gif)

**Resources**

The box lists the resources in and related to the specified business view, which you can use as group-by fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)**Replace button**

Select to replace the specified group-by field in the banded object with the selected field in the Resources box. Designer displays the button only when you use the dialog box for modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

**Group By**

The column shows the group-by fields on which you select to group data in the banded object.

**Sort**

The column shows how you want to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

### Summary Screen

Designer displays the Summary screen only when you use the dialog box for creating a banded object. You can use this screen to specify the summaries to calculate data in the banded object.

![Banded Wizard for business view - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404848631319/bdwzd_smry_bv.gif)

**Resources**

The box lists the resources in and related to the specified business view, which you can use to calculate data in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to calculate data in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

The column shows the fields that you add to calculate data in the banded object.

**Position**

The column shows the position of the summaries. Designer places the summary added for a group level in the group's footer panel; if you add a summary for the Banded Object level, Designer places it in the banded footer panel.

**Column**

The column shows where to place the summaries. By default, Designer places the summaries and their name labels in the first two detail columns.

### Filter Screen

Designer displays the Filter screen only when you use the dialog box for creating a banded object. You can use this screen to narrow down the data to display in the banded object.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Banded Wizard for business view - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404857010199/bdwzd_fltr_bv.gif)

### Style Screen

Use this screen to specify the style of the banded object.

![Banded Wizard for business view - Style](https://devnet.logianalytics.com/hc/article_attachments/4404857010711/bdwzd_sty_bv.gif)

**Style**

The box lists the styles that you can apply to the banded object. Select the style for the banded object.

* **<Custom>**  
  This style contains no information. It is only used to support reports that was built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Designer displays the option only when the banded object is inside another banded object, or to be inserted into another banded object. Select it if you want the banded object to inherit the style of its parent.

**Page Setup**

Designer displays the button only when you use the dialog box for creating a banded object in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) to specify page properties for the report tab.

## Banded Wizard Dialog Box - Query Based

When you use the Banded Wizard dialog box for creating or editing a banded object using a query resource, you see the following screens in the dialog box (Designer displays some screens only when you use the dialog box for creating a banded object):

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Group Screen](#Group)
* [Summary Screen](#Summary)
* [Chart Screen](#Chart)
* [Filter Screen](#Filter)
* [Style Screen](#Style)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish creating or modifying the banded object and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

### Data Screen

Use this screen to specify the dataset for the banded object.

![Banded Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404857011095/bdwzd_dt.gif)

**Data resource box**

The box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the banded object.

**More Options**/**Less Options**

Select to show or hide the options for specifying a dataset for the banded object.

* **New Dataset**  
  Select to create a dataset based on the current catalog data resources. When you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box).
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select the Edit button to edit the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select <New Dataset...> to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer enables this option only when you use the dialog box for editing a banded object and the parent object containing the banded object already applies a dataset. Select it if you want the banded object to inherit the dataset from its parent.

### Display Screen

Use this screen to specify the detail fields to display in the banded object.

![Banded Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848635031/bdwzd_dsply.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use as detail fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)**Replace button**

Select to replace the specified field in the banded object with the selected field in the Resources box. Designer displays the button only when you use the dialog box for modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Show Banded Group Structure**

Designer displays the option only when you use the dialog box for modifying a banded object. Select it if you want to show the group structure of the banded object.

**Display Fields**

The column shows the detail fields that you add to display in the banded object.

**Display Name**

The column shows the labels of the detail fields in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Select to open the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060542-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the banded object.

### Group Screen

Use this screen to specify the criteria for grouping data in the banded object.

![Banded Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404857011351/bdwzd_grp.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use as group-by fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404856888855/btn_replace.gif)**Replace button**

Select to replace the specified group-by field in the banded object with the selected field in the Resources box. Designer displays the button only when you use the dialog box for modifying a banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified group to a higher group level.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified group to a lower group level.

**Group By**

The column shows the group-by fields on which you select to group data in the banded object.

**Sort**

The column shows how you want to sort groups at each group level. You can select from the following options:

* **Ascend**  
  Select to sort groups at the specified group level in an ascending order (A, B, C).
* **Descend**  
  Select to sort groups at the specified group level in a descending order (C, B, A).
* **No Sort**  
  Select to sort groups at the specified group level in their original order in database.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) to define grouping information.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) to set how to sort the groups at the specified group level.

**Special Function**

The column shows the [special functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Function) that you select for the group-by fields of the Numeric, String, Date, and Time data types. Select a special function from the drop-down list to specify to which level to group the data of the specified field, or select Customize to set the function in the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096021-Customized-Function-Dialog-Box).

**Custom Sort**

Designer enables the button after you have selected Custom Sort from the Sort column to define the sort manner of groups for the specified group level. Select it to specify how to sort the groups.

**Special Group**

Designer enables the button after you have selected Special Group from the Sort column to define a special group. Select it to specify how to group your information.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition for the specified group level.

**Group Filter**

Select to open the [Group Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097461-Group-Filter-Dialog-Box) to specify the group filter condition.

### Summary Screen

Designer displays the Summary screen only when you use the dialog box for creating a banded object. You can use this screen to specify the fields on which to create summaries in the banded object.

![Banded Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404848635415/bdwzd_smry.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use to create summaries in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box based on which to create a summary in the banded object.

![Rremove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

The column shows the fields that you add to create summaries in the banded object.

**Aggregate Function**

The column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) that you select to use for the summaries.

**Distinct On**

Designer enables the option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box).

**Break Field**

The column shows the groups on which to calculate the summaries. If you add a summary for the Banded Object level, the break field is null and Designer calculates the summary based on the whole dataset.

**Position**

You can use the option together with the Column option to specify the location where to place a summary.

* **Header**  
  Select to place the summary in the header panel. If you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Banded Object level, Designer places it in the banded header panel.
* **Footer**  
  Select to place the summary in the footer panel. If you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Banded Object level, Designer places it in the banded footer panel.

**Column**

You can use the option together with the Position option to specify the location where to place a summary.

* **Detail**  
  Select to place the summary and its name label in the first two detail columns.
* **Summary**  
  Select to place the summary in a separate summary column.

### Chart Screen

Designer displays the Chart screen when you use the dialog box for creating a banded object, and enables the options in the screen when you have added at least one group and one summary for this group in the banded object. You can use the screen to create a chart together with the banded object, which Designer places in the banded header panel.

![Banded Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848635799/bdwzd_cht.gif)

**No Chart**

Select if you do not want to create the chart.

**Bar Chart**

Select to create a Clustered Bar 2-D chart together with the banded object.

**Line Chart**

Select to create a Line 2-D chart together with the banded object.

**Pie Chart**

Select to create a Clustered Pie chart together with the banded object.

**Category**

The drop-down list contains the group-by fields of the banded object on which you have added summaries. Select the field you want to display on the category (X) axis of the chart.

**Series**

The drop-down list contains the fields that you added as the group-by fields of the banded object. Select the field you want to display on the series (Z) axis of the chart.

**Show Values**

The drop-down list contains the summaries which are calculated based on the field you choose to display on the category axis of the chart. Select the value you want to display in the chart.

### Filter Screen

Designer displays the Filter screen only when you use the dialog box for creating a banded object. You can use this screen to narrow down the data to display in the banded object.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Banded Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404857011607/bdwzd_fltr.gif)

### Style Screen

Use this screen to specify the style of the banded object.

![Banded Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848636311/bdwzd_sty.gif)

**Style**

The box lists the styles that you can apply to the banded object. Select the style for the banded object.

* **<Custom>**  
  This style contains no information. It is only used to support reports that was built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Designer displays the option only when the banded object is inside another banded object, or to be inserted into another banded object. Select it if you want the banded object to inherit the style of its parent.

**Create a Banded Report**

Designer displays the option only when you use the dialog box for creating a banded object. Select it if you want to create a restricted version of a flow layout report, one that can contain a single banded object only. This layout option is intended to provide compatibility with Logi Report Version 7 report templates.

**Create a Flow Layout Report Containing a Banded Object**

Designer displays the option only when you use the dialog box for creating a banded object. Select it if you want to create a report that contains a banded object mapped to the specified dataset.

**Page Setup**

Designer displays the button only when you use the dialog box for creating a banded object in a page report tab. Select it to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) to specify page properties for the report tab.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095601-Applet-Parameter-Dialog-Box)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058082-Barcode-Expert-Dialog-Box)
