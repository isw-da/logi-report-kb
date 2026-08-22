---
title: "An Introduction to Business Views"
id: 1500009751441
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751441-An-Introduction-to-Business-Views
updated_at: 2021-07-25T07:18:36Z
---

# An Introduction to Business Views

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724662-Components-Supported-in-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751621-Quick-Start-with-a-Table-Report)

# An Introduction to Business Views

A business view contains database connections and relationships between view elements. It shields report end users from having to understand the underlying structure of a data source, and enables them to create complex reports containing multiple components and analyze data based on a set of view elements they can understand. All reports created from a business view automatically include all of the interactivity built into that business view. For example, they can include things like drill down, drill up so that end users are able to switch data from one group to another.

To make use of business views at server runtime, they need to be defined in Logi Report Designer in advance and then published to Logi Report Server. For additional information, refer to Business Views in the *Logi Report Designer Guide*.

A business view may contain category objects and the following view elements: group objects, aggregation objects and detail objects.

* **Category objects**  
   Category objects contain a collection of view elements. A business view may contain more than one category. The icon ![Category Object](https://devnet.logianalytics.com/hc/article_attachments/4404942471959/btn_bvctgry.gif) indicates that an object is a category. Categories are only for categorizing view elements, and they cannot be inserted into a report. The category is often used for indicating the name of the underlying DBMS table.
* **Group objects**  
   Group objects are view elements that will become the basis for analysis in a report. They characteristically return text or date values. The icon ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) indicates that an object is a group object. A group object can be inserted as a column or row field in a crosstab, or as a group field or detail field in a table or banded object, or displayed as category/series field in a chart.
* **Aggregation objects**  
   Aggregation objects are numeric view elements that are calculated dynamically at runtime. The icon ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) indicates that an object is an aggregation object. An aggregation object can be inserted into the group header or footer in a table or banded object, or into a crosstab as an aggregate field. An aggregation object can also be used as a detail field in a table. Web Report Studio will calculate the summary values based on the group level the aggregation object has been inserted into. An aggregation object is the only object that can provide the value on a chart.
* **Detail objects**  
   Detail objects provide additional information. The icon ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) indicates that an object is a detail object. A detail object can be inserted into a table or banded object as a detail field. Detail objects cannot be used in charts and crosstabs.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724662-Components-Supported-in-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751621-Quick-Start-with-a-Table-Report)
