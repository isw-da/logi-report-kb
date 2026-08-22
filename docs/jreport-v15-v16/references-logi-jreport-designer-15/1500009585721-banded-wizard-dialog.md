---
title: "Banded Wizard Dialog"
id: 1500009585721
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585721-Banded-Wizard-Dialog
updated_at: 2021-07-24T05:55:37Z
---

# Banded Wizard Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564562-Applet-Setting-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585741-Barcode-Expert-Dialog)

# Banded Wizard Dialog

The Banded Wizard varies with the data resource used to create the banded object: [query resource](#Query) or [business view](#BV).

## When Query Resource is Used

The wizard appears when you do either of the following:

* In the [Select Component for Page Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009588661-Select-Component-for-Page-Report-Tab-Dialog) dialog or [Select Component for Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009567422-Select-Component-for-Page-Report-Dialog) dialog, select the Banded component and then select OK. In this case, it helps you to [create a page report with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on a query resource.
* Right-click a banded object created on a query and select Banded Wizard on the shortcut menu. In this case, it helps you to [modify](https://devnet.logianalytics.com/hc/en-us/articles/1500009583341-Modifying-a-Banded-Object) the banded object.

The wizard consists of the following screens:

* [Data](#Data)
* [Display](#Display)
* [Group](#Group)
* [Summary](#Summary)
* [Chart](#Chart)
* [Filter](#Filter)
* [Style](#Style)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or modifying the banded object and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

### Data

Specifies the dataset for the banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889390743/bdwzd_dt.gif)

**Resource box**

Lists the available data resources in the current catalog. Select one to create the banded object.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the banded object.

* **New Dataset**  
   If checked, select a data source from the catalog resources to create a dataset that will be used to build the banded object. When you choose to create the dataset from a query, you can select the Edit button to edit the query if required.
* **Existing Dataset**  
   If checked, select a dataset from the ones existing in the open report to create the banded object. Select the Edit button to edit the query if required.
* **Current****Dataset**  
  If checked, the current dataset used by the parent object will be applied to the banded object.

### Display

Specifies the data fields to display in the banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404889390999/bdwzd_dsply.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected field in the banded object with the specified field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Show Banded Group Structure**

Specifies whether to show the group structure of the banded object. Available only when modifying a banded object.

**Display Fields**

Lists the fields that you have selected to display in the banded object.

**Display Name**

Shows the display names of the selected fields. You can select the name cells to edit them if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog to specify how to sort data in the banded object.

### Group

Specifies the fields to group the data. [See the screen](javascript:%20void(null)).

![Banded Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404893953559/bdwzd_grp.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected group by field in the banded object with the specified field in the Resources box.

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

### Summary

Specifies the fields on which to create aggregate functions. This screen is available only when you create a banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404893953815/bdwzd_sum.gif)

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

Lists all the fields that you want to display and to be summarized in the banded object. If an aggregation is added under the Banded Object node, it will be displayed in the banded panel. If an aggregation is added under the node of a specified group, it will be displayed in the corresponding group panel.

**Aggregate Function**

Specifies the function to summarize the selected field.

**Break Field**

Displays a defined field on which the summary will be calculated. If a summary field is added below the Banded Object node, the break field is null and the summary will be calculated on the whole dataset.

**Position**

Works together with the Column option to specify the location where the summary field will be put.

* **Header**  
   Specifies to put the summary field in the header row. If the summary is calculated on a group by field, it will be put in the group header row of the corresponding group; if the summary is calculated on the whole dataset, it will be put in the table header row.
* **Footer**  
   Specifies to put the summary field in the footer row. If the summary is calculated on a group by field, it will be put in the group footer row of the corresponding group; if the summary is calculated on the whole dataset, it will be put in the table footer row.

**Column**

Works together with the Position option to specify the location where the summary field will be put.

* **Detail**  
   The summary field with its label will be put in in the first two detail columns.
* **Summary**  
   The summary field will be displayed in a separate summary column.

### Chart

Specifies to create a chart together with the banded object, which will be placed in the banded header panel. This screen is available only when you create a banded object, and when there is at least one group by field and one summary field which is calculated on this group by field in the banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard - Chart screen](https://devnet.logianalytics.com/hc/article_attachments/4404889286551/bdwzd_cht.gif)

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

### Filter

Specifies to filter data displayed in the banded object. This screen is available only when you create a banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404893954071/bdwzd_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

### Style

Specifies the style of the banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404889391255/bdwzd_sty.gif)

**Style**

Specifies the style of the banded object.

* **<Custom>**  
   There is no style information on it and it is only used to support reports built with previous versions which did not bind any style or the bound style cannot be found in the style list.

**Preview**

Displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Specifies whether to make the banded object take the style of its parent. This option is available only when you modify a banded object and the banded object is inserted into another banded object.

**Create a Banded Report**

Creates a restricted version of a flow layout report, one that can contain a single banded object only. This layout option is intended to provide compatibility with Logi JReport Version 7 report templates.

**Create a Flow Layout Report Containing a Banded Object**

Creates a report that contains a banded object mapped to the specified dataset. This layout option is specified by default.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a banded object.

## When Business View is Used

This wizard appears when you do either of the following:

* In the [Select Component for Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009567422-Select-Component-for-Page-Report-Dialog) dialog, check Create Using Business View, select the Banded component, and then select OK. In this case, it helps you to [create a page report with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on a business view.
* When creating a report tab in a page report which is based on business views, in the [Select Component for Page Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009588661-Select-Component-for-Page-Report-Tab-Dialog) dialog, select the Banded component and select OK. In this case, it helps you to [create a page report tab with a banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on a business view.
* Right-click a banded object created based on a business view and select Banded Wizard on the shortcut menu. In this case, it helps you to [modify](https://devnet.logianalytics.com/hc/en-us/articles/1500009583341-Modifying-a-Banded-Object) the banded object.

The wizard consists of the following screens:

* [Data](#Data-bv)
* [Display](#Display-bv)
* [Group](#Group-bv)
* [Summary](#Summary-bv)
* [Filter](#Filter-bv)
* [Style](#Style-bv)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes creating or modifying the banded object and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

### Data

Specifies a business view for the banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard for business view - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404893954327/bdwzd_dt-bv.gif)

**Resources**

Lists all the business views in the current catalog. Specify the one you want to use.

### Display

Specifies the data fields to display in the banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard for business view - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404893954711/bdwzd_dsply-bv.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the specified field to use in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the specified field that is not required in the banded object.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected field in the banded object with the specified field in the Resources box.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified field one step down.

**Show Banded Group Structure**

Specifies whether to show the group structure of the banded object. Available only when modifying a banded object.

**Display Fields**

Lists the fields that you have selected to display in the banded object.

**Display Name**

Shows the display names of the selected fields. You can select the name cells to edit them if required.

**Sort Fields By**

Opens the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog to specify how to sort data in the banded object.

### Group

Specifies the fields to group the data. [See the screen](javascript:%20void(null)).

![Banded Wizard for business view - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404893955095/bdwzd_grp-bv.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field in the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif)

Replaces the selected group by field in the banded object with the specified field in the Resources box.

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
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009586161-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog to specify the Select N condition.

### Summary

Specifies the aggregations to display in the banded object. This screen is available only when you create a banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard for business view - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404893955351/bdwzd_sum-bv.gif)

**Resources**

Lists all the available aggregations.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected aggregation to the banded object.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected aggregation that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified aggregation one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified aggregation one step down.

**Summarized Fields**

Lists all the aggregations that you want to display in the banded object. If an aggregation is added under the Banded Object node, it will be displayed in the banded panel. If an aggregation is added under the node of a specific group, it will be displayed in the corresponding group panel.

**Position**

Works together with the Column option to specify the location where the aggregation will be put.

* **Footer**  
   Specifies to put the aggregation in the footer row. If the aggregation is calculated on a group by field, it will be put in the group footer row of the corresponding group; if the aggregation is calculated on the whole dataset, it will be put in the banded footer row.

**Column**

Works together with the Position option to specify the location where the aggregation will be put.

* **Detail**  
   The aggregation with its label will be put in in the first two detail columns.

### Filter

Specifies to filter data displayed in the banded object. This screen is available only when you create a banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard for business view - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404889391767/bdwzd_fltr-bv.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

### Style

Specifies the style of the banded object. [See the screen](javascript:%20void(null)).

![Banded Wizard for business view - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404893955607/bdwzd_sty-bv.gif)

**Style**

Specifies the style of the banded object.

**Preview**

Displays a diagram illustrating the effect of the selected style on the banded object.

**Inherit Style**

Specifies whether to make the banded object take the style of its parent. This option is available only when you modify a banded object which is inserted into another banded object.

**Page Setup**

Opens the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) dialog to specify page properties. Available only when creating a banded object.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564562-Applet-Setting-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585741-Barcode-Expert-Dialog)
