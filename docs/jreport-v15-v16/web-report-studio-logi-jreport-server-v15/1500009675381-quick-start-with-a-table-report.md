---
title: "Quick Start with a Table Report"
id: 1500009675381
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675381-Quick-Start-with-a-Table-Report
updated_at: 2021-07-24T20:53:33Z
---

# Quick Start with a Table Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675121-An-Introduction-to-Business-Views)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675141-Standard-Way-of-Report-Creation-Using-Wizard)

# Quick Start With a Table Report

There is a [quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio#Way) to create a web report: you need only to select data fields and then Logi JReport generates a table report based on the fields. This saves a lot of time compared to typical report design with the [report wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009675141-Standard-Way-of-Report-Creation-Using-Wizard). After the report is opened in Web Report Studio, you can make use of the visualization toolbar to convert between data components and add more data components easily.

1. On the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009648602-Accessing-Logi-JReport-Server-Guide-v15-Server-via-a-Web-Browser#Local), select **Web Reports** in the Create category.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626071/wbrpt_qckstrt_strtpg.gif)
2. In the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009672481-Select-Data-Source#Report) dialog, select the business view with which to create the report from the Data Source drop-down list.

   ![Select Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404926626327/slctdtsrc.gif)
3. Check the checkboxes ahead of the data fields you want to display in the table report. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356119/btn_sort.gif) and ![](https://devnet.logianalytics.com/hc/article_attachments/4404926626967/btn_srch.gif) to sort and search the required resources.
4. Select **OK**. A table is generated using the selected fields.
   When only detail objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif), or detail objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif) and group objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) are selected in the Select Data Source dialog, a table of the Group Above type is created. If detail objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif) and aggregation objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) are selected, it is the Group Left Above type. When no detail objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif) are added, a Summary Table is created.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920357271/wbrpt_qckstrt_tbl.gif)

You can then [manipulate the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components#Table) and [convert the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components#ConvertVT) to crosstab or chart or another table as required. However tables created in the quick start way have some special characteristics:

* Blank table footer and group footers will be automatically hidden.
* If a summary column contains only one aggregate field, when you remove the aggregate field from the column, the whole column will be deleted.
* When inserting a summary column, it inherits the properties of the nearest existing summary column (the summary column on its left has the higher priority). When there aren't any existing summary columns, the default properties will be applied to the newly added summary column.

You can also use URL command to directly [create a web report in the quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009650402-Creating-Reports#Quickstart).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675121-An-Introduction-to-Business-Views)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675141-Standard-Way-of-Report-Creation-Using-Wizard)
