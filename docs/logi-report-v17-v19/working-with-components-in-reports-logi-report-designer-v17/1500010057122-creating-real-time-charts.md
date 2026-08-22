---
title: "Creating Real Time Charts"
id: 1500010057122
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057122-Creating-Real-Time-Charts
updated_at: 2021-07-23T19:14:43Z
---

# Creating Real Time Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057142-Creating-Scrollable-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057082-Creating-Motion-Charts)

# Creating Real Time Charts

This topic introduces the characteristics of real time charts and how you can create a real time chart.

This topic contains the following sections:

* [What Are Real Time Charts?](#What)
* [Creating a Real Time Chart](#Create)

## What Are Real Time Charts?

A real time chart can update automatically at runtime by using data that changes rapidly with time such as stock market quotes. When the data in the data source that a real time chart uses is updated in real time, the chart automatically fetches data from the data source to update itself with the specified interval. The report users can then conveniently see the real time data information without updating the chart by themselves and without having to re-fetch all of the data. Logi Report only selects the new data since the last interval from the data source.

Before you create a real time chart, you have to make sure the data source you use contains real time data which can be updated periodically; otherwise, the chart loses its real time functionality.

Real time charts can only be of the Bar, Bench, Line, and Area types, and you can use them in web reports and library components only.

## Creating a Real Time Chart

1. Position the mouse pointer at the destination in the web report or a library component where you want to insert the chart.
2. Do either of the following:
   * From the **Components** panel, drag a chart icon in the Visual category to the destination.
   * Select **Insert** > **Chart** or **Home** > **Insert** > **Chart**.

   Designer displays the [Create Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010095861-Create-Chart-Dialog-Box#BV) wizard.
3. In the **Data** screen, select a business view in the current catalog using which to create the chart.

   ![Create Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/4404848612119/crtcht_dt_bv.gif)
4. In the **Type** screen, specify the type of the chart which can only be single chart of the Bar, Bench, Line, or Area type.

   ![Create Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/4404856996119/crtcht_type_bv.gif)
5. In the **Display** screen, specify a title for the chart in the **Title** text box. Select the **Real Time** checkbox.

   ![Define Real Time Chart](https://devnet.logianalytics.com/hc/article_attachments/4404857056663/cmpnt_cht_rltm.gif)
6. By default, Designer selects the **Use System Time for Category** checkbox and you can see the text **Use System Refresh Time** in the **Category** box, which means Designer usea the time at which the chart refreshes itself as the category value. You can clear Use System Time for Category and choose a group object ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404848663831/bv_grp.gif) or detail object ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664087/bv_detail.gif) in the specified business view, or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404857035543/bv_dynfmla_grp.gif) or dynamic formula used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664343/bv_dynfmla_dtl.gif) that you have created for the business view in the current report to display on the category axis, and define the [Order/Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500010094661-Modifying-Charts#SelectN) on it.
7. In the **Show Values** box, add the group objects and detail objects that are of the Numeric type to display on the value axis.

   You can only use group objects and details objects of the Numeric type on the value axis of a real time chart. If you add objects of other types to the Show Values box, Designer automatically clears the Real Time checkbox.
8. Specify the time interval at which the chart gets data and refreshes itself automatically in the **Refresh Interval** text box.
9. Specify the most recent N records you want to keep for the real time data in the **Show Most Recent** text box.
10. Select the **Incremental Fetch** button to add the fields as the unique key of the real time chart in the [Unique Key dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099121-Unique-Key-Dialog-Box), which guarantees there are no two records with the same unique key value in the chart.

    ![Unique Key dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848442519/unqkey.gif)

    Once you define a unique key, each time when the chart automatically updates itself, Logi Report filters the data that has the same unique key value as the previously loaded data records and only adds data with different unique key value to the chart. For instance, if you add the fields **Country** and **Product ID** as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, Logi Report adds no more records of this product ID in USA to the real time chart because they have the same unique key value. The most common usage is with a time field, so that when a time is part of the unique key, the data in the chart will be updated each time new records are added to the database with more recent times.
11. In the **Filter** screen, apply a filter to reduce the data to display in the chart. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the **Filter** drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

    ![Create Chart - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848612887/crtcht_fltr_bv.gif)
12. In the **Layout** screen, specify the [layout](https://devnet.logianalytics.com/hc/en-us/articles/1500010057042-Inserting-Charts-in-a-Report#Layout) of the chart.

    ![Create Chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404856997143/crtcht_layout.gif)
13. In the **Style** screen, select a style for the chart.

    ![Create Chart - Style](https://devnet.logianalytics.com/hc/article_attachments/4404856997399/crtcht_sty.gif)
14. Select **Finish** to create the chart.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057142-Creating-Scrollable-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057082-Creating-Motion-Charts)
