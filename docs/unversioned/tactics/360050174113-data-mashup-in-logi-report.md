---
title: "Data Mashup in Logi Report"
id: 360050174113
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050174113-Data-Mashup-in-Logi-Report
updated_at: 2022-11-01T03:18:18Z
---

# Data Mashup in Logi Report

You may have a data source in a Logi Report catalog which connects to different databases.  For example, a MySQL database, a SOAP web service data source, a MongoDB data source, etc. and you want to use data from all of the database connections in your report or dashboard. This can be achieved by the Data Mashup feature. No matter how many database connections you have, as long as they are in the same catalog data source, you can mash up multiple data sources from these connections into one single query or business view, which is essential for creating reports in Logi Report. You can also create joins between the mashed up data resources that are known as distributed joins.

Report provides the Add Table/View/Query dialog, with which you can easily mash up multiple data resources from different connections. The data resources include tables, views, synonyms, queries, imported SQL files, stored procedures, and user defined data sources.

* Data mashup in queries.  
  Data resources from different connections can be mashed up in a query before or after a query is created.

  ![Data Mashup in Queries](https://devnet.logianalytics.com/hc/article_attachments/9922830210967)

* Data mashup in business views.  
  Data resources from different connections can be mashed up in a business view before or after a business view is created.

  ![Data Mashup in Business Views](https://devnet.logianalytics.com/hc/article_attachments/9922830051863)

* Data mashup in catalog pre-joins.  
  Data resources from different connections can be mashed up when creating pre-joins in a catalog.

  ![Data Mashup in Catalog Pre-joins](https://devnet.logianalytics.com/hc/article_attachments/9922830043031)
