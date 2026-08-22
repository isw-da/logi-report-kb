---
title: "Searching for Text in a Report"
id: 1500009674021
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674021-Searching-for-Text-in-a-Report
updated_at: 2021-07-24T20:53:53Z
---

# Searching for Text in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674001-Sorting-Report-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673981-Saving-the-Report)

# Searching for Text in a Report

You can use the [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009669981-Search) dialog to find text in the values of a certain field or in the whole report content. To show this dialog, select **Menu > Edit** > **Search**, select the **Search** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926666519/btn_pgrpt_find.gif) on the toolbar, or right-click a field value or label (or object such as text box) and select **Search** on the shortcut menu.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920450327/search.gif)

* **To find text in the values of a particular field:**
  1. Make sure the Search in Whole Report option in the Search dialog is NOT checked.
  2. Select the field from the Select Field drop-down list.
  3. Set the range with which to search for the value from the Value Range drop-down list.
  4. Select the field value you want to search for from the Value drop-down list.
  5. Specify whether or not to match case, whether or not to match whole word, whether or not to highlight all the matching values and the searching direction.
  6. Select the **Search** button.
* **To find text in the report content:**
  1. In the Search dialog, check the **Search in Whole Report** checkbox.
  2. Type the string you want to search for in the Value box.
  3. Set the other options such as the searching direction.
  4. Select the **Search** button.

**Notes:**

* Finding text in the values of a particular field is not supported on crosstabs and charts.
* If you check Highlight All in the Search dialog, to clear the highlighting in the search result, uncheck the option and submit the search again, or refresh the report.
* If you have not selected the Search in Whole Report option, you will not be able to search special fields for strings.
* When All is selected in the Value Range drop-down list, the only item in the Value drop-down list will be All and cannot be changed. In this case when you submit the search, Logi JReport will search for all the values of the selected field.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674001-Sorting-Report-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673981-Saving-the-Report)
