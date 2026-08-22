---
title: "Select Resource"
id: 1500009722242
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722242-Select-Resource
updated_at: 2021-07-25T07:19:11Z
---

# Select Resource

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749361-Select-Fields)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722282-Select-Value)

# Select Resource

The Select Resource dialog box is used to specify the field on which a [dynamic aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-#Agg) will be based. It appears when you select ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) in the [Add Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009721182-Add-Aggregation) dialog box.

![Select Resource dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942524823/slctrsc.gif)

In this dialog box, all the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) and detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) in the current business view and the dynamic formulas ![Dynamic Formula](https://devnet.logianalytics.com/hc/article_attachments/4404936827543/btn_wbrpt_dynfml.gif) that have been created in the report will be listed. Select the required field and then select **OK**.

Note that a dynamic formula that is used as an aggregation cannot be applied as the mapping field of a dynamic aggregation.

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

**OK**

Selects the field and closes this dialog box.

**Cancel**

Cancels the selection of a field and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749361-Select-Fields)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722282-Select-Value)
