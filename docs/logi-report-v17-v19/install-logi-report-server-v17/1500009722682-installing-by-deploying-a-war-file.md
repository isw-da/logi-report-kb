---
title: "Installing by Deploying a WAR File"
id: 1500009722682
section: "Install Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722682-Installing-by-Deploying-a-WAR-File
updated_at: 2021-07-25T07:19:05Z
---

# Installing by Deploying a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749581-Installing-on-Unix-Manually)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749621-Installing-Updates-Service-Packs)

# Installing by Deploying a WAR File

The topic introduces how to install Logi Report Server by building a WAR File on Windows and then deploy it to Linux/Unix. There are user cases when they need to install Logi Report Server into application servers in the cloud and may not even own a machine of the type the application servers are installing to. For example you use Tomcat on Unix in a cloud environment but only have Windows machines available locally. You can then install Logi Report Server on Windows, make a war file and deploy it to the Java application server on Unix.

1. Install Logi Report Server on the local Windows machine.
2. Create a WAR via the following command line while specifying the reporthome. The reporthome uses the path on Unix on the target machine.

   `makewar.bat -Dreporthome=/opt/reporthome`
3. Add any JDBC drivers that are required into the `jreport.war/WEB-INF/lib` directory.
4. Visit your application server from the local machine using a browser, for example, for Tomcat the local machine URL is `http://<hostname>:8080/` (8080 is the default port of Tomcat), and deploy the WAR using your application server user interface.
5. Log onto the Logi Report Server console by the URL `http://<hostname>:8080/jreport` (assuming the war file is jreport.war) as an administrator to [configure the server database](https://devnet.logianalytics.com/hc/en-us/articles/1500009718822-Configuring-in-a-Standalone-Environment).
6. Restart Logi Report Server and access the server console to see if you can run the reports.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749581-Installing-on-Unix-Manually)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749621-Installing-Updates-Service-Packs)
