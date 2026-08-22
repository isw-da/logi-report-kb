---
title: "An Introduction to Business Views"
id: 1500009675121
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675121-An-Introduction-to-Business-Views
updated_at: 2021-07-24T20:53:37Z
---

# An Introduction to Business Views

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650202-Components-Supported-in-Web-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675381-Quick-Start-with-a-Table-Report)

# An Introduction to Business Views

A business view contains database connections and relationships between view elements. It shields report end users from having to understand the physical structure of a data source, and enables them to build reports and analyze data based on a set of view elements they can understand. It also enables IT professionals to maintain control of the business data and ensure its integrity, while presenting end users with an intuitive view of the underlying data structures.

To make use of business views at server runtime, they need to be defined in Logi JReport Designer in advance and then published to Logi JReport Server. For additional information, see "Business Views" in the *Logi JReport Designer User's Guide*.

A business view may contain category objects and the following view elements: group objects, aggregation objects and detail objects.

* **Category objects**  
   Category objects contain a collection of view elements. A business view may contain more than one category. The icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920411287/btn_bvctgry.gif) indicates that an object is a category. Categories are only for categorizing view elements, and they cannot be inserted into a report. The category is often used for indicating the name of the underlying DBMS table.
* **Group objects**  
   Group objects are view elements that will become the basis for analysis in a report. They characteristically return text or date values. The icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) indicates that an object is a group object. A group object can be inserted as a column or row field in a crosstab, or as a group field or detail field in a table, or displayed as category/series field in a chart.
* **Aggregation objects**  
   Aggregation objects are numeric view elements that are calculated dynamically at runtime. The icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) indicates that an object is an aggregation object. An aggregation object can be inserted into the group header or footer in a table, or into a crosstab as an aggregate field. An aggregation object can also be used as a detail field in a table although it will display the same aggregate value for every detail line. Web Report Studio will calculate the summary values based on the group level the aggregation object has been inserted into. An aggregation object is the only object that can provide the value on a chart.
* **Detail objects**  
   Detail objects provide additional information. The icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif) indicates that an object is a detail object. A detail object can be inserted into a table as a detail field. Detail objects cannot be used in charts and crosstabs.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650202-Components-Supported-in-Web-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675381-Quick-Start-with-a-Table-Report)
