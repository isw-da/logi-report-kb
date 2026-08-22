---
title: "Shape Map Data Binding Wizard Dialog"
id: 1500009566722
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566722-Shape-Map-Data-Binding-Wizard-Dialog
updated_at: 2021-07-24T05:55:02Z
---

# Shape Map Data Binding Wizard Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587821-Shape-Map-Canvas-Setup-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566742-Shape-Map-Editor-Dialog)

# Shape Map Data Binding Wizard Dialog

The wizard appears when you select Insert > Bind Data in the [Shape Map Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009566742-Shape-Map-Editor-Dialog). It helps you to [bind a dataset to a shape map](https://devnet.logianalytics.com/hc/en-us/articles/1500009584121-Binding-Data-to-a-Shape-Map) and make values displayed on the shape map areas according to your requirements.

The wizard consists of the following screens:

* [Data](#Data)
* [Group](#Group)
* [Summary](#Summary)
* [Filter](#Filter)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes data binding and closes this wizard.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Data

**Define a dataset for the object**

Specifies the dataset that will be bound with the map. [See the screen](javascript:%20void(null)).

![Shape Map Data Binding Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404889328407/mpdtbdingwzd_dt.gif)

* **New**  
  If checked, select a data source from the catalog resources to create a dataset to bind with the map. When you choose to create the dataset from a query, you can select the Modify button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) if required.
* **Existing**  
  If checked, select a dataset from the ones existing in the open report to bind with the map. Select the Modify button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if required.
* **Current**  
  If checked, the current dataset used by the parent object will be applied to the map.

## Group

Specifies the field to group the data. [See the screen](javascript:%20void(null)).

![Shape Map Data Binding Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404889328663/mpdtbdingwzd_grp.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the group by field.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected group by field that is not required.

**Group By**

Lists the field that is used to group data.

**Sort**

Specifies how groups will be sorted.

* **Ascend**  
  Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
  Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
  Groups will be sorted in the original order in database.
* **Special Group**  
  Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog to define grouping information.
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

![Shape Map Data Binding Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404893866391/mpdtbdingwzd_sum.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected field as the summary field.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected summary field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified summary field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified summary field one step down.

**Summarized Fields**

Lists all the fields that you want to display and to be summarized.

**Aggregate Function**

Specifies the function to summarize the selected field. For details about each function, see [Math Functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions).

**Break Field**

Displays a defined field on which the summary will be calculated.

## Filter

Specifies to filter the data displayed on the map areas. [See the screen](javascript:%20void(null)).

![Shape Map Data Binding Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404893866647/mpdtbdingwzd_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587821-Shape-Map-Canvas-Setup-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566742-Shape-Map-Editor-Dialog)
