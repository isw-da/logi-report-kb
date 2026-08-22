---
title: "Lesson 5: Administration of Logi Report Server"
id: 1500010093121
section: "Logi Report Tutorial v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010093121-Lesson-5-Administration-of-Logi-Report-Server
updated_at: 2021-07-23T19:14:17Z
---

# Lesson 5: Administration of Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056102-Lesson-4-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093141-Lesson-6-Security)

# Lesson 5: Administration of Logi Report Server

Server provides the Administration feature that enables the system analyst, report administrator, or application server administrator to manage the resources, databases, configuration, security, and so on of Server. Server lists all the administration tasks on the drop-down menu after you point to Administration on the system toolbar of the Server Console.

![Administration Menu](https://devnet.logianalytics.com/hc/article_attachments/4404848801815/admin_lsn5.gif)

**Security**

It allows you to create and manage realms, users, groups, roles, privileges, and alias, arrange users into different organizations, dynamically change the security policy applied to a catalog, and configure LDAP as a security provider for Server. For more information about security, see [Lesson 6](https://devnet.logianalytics.com/hc/en-us/articles/1500010093141-Lesson-6-Security) in this track.

**Server Profile**

It allows you to customize general settings of Server, Page Report Studio, Web Report Studio, and JDashboard for all users.

**Configuration**

It allows you to configure Server.

* **Service** - You can use it to set attributes of the HTTP connection.
* **Log** - You can use it to configure the Logi Report logging system.
* **Performance** - You can use it to preload particular catalogs and reports in cache so they will be faster to access the first time they are used.
* **Export** - You can use it to configure the default settings for exporting report results to e-mail, to configure your FAX hardware and software settings. You cannot distribute reports via e-mail or fax until these settings are configured.
* **Upload** - You can use it to specify the allowed image types when end users insert images from the local file system into reports or dashboards.
* **License Key** - You can use it to update the server license with a new one.
* **Cache** -
  You can use it to cache in-memory cubes for business views, report data for queries, reports, images, and security objects. These settings affect how quickly resources can be accessed; however, the more resources that are cached, the more memory is used and thus would harm performance rather than increase performance.
* **Server DB**  - You can use it to configure three logical databases in Server: system, realm, and profiling. The system database holds resources of the global server scope, such as server.properties and global NLS. The realm database holds information of folders, nodes, versions, the security system, and the completed table. The profiling database holds server runtime related information.
* **Cluster** -
  You can use it to set up groups of servers in a clustered environment.
* **E-mail Server** - You can use it to set up the linkage to your SMTP server to enable sending report results and notifications via e-mails.
* **Advanced** - You can use it to specify a miscellaneous set of options and settings.

**Language**

It allows
you to
edit global NLS for all reports and NLS for resources in the resource tree.

**Connection**

It allows you to
reload the connection settings after datasource.xml file is modified,
manage dynamic connections, and
keep cached connection for reuse.

**Other**

It provides other administration tasks.

* **Dashboard Listeners** - You can use it to manage implementations of the Dashboard Listener API.
* **Triggers** -
  You can use it to create and manage triggers for use when scheduling tasks.
* **Converting** - You can use it to permanently convert resources earlier than V8 in the server resource tree to adapt to the current version to avoid conversion at each run.
* **Custom Fields** - You can use it to manage user-defined fields which can be used as resource properties in Server.
* **Dynamic Display Names** - You can use it to manage dynamic display names for business view elements.
* **Batch Refresh Dynamic Resources** - You can use it to recompile dynamic resources in reports after the business views used by the reports are changed.
* **Monitor** - You can use it to access Server Monitor to log, monitor, and report on real-time system status and the performance of Server.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056102-Lesson-4-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093141-Lesson-6-Security)
