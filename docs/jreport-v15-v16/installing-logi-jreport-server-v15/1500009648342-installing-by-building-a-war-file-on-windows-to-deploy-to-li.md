---
title: "Installing by Building a WAR File on Windows to Deploy to Linux/Unix"
id: 1500009648342
section: "Installing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648342-Installing-by-Building-a-WAR-File-on-Windows-to-Deploy-to-Linux-Unix
updated_at: 2021-07-24T20:54:13Z
---

# Installing by Building a WAR File on Windows to Deploy to Linux/Unix

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648282-Installing-on-Unix-Manually)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648322-Upgrading-Logi-JReport-Server-Guide-v15-Server)

# Installing by Building a WAR File on Windows to Deploy to Linux/Unix

There are user cases when they need to install Logi JReport Server into application servers in the cloud and may not even own a machine of the type they are installing to. For example you use Tomcat on Linux in a cloud environment but only have Windows machines available locally. You can then install Logi JReport Server on Windows, make a war file and then deploy it to the Java application server on Linux.

1. Install Logi JReport Server on the local Windows machine.
2. Create a WAR via the following command line while specifying a report home. The report home uses the path on Linux on the target machine.

   `makewar.bat -Dreporthome=/opt/reporthome`
3. Add any JDBC drivers that are required into the `Logi JReport.war/WEB-INF/lib` directory.
4. Visit your application server from the local machine using a browser. For example, for Tomcat the local machine URL is `http://<host>:8080/`, deploy the WAR using your application server user interface. 8080 is the default port of Tomcat.
5. Log onto Logi JReport Server Administration console by the URL `http://<host>:8080/Logi JReport/admin`, (assuming the war file is Logi JReport.war and you are using Tomcat) go to the Data tab on the system toolbar, [configure the server database](https://devnet.logianalytics.com/hc/en-us/articles/1500009669101-Configuring-in-a-Standalone-Environment) for System DB/realm DB/Profiling DB. It shouldn't be Derby.
6. Restart Logi JReport Server and access `http://<host>:8080/Logi JReport` to see if you can run reports.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648282-Installing-on-Unix-Manually)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648322-Upgrading-Logi-JReport-Server-Guide-v15-Server)
