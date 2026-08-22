---
title: "Insert Banded Object"
id: 1500009748901
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748901-Insert-Banded-Object
updated_at: 2021-07-25T07:19:17Z
---

# Insert Banded Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748921-Insert-Banded-Group)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748941-Insert-Chart)

# Insert Banded Object

The Insert Banded Object dialog box is used to [insert a banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Banded) to a report. It appears when you drag Banded from the Components panel to the destination.

There are the following tabs in this dialog box: [Details](#Details), [Group](#Group) and [Summary](#Summary).

**Banded Title**

Specifies a title for the banded object.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif)

Specifies the font properties for title of the banded object. After you select the button, Report Server displays the following dialog box for you to edit the font properties:

![](https://devnet.logianalytics.com/hc/article_attachments/4404936817047/fontprpty.gif "Font Properties")

* **Font**  
  Specifies the font face of the title.
* **Font Style**   
  Specifies the font style of the title. It can be one of the following: regular, bold, italic, and bold italic.
* **Size**  
  Specifies the font size of the title.
* **Align**  
  Specifies the position of the title to be left, right, center, or justify.
* **Font Color**  
  Specifies the font color of the title.
* **Background Color**  
  Specifies the background color of the title.

  To specify a color, click the color image to select a color from the color palette, or select **More Colors** in the color palette to select a color using the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog.
* **OK**  
  Accepts the color settings and closes the dialog.
* **Cancel**  
  Cancels editing the color and closes the dialog

**Data Source**

Specifies the business view in the current catalog on which the banded object will be built.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009722162-Query-Filter) dialog box to specify the filter which you want to apply to the selected business view.

**OK**

Inserts a banded object and closes the dialog box.

**Cancel**

Cancels the insertion and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

## Details

Specifies the detail fields that you want to display in the banded object.

![Insert Banded Object dialog - Details](https://devnet.logianalytics.com/hc/article_attachments/4404936742551/insrtbd_dtl.gif)

**Resources**

Displays all the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) and detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) in the selected business view.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936713367/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

The order can be one of the following:

* **Predefined Order**  
  Sorts the view elements in the order defined in the Business View Editor on Logi Report Designer.
* **Resource Types**  
  Sorts the view elements by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Sorts the view elements in alphabetical order. Elements that are not in any category will be sorted first, then the categories, and the elements in each category will also be sorted alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif)

Launches the search bar to search for objects.

The following shows the options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404936734231/btn_srchtlbr.gif)

* **Text box**  
  Type in the text you want to search in the text box and the values containing the matched text will be listed.
* **X**  
  Closes the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404942460951/btn_srchtlbr_adv.gif)  
  Lists more search options.
  + **Highlight All**   
    Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Specifies whether to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404936734487/btn_srchtlbr_prv.gif)  
  When Highlight All is selected, you can use this button to go to the previous matched text.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404936734743/btn_srchtlbr_nxt.gif)  
   When Highlight All is selected, you can use this button to go to the next matched text.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif)

Adds the selected object to be displayed in the banded object.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936742039/btn_rmvitem.gif)

Removes the selected object that is added.

**Field**

Lists the group and detail objects that have been added to the banded object as the detail fields.

**Label**

Specifies the text for the labels of the detail fields, which by default are the display names of the added objects. You can select in the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif)

Moves the selected object one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif)

Moves the selected object one step down.

**Sort Fields By**

Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009748201-Custom-Sort) dialog box to specify how to sort data in the banded object.

## Group

Specifies the fields to group the data.

![Insert Banded Object dialog - Group](https://devnet.logianalytics.com/hc/article_attachments/4404942464791/insrtbd_grp.gif)

**Resources**

Displays all the available group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) you can use to group the data in the banded object.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936713367/btn_sort.gif)

Sorts the group objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif)

Launches the [search bar](#Search) to search for group objects.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif)

Adds the selected group object as a group-by field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936742039/btn_rmvitem.gif)

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
   Opens the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009748201-Custom-Sort) dialog box to set how groups will be sorted.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif)

Moves the selected group one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif)

Moves the selected group one step down.

## Summary

Specifies the fields on which to create summaries.

![Insert Banded Object dialog - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404936742807/insrtbd_sum.gif)

**Resources**

Displays all the available aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) you can use to create summaries in the banded object.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936713367/btn_sort.gif)

Sorts the aggregation objects in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif)

Launches the [search bar](#Search) to search for aggregation objects.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif)

Adds the selected aggregation object as the summary field.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936742039/btn_rmvitem.gif)

Removes the selected aggregation object.

**Field**

Lists the groups that have been added in the banded object and the aggregation objects added to summarize data in each group.

**Row**

Specifies to put the summary field in the header or footer row. If the summary is calculated on a group-by field, it will be put in the group header or footer of the corresponding group; if the summary is calculated on the banded object, it will be put in the banded header or footer.

**Column**

Works together with the Row option to specify the location where a summary will be placed.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif)

Moves the selected aggregation object one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif)

Moves the selected aggregation object one step down.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748921-Insert-Banded-Group)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748941-Insert-Chart)
