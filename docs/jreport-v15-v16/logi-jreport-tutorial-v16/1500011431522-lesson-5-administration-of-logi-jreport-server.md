---
title: "Lesson 5: Administration of Logi JReport Server"
id: 1500011431522
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011431522-Lesson-5-Administration-of-Logi-JReport-Server
updated_at: 2021-07-24T10:39:42Z
---

# Lesson 5: Administration of Logi JReport Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463561-Lesson-4-Scheduling-Reports) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901097111/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463541-Lesson-6-Security)

# Lesson 5: Administration of Logi JReport Server

Logi JReport Server provides the administration feature that allows the system analyst, report administrator, or application server administrator to manage the resources, databases, configuration, security and so on of Logi JReport Server. All the administration tasks are listed on the drop-down menu after pointing to Administration on the system toolbar of the Logi JReport Server console.

![Administration Menu](https://devnet.logianalytics.com/hc/article_attachments/4404901104023/admin_lsn5.gif)

**Security**

Allows you to create and manage realms, users, groups, roles, privileges and alias, arrange users into different organizations, dynamically change the security policy applied to a catalog, and configure LDAP as a security provider for Logi JReport Server. For more details about security, see [Lesson 6](https://devnet.logianalytics.com/hc/en-us/articles/1500011463541-Lesson-6-Security) in this track.

**Server Profile**

Allows you to customize general settings of Logi JReport Server, Page Report Studio, Web Report Studio and JDashboard for all users.

**Configuration**

Allows you to configure Logi JReport Server.

* **Service** - Used to set attributes of the HTTP connection.
* **Log** - Used to configure the Logi JReport Logging system.
* **Performance** - Used to preload particular catalogs and reports in cache so they will be faster to access the first time they are used.
* **Export** - Used to configure the default settings for exporting report results to e-mail, to configure your FAX hardware and software settings. You cannot distribute reports via e-mail or fax until these settings are configured.
* **Upload** - Used to specify the allowed image types when end users insert images from the local file system into reports or dashboards.
* **License Key** - Used to update the server license with a new one.
* **Cache** -
  Used to cache in-memory cubes for business views, report data for queries, reports, images, and security objects. These settings affect how quickly resources can be accessed; however, the more resources that are cached, the more memory is used and thus would harm performance rather than increase performance.
* **Server DB**  - Used to configure three logical databases in Logi JReport Server: system, realm, and profiling. The system database holds resources of the global server scope, such as server.properties, global NLS, and so on. The realm database holds information of folders, nodes, versions, the security system, and the completed table. The profiling database holds server runtime related information.
* **Cluster** -
  Used to set up groups of servers in a clustered environment.
* **E-mail Server** - Used to set up the linkage to your SMTP server to enable sending report results and notifications via e-mails.
* **Advanced** - A miscellaneous set of options and settings.

**Language**

Allows
you to
edit global NLS for all reports and NLS for resources in the resource tree.

**Connection**

Allows
you to
reload the connection settings after datasource.xml file is modified,
manage dynamic connections, and
keep cached connection for reuse.

**Other**

Provides other administration tasks.

* **Dashboard Listeners** - Used to manage implementations of the Dashboard Listener API.
* **Triggers** -
  Used to create and manage triggers for use when scheduling tasks.
* **Converting** - Used to permanently convert resources earlier than V8 in the server resource tree to adapt to the current version to avoid conversion at each run.
* **Custom Fields** - Used to manage user defined fields which can be used as resource properties in Logi JReport Server.
* **Dynamic Display Names** - Used to manage dynamic display names for business view elements.
* **Monitor** - Allows you to access Logi JReport Server Monitor to log, monitor and report on real-time system status and the performance of Logi JReport Server.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463561-Lesson-4-Scheduling-Reports) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901097111/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463541-Lesson-6-Security)
