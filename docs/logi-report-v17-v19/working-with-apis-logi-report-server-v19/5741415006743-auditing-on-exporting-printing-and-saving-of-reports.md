---
title: "Auditing on Exporting, Printing, and Saving of Reports"
id: 5741415006743
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741415006743-Auditing-on-Exporting-Printing-and-Saving-of-Reports
updated_at: 2022-10-31T17:15:47Z
---

# Auditing on Exporting, Printing, and Saving of Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741386288919-Tracing-Server-Resource-Change-Events)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400164119-Configuring-the-Security-Cache-System)

# Auditing on Exporting, Printing, and Saving of Reports

You can implement the two callback APIs - jet.bean.ReportCallback and jet.bean.CallbackInfo - to get the event and user information when a user exports, prints, or saves a report in Logi Report Server.

The information includes the event (export, print, or save), the time when the event occurs, the report ID, the username who performs the operation, the parameters and values that are used to run the report if there are any, and the file name that the report is exported to or saved to.

1. Write a class, for instance, **com.yourcompany.callback.CustomCallback**, to implement the callback interface **jet.bean.ReportCallback**.
2. Put the class into the `<install_root>\lib` directory of Logi Report Server.
3. Apply the class by adding the following JVM system property in the Logi Report startup file (.bat/.sh), or in the startup file of the application server that Logi Report is deployed to.

   `-Djreport.callback.class=com.yourcompany.callback.CustomCallback`
4. Logi Report calls your implementation right after a user exports, prints, or saves a report in Logi Report, and passes the information related to the operation to you.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741386288919-Tracing-Server-Resource-Change-Events)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400164119-Configuring-the-Security-Cache-System)
