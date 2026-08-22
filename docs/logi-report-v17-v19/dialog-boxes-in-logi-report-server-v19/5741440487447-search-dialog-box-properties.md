---
title: "Search Dialog Box Properties"
id: 5741440487447
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741440487447-Search-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:31Z
---

# Search Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741412182935-Save-Report-Template-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties)

# Search Dialog Box Properties

You can use the Search dialog box to [find specific text in a report](https://devnet.logianalytics.com/hc/en-us/articles/5741483083159-Searching-for-Text-in-Page-Report). This topic describes the properties in the dialog box.

![Search dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905660688407/search.gif)

You can find the contents in two places - in the values of a certain field, or in the report contents.

* To find a certain field value, select the field from the **Select Field** list, select a range in the **Value Range** list, and then select the value from the **Value** list.
* To find text in the report contents, select **Search in Whole Report**, and then type the search content in the **Value** box.

**Select Field**

Select the field among whose values you want to find the text. Server disables this property when you select **Search in Whole Report**.

**Value Range**

Select the range of the values so that you can select a required value quickly from the Value field. Server disables this property when you select **Search in Whole Report**.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If **ALL** is the Value Range, the only item in the **Value** list is **ALL**, and you cannot change the value. In this case, when you submit the search, Logi Report searches all the values of the selected field.

**Value**

Specify the text you want to find. You can select a value from the list when you do not select **Search in Whole Report**.

**Search in Whole Report**

Select if you want to find text in the report contents. Then, Server disables the **Select Field** and **Value Range** properties.

**Match Case**

Select to search for text that meets the case of the typed text.

**Find Whole Word**

Select to search for text that looks the same as the typed text.

**Highlight All**

Select to highlight all matched text.

**Direction**

Specify the searching direction.

* **Up**  
   Select to search from the last found string to the beginning of the report.
* **Down**  
   Select to search from the last found string to the end of the report.

**Search**

Select to find the next match of the specified text.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741412182935-Save-Report-Template-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties)
