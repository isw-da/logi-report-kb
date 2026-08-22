---
title: "Getting Started with Logi Report Server v18"
id: 4405690624791
section: "Introduction to Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690624791-Getting-Started-with-Logi-Report-Server-v18
updated_at: 2022-01-27T07:59:33Z
---

# Getting Started with Logi Report Server v18

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690444055-Logi-Report-Server-Guide-v18-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690625687-Logi-Report-Server-System-Requirements-Logi-Report-Server-v18)

# Getting Started with Logi Report Server v18

This topic guides you through the process of installing and configuring Logi Report Server, running and creating reports and dashboards in Logi Report web editors, and distributing reports to a variety of outputs.

[1. Product Installation](#)

1. Think about the number of Logi Report servers you need if you want to set up a Logi Report Server Cluster. See [Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/4405683570967-Logi-Report-Server-Cluster-Logi-Report-Server-v18).
2. Decide the licensed features that you want for each Logi Report server. See [Logi Report Licenses](https://devnet.logianalytics.com/hc/en-us/articles/4405683899543-Logi-Report-Licenses).
3. Prepare the computers on which you want to install Logi Report Server. See [Logi Report Server System Requirements](https://devnet.logianalytics.com/hc/en-us/articles/4405690625687-Logi-Report-Server-System-Requirements-Logi-Report-Server-v18).
4. Obtain the Logi Report Server install program. Also obtain the Logi Report Server Monitor install program if you want a Server Monitor. See [Logi Report download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
5. Install Logi Report Server using the way you prefer. See [Installing and Uninstalling Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405683904791-Installing-and-Uninstalling-Logi-Report-Server-v18).
6. Install Server Monitor if you want to monitor your server performance. See [Installing and Uninstalling Server Monitor](https://devnet.logianalytics.com/hc/en-us/articles/4405683527063-Installing-and-Uninstalling-Server-Monitor) in the *Logi Report Server Monitor Guide*.

[2. Server Database Configuration](#)

Configure the server database on the Server Console or using the configuration file if you didn't do this during the installation. See [Configuring the Server Database in a Standalone Environment](https://devnet.logianalytics.com/hc/en-us/articles/4405683583383-Configuring-the-Server-Database-in-a-Standalone-Environment).

[3. Product Security and Authorization](#)

1. Create security organizations to manage different groups of users. See [Multitenancy Supported via Organizations](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations).
2. Set up user accounts, roles, and groups, with appropriate privileges. See [Security System Data Model](https://devnet.logianalytics.com/hc/en-us/articles/4405684019735-Security-System-Data-Model).
3. Integrate with your security software, for example, LDAP. See [Using an LDAP Server's Security System](https://devnet.logianalytics.com/hc/en-us/articles/4405690681623-Using-an-LDAP-Server-s-Security-System).

[4. Resource Publish and Permissions](#)

1. Publish reports, catalogs, and library components to Logi Report Server. See [Publishing Resources](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources).
2. Set up user permissions on the server resources. See [Managing Permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions).
3. Optionally, obtain resources from the real path dynamically. See [Getting and Using Resources From a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/4405690643479-Getting-and-Using-Resources-From-a-Real-Path).

[5. Export Configuration](#)

1. Configure the email server if you want to deploy reports via email. See [Configuring the Email Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690490007-Configuring-the-Email-Server).
2. Configure settings for exporting reports to email and fax. See [Configuring Export Settings](https://devnet.logianalytics.com/hc/en-us/articles/4405690487319-Configuring-Export-Settings).

[6. Cluster Setup](#)

Set up a Logi Report Server Cluster in which multiple servers work together. See [Setting Up and Starting a Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/4405683573271-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster).

[7. Integration Setup](#)

1. Configure the server database. See [Configuring the Server Database in an Integrated Environment](https://devnet.logianalytics.com/hc/en-us/articles/4405683584407-Configuring-the-Server-Database-in-an-Integrated-Environment).
2. Create the Logi Report Server WAR/EAR. See [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).
3. Deploy the WAR/EAR to an application Server. See [Deploying Logi Report Server to a Java Application Server](https://devnet.logianalytics.com/hc/en-us/articles/4405683908375-Deploying-Logi-Report-Server-to-a-Java-Application-Server).

[8. Server Monitor](#)

1. Start and access the Server Monitor. See [Launching and Accessing Server Monitor](https://devnet.logianalytics.com/hc/en-us/articles/4405690463255-Launching-and-Accessing-Server-Monitor) in the *Logi Report Server Monitor Guide*.
2. Monitor the status and performance of Server. See [Using Server Monitor](https://devnet.logianalytics.com/hc/en-us/articles/4405683530775-Using-Server-Monitor) in the *Logi Report Server Monitor Guide*.

[9. Report Running and Scheduling](#)

1. Run reports directly or on demand. See [Running Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405690675223-Running-Reports).
2. Schedule tasks to run reports at the specified time to different locations in various formats. See [Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405690676119-Scheduling-Reports).

[10. Report Creating, Editing, and Exporting](#)

1. Create, edit, and export web reports using Web Report Studio. See [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/4405684031639-Web-Report-Studio-Server-v18).
2. Create, edit, and export page reports using Page Report Studio. See [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/4405683949591-Page-Report-Studio-Server-v18).
3. Create, edit, and export dashboards using JDashboard. See [Introduction to the Logi Report JDashboard](https://devnet.logianalytics.com/hc/en-us/articles/4405683592471-Introduction-to-the-Logi-Report-JDashboard-Logi-Report-Server-v18).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690444055-Logi-Report-Server-Guide-v18-Overview)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690625687-Logi-Report-Server-System-Requirements-Logi-Report-Server-v18)
