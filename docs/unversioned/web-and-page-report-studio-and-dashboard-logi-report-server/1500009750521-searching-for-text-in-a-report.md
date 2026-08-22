---
title: "Searching for Text in a Report"
id: 1500009750521
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750521-Searching-for-Text-in-a-Report
updated_at: 2021-07-25T07:18:52Z
---

# Searching for Text in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723482-Sorting-Report-Data)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723462-Saving-the-Report)

# Searching for Text in a Report

You can use the [Search](https://devnet.logianalytics.com/hc/en-us/articles/1500009746241-Search) dialog box to find text in the values of a certain field or in the whole report content. To show this dialog box, select **Menu > Edit** > **Search**, select the **Search** button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936772759/btn_pgrpt_find.gif) on the toolbar, or right-click a field value or label (or object such as text box) and select **Search** on the shortcut menu.

![Search dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942489367/search.gif)

**To find text in the values of a particular field:**

1. Make sure the Search in Whole Report option in the Search dialog box is NOT selected.
2. Select the field from the Select Field drop-down list.
3. Set the range with which to search for the value from the Value Range drop-down list.
4. Select the field value you want to search for from the Value drop-down list.
5. Specify whether or not to match case, whether or not to match whole word, whether or not to highlight all the matching values and the searching direction.
6. Select the **Search** button.

**To find text in the report content:**

1. In the Search dialog box, select the **Search in Whole Report** check box.
2. Type the string you want to search for in the Value box.
3. Set the other options such as the searching direction.
4. Select the **Search** button.

**Notes:**

* Finding text in the values of a particular field is not supported on crosstabs and charts.
* If you select Highlight All in the Search dialog box, to clear the highlighting in the search result, clear the option and submit the search again, or refresh the report.
* If you have not selected the Search in Whole Report option, you will not be able to search special fields for strings.
* When All is selected in the Value Range drop-down list, the only item in the Value drop-down list will be All and cannot be changed. In this case when you submit the search, Page Report Studio will search for all the values of the selected field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723482-Sorting-Report-Data)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723462-Saving-the-Report)
