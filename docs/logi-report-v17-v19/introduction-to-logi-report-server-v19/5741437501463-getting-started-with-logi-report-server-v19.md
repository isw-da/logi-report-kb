---
title: "Getting Started with Logi Report Server v19"
id: 5741437501463
section: "Introduction to Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741437501463-Getting-Started-with-Logi-Report-Server-v19
updated_at: 2022-10-31T17:17:55Z
---

# Getting Started with Logi Report Server v19

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741393125527-Logi-Report-Server-Guide-v19-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741460873751-Logi-Report-Server-System-Requirements-Logi-Report-Server-v19)

# Getting Started with Logi Report Server v19

This topic guides you through the process of installing and configuring Logi Report Server, running and creating reports and dashboards in Logi Report web editors, and distributing reports to a variety of outputs.

[1. Product Installation](#)

1. Think about the number of Logi Report servers you need if you want to set up a Logi Report Server Cluster. See [Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/5741415572759-Logi-Report-Server-Cluster-Logi-Report-Server-v19).
2. Decide the licensed features that you want for each Logi Report server. See [Logi Report Licenses](https://devnet.logianalytics.com/hc/en-us/articles/5741452341143-Logi-Report-Licenses).
3. Prepare the computers on which you want to install Logi Report Server. See [Logi Report Server System Requirements](https://devnet.logianalytics.com/hc/en-us/articles/5741460873751-Logi-Report-Server-System-Requirements-Logi-Report-Server-v19).
4. Obtain the Logi Report Server install program. Also obtain the Logi Report Server Monitor install program if you want a Server Monitor. See [Logi Report download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
5. Install Logi Report Server using the way you prefer. See [Installing and Uninstalling Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/5741437214615-Installing-and-Uninstalling-Logi-Report-Server-v19).
6. Install Server Monitor if you want to monitor your server performance. See [Installing and Uninstalling Server Monitor](https://devnet.logianalytics.com/hc/en-us/articles/5741385613463-Installing-and-Uninstalling-Server-Monitor) in the *Logi Report Server Monitor Guide*.

[2. Server Database Configuration for Metadata](#)

Configure the server database for metadata on the Server Console or using the configuration file if you didn't do this during the installation. See [Configuring Server Databases for Server Metadata in a Standalone Environment](https://devnet.logianalytics.com/hc/en-us/articles/5741415979543-Configuring-Server-Databases-for-Server-Metadata-in-a-Standalone-Environment).

[3. Product Security and Authorization](#)

1. Create security organizations to manage different groups of users. See [Multitenancy Supported via Organizations](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations).
2. Set up user accounts, roles, and groups, with appropriate privileges. See [Security System Data Model](https://devnet.logianalytics.com/hc/en-us/articles/5741463552151-Security-System-Data-Model).
3. Integrate with your security software, for example, LDAP. See [Using an LDAP Server's Security System](https://devnet.logianalytics.com/hc/en-us/articles/5741439835159-Using-an-LDAP-Server-s-Security-System).

[4. Resource Publish and Permissions](#)

1. Publish reports, catalogs, and library components to Logi Report Server. See [Publishing Resources](https://devnet.logianalytics.com/hc/en-us/articles/5741453495191-Publishing-Resources).
2. Set up user permissions on the server resources. See [Managing Permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions).
3. Optionally, obtain resources from the real path dynamically. See [Getting and Using Resources From a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/5741482166807-Getting-and-Using-Resources-From-a-Real-Path).

[5. Export Configuration](#)

1. Configure the email server if you want to deploy reports via email. See [Configuring the Email Server](https://devnet.logianalytics.com/hc/en-us/articles/5741416139159-Configuring-the-Email-Server).
2. Configure settings for exporting reports to email and fax. See [Configuring Export Settings](https://devnet.logianalytics.com/hc/en-us/articles/5741416077591-Configuring-Export-Settings).

[6. Cluster Setup](#)

Set up a Logi Report Server Cluster in which multiple servers work together. See [Setting Up and Starting a Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/5741415669527-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster).

[7. Integration Setup](#)

1. Configure the server database. See [Configuring Server Databases for Server Metadata in an Integrated Environment](https://devnet.logianalytics.com/hc/en-us/articles/5741395898263-Configuring-Server-Databases-for-Server-Metadata-in-an-Integrated-Environment).
2. Create the Logi Report Server WAR/EAR. See [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/5741473837719-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).
3. Deploy the WAR/EAR to an application Server. See [Deploying Logi Report Server to a Java Application Server](https://devnet.logianalytics.com/hc/en-us/articles/5741431629463-Deploying-Logi-Report-Server-to-a-Java-Application-Server).

[8. Server Monitor](#)

1. Start and access the Server Monitor. See [Launching and Accessing Server Monitor](https://devnet.logianalytics.com/hc/en-us/articles/5741394277911-Launching-and-Accessing-Server-Monitor) in the *Logi Report Server Monitor Guide*.
2. Monitor the status and performance of Server. See [Using Server Monitor](https://devnet.logianalytics.com/hc/en-us/articles/5741399649175-Using-Server-Monitor) in the *Logi Report Server Monitor Guide*.

[9. Report Running and Scheduling](#)

1. Run reports directly or on demand. See [Running Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741439314455-Running-Reports).
2. Schedule tasks to run reports at the specified time to different locations in various formats. See [Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741483442455-Scheduling-Reports).

[10. Report Creating, Editing, and Exporting](#)

1. Create, edit, and export web reports using Web Report Studio. See [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741464180119-Web-Report-Studio-Server-v19).
2. Create, edit, and export page reports using Page Report Studio. See [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741462429975-Page-Report-Studio-Server-v19).
3. Create, edit, and export dashboards using JDashboard. See [Introduction to the Logi Report JDashboard](https://devnet.logianalytics.com/hc/en-us/articles/5741387513879-Introduction-to-the-Logi-Report-JDashboard-Logi-Report-Server-v19).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741393125527-Logi-Report-Server-Guide-v19-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741460873751-Logi-Report-Server-System-Requirements-Logi-Report-Server-v19)
