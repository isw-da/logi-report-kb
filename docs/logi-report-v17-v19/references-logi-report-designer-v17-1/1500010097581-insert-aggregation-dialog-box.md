---
title: "Insert Aggregation Dialog Box"
id: 1500010097581
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097581-Insert-Aggregation-Dialog-Box
updated_at: 2021-07-23T19:15:38Z
---

# Insert Aggregation Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097561-Information-Bus-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059602-Insert-Detail-Column-Dialog-Box)

# Insert Aggregation Dialog Box

You can use the Insert Aggregation dialog box to [add an aggregation in a crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#InsertAgg) based on the selected field. This topic describes the options in the dialog box.

Designer displays the Insert Aggregation dialog box when you drag a field that can be used as aggregate field from the Data panel to the aggregation area in a crosstab.

![Insert Aggregation dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848524311/instaggrgt.gif)

You see the following options in the dialog box:

**Aggregate Function**

The drop-down list contains the [aggregate functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) that you can use for the aggregation. Select the function you need.

* **Distinct On**  
  Designer enables the option and you should set it when you select DistinctSum as the aggregate function. Select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the fields according to whose unique values to calculate DistinctSum in the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box).

If the field that you select in the crosstab has predefined aggregate function, the option is Aggregation. Designer displays the name of the field in the text box and you cannot edit the name.

**Label**

Specify the label of the new aggregation in the crosstab. You can leave it blank.

**Auto Map Field Name**

Designer displays the option when you use the dialog box to insert an aggregation into a crosstab that uses a business view. Select it to automatically map the label for the aggregation in the crosstab to the dynamic display name of the field used for the aggregation at runtime.

**OK**

Select to the aggregate field and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097561-Information-Bus-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059602-Insert-Detail-Column-Dialog-Box)
