---
title: "Searching for Text in Page Report"
id: 4405683961623
section: "Page Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683961623-Searching-for-Text-in-Page-Report
updated_at: 2022-01-27T07:59:44Z
---

# Searching for Text in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690652311-Sorting-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690651415-Saving-a-Page-Report)

# Searching for Text in Page Report

You can use the [Search](https://devnet.logianalytics.com/hc/en-us/articles/4405683678615-Search-Dialog-Box-Properties) dialog box to find text in the values of a certain field or in the whole report content. This topic describes how you can search for text in Page Report.

To show the Search dialog box, select **Menu > Edit** > **Search**, select the **Search** button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420447141015/btn_pgrpt_find.gif) on the toolbar, or right-click a field value or label (or object such as text box) and select **Search** on the shortcut menu.

![Search dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453484695/search.gif)

**To find text in the values of a particular field:**

1. DO NOT select the **Search in Whole Report** option in the Search dialog box.
2. Select a field from the **Select Field** drop-down list.
3. Set the range with which to search for the value from the **Value Range** drop-down list.
4. Select the field value you want to search for from the **Value** drop-down list.
5. Specify whether to match case, match whole word, and highlight all the matching values, and select the searching direction.
6. Select the **Search** button.

**To find text in the report content:**

1. In the Search dialog box, select **Search in Whole Report**.
2. Type the string you want to search for in the **Value** box.
3. Set the other options such as the searching direction.
4. Select the **Search** button.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* Finding text in the values of a particular field is not supported on crosstabs and charts.
* If you select **Highlight All** in the Search dialog box, to clear the highlighting in the search result, clear the option and submit the search again, or refresh the report.
* If you have not selected the **Search in Whole Report** option, you cannot search special fields for strings.
* When you select **All** in the Value Range drop-down list, the only item in the Value drop-down list is **All** and you cannot change it. In this case when you submit the search, Page Report Studio searches for all the values of the selected field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690652311-Sorting-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690651415-Saving-a-Page-Report)
