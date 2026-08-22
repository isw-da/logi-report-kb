---
title: "Creating and Deleting a Report"
id: 1500009582781
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582781-Creating-and-Deleting-a-Report
updated_at: 2021-07-24T05:56:19Z
---

# Creating and Deleting a Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562422-Using-the-Design-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582861-Opening-and-Closing-a-Report)

# Creating and Deleting a Report

When creating reports, the reports should be created based on an existing catalog file, otherwise you will get an error.

* **createReportSet(String name)**  
   Creates a new page report with the specified name.
* **addReport(String reportsetHandle, String name)**  
   Creates a new report tab with the specified name in the specified page report.
* **createWebReportSet(String reportsetName, String reportTabName)**  
   Creates a new web report with the specified name. Creating a web report will create a report tab in the web report automatically.
* **deleteReport(java.lang.String name)**  
   Deletes an existing report with the specified name, and returns true if the report has been successfully removed.

**Parameters**

* name - The name of the report or page report tab that is to be created or deleted.
* reportsetHandle - The handle of the page report into which the report tab will be added.
* reportsetName - The name of the web report that is to be created.
* reportTabName - The report tab name in the web report that is to be created. Optional.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562422-Using-the-Design-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582861-Opening-and-Closing-a-Report)
