---
title: "Auditing on Exporting, Printing, and Saving of Reports"
id: 12491124206733
section: "Working with APIs - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491124206733-Auditing-on-Exporting-Printing-and-Saving-of-Reports
updated_at: 2026-02-25T23:50:53Z
source_host: docs-report.zendesk.com
---
# 
Auditing on Exporting, Printing, and Saving of Reports

You can use the two callback APIs - jet.bean.ReportCallback and jet.bean.CallbackInfo - to get the event and user information when a user exports, prints, or saves a report in Designer. The information includes the event (Export, Print, or Save), the time when the event occurs, the report ID, the user name who performs the operation, the parameters and values for running the report if there are any, and the file name that the report is exported to or saved to. This topic describes how you can implement the APIs to audit the Export, Print, and Save operations on reports.        

- Write a class, for instance, com.yourcompany.callback.CustomCallback, to implement the callback interface jet.bean.ReportCallback.

- Put the class into the <install_root>\lib directory of  Designer.

- Apply the class by adding the following JVM option to Designer's startup file JReport.bat/JReport.sh in <install_root>\lib. ...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Djreport.callback.class=com.yourcompany.callback.CustomCallback -Djreport.url.encoding="UTF-8"...

- Designer calls your implementation right after a user exports, prints, or saves a report, and passes the information related to the operation to you.
