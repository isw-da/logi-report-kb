---
title: "Creating a Real Time Chart"
id: 1500009583761
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583761-Creating-a-Real-Time-Chart
updated_at: 2021-07-24T05:56:04Z
---

# Creating a Real Time Chart

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583781-Creating-a-Scrollable-Chart)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563262-Creating-a-Motion-Chart)

# Creating a Real Time Chart

A real time chart can be updated automatically at runtime by using data that changes rapidly with time such as stock market quotes. After you create a real time chart, when the data in the data source the chart uses is updated in real time, the chart will automatically fetch data from the data source to update itself with the interval you specify. Then, you will conveniently see the real time data information without updating the chart by yourself and without having to re-fetch all of the data. Only the new data since the last interval is selected by the query.

Before you create a real time chart, you have to make sure the data source you use contains real time data which can be updated periodically. Otherwise, the chart will lose its real time meaning.

Currently, real time charts are supported on web reports and library components only.

**To insert a real time chart into a web report or a library component:**

1. Position the mouse pointer at the destination where you want to insert the chart.
2. Do one of the following to open the [Create Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009564882-Create-Chart-Dialog-Business-View-Based-) wizard:
   * Drag the corresponding button of the chart type you want to insert from the Components panel to the destination.
   * Select **Insert** > **Chart** or **Home** > **Insert** > **Chart**.
3. In the Data screen of the wizard, select a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) in the current catalog on which the chart will be created.
4. In the Type screen, specify the type of the chart which can only be single chart of bar, bench, line, or area type.
5. In the Display screen, specify a title for the chart in the Title text field. Check the **Real Time** checkbox.

   ![Create Chart wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404893942679/crtcht_dsply_wb.gif)
6. By default, Use System Time for Category is checked and you can see the text Use System Refresh Time is displayed in the category box, which means the time at which the chart refreshes itself will be used as the category value. You can uncheck the Use System Time for Category option and add another field to be displayed on the category (X) axis, and define the [Order/Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009583701-Modifying-a-Chart#SelectN) on the field if required. Then, add the fields of numeric type which cannot be summary fields to the value box.
7. Specify the time interval at which the chart will get data and refresh itself automatically in the Refresh Interval text field.
8. Specify the most recent N records to be kept for the real time data on the chart in the Show Most Recent text field.
9. Select the **Incremental Fetch** button to add the fields you want to use as the unique key of the real time chart in the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009567822-Unique-Key-dialog-Dialog) dialog.

   ![Unique Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893845527/unqkey.gif)

   Once a unique key is defined, each time when the real time chart automatically updates itself, duplicate data records will be filtered out based on the unique key. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, no more records of this product ID in USA will be added to the real time chart because they have the same unique key value. Normally the unique key will include a time value so that new data is always fetched containing the new key.
10. In the Filter screen, select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters) of the specified business view if there is from the Filter drop-down list to apply, or select **User Defined** in the list to define a new filter. For how to define a filter, refer to [Filtering the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).
11. In the Layout screen, specify the layout of the chart.
12. In the Style screen, select a style for the chart.
13. Select **Finish** to create the chart.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583781-Creating-a-Scrollable-Chart)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563262-Creating-a-Motion-Chart)
