---
title: "Search Dialog Box Properties"
id: 1500009772981
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772981-Search-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:05Z
---

# Search Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745122-Save-Report-Template-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties)

# Search Dialog Box Properties

You can use the Search dialog box to [find specific text in a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009777641-Searching-for-Text-in-Page-Report). This topic describes the options in the dialog box.

![Search dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885384343/search.gif)

You can find the content in two places - in the values of a certain field, or in the report content.

* To find a certain field value, select the field from the Select Field drop-down list, define the value range in the Value Range drop-down list and then select the value from the Value drop-down list.
* To find text in the report content, select the **Search in Whole Report**  check box, type the search content in the Value box.

**Select Field**

* Specifies the field in which you want to find the text. Server disables this option when you select **Search in Whole Report**.

**Value Range**

Specifies the range of the displayed values so that you can select a required value quickly from the Value field. Server disables this option when you select **Search in Whole Report**.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If **All** is the Value Range, the only item in the **Value** drop-down list is **All**, and you cannot change the value. In this case, when you submit the search, Logi Report searches all the values of the selected field.

**Value**

Specifies the text you want to find. You can select a value from the drop-down list when you do not select **Search in Whole Report**.

**Search in Whole Report**

Finds text in the report content. When you select this option, Server disables the **Select Field** drop-down list and the **Value Range** drop-down list.

**Match Case**

Finds text only if it matches the capitalization of the text you have typed.

**Find Whole Word**

Finds text only if it matches a whole word.

**Highlight All**

Highlights all the matching text.

**Direction**

Specifies the searching direction.

* **Up**  
   Searches from the last found string to the beginning of the report.
* **Down**  
   Searches from the last found string to the end of the report. This option is selected by default.

**Search**

Searches the report or field value for the next match of the specified text.

**Cancel**

Cancels the operation and closes this dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745122-Save-Report-Template-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties)
