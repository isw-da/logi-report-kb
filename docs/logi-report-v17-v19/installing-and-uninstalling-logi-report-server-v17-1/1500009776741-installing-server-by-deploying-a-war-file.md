---
title: "Installing Server by Deploying a WAR File"
id: 1500009776741
section: "Installing and Uninstalling Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776741-Installing-Server-by-Deploying-a-WAR-File
updated_at: 2021-07-24T00:48:05Z
---

# Installing Server by Deploying a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776681-Installing-Server-on-Unix-Linux-Manually)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748282-Installing-Server-Updates-Service-Packs)

# Installing Server by Deploying a WAR File

This topic describes how you can install Server by building a WAR File on Windows and then deploy it to Linux/Unix.

You may need to install Server into application servers in the cloud when you do not even own a machine of the type the application servers are installed to. For example, you use Tomcat on Unix in a cloud environment but only have Windows machines locally. You can then install Server on Windows, make a WAR file, and deploy it to the Java application server on Unix.

1. Install Server on the local Windows machine.
2. Create a WAR via the following command line while specifying the report home. The report home uses the path on Unix on the target machine.

   `makewar.bat -Dreporthome=/opt/reporthome`
3. Add any JDBC drivers that are required into the `jreport.war/WEB-INF/lib` directory.
4. Visit your application server from the local machine using a browser, for example, for Tomcat the local machine URL is `http://<hostname>:8080/` (8080 is the default port of Tomcat), and deploy the WAR using your application server user interface.
5. Log onto the Server Console by the URL `http://<hostname>:8080/jreport` (assuming the war file is jreport.war) as an administrator to [configure the server database](https://devnet.logianalytics.com/hc/en-us/articles/1500009771541-Configuring-the-Server-Database-in-a-Standalone-Environment).
6. Restart Server and access the Server Console to see if you can run reports.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776681-Installing-Server-on-Unix-Linux-Manually)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748282-Installing-Server-Updates-Service-Packs)
