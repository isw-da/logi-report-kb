---
title: "Select Resource"
id: 1500009690702
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009690702-Select-Resource
updated_at: 2021-11-03T06:57:08Z
---

# Select Resource

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009716981-Select-Fields)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717001-Select-Value)

# Select Resource

The Select Resource dialog helps you to specify the field on which the dynamic aggregation will be based. This dialog appears when you select ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4412112493207/btn_chsr.gif) in the [Add Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009689382-Add-Aggregation) dialog.

![Select Resource dialog](https://devnet.logianalytics.com/hc/article_attachments/4412139542935/slctrsc.gif)

In this dialog, all the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4412112493463/btn_bvgrp.gif) and detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4412139491991/btn_bvdtl.gif) in the current business view and the dynamic formulas ![Dynamic Formula](https://devnet.logianalytics.com/hc/article_attachments/4412112580503/btn_wbrpt_dynfml.gif) that have been created in the report will be listed. Select the required field and then select **OK**.

Note that a dynamic formula that is used as an aggregation cannot be applied as the mapping field of a dynamic aggregation.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

* **Predefined Order**  
   Sorts the view elements in the order defined in the Business View Editor on Logi JReport Designer.
* **Resource Types**  
   Sorts the view elements by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
   Sorts the view elements in alphabetical order. Elements that are not in any category will be sorted first, then the categories, and the elements in each category will also be sorted alphabetically.

**Search**

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif)

Launches the search bar to search for view elements.

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4412139498519/btn_srchtlbr.gif)

* **Text box**  
   Type in the text you want to search for and the view elements containing the matched text will be listed.
* **X**  
   Closes the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4412112501655/btn_srchtlbr_adv.gif)  
   Lists more search options.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
* ![Previous button](https://devnet.logianalytics.com/hc/article_attachments/4412139498775/btn_srchtlbr_prv.gif)  
   When Highlight All is selected, you can use this button to go to the previous matched text.
* ![Next button](https://devnet.logianalytics.com/hc/article_attachments/4412139499031/btn_srchtlbr_nxt.gif)  
   When Highlight All is selected, you can use this button to go to the next matched text.

**OK**

Selects the field and closes this dialog.

**Cancel**

Cancels the selection of a field and closes the dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009716981-Select-Fields)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717001-Select-Value)
