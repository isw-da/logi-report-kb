---
title: "Shape Map Data Binding Wizard Dialog"
id: 1500010031722
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031722-Shape-Map-Data-Binding-Wizard-Dialog
updated_at: 2021-07-24T10:38:35Z
---

# Shape Map Data Binding Wizard Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031702-Shape-Map-Canvas-Setup-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067141-Shape-Map-Editor-Dialog)

# Shape Map Data Binding Wizard Dialog

The Shape Map Data Binding Wizard helps you to [bind a dataset to a shape map](https://devnet.logianalytics.com/hc/en-us/articles/1500010063881-Shape-Maps#BindData) and make values displayed on the shape map areas according to your requirements. It appears when you select Insert > Bind Data in the [Shape Map Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067141-Shape-Map-Editor-Dialog).

The wizard contains the following screens: [Data](#Data), [Group](#Group), [Summary](#Summary) and [Filter](#Filter).

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

Specifies the dataset that will be bound with the map.

![Shape Map Data Binding Wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404901195287/mpdtbdingwzd_dt.gif)

**Resource box**

Lists the available data resources in the current catalog. Select one to be bound with the map.

**More Options**/**Less Options**

Shows or hides the dataset selection panel to choose a dataset for the map.

* **New Dataset**  
   Specifies to create a dataset from the current catalog data resources. When a query is selected, you can select the Edit button to edit the query in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog) if required.
* **Existing Dataset**  
   Specifies to use a dataset from the ones existing in the current page report. Select the Edit button to edit the dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010030342-Dataset-Editor-Dialog) if required.
* **Current Dataset**  
   Specifies to inherit the dataset used by the parent object.

## Group

Specifies the field to group the data.

![Shape Map Data Binding Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404901195543/mpdtbdingwzd_grp.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field as the group-by field.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected group-by field that is not required.

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
   Opens the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog) dialog to define grouping information.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010065201-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Special Function**

If the group-by field is of Numeric/String/Date/Time type, you can select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Function) for the field in the Special Function column to further specify to which level the data will be grouped by.

If Customize is selected, the [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010065221-Customized-Function-Dialog) dialog will be displayed, in which you can set the function.

**Custom Sort**

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sorting manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500010067821-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010031302-Group-Filter-Dialog) dialog to specify the group filter condition.

## Summary

Specifies the fields on which to create aggregate functions.

![Shape Map Data Binding Wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404901196183/mpdtbdingwzd_sum.gif)

**Resources**

Lists all the available data resources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field as the summary field.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected summary field that is not required.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the specified summary field one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the specified summary field one step down.

**Summarized Fields**

Lists all the fields that you want to display and to be summarized.

**Aggregate Function**

Specifies the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) to summarize the selected field.

**Distinct On**

Available and should be set when DistinctSum is selected as the aggregate function. It specifies the fields according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) in the text box to select the required fields in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.

**Break Field**

Displays a defined field on which the summary will be calculated.

## Filter

Specifies to filter the data displayed on the map areas.

![Shape Map Data Binding Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404901196439/mpdtbdingwzd_fltr.gif)

The options in the screen are the same as those in the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010065601-Edit-Filter-Dialog) dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031702-Shape-Map-Canvas-Setup-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067141-Shape-Map-Editor-Dialog)
