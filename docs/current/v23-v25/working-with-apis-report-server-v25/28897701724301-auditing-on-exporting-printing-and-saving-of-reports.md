---
title: "Auditing on Exporting, Printing, and Saving of Reports"
id: 28897701724301
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897701724301-Auditing-on-Exporting-Printing-and-Saving-of-Reports
updated_at: 2026-02-26T02:11:02Z
source_host: docs-report.zendesk.com
---
# 
Auditing on Exporting, Printing, and Saving of Reports 

You can implement the two callback APIs - jet.bean.ReportCallback and jet.bean.CallbackInfo - to get the event and user information when a user exports, prints, or saves a report in Report Server. 

The information includes the event (export, print, or save), the time when the event occurs, the report ID, the username who performs the operation, the parameters and values that are used to run the report if there are any, and the file name that the report is exported to or saved to.

- Write a class, for instance, com.yourcompany.callback.CustomCallback, to implement the callback interface jet.bean.ReportCallback.

- Put the class into the <install_root>\lib directory of Report Server.

- Apply the class by adding the following JVM system property in the Report startup file (.bat/.sh), or in the startup file of the application server that Report is deployed to. -Djreport.callback.class=com.yourcompany.callback.CustomCallback

- 
Report calls your implementation right after a user exports, prints, or saves a report in Report, and passes the information related to the operation to you.
