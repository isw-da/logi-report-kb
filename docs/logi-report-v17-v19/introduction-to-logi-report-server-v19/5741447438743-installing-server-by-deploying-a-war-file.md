---
title: "Installing Server by Deploying a WAR File"
id: 5741447438743
section: "Introduction to Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741447438743-Installing-Server-by-Deploying-a-WAR-File
updated_at: 2022-10-31T17:17:54Z
---

# Installing Server by Deploying a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741467324823-Installing-Server-on-UNIX-Linux-Manually)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741437384727-Installing-Server-Service-Packs)

# Installing Server by Deploying a WAR File

This topic describes how you can install Server by building a WAR File on Windows and then deploy it to Linux/UNIX.

You may need to install Server into application servers in the cloud when you do not even own a machine of the type the application servers are installed to. For example, you use Tomcat on UNIX in a cloud environment but only have Windows machines locally. You can then install Server on Windows, make a WAR file, and deploy it to the Java application server on UNIX.

1. Install Server on the local Windows machine.
2. Create a WAR via the following command line while specifying the report home. The report home uses the path on UNIX on the target machine.

   `makewar.bat -Dreporthome=/opt/reporthome`
3. Add any JDBC drivers that are required into the `jreport.war/WEB-INF/lib` directory.
4. Visit your application server from the local machine using a browser, for example, for Tomcat the local machine URL is `http://<hostname>:8080/` (8080 is the default port of Tomcat), and deploy the WAR using your application server user interface.
5. Sign in to the Server Console by the URL `http://<hostname>:8080/jreport` (assuming the war file is jreport.war) as an administrator to [configure the server database](https://devnet.logianalytics.com/hc/en-us/articles/5741415979543-Configuring-Server-Databases-for-Server-Metadata-in-a-Standalone-Environment).
6. Restart Server and access the Server Console to see if you can run reports.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741467324823-Installing-Server-on-UNIX-Linux-Manually)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741437384727-Installing-Server-Service-Packs)
