---
title: "Lesson 5: Administration of Logi Report Server"
id: 5735505964823
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735505964823-Lesson-5-Administration-of-Logi-Report-Server
updated_at: 2022-11-29T03:39:09Z
---

# Lesson 5: Administration of Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511111191-Lesson-4-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563090967-Lesson-6-Security)

# Lesson 5: Administration of Logi Report Server

Server provides the Administration feature for the system analyst, report administrator, or application server administrator to manage its resources, databases, configuration, security, and so on. Server lists all the administration commands on the Administration menu on the system toolbar of the Server Console.

![Administration Menu](https://devnet.logianalytics.com/hc/article_attachments/9898523289751/admin_lsn5.gif)

**Security**

You can create and manage realms, users, groups, roles, privileges, and alias, arrange users into different organizations, dynamically change the security policy applied to a catalog, and configure LDAP as a security provider for Server. For more information about security, see [Lesson 6](https://devnet.logianalytics.com/hc/en-us/articles/5735563090967-Lesson-6-Security) in this track.

**Server Profile**

You can customize general settings of Server, Page Report Studio, Web Report Studio, and JDashboard for all users.

**Configuration**

It provides the configuration tasks.

* **Service**  
  You can use it to set attributes of the HTTP connection.
* **Log**  
  You can use it to configure the Logi Report logging system.
* **Performance**  
  You can use it to preload catalogs and reports in the cache so it is faster to access them the first time you use them.
* **Export**  
  You can use it to configure the default settings for exporting reports to email, to configure your FAX hardware and software settings. You cannot distribute reports via email or fax until these settings are configured.
* **Upload**  
  You can use it to specify the allowed image types when end users insert images from the local file system into reports or dashboards.
* **License Key**  
  You can use it to update your Server license with a new one.
* **Cache**  
  You can use it to cache in-memory cubes for business views, report data for queries, reports, images, and security objects. These settings affect how quickly resources can be accessed. However, the more resources that are cached, the more memory is used and thus would harm performance rather than increase performance.
* **Server DB**  
  You can use it to configure three logical databases on Server: system, realm, and profiling. The system database holds resources of the global server scope, such as server.properties and global NLS. The realm database holds information of folders, nodes, versions, the security system, and the completed table. The profiling database holds server runtime related information.
* **Cluster**  
  You can use it to set up groups of servers in a clustered environment.
* **E-mail Server**  
  You can use it to set up the linkage to your SMTP server to enable sending reports and notifications via emails.
* **Advanced**  
  You can use it to specify a miscellaneous set of options and settings.

**Language**

You can edit global NLS for all reports and NLS for resources in the resource tree.

**Connection**

You can reload the connection settings after you modified the datasource.xml file, manage dynamic connections, and keep cached connection for reuse.

**Other**

It provides other administration tasks.

* **Dashboard Listeners**  
  You can use it to manage implementations of the Dashboard Listener API.
* **Triggers**  
  You can use it to create and manage triggers for use when scheduling tasks.
* **Converting**  
  You can use it to permanently convert resources earlier than v8 in the server resource tree to adapt to the current version to avoid conversion at each run.
* **Custom Fields**  
  You can use it to manage user-defined fields that can be used as resource properties on Server.
* **Dynamic Display Names**  
  You can use it to manage dynamic display names for business view elements.
* **Batch Refresh Dynamic Resources**  
  You can use it to recompile dynamic resources in reports after the business views used by the reports are changed.
* **Business Views for Reports**  
  You can use it to import business views from a file and apply them to reports.
* **Monitor**  
  You can use it to access Server Monitor to log, monitor, and report on real time system status and the performance of Server.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511111191-Lesson-4-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563090967-Lesson-6-Security)
