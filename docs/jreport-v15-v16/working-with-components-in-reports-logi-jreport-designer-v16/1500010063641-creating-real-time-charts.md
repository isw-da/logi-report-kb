---
title: "Creating Real Time Charts"
id: 1500010063641
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063641-Creating-Real-Time-Charts
updated_at: 2021-07-24T10:39:24Z
---

# Creating Real Time Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063661-Creating-Scrollable-Charts) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029002-Creating-Motion-Charts)

# Creating Real Time Charts

A real time chart can be updated automatically at runtime by using data that changes rapidly with time such as stock market quotes. After you create a real time chart, when the data in the data source the chart uses is updated in real time, the chart will automatically fetch data from the data source to update itself with the interval you specify. Then, you will conveniently see the real time data information without updating the chart by yourself and without having to re-fetch all of the data. Only the new data since the last interval is selected by the query.

Before you create a real time chart, you have to make sure the data source you use contains real time data which can be updated periodically. Otherwise the chart will lose its real time functionality.

Real time charts can only be of the Bar, Bench, Line and Area types and are supported in web reports and library components only.

**To create a real time chart in a web report or a library component:**

1. Position the mouse pointer at the destination in the report where you want to insert the chart.
2. Do either of the following:
   * Drag a chart button from the Visual category of the Components panel to the destination.
   * Select **Insert** > **Chart** or **Home** > **Insert** > **Chart**.

   The [Create Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010030062-Create-Chart-Dialog#BV) wizard appears, which contains a set of screens for helping you define a chart easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select a business view in the current catalog using which to create the chart.

   ![Create Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/4404909235863/crtcht_dt_bv.gif)
4. In the Type screen, specify the type of the chart which can only be single chart of the Bar, Bench, Line, or Area type.

   ![Create Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/4404901281687/crtcht_type_bv.gif)
5. In the Display screen, specify a title for the chart in the Title text box. Check the **Real Time** checkbox.

   ![Define Real Time Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901332887/cmpnt_cht_rltm.gif)
6. By default, Use System Time for Category is checked and you can see the text Use System Refresh Time is displayed in the Category box, which means the time at which the chart refreshes itself will be used as the category value. You can uncheck **Use System Time for Category** and choose a group object ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404901314071/bv_grp.gif) or detail object ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404901314327/bv_detail.gif) in the specified business view, or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404901314583/bv_dynfmla_grp.gif) or dynamic formula used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404909271703/bv_dynfmla_dtl.gif) created for the business view in the current report to display on the category axis, and define the [Order/Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500010063621-Modifying-Charts#SelectN) on it if required.
7. In the Show Values box, add the group objects and detail objects that are of Numeric type to display on the value axis.

   Only group objects and details objects of Numeric type are supported on the value axis of a real time chart. If you add objects of other types to the Show Values box, you will find that the Real Time checkbox is automatically unchecked.
8. Specify the time interval at which the chart will get data and refresh itself automatically in the Refresh Interval text box.
9. Specify the most recent N records to be kept for the real time data on the chart in the Show Most Recent text box.
10. Select the **Incremental Fetch** button to add the fields you want to use as the unique key of the real time chart in the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500010032922-Unique-Key-dialog-Dialog) dialog, which is used to guarantee there are no two records with the same unique key value in the chart.

    ![Unique Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901148055/unqkey.gif)

    Once a unique key is defined, each time when the chart automatically updates itself, the data that has the same unique key value as the previously loaded data records will be filtered and only data with different unique key value will be added to the chart. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, no more records of this product ID in USA will be added to the real time chart because they have the same unique key value. The most common usage is with a time field so when a time is part of the unique key the data in the chart will be updated each time new records are added to the database with more recent times.
11. In the Filter screen, apply a filter to reduce the data displayed in the chart. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010034562-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the Filter drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

    ![Create Chart - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404909236631/crtcht_fltr_bv.gif)
12. In the Layout screen, specify the [layout](https://devnet.logianalytics.com/hc/en-us/articles/1500010063601-Inserting-Charts-in-a-Report#Layout) of the chart.

    ![Create Chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404901282199/crtcht_layout.gif)
13. In the Style screen, select a style for the chart.

    ![Create Chart - Style](https://devnet.logianalytics.com/hc/article_attachments/4404901282583/crtcht_sty.gif)
14. Select **Finish** to create the chart.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063661-Creating-Scrollable-Charts) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029002-Creating-Motion-Charts)
