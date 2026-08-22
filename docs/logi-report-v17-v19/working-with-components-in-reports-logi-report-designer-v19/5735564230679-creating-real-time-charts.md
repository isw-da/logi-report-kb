---
title: "Creating Real Time Charts"
id: 5735564230679
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735564230679-Creating-Real-Time-Charts
updated_at: 2022-11-02T04:28:09Z
---

# Creating Real Time Charts

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735498899351-Creating-Scrollable-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527456279-Creating-Motion-Charts)

# Creating Real Time Charts

This topic introduces the characteristics of real time charts and how you can create a real time chart.

This topic contains the following sections:

* [What Are Real Time Charts?](#What)
* [Creating a Real Time Chart](#Create)

## What Are Real Time Charts?

A real time chart can update automatically at runtime by using data that changes rapidly with time such as stock market quotes. When the data in the data source that a real time chart applies is updated in real time, the chart automatically fetches data from the data source to update itself with the specified interval. Users can then conveniently see the real time data information without updating the chart by themselves and without having to refetch all of the data. Logi Report only selects the new data since the last interval from the data source.

Before you create a real time chart, you have to make sure the data source you use contains real time data which can be updated periodically; otherwise, the chart loses its real time functionality.

Real time charts can only be of the Bar, Bench, Line, and Area types, and you can use them in web reports and library components only.

## Creating a Real Time Chart

1. Position the mouse pointer at the destination in the web report or a library component where you want to insert the chart.
2. Do either of the following:
   * From the **Components** panel, drag a chart icon in the Visual category to the destination.
   * Navigate to **Insert** > **Chart** or **Home** > **Insert** > **Chart**.

   Designer displays the [Create Chart](https://devnet.logianalytics.com/hc/en-us/articles/5735565283351-Create-Chart-Dialog-Box#BV) dialog box.
3. In the **Data** screen, [specify the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC) you want to use to create the
   chart.

   ![Create Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/9898532640535/crtcht_dt_bv.gif)
4. In the **Type** screen, specify the type of the chart which can only be single chart of the Bar, Bench, Line, or Area type.

   ![Create Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/9898532645783/crtcht_type_bv.gif)
5. In the **Display** screen, specify a title for the chart in the **Title** text box. Select **Real Time**.

   ![Define Real Time Chart](https://devnet.logianalytics.com/hc/article_attachments/9898535257751/cmpnt_cht_rltm.gif)
6. By default, Designer selects **Use System Time for Category** and you can see the text **Use System Refresh Time** in the **Category** box, which means Designer usea the time at which the chart refreshes itself as the category value. You can clear Use System Time for Category and choose a group object ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898534261399/bv_grp.gif) or detail object ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/9898517937943/bv_detail.gif) in the specified business view, or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Formula) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898517940503/bv_dynfmla_grp.gif) or dynamic formula used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/9898517944087/bv_dynfmla_dtl.gif) that you have created for the business view in the current report to display on the category axis, and define the [Order/Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/5735498861207-Modifying-Charts#SelectN) on it.
7. In the **Show Values** box, add the group objects and detail objects that are Numeric data type to display on the value axis.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can only use Numeric group objects and details objects on the value axis of a real time chart. If you add objects of other data types to the Show Values box, Designer automatically clears the Real Time checkbox.
8. Specify the time interval at which the chart gets data and refreshes itself automatically in the **Refresh Interval** text box.
9. Specify the most recent N records you want to keep for the real time data in the **Show Most Recent** text box.
10. Select **Incremental Fetch** to add the fields as the unique key of the real time chart in the [Unique Key dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515926551-Unique-Key-Dialog-Box), which guarantees there are no two records with the same unique key value in the chart. Once you define a unique key, each time when the chart automatically updates itself at runtime, Logi Report Engine filters the data that has the same unique key value as the previously loaded records and only adds data with different unique key value to the chart. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, Logi Report Engine adds no more records of this product ID in USA to the real time chart because they have the same unique key value. The most common usage is with a time field, so that when a time is part of the unique key, you can find the chart updated each time new records are added to the database with more recent times.

    ![Unique Key dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898458736663/unqkey.gif)
11. In the **Dataset Filter** screen, ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")[filter the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report) the chart applies. If you have added filter conditions to the dataset somewhere else, Designer displays the conditions in the screen. You can further edit the conditions. Be aware that a filter on a dataset applies to all data components in the same report that use this dataset.

    ![Create Chart - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898532682391/crtcht_fltr_bv.gif)
12. In the **Layout** screen, specify the [layout](https://devnet.logianalytics.com/hc/en-us/articles/5735512245143-Inserting-Charts-in-a-Report#Layout) of the chart.

    ![Create Chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/9898516230423/crtcht_layout_bv.gif)
13. In the **Style** screen, select a style for the chart.

    ![Create Chart - Style](https://devnet.logianalytics.com/hc/article_attachments/9898516235927/crtcht_sty_bv.gif)
14. Select **Finish** to create the chart.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735498899351-Creating-Scrollable-Charts)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527456279-Creating-Motion-Charts)
