---
title: "Auditing on Exporting, Printing, and Saving of Reports"
id: 4405661304599
section: "Working with APIs - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661304599-Auditing-on-Exporting-Printing-and-Saving-of-Reports
updated_at: 2022-01-27T20:34:15Z
---

# Auditing on Exporting, Printing, and Saving of Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661323671-Applying-Security-Context-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661256087-References)

# Auditing on Exporting, Printing, and Saving of Reports

You can use the two callback APIs - jet.bean.ReportCallback and jet.bean.CallbackInfo - to get the event and user information when a user exports, prints, or saves a report in Designer. The information includes the event (Export, Print, or Save), the time when the event occurs, the report ID, the user name who performs the operation, the parameters and values for running the report if there are any, and the file name that the report is exported to or saved to. This topic describes how you can implement the APIs to audit the Export, Print, and Save operations on reports.

1. Write a class, for instance, **com.yourcompany.callback.CustomCallback**, to implement the callback interface **jet.bean.ReportCallback**.
2. Put the class into the `<install_root>\lib` directory of Designer.
3. Apply the class by adding the following JVM system property in the Designer startup file, **JReport.bat**/**JReport.sh**, which is stored in `<install_root>\lib`.

   `-Djreport.callback.class=com.yourcompany.callback.CustomCallback`
4. Designer calls your implementation right after a user exports, prints, or saves a report, and passes the information related to the operation to you.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661323671-Applying-Security-Context-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661256087-References)
