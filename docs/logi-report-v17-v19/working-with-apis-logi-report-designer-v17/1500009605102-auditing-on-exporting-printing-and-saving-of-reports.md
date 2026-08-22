---
title: "Auditing on Exporting, Printing, and Saving of Reports"
id: 1500009605102
section: "Working with APIs - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605102-Auditing-on-Exporting-Printing-and-Saving-of-Reports
updated_at: 2021-07-24T16:05:29Z
---

# Auditing on Exporting, Printing, and Saving of Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628181-Security-Context-Support) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628201-Accessibility)

# This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Auditing on Exporting, Printing, and Saving of Reports

You can make use of the two callback APIs - jet.bean.ReportCallback and jet.bean.CallbackInfo - to get the event and user information when a user export, print, or save a report in Logi Report Designer. The information includes the event (Export, Print, or Save), the time when the event occurs, the report ID, the user name who performs the operation, the parameters and values that are used to run the report if there are any, and the file name that the report is exported to or saved to. This topic describes how to implement the APIs to audit the Export, Print, and Save operations on reports.

1. Write a class, for instance, **com.yourcompany.callback.CustomCallback**, to implement the callback interface **jet.bean.ReportCallback**.
2. Put the class into the `<install_root>\lib` directory of Logi Report Designer.
3. Apply the class by adding the following JVM system property in the Logi Report startup file, JReport.bat/JReport.sh, which is stored in `<install_root>\lib`.

   `-Djreport.callback.class=com.yourcompany.callback.CustomCallback`
4. Logi Report will call your implementation right after a user export, print, or save a report in Logi Report and pass the information related to the operation to you.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628181-Security-Context-Support) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628201-Accessibility)
