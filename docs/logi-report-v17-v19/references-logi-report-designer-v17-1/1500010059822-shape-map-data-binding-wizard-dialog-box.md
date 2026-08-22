---
title: "Shape Map Data Binding Wizard Dialog Box"
id: 1500010059822
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059822-Shape-Map-Data-Binding-Wizard-Dialog-Box
updated_at: 2021-07-23T19:15:44Z
---

# Shape Map Data Binding Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059802-Shape-Map-Canvas-Setup-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059842-Shape-Map-Editor-Dialog-Box)

# Shape Map Data Binding Wizard Dialog Box

You can use the Shape Map Data Binding Wizard dialog box to [bind a dataset to a shape map](https://devnet.logianalytics.com/hc/en-us/articles/1500010094801-Using-Shape-Maps#BindData) and display values on the shape map areas. This topic describes the options in the dialog box.

Designer displays the Shape Map Data Binding Wizard dialog box when you select Menu > Insert > Bind Data, or select Bind Data on the toolbar in the [Shape Map Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059842-Shape-Map-Editor-Dialog-Box).

The dialog box contains the following screens:

* [Data Screen](#Data)
* [Group Screen](#Group)
* [Summary Screen](#Summary)
* [Filter Screen](#Filter)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish binding data to the shape map and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Data Screen

Use this screen to specify the dataset that you want to bind with the shape map.

![Shape Map Data Binding Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856908695/mpdtbdingwzd_dt.gif)

**Data resource box**

The box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the shape map.

**More Options**/**Less Options**

Select to show or hide the options for specifying a dataset for the shape map.

* **New Dataset**  
  Select to create a dataset based on the current catalog data resources. When you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box).
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select the Edit button to edit the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select <New Dataset...> to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Select to inherit the dataset from the parent object.

## Group Screen

Use this screen to specify the criteria for grouping data in the selected dataset.

![Shape Map Data Binding Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848508823/mpdtbdingwzd_grp.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use to group data of the dataset.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field to group data of the dataset. You can add only one group for the dataset.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field.

**Group By**

The column shows the group-by field on which you select to group data of the dataset.

**Sort**

Specify how you want to sort the groups. You can select from the following options:

* **Ascend**  
  Select to sort the groups in an ascending order (A, B, C).
* **Descend**  
  Select to sort the groups in a descending order (C, B, A).
* **No Sort**  
  Select to sort the groups in their original order in database.
* **Special Group**  
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) to define grouping information.
* **Custom Sort**  
  Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) to set how to sort the groups.

**Special Function**

Select the [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Function) for the group-by field if it is of the Numeric, String, Date, or Time data type. Select a special function from the drop-down list to specify to which level to group the data, or select Customize to set the function in the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096021-Customized-Function-Dialog-Box).

**Custom Sort**

Designer enables the button after you have selected Custom Sort from the Sort column to define the sort manner of the groups. Select it to specify how to sort the groups.

**Special Group**

Designer enables the button after you have selected Special Group from the Sort column to define a special group. Select it to specify how to group your information.

**Select N**

Select to open the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box) to specify the Select N condition for the groups.

**Group Filter**

Select to open the [Group Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097461-Group-Filter-Dialog-Box) to specify the group filter condition.

## Summary Screen

Use this screen to specify the fields on which to create summaries to calculate data based on the group that you add for the dataset.

![Shape Map Data Binding Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404848509079/mpdtbdingwzd_sum.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use to create summaries for the group.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box based on which to create a summary.

![Rremove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified summary.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified summary higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified summary lower in the display order.

**Summarized Fields**

The column shows the fields that you add to create summaries for the group.

**Aggregate Function**

The column shows the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) that you select to use for the summaries.

**Distinct On**

Designer enables the option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box).

**Break Field**

The column shows the name of the group-by field that you add in the Group screen. Designer calculates the summaries based on this group.

## Filter

Use this screen to narrow down the data to display on the map areas.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Shape Map Data Binding Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848509463/mpdtbdingwzd_fltr.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059802-Shape-Map-Canvas-Setup-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059842-Shape-Map-Editor-Dialog-Box)
