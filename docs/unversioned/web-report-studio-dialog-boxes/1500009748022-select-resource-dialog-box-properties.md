---
title: "Select Resource Dialog Box Properties"
id: 1500009748022
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748022-Select-Resource-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:11Z
---

# Select Resource Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776261-Select-Fields-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776301-Select-Value-Dialog-Box-Properties)

# Select Resource Dialog Box Properties

This topic describes how you can use the Select Resource dialog box to select the field on which you want to base a [dynamic aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009750082-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-#Agg). Server displays the dialog box when you select ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404885320983/btn_chsr.gif) in the [Add Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009746682-Add-Aggregation-Dialog-Box-Properties) dialog box.

![Select Resource dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880336535/slctrsc.gif)

In this dialog box, Server lists all the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) and detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) in the current business view and the dynamic formulas ![Dynamic Formula](https://devnet.logianalytics.com/hc/article_attachments/4404880337559/btn_wbrpt_dynfml.gif) that you have created in the report. Select the required field and then select **OK**.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)You cannot apply a dynamic formula that you used as an aggregation, as the mapping field of a dynamic aggregation.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

* **Predefined Order**  
  Select if you want to sort the view elements in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the view elements by resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the view elements in alphabetical order. Logi Report sorts the elements that are not in any category first, and then the categories. It also sorts the elements in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the search bar to search for view elements.

See the following options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **X**  
  Select to close the search bar or clear the typed text.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
  When you selected **Highlight All**, you can use this button to go to the previous matched text.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
   When you selected **Highlight All**, you can use this button to go to the next matched text.

**OK**

Selects the field and closes this dialog box.

**Cancel**

Cancels the selection of a field and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776261-Select-Fields-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776301-Select-Value-Dialog-Box-Properties)
