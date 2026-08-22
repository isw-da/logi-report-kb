---
title: "Mailing Label Wizard Dialog Box"
id: 1500010097861
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097861-Mailing-Label-Wizard-Dialog-Box
updated_at: 2021-07-23T19:15:43Z
---

# Mailing Label Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059702-Link-Data-Container-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097881-Manage-Customized-Controls-Dialog-Box)

# Mailing Label Wizard Dialog Box

You can use the Mailing Label Wizard dialog box to [create a page report with a cross banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page), which is in the form of a mailing label layout. This topic describes the options in the dialog box.

Designer displays the Mailing Label Wizard dialog box when you select the Mailing Label layout in the [Select Component for Page Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060402-Select-Component-for-Page-Report-Dialog-Box) or [Select Component for Page Report Tab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060422-Select-Component-for-Page-Report-Tab-Dialog-Box) and select OK.

The dialog box contains the following screens:

* [Data Screen](#Data)
* [Display Screen](#Display)
* [Group Screen](#Group)
* [Summary Screen](#Summary)
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

Select to finish creating the banded object and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Data Screen

Use this screen to specify the dataset for the banded object.

![Mailing Label Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404848511895/mllblwzd_dt.gif)

**Data resource box**

The box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the banded object.

**More Options**/**Less Options**

Select to show or hide the options for specifying a dataset for the banded object.

* **New Dataset**  
  Select to create a dataset based on the current catalog data resources. When you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box).
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select the Edit button to edit the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select <New Dataset...> to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer does not support the option when you create the banded object in a new page report tab.

## Display Screen

Use this screen to specify the detail fields to display in the banded object.

![Mailing Label Wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404856911383/mllblwzd_dsply.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use as detail fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box to the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified field from the banded object.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified field higher in the display order.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified field lower in the display order.

**Display Fields**

The column shows the detail fields that you add to display in the banded object.

**Display Name**

The column shows the labels of the detail fields in the banded object, which by default are the display names of the added fields. You can select in the text boxes to edit the labels.

**Sort Fields By**

Select to open the [Sort Fields By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060542-Sort-Fields-By-Dialog-Box) to specify how to sort the detail data in the banded object.

## Group Screen

Use this screen to specify the criteria for grouping data in the banded object.

![Mailing Label Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848512407/mllblwzd_grp.gif)

**Resources**

The box lists the data fields in and related to the specified query resource, which you can use as group-by fields in the banded object.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified field in the Resources box as a group-by field in the banded object.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified group-by field from the banded object.

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

## Summary Screen

Use this screen to specify the fields on which to create summaries in the banded object.

![Mailing Label Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404856912279/mllblwzd_sum.gif)

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
  Select it to place the summary in the header panel. If you add the summary for a specific group, Designer places it in the group's header panel; if you add the summary for the Banded Object level, Designer places it in the banded header panel.
* **Footer**  
  Select it to place the summary in the footer panel. If you add the summary for a specific group, Designer places it in the group's footer panel; if you add the summary for the Banded Object level, Designer places it in the banded footer panel.

**Column**

You can use the option together with the Position option to specify the location where to place a summary.

* **Detail**  
  Select it to place the summary and its name label in the first two detail columns.
* **Summary**  
  Select it to place the summary in a separate summary column.

## Chart Screen

Designer enables the options in the Chart screen when you have added at least one group and one summary for this group in the banded object. You can use the screen to create a chart together with the banded object, which Designer places in the banded header panel.

![Mailing Label Wizard - Chart](https://devnet.logianalytics.com/hc/article_attachments/4404856912663/mllblwzd_cht.gif)

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

## Filter Screen

Use this screen to narrow down the data to display in the banded object.

Designer displays the same options in the Filter screen as in the [Edit Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box).

![Mailing Label Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856913175/mllblwzd_fltr.gif)

## Layout Screen

Use this screen to specify the layout of the banded object.

![Mailing Label Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404856913431/mllblwzd_layout.gif)

**Label Size**

You can specify the size for the labels in the banded object in this box.

* **Width**  
  Specify the width of the labels.
* **Height**  
  Specify the height of the labels.

**Gap Between Labels**

You can specify the gap between each two labels in this box.

* **Horizontal Gap**  
  Specify the horizontal gap between two labels.
* **Vertical Gap**  
  Specify the vertical gap between two labels.

**Preview**

The box displays a preview sample of the specified layout for the labels.

## Style Screen

Use this screen to specify the style of the banded object.

![Mailing Label Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848512919/mllblwzd_sty.gif)

**Style**

The box lists the styles that you can apply to the banded object. Select the style for the banded object.

**Preview**

The box displays a diagram illustrating the effect of the selected style on the banded object.

**Create a Banded Report**

Select to create a restricted version of a flow layout report, one that can contain a single banded object only. This layout option is intended to provide compatibility with Logi Report Version 7 report templates.

**Create a Flow Layout Report Containing a Banded Object**

Select to create a report that contains a banded object mapped to the specified dataset.

**Page Setup**

Select to open the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box) to specify page properties for the report tab.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059702-Link-Data-Container-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097881-Manage-Customized-Controls-Dialog-Box)
