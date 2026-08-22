---
title: "Convert to Crosstab"
id: 1500009748161
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748161-Convert-to-Crosstab
updated_at: 2021-07-25T07:19:28Z
---

# Convert to Crosstab

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748141-Convert-to-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721382-Convert-to-Table)

# Convert to Crosstab

The Convert to Crosstab dialog box is used to convert a table or chart to a crosstab. It appears when you focus on a table or a chart and then select ![Convert to Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404936721559/btn_wbrpt_2crstb.gif) on the visualization toolbar but the data fields in the table or chart are not enough for a crosstab.

![Convert to Crosstab dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942458775/cnvtcrstb.gif)

**Crosstab Title**

Specifies a title for the crosstab.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif)

Specifies the font properties of the crosstab title. After you select the button, Report Server displays the following dialog box for you to edit the font properties:

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

Specifies a business view on which the crosstab will be built from the Data Source drop-down list.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009722162-Query-Filter) dialog box to specify the filter which you want to apply to the selected business view.

**Resources**

Displays the elements in the selected business view.

**Show All Fields/Show Used Fields**

Specifies to show all the business view elements or only the ones used in the current data component in the Resources box. Not available when you select another business view to convert to crosstab with.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936713367/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

* **Predefined Order**  
  Sorts the view elements in the order defined in the Business View Editor on Logi Report Designer.
* **Resource Types**  
  Sorts the view elements by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Sorts the view elements in alphabetical order. Elements that are not in any category will be sorted first, then the categories, and the elements in each category will also be sorted alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif)

Launches the search bar to search for view elements.

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

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) to be displayed in the columns of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404936739735/btn_addrow.gif)

Adds the selected group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) to be displayed in the rows of the crosstab.

![](https://devnet.logianalytics.com/hc/article_attachments/4404942464023/btn_addsum.gif)

Adds the selected aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) or detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) to be the summary field of the crosstab.

**Columns/Rows**

* **Field**  
   Lists the group objects that will be displayed in the columns/rows of the crosstab.
* **Label**  
   Specifies the text of the labels for the column/row headers. You can select the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Sort**  
   Specifies the sort order of the group objects.

**Summaries**

* **Field**  
   Lists the objects that you select to create summaries.
* **Label**  
   Specifies the text of the labels for the summaries. You can select the text boxes to edit the label text, or select the Auto Map Field Name check boxes beside the text boxes to automatically map the label text to the dynamic display names of the objects.
* **Aggregate**  
   Specifies the functions used to summarize data of the selected detail objects.
* **Distinct On**  
  Available and should be set when DistinctSum is selected as the aggregate function. It specifies the detail objects according to whose unique values to calculate DistinctSum. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) in the text box to select the detail objects in the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009749361-Select-Fields) dialog box.
* **Comparison Function**  
   Opens the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009721362-Comparison-Function) dialog box to add a comparison function as an aggregate for the crosstab.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif)

Moves the selected view element one level up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif)

Moves the selected view element one level down.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif)

Removes the selected resource.

**OK**

Converts to the specified crosstab and closes the dialog box.

**Cancel**

Cancels the conversion and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748141-Convert-to-Chart)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721382-Convert-to-Table)
