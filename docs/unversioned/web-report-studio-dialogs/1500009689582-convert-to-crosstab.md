---
title: "Convert to Crosstab"
id: 1500009689582
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009689582-Convert-to-Crosstab
updated_at: 2021-11-03T06:57:29Z
---

# Convert to Crosstab

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009689562-Convert-to-Chart)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009689602-Convert-to-Table)

# Convert to Crosstab

The Convert to Crosstab dialog helps you to convert a table or chart to a crosstab. This dialog appears when you focus on a table or a chart and then select ![Convert to Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4412139487639/btn_wbrpt_2crstb.gif) on the visualization toolbar but the data fields in the table or chart are not enough for a crosstab.

![Convert to Crosstab dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112499863/cnvtcrstb.gif)

**Crosstab Title**

Specifies a title for the crosstab.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4412131381399/btn_wbrpt_font.gif)

Specifies the font properties of the crosstab title.

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
* **OK**  
   Applies the changes.
* **Cancel**  
   Cancels the changes.

**Data Source**

Specifies a business view on which the crosstab will be built from the Data Source drop-down list.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009716841-Query-Filter) dialog to specify the filter which you want to apply to the selected business view.

**Resources**

Displays the elements in the selected business view.

**Show All Fields/Show Used Fields**

Specifies to show all the business view elements or only the ones used in the current data component in the Resources box. Not available when you select another business view to convert to crosstab with.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

* **Predefined Order**  
   Sorts the view elements in the order defined in the Business View Editor on Logi JReport Designer.
* **Resource Types**  
   Sorts the view elements by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
   Sorts the view elements in alphabetical order. Elements that are not in any category will be sorted first, then the categories, and the elements in each category will also be sorted alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)

Launches the search bar to search for view elements. For the usage of the search bar, see [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource#Search).

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4412131391639/btn_additem.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) to be displayed in the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4412131392151/btn_addrow.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) to be displayed in the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4412112504343/btn_addsum.gif)

Adds the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4412131382167/btn_bvaggrgtn.gif) or detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4412139491991/btn_bvdtl.gif) to be the summary field of the crosstab.

**Columns/Rows**

* **Field**  
   Lists the group objects that will be displayed in the columns/rows of the crosstab.
* **Label**  
   Specifies the text of the labels for the column/row headers. You can select the text boxes to edit the label text, or check the Auto Map Field Name checkboxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Sort**  
   Specifies the sort order of the group objects.

**Summaries**

* **Field**  
   Lists the objects that you select to create summaries.
* **Label**  
   Specifies the text of the labels for the summaries. You can select the text boxes to edit the label text, or check the Auto Map Field Name checkboxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Aggregate**  
   Specifies the functions used to summarize data of the selected detail objects.
* **Distinct On**  
  Available and should be set when DistinctSum is selected as the aggregate function. It specifies the detail objects according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4412112493207/btn_chsr.gif) in the text box to select the detail objects in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009716981-Select-Fields) dialog.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009715701-Comparison-Function) dialog to add a comparison function as an aggregate for the crosstab.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif)

Moves the selected view element one level up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif)

Moves the selected view element one level down.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4412112484759/btn_delete.gif)

Removes the selected resource.

**OK**

Converts to the specified crosstab and closes the dialog.

**Cancel**

Cancels the conversion and closes the dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009689562-Convert-to-Chart)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009689602-Convert-to-Table)
