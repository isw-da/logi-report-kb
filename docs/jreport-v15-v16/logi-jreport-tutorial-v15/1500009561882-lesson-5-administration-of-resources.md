---
title: "Lesson 5: Administration of Resources"
id: 1500009561882
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009561882-Lesson-5-Administration-of-Resources
updated_at: 2021-07-24T05:56:28Z
---

# Lesson 5: Administration of Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009561862-Lesson-4-Scheduling-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582261-Lesson-6-Security)

# Lesson 5: Administration of Resources

Logi JReport Server provides the administration console that allows the system analyst, report administrator, or application server administrator to manage the resources, databases, configuration, security and so on of Logi JReport Server. This topic describes the administrative tasks that you can perform through the administration console.

* [Task 1: Access the Administration Console](#Task1)
* [Task 2: Review the Resources Page](#Task2)
* [Task 3: Review the Configuration Page](#Task3)
* [Task 4: Understand the Monitor Page](#Task4)
* [Task 5: Review the Remaining Pages](#Task5)

## Task 1: Access the Administration Console

1. Select **Start** > **Logi JReport 15** > **System Admin**.
2. A browser window with the Sign in dialog is displayed. Enter **admin** for the user name and **admin** for the password, then select **Login**.

   These are the initial administrative user credentials built-in to Logi JReport Server. One of the first things an administrator should do is to set up the correct user credentials so that appropriate access to the reports is granted.

   The Logi JReport Administration page is displayed:

   ![Server Admin Page](https://devnet.logianalytics.com/hc/article_attachments/4404889457303/admin_lsn5_admpg.gif)

## Task 2: Review the Resources page

The Resources page of the administration console lists the resources that have been published to Logi JReport Server. The resource list shown here is similar to that of the user console, however the report name is not a link so you cannot run report from the administration console.

The User Directory is hidden on the left showing the folders of published resources. By default, the root folder is open when you first log onto the administration console.

The NLS Editor button ![NLS Editor button](https://devnet.logianalytics.com/hc/article_attachments/4404889457559/btn_nls.gif) allows you to translate a report or dashboard into a different language from the original one.

Other buttons, Versions ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4404894051479/btn_vrsn.gif), Properties ![Properties button](https://devnet.logianalytics.com/hc/article_attachments/4404894050967/btn_prpty.gif) and Delete ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404894051735/btn_delete.gif), are the same as described in [Lesson 1](https://devnet.logianalytics.com/hc/en-us/articles/1500009582241-Lesson-1-Starting-Logi-JReport-Server#Command) of this track.

## Task 3: Review the Configuration Page

The Configuration page allows you to configure and manage Logi JReport Server as follows:

* **Service** - Used to set attributes of the HTTP connection.
* **Log** - Used toconfigure the Logi JReport logging system.
* **Performance** - Used to preload particular catalogs and reports in cache so they will be faster to access the first time they are used.
* **LDAP** - Used to configure LDAP as a security provider for Logi JReport Server. A large number of different LDAP products are supported. In order to use them, a detailed knowledge of how to talk to your LDAP product is required.
* **Export** - Used to configure the default settings for exporting report results to e-mail, to configure your FAX hardware and software settings. You cannot distribute reports via e-mail or fax until these settings are configured.
* **Connection** - Used to reload the connection settings after datasource.xml file is modified when Logi JReport Server is running.
* **Connection Pool** - Used to keep cached connection for reuse.
* **Upload** - Used to specify the allowed image types when end users insert images from the local file system into reports or dashboards.
* **Custom Fields** - Used to manage user defined fields which can be used as resource properties in Logi JReport Server.
* **Dashboard Listeners** - Used to manage implementations of the Dashboard Listener API.
* **Dynamic Connections** - Used to manage dynamic connections.
* **Dynamic Display Names** - Used to manage dynamic display names for business view elements.
* **Organizations** - Used to organize users into different groups.
* **E-mail Server** - Used to set up the linkage to your SMTP server to enable sending report results and notifications via e-mails.
* **License Key** - Used to update the server license with a new one.
* **Advanced** - A miscellaneous set of options and settings.

## Task 4: Understand the Monitor Page

Logi JReport Server Monitor allows system administrators to log, monitor and report on real-time system status and the performance of the Logi JReport Server. It can be accessed via any web browser, enabling administrators to remotely monitor and manage Logi JReport Servers.

Logi JReport Server Monitor allows you to track the status of Logi JReport Server, see what reports are running or have run as well as which users are accessing the system.

Logi JReport Server Monitor is downloaded separately from Logi JReport Server, and must be installed before this page can be used.

## Task 5: Review the Remaining Pages

* **Security**  
   Allows you to create and manage realms, users, groups, roles, privileges, and alias. This is required if you are going to use My Reports so that users will only see their own reports in the My Reports folder. For more details about security, see [Lesson 6](https://devnet.logianalytics.com/hc/en-us/articles/1500009582261-Lesson-6-Security) in this track.
* **Profile**  
   Allows you to customize general settings of Logi JReport Server, Page Report Studio, Web Report Studio and JDashboard.
* **Cluster**  
   Allows you to set up groups of servers in a clustered environment.
* **Triggers**  
   Allows you to create and manage triggers.
* **Data**  
  Logi JReport Server needs to read and write to a DBMS system to store information about the server and the available reports and report version. By default the DBMS is the 100% Java Apache Derby DBMS embedded in Logi JReport. This can easily be changed to use your preferred DBMS such as Oracle or MySQL.
* **Cube**  
   Creates and manages in-memory cubes for business views.
* **Cache**  
   Allows you to cache data, reports, security objects, and images. These settings affect how quickly resources can be accessed; however, the more resources that are cached, the more memory is used and thus would harm performance rather than increase performance.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009561862-Lesson-4-Scheduling-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582261-Lesson-6-Security)
