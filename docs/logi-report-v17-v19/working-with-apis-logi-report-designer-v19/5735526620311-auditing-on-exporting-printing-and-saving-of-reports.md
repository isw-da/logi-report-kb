---
title: "Auditing on Exporting, Printing, and Saving of Reports"
id: 5735526620311
section: "Working with APIs - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735526620311-Auditing-on-Exporting-Printing-and-Saving-of-Reports
updated_at: 2022-11-02T08:17:02Z
---

# Auditing on Exporting, Printing, and Saving of Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511625623-Applying-Security-Context-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735484099095-References)

# Auditing on Exporting, Printing, and Saving of Reports

You can use the two callback APIs - jet.bean.ReportCallback and jet.bean.CallbackInfo - to get the event and user information when a user exports, prints, or saves a report in Designer. The information includes the event (Export, Print, or Save), the time when the event occurs, the report ID, the user name who performs the operation, the parameters and values for running the report if there are any, and the file name that the report is exported to or saved to. This topic describes how you can implement the APIs to audit the Export, Print, and Save operations on reports.

1. Write a class, for instance, **com.yourcompany.callback.CustomCallback**, to implement the callback interface **jet.bean.ReportCallback**.
2. Put the class into the `<install_root>\lib` directory of Designer.
3. Apply the class by adding the following JVM option to Designer's startup file **JReport.bat**/**JReport.sh** in `<install_root>\lib`.

   `...-classpath "%CLASSPATH%" -Dreporthome="%REPORTHOME%" -Djreport.callback.class=com.yourcompany.callback.CustomCallback -Djreport.url.encoding="UTF-8"...`
4. Designer calls your implementation right after a user exports, prints, or saves a report, and passes the information related to the operation to you.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511625623-Applying-Security-Context-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735484099095-References)
