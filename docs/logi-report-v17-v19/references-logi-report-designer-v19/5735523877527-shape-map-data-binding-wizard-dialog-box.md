---
title: "Shape Map Data Binding Wizard Dialog Box"
id: 5735523877527
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735523877527-Shape-Map-Data-Binding-Wizard-Dialog-Box
updated_at: 2022-11-02T04:39:46Z
---

# Shape Map Data Binding Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735566717079-Shape-Map-Canvas-Setup-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735523889559-Shape-Map-Editor-Dialog-Box)

# Shape Map Data Binding Wizard Dialog Box

You can use the Shape Map Data Binding Wizard dialog box to [bind a dataset to a shape map](https://devnet.logianalytics.com/hc/en-us/articles/5735521118231-Using-Shape-Maps#BindData) and display values on the shape map areas. This topic describes the options in the dialog box.

Designer displays the Shape Map Data Binding Wizard dialog box when you navigate to Menu > Insert > Bind Data, or select Bind Data on the toolbar in the [Shape Map Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735523889559-Shape-Map-Editor-Dialog-Box).

The dialog box contains the following screens:

* [Data Screen](#Data)
* [Group Screen](#Group)
* [Summary Screen](#Summary)
* [Filter Screen](#Filter)

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

## Data Screen

Use this screen to specify the dataset to bind to the shape map.

![Shape Map Data Binding Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/9898461576087/mpdtbdingwzd_dt.gif)

**Data resource box**

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it to bind to the shape map.

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
  Designer enables this option when the parent object where you have specified to insert the shape map already applies a dataset. Select it if you want the shape map to inherit the dataset from its parent.

**Edit**

Select to edit the specified query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box) or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box).

## Group Screen

Use this screen to specify the criteria for grouping data in the dataset.

![Shape Map Data Binding Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/9898461615511/mpdtbdingwzd_grp.gif)

**Resources**

This box lists the available data fields that you can use to group data of the dataset.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field to group data of the dataset. You can add only one group for the dataset.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field.

**Group By**

This column shows the group-by field on which you select to group data of the dataset.

**Sort**

Specify how you want to sort the groups. You can select from the following options:

* **Ascend**  
  Select to sort the groups in an ascending order (A, B, C).
* **Descend**  
  Select to sort the groups in a descending order (C, B, A).
* **No Sort**  
  Select to sort the groups in their original order in database.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544779031-User-Defined-Group-Dialog-Box) to define grouping information.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565346071-Custom-Sort-Dialog-Box) to set how to sort the groups.

**Special Function**

Select the [special function](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables#Function) for the group-by field when it is Numeric, String, Date, or Time data type. Select a special function from the drop-down list to specify to which level to group the data, or select Customize to set the function in the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522295831-Customized-Function-Dialog-Box).

**Custom Sort**

Designer enables this button after you have selected Custom Sort from the Sort column to define the sort manner of the groups. Select it to specify how to sort the groups.

**Special Group**

Designer enables this button after you have selected Special Group from the Sort column to define a special group. Select it to specify how to group your information.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567350807-Select-N-Dialog-Box) to specify the Select N condition for the groups.

**Group Filter**

Select to open the [Group Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530070167-Group-Filter-Dialog-Box) to specify the group filter condition.

## Summary Screen

Use this screen to specify the fields on which to create summaries to calculate data based on the group that you add for the dataset.

![Shape Map Data Binding Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898461623703/mpdtbdingwzd_sum.gif)

**Resources**

This box lists the available data fields that you can use to create summaries for the group.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box based on which to create a summary.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

This column shows the fields that you add to create summaries for the group.

**Aggregate Function**

This column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) that you select to use for the summaries.

**Distinct On**

Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box).

**Break Field**

This column shows the name of the group-by field that you add in the Group screen. Designer calculates the summaries based on this group.

## Filter

Use this screen to narrow down the data to display on the map areas.

Designer displays the same options in the Filter screen as those in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522539031-Edit-Filter-Dialog-Box).

![Shape Map Data Binding Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898461632279/mpdtbdingwzd_fltr.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735566717079-Shape-Map-Canvas-Setup-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735523889559-Shape-Map-Editor-Dialog-Box)
