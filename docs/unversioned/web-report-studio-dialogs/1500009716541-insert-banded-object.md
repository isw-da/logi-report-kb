---
title: "Insert Banded Object"
id: 1500009716541
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009716541-Insert-Banded-Object
updated_at: 2021-11-03T06:57:15Z
---

# Insert Banded Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009716561-Insert-Banded-Group)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009690342-Insert-Chart)

# Insert Banded Object

The Insert Banded Object dialog helps you to [insert a banded object to a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009719181-Inserting-Components#Banded) and consists of the following tabs: [Details](#Details), [Group](#Group) and [Summary](#Summary).
This dialog appears when you drag Banded from the Components panel to the destination.

**Banded Title**

Specifies a title for the banded object.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4412131381399/btn_wbrpt_font.gif)

Specifies the font properties for title of the banded object.

* **Font**  
   Lists all the available font faces that can be selected to apply to the title.
* **Font Style**   
   Specifies the font style of the title. It can be one of the following: plain, bold, italic, and bold italic.
* **Size**  
   Specifies the font size of the title.
* **Align**  
   Specifies the position of the title to be left, right, center or justify.
* **Font Color**  
   Specifies the font color of the title.
* **Background Color**  
   Specifies the background color of the title.

**Data Source**

Specifies the business view in the current catalog on which the banded object will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009716841-Query-Filter) dialog to specify the filter which you want to apply to the selected business view.

**OK**

Inserts a banded object and closes the dialog.

**Cancel**

Cancels the insertion and closes the dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

## Details

Specifies the detail fields that you want to display in the banded object.

![Insert Banded Object dialog - Details](https://devnet.logianalytics.com/hc/article_attachments/4412131394967/insrtbd_dtl.gif)

**Resources**

Displays all the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) and detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4412139491991/btn_bvdtl.gif) in the selected business view.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)

Sorts the objects in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.

* **Predefined Order**  
   Sorts the objects in the order defined in the Business View Editor on Logi JReport Designer.
* **Resource Types**  
   Sorts the objects by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
   Sorts the objects in alphabetical order. Objects that are not in any category will be sorted first, then the categories, and the objects in each category will also be sorted alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)

Launches the search bar to search for objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)

Adds the selected object to be displayed in the banded object.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)

Removes the selected object that is added.

**Field**

Lists the group and detail objects that have been added to the banded object as the detail fields.

**Label**

Specifies the text for the labels of the detail fields, which by default are the display names of the added objects. You can select in the text boxes to edit the label text, or check the Auto Map Field Name checkboxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)

Moves the selected object one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)

Moves the selected object one step down.

**Sort Fields By**

Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009715841-Custom-Sort) dialog to specify how to sort data in the banded object.

## Group

Specifies the fields to group the data.

![Insert Banded Object dialog - Group](https://devnet.logianalytics.com/hc/article_attachments/4412139502871/insrtbd_grp.gif)

**Resources**

Displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) you can use to group the data in the banded object.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)

Sorts the group objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)

Launches the search bar to search for group objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)

Adds the selected group object as a group-by field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)

Removes the selected group object.

**Field**

Lists all the group objects that have been added as the group-by fields.

**Sort**

Specifies the sort order for groups at the specific group level.

* **Ascend**  
   Groups will be sorted in an ascending order (A, B, C).
* **Descend**  
   Groups will be sorted in a descending order (C, B, A).
* **No Sort**  
   Groups will be sorted in the original order in database.
* **Custom Sort**  
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009715841-Custom-Sort) dialog to set how groups will be sorted.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)

Moves the selected group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)

Moves the selected group one step down.

## Summary

Specifies the fields on which to create summaries.

![Insert Banded Object dialog - Summary](https://devnet.logianalytics.com/hc/article_attachments/4412112508055/insrtbd_sum.gif)

**Resources**

Displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4412131382167/btn_bvaggrgtn.gif) you can use to create summaries in the banded object.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)

Sorts the aggregation objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view objects are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)

Launches the search bar to search for aggregation objects. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)

Adds the selected aggregation object as the summary field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4412112506519/btn_rmvitem.gif)

Removes the selected aggregation object.

**Field**

Lists the groups that have been added in the banded object and the aggregation objects added to summarize data in each group.

**Row**

Specifies to put the summary field in the header or footer row. If the summary is calculated on a group-by field, it will be put in the group header or footer of the corresponding group; if the summary is calculated on the banded object, it will be put in the banded header or footer.

**Column**

Works together with the Row option to specify the location where a summary will be placed.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)

Moves the selected aggregation object one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)

Moves the selected aggregation object one step down.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009716561-Insert-Banded-Group)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009690342-Insert-Chart)
