---
title: "Installing Server by Deploying a WAR File"
id: 45204001381261
section: "Introduction to Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204001381261-Installing-Server-by-Deploying-a-WAR-File
updated_at: 2026-04-30T14:10:15Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Installing Server by Deploying a WAR File 

This topic describes how you can install Server by building a WAR File on Windows and then deploy it to Linux/UNIX. 

You may need to install Server into application servers in the cloud when you do not even own a machine of the type the application servers are installed to. For example, you use Tomcat on UNIX in a cloud environment but only have Windows machines locally. You can then install Server on Windows, make a WAR file, and deploy it to the Java application server on UNIX.

- Install Server on the local Windows machine.

- Create a WAR via the following command line while specifying the report home. The report home uses the path on UNIX on the target machine.
    makewar.bat -Dreporthome=/opt/reporthome

- Add any JDBC drivers that are required into the jreport.war/WEB-INF/lib directory.

- Visit your application server from the local machine using a browser, for example, for Tomcat the local machine URL is http://<hostname>:8080/ (8080 is the default port of Tomcat), and deploy the WAR using your application server user interface. 

- Sign in to the  Server Console by the URL http://<hostname>:8080/jreport (assuming the war file is jreport.war) as an administrator to configure the server database.

- Restart Server and access the Server Console to see if you can run reports.
