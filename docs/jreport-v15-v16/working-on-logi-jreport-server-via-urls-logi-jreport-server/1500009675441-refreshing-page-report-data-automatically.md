---
title: "Refreshing Page Report Data Automatically"
id: 1500009675441
section: "Working on Logi JReport Server via URLs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675441-Refreshing-Page-Report-Data-Automatically
updated_at: 2021-07-24T20:53:32Z
---

# Refreshing Page Report Data Automatically

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675481-Running-a-Report-Tab-in-a-Page-Report)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675501-Opening-Web-Reports-in-Web-Report-Studio-via-JSON)

### Refreshing Page Report Data Automatically

When running a page report in Page Report Studio, you can ask Logi JReport to automatically refresh the report data at certain interval. To achieve this, you need to run the report with run.jsp and add the following two properties in the URL:

* **jrs.auto\_refresh\_data=true**  
   Specifies to automatically refresh the report data.
* **jrs.auto\_refresh\_data\_time=[a number in seconds]**  
   Specifies the time interval at which to refresh the report data.

The following is a URL example:

`http://localhost:8888/webos/app/pagestudio/run.jsp?jrs.report=%2fSampleReports%2fCustomerAnalysis.cls&jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.auto_refresh_data=true&jrs.auto_refresh_data_time=10`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675481-Running-a-Report-Tab-in-a-Page-Report)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675501-Opening-Web-Reports-in-Web-Report-Studio-via-JSON)
