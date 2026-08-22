---
title: "Checking Server Data Integrity"
id: 1500009648742
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648742-Checking-Server-Data-Integrity
updated_at: 2021-07-24T20:54:04Z
---

# Checking Server Data Integrity

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648722-Managing-Server-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673501-Backing-Up-and-Restoring-Server-Data)

# Checking Server Data Integrity

In abnormal circumstances, server data may not be saved correctly or completely in the databases. Logi JReport Server allows you to check the integrity of server data.

The integrity check mainly examines two aspects of the realm database:

* Integrality and consistency among tables - checking records among the tables to see whether they are complete and consistent.
* Integrality and consistency between realm database and the external files - checking to see whether the records in the tables match the related external files.

If any inconsistent or incomplete server data is found, it will be removed from the realm database since it is unused. The same process also applies to files.

To check server data integrity, do one of the following:

* Launch Logi JReport Server on the command line, using parameter `-cleanup`.

  `C:\Logi JReport\Server\bin>JRServer -cleanup`
* Open the batch file used to start Logi JReport Server, add **`-Dcheck.realmtables=true`** to the line that starts Logi JReport Server:

  `"%JAVAHOME%\bin\java.exe" -Dcheck.realmtables=true "-Dinstall.root= <install_root>"` ...

**Note:** The integrity check checks only the realm database.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648722-Managing-Server-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673501-Backing-Up-and-Restoring-Server-Data)
