---
title: "Installing by Deploying a WAR File"
id: 1500009691082
section: "Introduction to Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691082-Installing-by-Deploying-a-WAR-File
updated_at: 2021-11-03T06:57:01Z
---

# Installing by Deploying a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691042-Installing-on-Unix-Manually)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691002-Logi-Report-Server-Reporthome-Directory-Overview)

# Installing by Deploying a WAR File

The topic introduces how to install Logi JReport Server by building a WAR File on Windows and then deploy it to Linux/Unix. There are user cases when they need to install Logi JReport Server into application servers in the cloud and may not even own a machine of the type the application servers are installing to. For example you use Tomcat on Unix in a cloud environment but only have Windows machines available locally. You can then install Logi JReport Server on Windows, make a war file and deploy it to the Java application server on Unix.

1. Install Logi JReport Server on the local Windows machine.
2. Create a WAR via the following command line while specifying the reporthome. The reporthome uses the path on Unix on the target machine.

   `makewar.bat -Dreporthome=/opt/reporthome`
3. Add any JDBC drivers that are required into the `jreport.war/WEB-INF/lib` directory.
4. Visit your application server from the local machine using a browser, for example, for Tomcat the local machine URL is `http://<hostname>:8080/` (8080 is the default port of Tomcat), and deploy the WAR using your application server user interface.
5. Log onto the Logi JReport Server console by the URL `http://<hostname>:8080/jreport` (assuming the war file is jreport.war) as an administrator to [configure the server database](https://devnet.logianalytics.com/hc/en-us/articles/1500009686682-Configuring-in-a-Standalone-Environment).
6. Restart Logi JReport Server and access the server console to see if you can run the reports.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691042-Installing-on-Unix-Manually)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691002-Logi-Report-Server-Reporthome-Directory-Overview)
