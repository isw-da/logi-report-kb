---
title: "Select Resource"
id: 1500009672521
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009672521-Select-Resource
updated_at: 2021-07-24T20:54:22Z
---

# Select Resource

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672501-Select-Field)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009672561-Select-Value)

# Select Resource

The Select Resource dialog appears when you select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385815/btn_chsr.gif) in the [Add Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009671461-Add-Aggregation) dialog. It helps you to specify the field on which the dynamic aggregation will be based. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920512663/slctrsc.gif)

In this dialog, all the group objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) and detail objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif) in the current business view and the dynamic formulas ![](https://devnet.logianalytics.com/hc/article_attachments/4404926707351/btn_wbrpt_dynfml.gif) that have been created in the report will be listed. Select the required field and then select **OK**.

Note that a dynamic formula that is used as an aggregation cannot be applied as the mapping field of a dynamic aggregation.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

* **Predefined Order**  
   Sorts the view elements in the order defined in the Business View Editor on Logi JReport Designer.
* **Resource Types**  
   Sorts the view elements by resource type, namely category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
   Sorts the view elements in alphabetical order. Elements that are not in any category will be sorted first, then the categories, and the elements in each category will also be sorted alphabetically.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif)

Launches the quick search toolbar to search for view elements.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920384023/btn_srchtlbr.gif)

* **Text box**  
   The quick search toolbar treats view element names as strings and searches by consecutive text. Type in the text you want to search for in the text box and the view elements containing the matched text will be listed.
* **X**  
   Closes the quick search toolbar.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920384279/btn_srchtlbr_adv.gif)  
   Lists more search options.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920384535/btn_srchtlbr_prv.gif)  
   When Highlight All is selected, you can use this button to go to the previous matched text.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404920384791/btn_srchtlbr_nxt.gif)  
   When Highlight All is selected, you can use this button to go to the next matched text.

**OK**

Selects the field and closes this dialog.

**Cancel**

Cancels the selection of a field and closes the dialog.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920501783/btn_help.gif)

Displays the help document about this feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926700311/btn_close.gif)

Ignores the setting and closes this dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672501-Select-Field)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009672561-Select-Value)
