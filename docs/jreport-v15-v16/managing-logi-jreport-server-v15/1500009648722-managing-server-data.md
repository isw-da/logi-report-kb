---
title: "Managing Server Data"
id: 1500009648722
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648722-Managing-Server-Data
updated_at: 2021-07-24T20:54:05Z
---

# Managing Server Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648962-Task-level-Timeout-for-Advanced-Run-and-Schedule-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648742-Checking-Server-Data-Integrity)

# Managing Server Data

During its running process, Logi JReport Server keeps track of server information and stores it to its own database for the purpose of running various managing and monitoring tasks, such as managing the resources on the server, monitoring the task running status, and collecting server running statistics.

The server database includes system, realm, and profiling. The system database holds resources of the global server scope, such as server.properties, global NLS, and so on. The realm database holds information of folders, nodes, versions, the security system, and the completed table. The profiling database holds server runtime related information. You can refer to
[Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009669081-Configuring-the-Server-Database) for details about how to configure the databases.

Logi JReport provides completed SQL files to create tables for all databases supported. They reside in `<install_root>\script_files`.

This section covers the following topics:

* [Checking Server Data Integrity](https://devnet.logianalytics.com/hc/en-us/articles/1500009648742-Checking-Server-Data-Integrity)
* [Backing Up and Restoring Server Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009673501-Backing-Up-and-Restoring-Server-Data)
* [Archiving and Restoring Server Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009673481-Archiving-and-Restoring-Server-Data)
* [Viewing the Summary Information of Archive Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009673561-Viewing-the-Summary-Information-of-Archive-Files)
* [Clearing Invalid Nodes From the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009673521-Clearing-Invalid-Nodes-from-the-Server-Database)
* [Migrating Server Data From One Machine to Another](https://devnet.logianalytics.com/hc/en-us/articles/1500009673541-Migrating-Server-Data-from-One-Machine-to-Another)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648962-Task-level-Timeout-for-Advanced-Run-and-Schedule-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648742-Checking-Server-Data-Integrity)
