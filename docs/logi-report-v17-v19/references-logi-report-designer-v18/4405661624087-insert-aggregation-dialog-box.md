---
title: "Insert Aggregation Dialog Box"
id: 4405661624087
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661624087-Insert-Aggregation-Dialog-Box
updated_at: 2022-01-27T20:35:35Z
---

# Insert Aggregation Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661623063-Information-Bus-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661625111-Insert-Detail-Column-Dialog-Box)

# Insert Aggregation Dialog Box

You can use the Insert Aggregation dialog box to [add an aggregation in a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/4405661377559-Modifying-Crosstabs#InsertAgg) based on the selected field. This topic describes the options in the dialog box.

Designer displays the Insert Aggregation dialog box when you drag a field that can be used as aggregate field from the Data panel to the aggregation area in a crosstab.

![Insert Aggregation dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556153495/instaggrgt.gif)

You see the following options in the dialog box:

**Aggregate Function**

This drop-down list contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries#Function) that you can use for the aggregation. Select the function you need.

* **Distinct On**  
  Designer enables this option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664572951-Select-Fields-Dialog-Box).

When the field you select in the crosstab has predefined aggregate function, this option is Aggregation. Designer displays the name of the field in the text box and you cannot edit the name.

**Label**

Specify the label of the new aggregation in the crosstab. You can leave it blank.

**Auto Map Field Name**

Designer displays this option when you use the dialog box to insert an aggregation into a crosstab that uses a business view. Select it to apply the display name of the field as the aggregation label and map the label to the dynamic display name of the field at runtime if the Server administrator defines it.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661623063-Information-Bus-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661625111-Insert-Detail-Column-Dialog-Box)
