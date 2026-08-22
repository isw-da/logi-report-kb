---
title: "Searching for Text in Page Report"
id: 1500009777641
section: "Editing Page Reports in Page Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777641-Searching-for-Text-in-Page-Report
updated_at: 2021-07-24T00:47:50Z
---

# Searching for Text in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777621-Sorting-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777601-Saving-a-Page-Report)

# Searching for Text in Page Report

You can use the [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009772981-Search-Dialog-Box-Properties) dialog box to find text in the values of a certain field or in the whole report content. This topic describes how you can search for text in Page Report.

To show the Search dialog box, select **Menu > Edit** > **Search**, select the **Search** button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404885378711/btn_pgrpt_find.gif) on the toolbar, or right-click a field value or label (or object such as text box) and select **Search** on the shortcut menu.

![Search dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885384343/search.gif)

**To find text in the values of a particular field:**

1. DO NOT select the **Search in Whole Report** option in the Search dialog box.
2. Select a field from the **Select Field** drop-down list.
3. Set the range with which to search for the value from the **Value Range** drop-down list.
4. Select the field value you want to search for from the **Value** drop-down list.
5. Specify whether to match case, match whole word, and highlight all the matching values, and select the searching direction.
6. Select the **Search** button.

**To find text in the report content:**

1. In the Search dialog box, select the **Search in Whole Report** check box.
2. Type the string you want to search for in the **Value** box.
3. Set the other options such as the searching direction.
4. Select the **Search** button.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* Finding text in the values of a particular field is not supported on crosstabs and charts.
* If you select **Highlight All** in the Search dialog box, to clear the highlighting in the search result, clear the option and submit the search again, or refresh the report.
* If you have not selected the **Search in Whole Report** option, you cannot search special fields for strings.
* When you select **All** in the Value Range drop-down list, the only item in the Value drop-down list is **All** and you cannot change it. In this case when you submit the search, Page Report Studio searches for all the values of the selected field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777621-Sorting-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777601-Saving-a-Page-Report)
