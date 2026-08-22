---
title: "Insert Group Column Dialog"
id: 1500010031462
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031462-Insert-Group-Column-Dialog
updated_at: 2021-07-24T10:38:39Z
---

# Insert Group Column Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066901-Insert-Filter-Control-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066921-Insert-Link-Dialog)

# Insert Group Column Dialog

The Insert Group Column dialog helps you to [insert new group columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010029302-Modifying-Tables#GroupColumn) into a table. It appears when you right-click a table or a table column and select Insert > Group Column from the shortcut menu.

Options in the dialog vary according to the data resource type the table uses: [business view](#BV) or [query resource](#Query).

When the table is created on a business view, the dialog contains the following options:

![Insert Group Column dialog - Business View](https://devnet.logianalytics.com/hc/article_attachments/4404901204503/instgrpclmn-bv.gif)

**Resources**

Lists the view elements in and related to the business view the table uses that can be used for group columns.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field in the Resources box as a group-by field to the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected group-by field from the table.

**![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404901173527/btn_replace.gif)**

Replaces the selected group-by field with the specified field in the Resources box.

**Group By**

Lists the group-by fields that are added to group data in the table.

**Sort**

Specifies how groups at the specific group level will be sorted.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010065201-Custom-Sort-Dialog) dialog to set how groups will be sorted.

**Table (Group Above)**

Specifies to place the selected group-by field above the detail information.

**Table (Group Left Above)**

Specifies to place the selected group-by field left above the detail information.

**Table (Group Left)**

Specifies to place the selected group-by field left to the detail information.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the specified group one step down.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

---

When the table is created on a query resource, the dialog contains the following options:

![Insert Group Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901204887/instgrpclmn.gif)

**Resources**

Lists the data fields in and related to the query resource the table uses that can be used for group columns.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)**

Adds the selected field in the Resources box as a group-by field to the table.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)**

Removes the selected group-by field from the table.

**![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404901173527/btn_replace.gif)**

Replaces the selected group-by field with the specified field in the Resources box.

**Group By**

Lists the group-by fields that are added to group data in the table.

**Sort**

Specifies how groups at the specific group level will be sorted.

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

**Table (Group Above)**

Specifies to place the selected group-by field above the detail information.

**Table (Group Left Above)**

Specifies to place the selected group-by field left above the detail information.

**Table (Group Left)**

Specifies to place the selected group-by field left to the detail information.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the specified group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the specified group one step down.

**Custom Sort**

Specifies how to sort the groups. Activated only when you have selected Custom Sort from the Sort column to define the sorting manner of groups for the selected group level.

**Special Group**

Specifies how to group your information. Activated only when you have selected Special Group from the Sort column to define a special group.

**Select N**

Opens the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500010067821-Select-N-Dialog) dialog to specify the Select N condition.

**Group Filter**

Opens the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010031302-Group-Filter-Dialog) dialog to specify the group filter condition.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066901-Insert-Filter-Control-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066921-Insert-Link-Dialog)
